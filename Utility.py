
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
def PlotConfusionMatrix2(y, y_pred):

  conf = confusion_matrix(y,y_pred)
  fig = plt.figure(figsize=(12,8))
  sns.heatmap(conf, cmap='BuPu',  cbar=False, annot=True, fmt='d', annot_kws={'fontsize' : 14, 'weight' : 'bold'})

  plt.tick_params(axis='both', pad=4, labelsize=16, size=0)

  plt.gca().set_xticklabels(['Low','Mid','High','Flagship'])
  plt.gca().set_yticklabels(['Low','Mid','High','Flagship'])

  plt.title('Confusion Matrix for {}'.format('Support Vector Classifier'), 
                fontsize=17, pad=14)

  plt.ylabel('True Label', fontsize=16, labelpad=14)
  plt.xlabel('Predicted Label', fontsize=16, labelpad=14)

  return fig