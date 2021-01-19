#!/usr/bin/env python 
from datetime import datetime
import json 

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Namespace, Resource, fields, marshal, marshal_with
from config import VIDEO_CONVERSION_PRESETS

api = Namespace('Presets', description='Video conversion presets')

# envelope 
video_preset_envelope = api.model('VideoPresetModel', {
    'name': fields.String(description='news unique id'),
    'output_format': fields.String(description='news url'),
    'resolution': fields.String(description='news source/provider'),
    'compression_ratio': fields.String(description='news title')
})

@api.route('/')
class VideoPresets(Resource):
    @api.doc('Get list video presets')
    @api.marshal_with(video_preset_envelope)
    def get(self):
        return VIDEO_CONVERSION_PRESETS