# template_python

- コード依頼テンプレ

  - 全部関数化する。

  - メインのスクリプトは、`main` とする。

  - 以下の形式で実行をする。

    ```python
    if __name__ == "__main__":
        main(**vars(_retrieve_argparse()))
    ```

  - `isort` + `black` でフォーマットをかける。

  - ファイルやディレクトリのパスは、pathlib.Path を用いる。

    ```python
    from pathlib import Path
    ```

  - matplotlib を使うときはオブジェクト思考で作る。

    ```python
    fig, ax = plt.subplots()

    ```

- 事前設定

  - 改行コードの統一

    ```sh
    $ cat .gitattributes
    * text eol=lf
    ```

  - gitignore 設定

    ```sh
    $ cat .gitignore
    .envrc
    ```
