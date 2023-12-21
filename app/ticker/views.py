import os

from app.settings import BASE_DIR
from ticker.ticker_init import create_ticker
from ticker.models import Requests

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, HttpResponse


def get_ticker(request, text: str):
    video_path = os.path.join(BASE_DIR, 'ticker', 'data', 'ticker.mp4')
    if not Requests.objects.filter(name=text).exists():
        request_instance = Requests(name=text)
        request_instance.save()

    create_ticker(text, video_path)
    if os.path.exists(video_path):
        f = open(video_path, 'rb')
        response = FileResponse(f)
        response['Content-Disposition'] = 'attachment; filename="ticker.mp4"'
        return response
    
    return Http404("Video file not found")


def get_db_requests(request):
    requests_instances = Requests.objects.all()
    for request_instance in requests_instances:
        print(request_instance.name)

    return render(request, 'ticker/requests.html', {'requests_instances': requests_instances})
    