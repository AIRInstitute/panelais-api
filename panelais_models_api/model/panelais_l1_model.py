#!/usr/bin/python3
# Copyright 2023 BISITE
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@GandalFran on GitHub)


import numpy as np
import pandas as pd
import plotly as py
import plotly.io as pio
from typing import Any
import plotly.graph_objs as go
from plotly.offline import iplot
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


class PanelaisL1Model:

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
        Prod1 = self.data.copy()
        Prod1 = Prod1.drop(columns = 'data', axis = 1)
        columns = [5,6,21,22,33,39]
        for i in range(44, 79):
            columns.append(i)
        Prod1 = Prod1.drop(columns=Prod1.columns[columns], axis = 1)
        Prod1 = Prod1.fillna(method='bfill', axis=0)

        #Preprocesado de los datos
        Scaler = MinMaxScaler()
        Scaler.fit(Prod1)
        X = pd.DataFrame(Scaler.transform(Prod1))

        #Clustering con Kmedias
        kmeans = KMeans(n_clusters=8)
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
        cluster3 = plotX[plotX["Cluster"] == 3]
        cluster4 = plotX[plotX["Cluster"] == 4]
        cluster5 = plotX[plotX["Cluster"] == 5]
        cluster6 = plotX[plotX["Cluster"] == 6]
        cluster7 = plotX[plotX["Cluster"] == 7]

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
                            marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                            text = None)

        #trace4 is for 'Cluster 3'
        trace4 = go.Scatter(
                            x = cluster3["PC1_2d"],
                            y = cluster3["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 3",
                            marker = dict(color = 'rgba(255, 0, 0, 1)'),
                            text = None)

        #trace5 is for 'Cluster 4'
        trace5 = go.Scatter(
                            x = cluster4["PC1_2d"],
                            y = cluster4["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 4",
                            marker = dict(color = 'rgba(255, 255, 0, 1)'),
                            text = None)

        #trace6 is for 'Cluster 5'
        trace6 = go.Scatter(
                            x = cluster5["PC1_2d"],
                            y = cluster5["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 5",
                            marker = dict(color = 'rgba(150, 0, 166, 1)'),
                            text = None)

        #trace7 is for 'Cluster 6'
        trace7 = go.Scatter(
                            x = cluster6["PC1_2d"],
                            y = cluster6["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 6",
                            marker = dict(color = 'rgba(0, 220, 255, 1)'),
                            text = None)

        #trace8 is for 'Cluster 7'
        trace8 = go.Scatter(
                            x = cluster7["PC1_2d"],
                            y = cluster7["PC2_2d"],
                            mode = "markers",
                            name = "Cluster 7",
                            marker = dict(color = 'rgba(125, 0, 0, 1)'),
                            text = None)

        
        title = "Visualizing Clusters in Two Dimensions Using PCA"

        fig = go.Figure(layout_title_text = title)
        fig.add_trace(trace1)
        fig.add_trace(trace2)
        fig.add_trace(trace3)
        fig.add_trace(trace4)
        fig.add_trace(trace5)
        fig.add_trace(trace6)
        fig.add_trace(trace7)
        fig.add_trace(trace8)

        # image export

        image_bytes = pio.to_image(fig, format='png')
        
        return image_bytes