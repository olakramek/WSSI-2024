import numpy as np
from collections import Counter



class Node:

    def __init__(self, feature=None, threshold=0.0, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value



    def is_leaf_node(self):
        return self.value is not None



class DecisionTree:

    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None



    def fit(self, X, y):

        self.n_features = X.shape[1] if self.n_features is None else min(self.n_features, X.shape[1])
        self.root = self._grow_tree(X, y)


    def _grow_tree(self, X, y,depth=0):

        number_of_samples, number_of_features = X.shape
        number_of_labels = len(np.unique(y))

        if (depth>=self.max_depth or number_of_labels == 1 or number_of_samples < self.min_samples_split):

            counter = Counter(y)
            value = counter.most_common(1)[0][0]
            leaf_value = value

            return Node(value=leaf_value)

        features_indexs = np.random.choice(number_of_features,self.n_features,replace=False)

        best_feature, best_threshold = self._best_split(X, y,features_indexs)

        left_indexes,right_indexes = self._split(X[:,best_feature],best_threshold)

        left = self._grow_tree(X[left_indexes,:], y[left_indexes],depth+1)
        right = self._grow_tree(X[right_indexes,:], y[right_indexes],depth+1)

        return Node(best_feature,best_threshold,left,right)

    def _best_split(self, X, y, features_indexs):

        best_gain = -1
        split_index = None
        split_threshold = None

        for feature_index in features_indexs:

            X_column = X[:, feature_index]
            threasholds = np.unique(X_column)

            for threshhold in threasholds:
                gain = self._information_gain(y, X_column, threshhold)

                if gain > best_gain:
                    best_gain = gain
                    split_index = feature_index
                    split_threshold = threshhold

        return split_index,split_threshold


    def _information_gain(self, y, X_column, threshold):
        parent_entropy = self._entropy(y)
        left_indexes,right_indexes = self._split(X_column, threshold)

        if len(left_indexes) == 0 or len(right_indexes) == 0:
            return 0

        number_of_samples = len(y)
        number_of_samples_left = len(left_indexes)
        number_of_samples_right = len(right_indexes)
        entropy_left = self._entropy(y[left_indexes])
        entropy_right =  self._entropy(y[right_indexes])

        child_entropy = (number_of_samples_left/number_of_samples) * entropy_left +  (number_of_samples_right/number_of_samples) *entropy_right
        information_gain = parent_entropy - child_entropy
        return information_gain
    def _split(self, X_column, split_threshold):
        left_indexes = np.argwhere(X_column <= split_threshold).flatten()
        right_indexes = np.argwhere(X_column > split_threshold).flatten()
        return left_indexes, right_indexes

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p*np.log(p) for p in ps if p > 0])




    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)

        return self._traverse_tree(x, node.right)


    def predict(self, X):
        return np.array([self._traverse_tree(x,self.root )for x in X])

