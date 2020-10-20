# pytorchの学習メモ

[公式ドキュメント](https://pytorch.org/)

## Tensors

`Tensors`はnumpyのndarraysのようなもの。GPUの高速計算にも対応している

```a.py
from __future__ import print_function
import torch
# 空の行列を用意する
x = torch.empty(5, 3)
# 乱数で初期化する
x = torch.rand(5, 3)
# 全部0で初期化する
x = torch.zeros(5, 3)
# 行列の表示
print(x)
```

実行結果

```
tensor([[3.7749e+07, 5.5351e-43, 3.7749e+07],
        [5.5351e-43, 3.7755e+07, 5.5351e-43],
        [3.7755e+07, 5.5351e-43, 3.7749e+07],
        [5.5351e-43, 3.7749e+07, 5.5351e-43],
        [3.7761e+07, 5.5351e-43, 3.7761e+07]])
```