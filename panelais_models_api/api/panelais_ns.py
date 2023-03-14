#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import Resource
from panelais_models_api import config, logger
from panelais_models_api.api.panelais_models import *
from panelais_models_api.api.panelais_parsers import *
from panelais_models_api.api.v1 import api
from panelais_models_api.core import cache, limiter
from panelais_models_api.service.panelais_service import PanelaisModelsService
from panelais_models_api.utils import handle500error

panelais_ns = api.namespace('model', description='Image serving model')


service = PanelaisModelsService(data_base_path=config.DATA_PATH)


@panelais_ns.route('/l1')
class L1Model(Resource):

    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(panelais_image_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour')
    @cache.cached(timeout=3600, query_string=True)
    def get(self):
        """
        Performs predicions on L1 model.
        """

        global service

        logger.info('GET /model/l1')

        # build prediction
        try:
            image = service.predictl1()
        except Exception as e:
            logger.exception(f'Unknown error occurred {e}')
            return handle500error(panelais_ns)

        # format results
        result = {'image': image}

        logger.info('GET /model/l1 status 200')

        return result


@panelais_ns.route('/l2')
class L2Model(Resource):

    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(panelais_image_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour')
    @cache.cached(timeout=3600, query_string=True)
    def get(self):
        """
        Performs predicions on L2 model.
        """

        global service

        logger.info('GET /model/l2')

        # build prediction
        try:
            image = service.predictl2()
        except Exception as e:
            logger.exception(f'Unknown error occurred {e}')
            return handle500error(panelais_ns)

        # format results
        result = {'image': image}

        logger.info('GET /model/l2 status 200')

        return result
