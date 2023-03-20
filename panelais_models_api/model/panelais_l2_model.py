#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import numpy as np
import pandas as pd
import plotly as py
from typing import Any
import plotly.io as pio
import plotly.graph_objs as go
from plotly.offline import iplot
from scikit-learn.decomposition import PCA
from scikit-learn.cluster import KMeans
from scikit-learn.preprocessing import MinMaxScaler


class PanelaisL2Model:

    def __init__(self, data_path: str) -> None:
        """
        
        Args:
            data_path: file where data is located.
        """

        self.data = None
        self._load_data(data_path)

    def _load_data(self, data_path: str) -> None:
        """Loads data for model running.
        """

        self.data = pd.read_csv(data_path, sep = ";")


    def run(self) -> Any:
        """Applies model and generates image
        """

        #Lectura de datos y selección de variables
        Prod2 = self.data.copy()
        Prod2 = Prod2.drop(columns = 'data', axis = 1)
        columns = [3,17,18,19,20,21]
        Prod2 = Prod2.drop(columns=Prod2.columns[columns], axis = 1)
        Prod2 = Prod2.fillna(method='bfill', axis=0)

        #Preprocesado de los datos
        Scaler = MinMaxScaler()
        Scaler.fit(Prod2)
        X = pd.DataFrame(Scaler.transform(Prod2))

        #Clustering con Kmedias
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        clusters = kmeans.predict(X)
        X["Cluster"] = clusters

        #Guardamos los datos para la representacion
        plotX = pd.DataFrame(np.array(X.sample(10000)))
        plotX.columns = X.columns

        #Hacemos PCA para repsentar los clusters en 2D
        pca_2d = PCA(n_components=2)
        pca_2d.fit(plotX.drop(["Cluster"], axis=1))
        PCs_2d = pd.DataFrame(pca_2d.transform(plotX.drop(["Cluster"], axis=1)))
        PCs_2d.columns = ["PC1_2d", "PC2_2d"]
        plotX = pd.concat([plotX,PCs_2d], axis=1, join='inner')

        #Guardamos los datos por cluster para representar
        cluster0 = plotX[plotX["Cluster"] == 0]
        cluster1 = plotX[plotX["Cluster"] == 1]
        cluster2 = plotX[plotX["Cluster"] == 2]

        #Representacion
        #trace1 is for 'Cluster 0'
        trace1 = go.Scatter(
                            x = cluster0["PC1_2d"],
                            y = cluster0["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 0",
                            marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                            text = None)

        #trace2 is for 'Cluster 1'
        trace2 = go.Scatter(
                            x = cluster1["PC1_2d"],
                            y = cluster1["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 1",
                            marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                            text = None)

        #trace3 is for 'Cluster 2'
        trace3 = go.Scatter(
                            x = cluster2["PC1_2d"],
                            y = cluster2["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 2",
                            marker = dict(color = 'rgba(255, 0, 0, 1)'),
                            text = None)
        
        data = [trace1, trace2, trace3]


        title = "Visualizing Clusters in Two Dimensions Using PCA"

        fig = go.Figure(layout_title_text = title)
        fig.add_trace(trace1)
        fig.add_trace(trace2)
        fig.add_trace(trace3)

        # image export

        image_bytes = pio.to_image(fig, format='png')
        
        return image_bytes