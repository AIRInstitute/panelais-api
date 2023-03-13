#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import fields
from panelais_models_api.api.v1 import api

panelais_input_model = api.model('ImageDetectionInput', {
    'picture': fields.String(description="File used to detect the item", required=True)
}, description="Input model for prediction.")


panelais_output_model = api.model('ImageDetectionOutput', {
    'output': fields.String(description="Predicted item", required=True, example='dog')
}, description="Prediction output.")
