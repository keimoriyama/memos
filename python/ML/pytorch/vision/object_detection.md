# TORCHVISION OBJECT DETECTION FINETUNING TUTORIAL

Mask R-CNNをファインチューニングして通行人の検知をする。

## データセットの定義

データセットは`torch.utils.data.Dataset`クラスを継承し、`__len__`メソッド、`__getitem__`メソッドを実装する必要がある

`__getitem__`は次の要素を返す必要がある。

- image:大きさ`(H, W)`のPIL（python image library)の画像

- target:以下のフィールドを持つ辞書
  - boxes([N, 4]): 0~W,0~Hの範囲のボックス`[x0, y0, x1, y1]`
  - labels([N]): 囲ってある箱の番号（0番は何も無い事を表す）
  - image_id([1]): 画像の識別番号
  - area([N]): 境界線の場所。COCOデータセットを使っているときに、境界線の大きさの評価に使う
  - iscrowd([N]): iscrowdがTrueのときに、評価時に使われない

## PennFudanを使ってデータセットを作る

[PennFudanのURL](https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip)