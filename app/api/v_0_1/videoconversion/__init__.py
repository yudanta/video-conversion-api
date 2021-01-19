#!/usr/bin/env python 
import os 

from datetime import datetime
from hashlib import md5
import json 

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import send_from_directory, send_file
from flask_restplus import Namespace, Resource, fields, marshal, marshal_with, reqparse
from werkzeug.datastructures import FileStorage
from ffmpy import FFmpeg

from config import VIDEO_CONVERSION_PRESETS
from app import app 

api = Namespace('VideoConversion', description='Video Conversion API')

# post request expect parser
parser = api.parser()
parser.add_argument('preset', type=str, required=False, default='mobile_preset', help='please refer to GET /api/v.0.1/')
parser.add_argument('file', location='files', type=FileStorage, required=True)

@api.route('/convert')
class VideoConverter(Resource):
    @api.doc('convert video from various format with ffmpeg')
    @api.expect(parser, validate=True)
    def post(self):
        args = parser.parse_args()
        
        # convert on the fly 
        if args['preset'] not in list(map(lambda x: x['name'], VIDEO_CONVERSION_PRESETS)):
            return {
                'msg': 'preset not found, please refer to /api/v.0.1/presets/'
            }, 412

        preset = None 
        for p in VIDEO_CONVERSION_PRESETS:
            if p['name'] == args['preset']:
                preset = p
                break 

        contentfiles_input_dir = os.path.join(app.config['BASEDIR'], 'app/contentfiles/inputs', datetime.now().strftime('%Y/%m/%d'))
        contentfiles_output_dir = os.path.join(app.config['BASEDIR'], 'app/contentfiles/outputs', datetime.now().strftime('%Y/%m/%d'))
        
        # temporary in & temporary out 
        if not os.path.exists(contentfiles_input_dir):
            os.makedirs(contentfiles_input_dir)

        if not os.path.exists(contentfiles_output_dir):
            os.makedirs(contentfiles_output_dir)

        # name in & name out 
        fin_path = os.path.join(contentfiles_input_dir, '{hash_name}.{file_format}'.format(
            hash_name=md5(''.join([args['file'].filename, args['file'].mimetype, datetime.now().strftime('%s')]).encode('utf-8')).hexdigest(), 
            file_format=args['file'].mimetype.split('/')[-1]))
        
        # save current file to temporary file
        args['file'].save(fin_path)

        fout_path = os.path.join(contentfiles_output_dir, '{hash_name}_{preset}_{timestamp}.{output_format}'.format(
            hash_name=md5(''.join([args['file'].filename, args['file'].mimetype, datetime.now().strftime('%s')]).encode('utf-8')).hexdigest(),
            preset=preset['name'],
            timestamp=datetime.now().strftime('%s'),
            output_format=preset['output_format']
        ))

        print(fout_path)

        ff = FFmpeg(
            inputs={fin_path: None},
            outputs={fout_path: preset['ffmpeg_preset']}
        )

        print(ff.cmd)
        ff.run()

        # return converted file 
        attachment_fname = 'video_{}_{}.{}'.format(preset['name'], datetime.now().strftime('%s'), preset['output_format'])
        response = send_file(fout_path, mimetype=preset['mimetype'], as_attachment=True, attachment_filename=attachment_fname)
        
        cd = 'attachment; filename="{}"'.format(attachment_fname)
        response.headers['Content-Disposition'] = cd 
        return response
