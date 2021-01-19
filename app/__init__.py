#!/usr/bin/env python 
from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, jsonify
from flask_cors import CORS

# APP Config
app = Flask(__name__, instance_relative_config=True)

# load config 
app.config.from_object('config')
app.config.from_pyfile('application.cfg', silent=True)

# CORS
CORS(app, resources={r"/api/*": {"origins": "*"}} )
# CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'Video Conversion API'

# import api + register as blueprint
from app.api.v_0_1 import api_v_0_1
from app.api.v_0_1 import api

app.register_blueprint(api_v_0_1)
