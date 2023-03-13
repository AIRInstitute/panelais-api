#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import os

# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/panelais-models-api/v1'
DEBUG_MODE = False

# model path config
MODEL_PATH = os.getenv('MODEL_PATH', default='./model')
