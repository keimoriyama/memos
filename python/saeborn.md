# seaborn(データの可視化)

matplotlib よりも簡単に可視化できるらしい

[公式ドキュメント](https://seaborn.pydata.org/)

```
import seaborn as sns
# dataには描画もとのデータを入れる
# xのデータに対してhueのデータの集計を取る
sns.countplot(x='SibSp',hue='Survived', data = train)
plt.legend(loc= 'upper right', title = 'survived')
```