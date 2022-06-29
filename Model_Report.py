import pandas as pd
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, RocCurveDisplay

def model_report(y, y_preds, labels, test_data=False, conf_matrix=False, class_report=False, roc_curve=False):

  '''
  This function can be used to:
  1. Plot Confusion Martix
  2. Print Classification Report
  3. Plot ROC Curve

  In any combination, by default the function does nothing but the functionality can
  be turned on by simply passing arguments for:
  1. conf_matrix: True for plotting confusion matrix
  2. class_report: True for printing classification report
  3. ROC_Curve: True for plotting ROC Cruve

  User can specify whether to use training data or test data by:
  test_data: True for using test data & False for using training data
  '''

  clf_name = str(type(clf)).split('.')[-1][:-2]

  #Plotting Confusion Matrix 
  if conf_matrix:
    fig = plt.figure(figsize=(12,8))
    ConfusionMatrixDisplay.from_predictions(y, y_preds, display_labels=labels, cmap='BuPu', 
                                            ax=plt.gca(), colorbar=False)

    plt.tick_params(axis='both', pad=4, labelsize='large')
    plt.title(f'Confusion Matrix for {clf_name}',fontsize=15)
    plt.ylabel('True Label', fontsize=15)
    plt.xlabel('Predicted Label', fontsize=15)
    plt.show();
    print('\n\n')
  
  #Classification report
  if class_report:
    if test_data: print('Test Data Report:\n')
    else: print('Train Data Report:\n') 
    print(classification_report(y, y_preds, digits=3))
    print('='*60)
    print('\n')

  if conf_matrix:
    return fig

  else:
    return None
