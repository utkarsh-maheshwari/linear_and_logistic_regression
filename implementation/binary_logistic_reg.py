__author__ = 'Jorge Cotillo'

import helpers.helpers as _helpers
import interfaces.regression_abstract as _abstract
import numpy as np


class BinaryLogisticRegression(_abstract.RegressionAbstract):

    def __init__(self):
        self.alpha = 0.01

    def retrieve_training_set(self):
        x_input_variables = ['wind_speed_mph']
        xs, ys = _helpers.Helpers.get_binary_training_data_from_csv('data/binary_training_examples_one_feature.csv',
                                                                    x_input_variables,
                                                                    'polluted')
        return xs, ys

    def train_algorithm(self, xs, ys, n):
        if n is None:
            n = 1000

        for i in range(n):
            self.theta += self.alpha * self.__gradient(xs, ys)

        return self.theta

    def __gradient(self, xs, ys):
        return xs.T * (ys - self.__sigmoid(xs * self.theta))

    def get_gradient_descent(self):
        return self.get_gradient_descent_intern(1, 2, 3)

    @staticmethod
    def __get_gradient_descent_intern(self, param1, param2, param3):
        return 5.0

    def __sigmoid(self, z):
        return 1.0 / (1 + np.exp(-z))

    def __get_cost(self, xs, ys):
        prob = self.__set_hypothesis(xs * self.theta)
        cost = ys.T * np.log(prob) + (1 - ys).T * np.log(1 - prob)
        # final cost equation -1/m sum(cost)
        return float(-(1.0 / len(xs) * cost))