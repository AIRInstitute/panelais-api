#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import base64
import os

from panelais_models_api import logger
from panelais_models_api.model import PanelaisL1Model, PanelaisL2Model


class PanelaisModelsService:
    """Loads the model and perform predictions over it.
    """

    def __init__(self, data_base_path: str, l1_file='ProdL1.csv', l2_file='ProdL2.csv') -> None:
        """
        Args:
            data_base_path: the path of the base data for model
        """

        self.l1, self.l2 = None, None
        self._load_models(data_base_path=data_base_path, l1_file=l1_file, l2_file=l2_file)

    def _load_models(self, data_base_path: str, l1_file: str, l2_file: str
                     ) -> None:
        """Loads the models and data

        Args:
            data_base_path: the base path where model files are located
        """

        logger.info('loading model')

        l1_path = os.path.join(data_base_path, l1_file)
        l2_path = os.path.join(data_base_path, l2_file)

        self.l1 = PanelaisL1Model(data_path=l1_path)
        self.l2 = PanelaisL2Model(data_path=l2_path)

        logger.info('model loaded sucessfully')

    def predictl1(self) -> str:
        """Runs L1 model

        Returns:
            the picture generated as result of L1 model
        """

        logger.info('applying model')

        image = self.l1.run()
        encoded_image = base64.b64encode(image).decode('utf-8')

        logger.info('prediction finished successfully')

        return encoded_image

    def predictl2(self) -> str:
        """Runs L2 model

        Returns:
            the picture generated as result of L2 model
        """

        logger.info('applying model')

        image = self.l2.run()
        encoded_image = base64.b64encode(image).decode('utf-8')

        logger.info('prediction finished successfully')

        return encoded_image
