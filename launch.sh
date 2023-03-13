#!/bin/bash
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install -r requirements.txt
sudo python3 -m pip install . --upgrade
sudo panelais_models_api
