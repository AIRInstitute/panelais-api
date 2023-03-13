#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

panelais_parser = reqparse.RequestParser()
panelais_parser.add_argument('picture', location='files', type=FileStorage, required=True)
