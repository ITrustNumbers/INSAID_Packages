import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def PlotClusters(df):
  fig = plt.figure(figsize=(13,11))
  for i in range(4):
    n = len(df[df['Labels'] == i].iloc[:,0])
    plt.scatter(df[df['Labels'] == i].iloc[:,0] , df[df['Labels'] == i].iloc[:,1], alpha=0.55, s= list(random.choices(list(range(20,60)), k=n)), label = f'Cluster: {i + 1}')

  plt.ylabel('Principal Component 1', fontsize=15, labelpad=10)
  plt.xlabel('Principal Component 2', fontsize=15, labelpad=12)
  for spine in plt.gca().spines.values():
    spine.set_visible(False)

  plt.grid(alpha=0.5, color='lightgrey')
  plt.legend(fontsize=15, frameon=False)
  return fig
