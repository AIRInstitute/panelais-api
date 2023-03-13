#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import Api

api = Api(version='1.0',
                  title='panelais-models-api',
                  description="API for serving models developed for PANELAIS proyect")
