#!/usr/bin/env python 
import os 
import sys 

from os import path 
from datetime import datetime, timedelta

APP_NAME = 'Simple Video Conversion API'

BASEDIR = os.path.abspath(os.path.dirname(__file__))
# DEBUG
DEBUG = True 

SECRET_KEY = 'ca2b84ac72a91a20cbda8be2d1f2c1fb7521123ouo'

# video conversion presets 
VIDEO_CONVERSION_PRESETS = [
    {
        'name': 'mobile_preset', 
        'output_format': 'mp4', 
        'mimetype': 'video/mp4',
        'resolution': '480p', 
        'compression_ratio': 'low', 
        'ffmpeg_preset': '-preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 1000k -minrate 500k -maxrate 2000k -bufsize 2000k -vf scale=854:480 -y'
    },
    {
        'name': 'tablet_preset', 
        'output_format': 'mp4', 
        'mimetype': 'video/mp4',
        'resulition': '720p', 
        'compression_ratio': 'medium',
        'ffmpeg_preset': '-preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 2500k -minrate 1500k -maxrate 4000k -bufsize 5000k -vf scale=-1:720 -y'
    },
    {
        'name': 'desktop_preset', 
        'output_format': 'mp4', 
        'mimetype': 'video/mp4',
        'resolution': '1080p', 
        'compression_ratio': 'high',
        'ffmpeg_preset': '-preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 4500k -minrate 4500k -maxrate 9000k -bufsize 9000k -vf scale=-1:1080 -y'
    }
]