
# import packages
import pandas as pd
import numpy as np
import os re
from random import sample
from sklearn import datasets
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import m2cgen as m2c

seed = 2020
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# fit model on training data
model = XGBClassifier()
model.fit(X_train, y_train)


code = m2c.export_to_visual_basic(model, function_name = 'pred')