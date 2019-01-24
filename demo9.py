#岭回归预测交通流量

import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('ridge.csv')
a = np.array(data)
plt.plot(a[:, 5])
plt.show()
x = a[:, 1:5]
y = a[:, 5]
poly = PolynomialFeatures(6)
x = poly.fit_transform(x)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size = 0.2,random_state = 0)
clf = Ridge(alpha = 1.0, fit_intercept = True)
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
start = 200
end = 300
time = np.arange(start, end)
time
y_pre = clf.predict(x)
plt.plot(time, y[start:end], 'b', label = 'real')
plt.plot(time, y_pre[start:end], 'r', label = 'predict')
plt.legend(loc = 'upper left')
plt.show()