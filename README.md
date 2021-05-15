# Pythonボイラープレート

Python Template Repository

* .gitignore
* docker によるインフラのコード化・コンテナ化
* 設定ファイルの読み込み
  * settings.json
  * secrets.json
* コマンド引数のパース
* ロガー
  * ログの stderr 及びファイル出力
  * ログファイルのローテーション
* pytest
  * tests ディレクトリから src へのパス解決
* 起動シェル

など

参考： [Python 3 boilerplate - python-boilerplate.com](https://www.python-boilerplate.com/py3+executable)

## 使い方

* 今回用のリポジトリ作成

```bash
# git clone https://github.com/bulldra/python-boilerplate.git project
# cd project
# git init
# git remote -v
# git remote set-url origin https://github.com/xxx/xxx.git
# git remote -v
# git branch -m master
# git add .
# git commit -m 'clone from boilerplate'
# git push origin master
```
