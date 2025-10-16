# template_python

- コード依頼テンプレ

  - `main.py` と `utils.py` はサンプルなので、それ以外のファイルを git のルートに保存する。

  - 全部関数化する。

  - メインのスクリプトは、`main` とする。

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

  - precommit を有効化する。

    ```sh
    pre-commit install
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
