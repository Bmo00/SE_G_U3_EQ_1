

import tensorflow as tf
print('Version de TensorFlow: ',tf.__version__, end="\n\n")

import numpy as n
a = [1, 2, 3]
a = n.array(a)
print(a, end="\n\n")

import pandas as pd
s = pd.Series([1,3,5, n.nan,6, 8])
print(s)
