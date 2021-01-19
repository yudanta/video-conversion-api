#!/usr/bin/env python 
import io
import os 
import unittest
import json 

from werkzeug.datastructures import FileStorage
from app import app 

API_VERSION = '/api/v.0.1'
VIDEO_CONVERSION_ENDPOINT = '/video/convert'

class TestConvertVideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_convert_video_with_preset(self):
        VIDEO_PRESET = 'mobile_preset'
        conversion_path = VIDEO_CONVERSION_ENDPOINT + "?preset={}".format(VIDEO_PRESET)
        
        sample_video_path = os.path.join("sampel_videos/Netflix_Logo_Animation_2019.mp4")
        sample_video = FileStorage(
            stream=open(sample_video_path, 'rb'),
            filename="Netflix_Logo_Animation_2019.mp4",
            content_type="video/mp4"
        )


        resp = self.app.post(''.join([API_VERSION, conversion_path]), data={"file": sample_video}, headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'})
        self.assertEqual(resp.status_code, 200)

    def test_convert_video_from_webm_format(self):
        VIDEO_PRESET = 'mobile_preset'
        conversion_path = VIDEO_CONVERSION_ENDPOINT + "?preset={}".format(VIDEO_PRESET)
        
        sample_video_path = os.path.join("sampel_videos/Netflix_Logo_Animation_2019.webm")
        sample_video = FileStorage(
            stream=open(sample_video_path, 'rb'),
            filename="Netflix_Logo_Animation_2019.webm",
            content_type="video/webm"
        )


        resp = self.app.post(''.join([API_VERSION, conversion_path]), data={"file": sample_video}, headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'})
        self.assertEqual(resp.status_code, 200)
    
    def test_convert_video_with_invalid_preset(self):
        VIDEO_PRESET = 'invalid_preset'
        conversion_path = VIDEO_CONVERSION_ENDPOINT + "?preset={}".format(VIDEO_PRESET)
        
        sample_video_path = os.path.join("sampel_videos/Netflix_Logo_Animation_2019.mp4")
        sample_video = FileStorage(
            stream=open(sample_video_path, 'rb'),
            filename="Netflix_Logo_Animation_2019.mp4",
            content_type="video/mp4"
        )


        resp = self.app.post(''.join([API_VERSION, conversion_path]), data={"file": sample_video}, headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'})
        self.assertNotEqual(resp.status_code, 200)
        

