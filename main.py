import argparse
from logging import getLogger
from pathlib import Path

import matplotlib_fontja  # noqa

from utils import set_base_log_level, set_log_level


def _retrieve_args():
    parser = argparse.ArgumentParser(
        description="description of the code",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--directory",
        type=Path,
        default=Path("/path/to/directory"),
        help="set directory path",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("/path/to/file"),
        help="set file path",
    )
    parser.add_argument(
        "--param",
        type=str,
        required=True,
        help="str parameter",
    )
    parser.add_argument(
        "--choise-param",
        type=str,
        choices=["a", "b"],
        nargs="+",
        help="choice param",
    )
    parser.add_argument(
        "--show",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="plot を表示する/しない (デフォルトは表示する)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=1,
        help="increase output verbosity",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="count",
        default=0,
        help="decrease output verbosity",
    )

    args = parser.parse_args()

    if not args.directory.is_dir():
        raise FileNotFoundError(f"{args.directory}")

    if not args.file.is_file():
        raise FileNotFoundError(f"{args.file}")

    args.verbose -= args.quiet
    del args.quiet

    return args


def main(
    directory: Path,
    file: Path,
    param: str,
    choise_param: list[str],
    show: bool,
    verbose: int,
) -> None:
    logger = getLogger(__name__)
    set_base_log_level(verbose)
    set_log_level(["PIL", "matplotlib"])
    logger.info("start")


if __name__ == "__main__":
    main(**vars(_retrieve_args()))
