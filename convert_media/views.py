import base64
import datetime
from django.utils import timezone 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Media, TokenStore
from .serializers import MediaSerializer
from tasks import generate_video
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from cryptography.fernet import Fernet
from django.conf import settings

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        media_id = response.data['id']
        generate_video.delay(media_id)
        return response

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        media = self.get_object()
        return Response({'status': media.status})

# Generate a key for encryption and decryption (this should be kept secure and secret)
# key = Fernet.generate_key()
cipher_suite = Fernet(settings.FERNET_KEY)

@csrf_exempt
def generate_token(request, video_id):
    # Encrypt the video_id to create a token
    token = cipher_suite.encrypt(str(video_id).encode())
    token = base64.urlsafe_b64encode(token).decode('utf-8')
    
    # Store the token with creation time
    token_store = TokenStore(token=token, created_at=datetime.datetime.now())
    token_store.save()

    # Return the token to the client
    return JsonResponse({'token': token})

def stream_video(request, token):
    try:
        print(token)
        decoded_video_id = base64.urlsafe_b64decode(token.encode()).decode('utf-8')
        video_id = cipher_suite.decrypt(decoded_video_id.encode()).decode('utf-8')

        # Validate and expire the token after one use or after a certain period (e.g., 24 hours)
        token_store = TokenStore.objects.filter(token=token).first()
        if not token_store or (timezone.now() - token_store.created_at).total_seconds() > 20:
            return JsonResponse({'error': 'Token expired or invalid'}, status=400)

        # Delete the token after use
        token_store.delete()

        # Get the video from database
        video = get_object_or_404(Media, id=video_id)
        response = FileResponse(open(video.video.path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(video.video.name)
        response['X-Content-Type-Options'] = 'nosniff'
        response['Cache-Control'] = 'private, no-store, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

