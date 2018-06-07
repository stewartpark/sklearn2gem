# sklearn2gem

sklearn2gem ports a Pickle'd scikit-learn model into a ruby C extension gem.

# How to install

```
pip install sklearn2gem
```

# Usage

Just have a model dumped with `sklearn.externals.joblib`, and run `sklearn2gem model_name@version your_model.pkl foo/bar/model_name`. You should be able to see a newly created folder named `model_name` under `foo/bar/`.

See [`examples/iris.py`](https://github.com/stewartpark/sklearn2gem/blob/master/examples/iris.py) to try it out.

To produce a pre-compiled binary gem, use [gem-compiler](https://github.com/luislavena/gem-compiler).

# What machine learning algorithms are supported?

Since sklearn2gem uses `nok/sklearn-porter` to convert a model into a C file, you can refer to [this page](https://github.com/nok/sklearn-porter#machine-learning-algorithms).
