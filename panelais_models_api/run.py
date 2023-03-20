#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


from flask import Blueprint, Flask, redirect, request
from flask_cors import CORS
from panelais_models_api import config
from panelais_models_api.api import namespaces
from panelais_models_api.api.v1 import api
from panelais_models_api.core import cache, limiter

app = Flask(__name__)

VERSION = (1, 0)
AUTHOR = 'BISITE'


def get_version():
    """
    This function returns the API version that is being used.
    """

    return '.'.join(map(str, VERSION))


def get_authors():
    """
    This function returns the API's author name.
    """

    return str(AUTHOR)


__version__ = get_version()
__author__ = get_authors()


@app.route('/')
def register_redirection():
    """
    Redirects to dcoumentation page.
    """

    return redirect(f'{request.url_root}/{config.URL_PREFIX}', code=302)


def initialize_app(flask_app):
    """
    This function initializes the Flask Application, adds the namespace and registers the blueprint.
    """

    CORS(flask_app)

    v1 = Blueprint('api', __name__, url_prefix=config.URL_PREFIX)
    api.init_app(v1)

    limiter.exempt(v1)
    cache.init_app(flask_app)
    flask_app.register_blueprint(v1)
    flask_app.config.from_object(config)

    for ns in namespaces:
        api.add_namespace(ns)


def main():

    # initialize api
    initialize_app(app)
    separator_str = ''.join(map(str, "=" * 100))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Base URL: http://localhost:{config.PORT}{config.URL_PREFIX}')
    print(separator_str)
    context = ('/home/cert.pem', '/home/key2.pem')
    app.run(host=config.HOST, port=config.PORT, ssl_context=context, debug=config.DEBUG_MODE)


if __name__ == '__main__':
    main()
