# sklearn2gem

[![PyPI version](https://badge.fury.io/py/sklearn2gem.svg)](https://badge.fury.io/py/sklearn2gem)
[![Requirements Status](https://requires.io/github/stewartpark/sklearn2gem/requirements.svg?branch=master)](https://requires.io/github/stewartpark/sklearn2gem/requirements/?branch=master)

sklearn2gem ports a Pickle'd scikit-learn model into a ruby C extension gem.

# Getting Started

Install sklearn2gem using `pip`:

```
pip install sklearn2gem
```

or via `easy_install`:

```
easy_install sklearn2gem
```

After that, dump your scikit-learn model with `sklearn.externals.joblib`, and run `sklearn2gem model_name@version your_model.pkl foo/bar/model_name`. You should be able to see a newly created folder named `model_name` under `foo/bar/`.

See [`examples/iris.py`](https://github.com/stewartpark/sklearn2gem/blob/master/examples/iris.py) to try it out.

To produce a pre-compiled binary gem, use [gem-compiler](https://github.com/luislavena/gem-compiler).

# What machine learning algorithms are supported?

Since sklearn2gem uses `nok/sklearn-porter` to convert a model into a C file, you can refer to [this page](https://github.com/nok/sklearn-porter#machine-learning-algorithms).
