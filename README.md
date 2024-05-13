# gitのサンプル

起動

```bash
docker compose build
docker compose up -d
```

gitのバージョン

```bash
docker compose exec myubuntu git --version
```

gitの設定

```bash
docker compose exec myubuntu bash
git config --global user.name "Your Name"
git config --global user.email your@email.address.com
```

gitリポジトリの初期化

```bash
git init your_repository_name
cd your_repository_name/
```

ステージングとコミット

```bash
git add main.py
git commit -m "your commit lot" main.py
```

ログ表示

```bash
git log
```

作業ディレクトリの状態

```bash
git status
```

コミット間差分

```bash
git diff
```

ブランチ名の変更

```bash
git branch -M main
```

ブランチの作成

```bash
git branch new_branch_name
```

ブランチの切り替え

```bash
git branch branch_name
```

停止

```bash
docker compose down
```
