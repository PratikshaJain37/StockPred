"""
Created on Sat May  8 16:09:37 2021

@author: JOKER
Edited by: Pratiksha Jain
"""

# Imports needed
import pandas as pd
import numpy as np
from datetime import datetime, date
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn import ensemble
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score



# Put stock here
stock = 'ABB'
# Future prediction, add dates here for which you want to predict
dates = ["2020-12-23", "2020-12-24", "2020-12-25", "2020-12-26", "2020-12-27",]
 

def prepareData(stock, column):
  df = pd.read_csv("stock_details/%s.csv"%(stock), index_col='Date')
  prices = df[[column]]
  prices.reset_index(level=0, inplace=True)
  prices["timestamp"] = pd.to_datetime(prices.Date).astype(np.int64) // (10**9)
  prices = prices.drop(['Date'], axis=1)

  dataset = prices.values
  X = dataset[:,1].reshape(-1,1)
  Y = dataset[:,0:1]

  return X, Y

def compareModel(models, X_train, X_validation, Y_train, Y_validation):
  # Test options and evaluation metric
  num_folds = 10
  seed = 7
  scoring = "r2"

  # evaluate each model in turn
  results = []
  names = []
  for name, model in models:
      kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
      cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
      # print(cv_results)
      results.append(cv_results)
      names.append(name)
      msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
      #print(msg)
  
  # For GBR
  params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
  model = ensemble.GradientBoostingRegressor(**params)
  model.fit(X_train, Y_train)
  model_score = model.score(X_train, Y_train)
  # Have a look at R sq to give an idea of the fit ,
  # Explained variance score: 1 is perfect prediction
  #print('Test Variance score: %.2f' % r2_score(Y_validation, y_predicted))
  #print('GBR: %f',model_score)

  return models[5][1]


def predictPrice(stock, column, dates):
  global models
  X, Y = prepareData(stock, column)
  X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.2, random_state=7)
  model = compareModel(models, X_train, X_validation, Y_train, Y_validation)

  # Fit to model
  model.fit(X_train, Y_train)
  # predict
  
  #convert to time stamp
  for dt in dates:
    datetime_object = datetime.strptime(dt, "%Y-%m-%d")
    timestamp = datetime.timestamp(datetime_object)
    # to array X
    X = np.append(X, int(timestamp))
  X = X.reshape((len(X),1))

  predictions = model.predict(X)
  """
  #matplotlib inline 
  fig= plt.figure(figsize=(24,12))
  plt.plot(X,Y)
  plt.plot(X,predictions)
  plt.show()
  """
  return pd.Series(predictions)



# Driver Code

# Spot-Check Algorithms
models = []
models.append(('LR ', LinearRegression()))
models.append(('LASSO ', Lasso()))
models.append(('EN ', ElasticNet()))
models.append(('KNN ', KNeighborsRegressor()))
models.append(('CART ', DecisionTreeRegressor()))
models.append(('SVR ', SVR()))

'''
print("Low")
predictions_low = predictPrice(stock, 'Low', dates)
#for i in range(0,5):
#    print("For date: ", dates[i]," Price = ", predictions_low[len(predictions_low)-5+i])


print("High")
predictions_high = predictPrice(stock, "High", dates)
for i in range(0,5):
    print("For date: ", dates[i]," Price = ", predictions_high[len(predictions_high)-5+i])
'''

def calculateProfit(stock, dates):
  predictions_low = predictPrice(stock, 'Low', dates)[-len(dates):].reset_index(drop=True)
  predictions_high = predictPrice(stock, "High", dates)[-len(dates):].reset_index(drop=True)
  
  table = pd.concat([pd.Series(dates).rename('Date'), predictions_low.rename('Pred_Low'), predictions_high.rename('Pred_High')], axis=1)
  
  table['Pred_Difference'] = table['Pred_High'] - table['Pred_Low']
  table['Pred_Difference_Percentage'] = (table['Pred_Difference'] / table['Pred_Low'])*100


  return table


table = calculateProfit(stock, dates)

print(stock)
print(table)