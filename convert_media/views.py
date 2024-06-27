from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Media
from .serializers import MediaSerializer
from .tasks import generate_video

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
