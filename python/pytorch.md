# pytorchの学習メモ

[公式ドキュメント](https://pytorch.org/)

## Tensors

`Tensors`はnumpyのndarraysのようなもの。GPUの高速計算にも対応している

```a.py
from __future__ import print_function
import torch

x = torch.empty(5, 3)
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