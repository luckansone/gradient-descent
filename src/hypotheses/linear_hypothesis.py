import numpy as np
from sklearn.preprocessing import PolynomialFeatures 
from hypotheses import Abstract_Hypothesis 


class Linear(Abstract_Hypothesis):

    def __init__(self, X, y, w=None, degree=1):
        poly = PolynomialFeatures(degree=degree)
        self.X = poly.fit_transform(X)
        self.X_raw = self.X
        self.y = y 
        self.weight = np.random.normal(size=(self.X.shape[1], 1)) if w is None else w
        self.degree = degree
           
    def hypothesis(self, X=None, w=None):
        if w is None:
            w = self.weight

        if X is None:
            X = self.X

        return np.dot(X, w)

    def hypothesis_grad(self):
        return self.X
