from celery import shared_task
from .models import Media
from time import sleep
from django.core.files.base import ContentFile
import io
from PIL import Image as PILImage

@shared_task
def generate_video(media_id):
    media = Media.objects.get(id=media_id)
    media.status = 'processing'
    media.save()
    sleep(30)  # Simulate video generation delay

    # Mock video generation
    pil_image = PILImage.open(media.image)
    video_content = ContentFile(b'video content')  # Placeholder for actual video content
    media.video.save(f'{media_id}.mp4', video_content)

    media.status = 'completed'
    media.save()
