# numpyのメモ

[公式ドキュメント](https://numpy.org/doc/1.19/#)

## numpy.ndarray

numpyの基本的なデータ構造。複数次元かつ同等の要素を持つ

### numpy.ndarray.ravel()

平にした行列を返す。次元を一つ減らす？

```a.py
>>> X
array([[2, 3, 4],
       [2, 3, 4],
       [2, 3, 4]])
>>> X.ravel()
array([2, 3, 4, 2, 3, 4, 2, 3, 4])
```

### numpy.ndarray.T

行列の転地をする

```a.py
>>> x = np.array([[1,2],[3,4]])
>>> x
array([[1, 2],
       [3, 4]])
>>> x.T
array([[1, 3],
       [2, 4]])
>>>
```

## numpy.arange

階差数列を作る時とかに使う

`numpy.arange(start, end, step)`

`start`から`end`まで`step`刻みの階差数列を作る

```a.py
>>> import numpy as np
>>> np.arange(4)
array([0, 1, 2, 3])
>>> np.arange(0, 5, 2)
array([0, 2, 4])
```
## numpy.meshgrid

格子点を返してくれる。2つのベクトルや配列の

```a.py
>>> x = np.arange(2, 5)
>>> y = np.arange(2, 5)
>>> x
array([2, 3, 4])
>>> y
array([2, 3, 4])
>>> X, Y = np.meshgrid(x, y)
>>> X
array([[2, 3, 4],
       [2, 3, 4],
       [2, 3, 4]])
>>> Y
array([[2, 2, 2],
       [3, 3, 3],
       [4, 4, 4]])
```
