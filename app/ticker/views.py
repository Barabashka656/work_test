import os

from app.settings import BASE_DIR
from ticker.ticker_init import create_ticker

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, HttpResponse


def index(request, text: str):
    video_path = os.path.join(BASE_DIR, 'ticker', 'data', 'ticker.mp4')
    create_ticker(text, video_path)
    if os.path.exists(video_path):
        f = open(video_path, 'rb')
        response = FileResponse(f)
        response['Content-Disposition'] = 'attachment; filename="ticker.mp4"'
        
        return response
    
    return Http404("Video file not found")
