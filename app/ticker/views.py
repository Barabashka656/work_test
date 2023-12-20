import os

from app.settings import BASE_DIR
from ticker.ticker_init import create_ticker


from django.shortcuts import render, HttpResponse

def index(request, text: str):
    video_path = os.path.join(BASE_DIR, 'ticker', 'data', 'ticker.mp4')
    
    create_ticker(text, video_path)
    return HttpResponse('HELLO')
