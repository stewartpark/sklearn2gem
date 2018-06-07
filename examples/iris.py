from sklearn.datasets import load_iris
from sklearn.tree import tree
from sklearn.externals import joblib

# load data and train the classifier:
samples = load_iris()
X, y = samples.data, samples.target
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

joblib.dump(clf, 'model.pkl')

# After this, simply run `sklearn2gem iris_classifier@0.0.1 model.pkl iris_classifier`
