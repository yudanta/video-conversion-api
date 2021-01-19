#!/usr/bin/env python 
import unittest
import json 
from app import app 

API_VERSION = '/api/v.0.1'
PRESET_ENDPOINT = '/presets/'

class TestPresetAPI(unittest.TestCase):
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

    def test_get_available_video_presets(self):
        resp = self.app.get(''.join([API_VERSION, PRESET_ENDPOINT]), content_type='application/json')
        
        self.assertEqual(resp.status_code, 200)
        
        resp_json = json.loads(resp.data.decode())
        
        self.assertGreater(len(resp_json), 0)
        
        item_sample = resp_json[0]
        self.assertTrue('name' in item_sample)
        self.assertTrue('output_format' in item_sample)
        self.assertTrue('resolution' in item_sample)
        self.assertTrue('compression_ratio' in item_sample)
        