#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import Resource
from panelais_models_api import config, logger
from panelais_models_api.api.panelais_models import *
from panelais_models_api.api.panelais_parsers import *
from panelais_models_api.api.v1 import api
from panelais_models_api.core import limiter
from panelais_models_api.service.panelais_service import PanelaisModelsService
from panelais_models_api.utils import handle500error

panelais_ns = api.namespace('model', description='Image serving model')


service = PanelaisModelsService(model_path=config.MODEL_PATH)


@panelais_ns.route('/predict')
class Predict(Resource):

    @api.expect(panelais_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(panelais_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour')
    def post(self):
        """
        Returns the item indicated in the attached file.
        """

        global service

        logger.info('new request arrived')

        # retrieve arguments
        obj = panelais_parser.parse_args()
        picture = obj['picture']

        logger.info('performing model prediction')

        # build prediction
        try:
            output = service.classify(picture=picture)
        except Exception as e:
            logger.exception(f'Unknown error occurred {e}')
            return handle500error(panelais_ns)

        # format results
        result = {
            'output': output.upper()
        }

        logger.info('request processed sucessfully')

        return result
