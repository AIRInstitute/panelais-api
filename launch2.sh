#!/bin/bash
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


sudo python3 -m pip install pip --upgrade
sudo python3 setup.py install --force
sudo panelais_models_api
