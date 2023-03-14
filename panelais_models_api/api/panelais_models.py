#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import fields
from panelais_models_api.api.v1 import api

panelais_image_output_model = api.model('Image', {
    'image': fields.String(description='Image in base64-encoded format')
}, description="Image served as output")
