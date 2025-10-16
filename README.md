# template_python

- 基本設定

  - `main.py` と `utils.py` はサンプルなので、それ **以外のファイル** を git のルートに保存する。
 
  - `pip install -r requirements.txt` を実行する。
 
  - `pre-commit install` を実行する。

- リーダブルコードの作成依頼

  - 全部関数化する。

  - 以下の形式で実行をする。

    ```python
    if __name__ == "__main__":
        main(**vars(_retrieve_args()))
    ```

  - ファイルやディレクトリのパスは、pathlib.Path を用いる。

    ```python
    from pathlib import Path
    ```

  - matplotlib を使うときはオブジェクト思考で作る。

    ```python
    fig, ax = plt.subplots()

    ```

- 事前設定 (レポジトリオーナー向け)

  - 改行コードの統一

    ```sh
    $ cat .gitattributes
    * text eol=lf
    ```

  - gitignore 設定

    ```sh
    $ cat .gitignore
    .envrc
    .mypy_cache
    .swp
    ```
