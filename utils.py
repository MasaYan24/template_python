import logging as log_module
import time
from functools import wraps
from logging import getLogger

import cv2
import japanize_matplotlib  # noqa
import numpy as np


def retrieve_logging(verbosity: int) -> int:
    if verbosity < -1:
        return log_module.CRITICAL
    if verbosity == -1:
        return log_module.ERROR
    if verbosity == 0:
        return log_module.WARNING
    if verbosity == 1:
        return log_module.INFO
    if verbosity == 2:
        return log_module.DEBUG
    return log_module.NOTSET


def set_base_log_level(verbosity: int) -> None:
    log_module.basicConfig(level=retrieve_logging(verbosity))


def set_log_level(loggers: list[str], level: int = log_module.WARNING) -> None:
    for lgr in loggers:
        log_module.getLogger(lgr).setLevel(level=level)


def stop_watch(func):
    """
    ref: https://tksmml.hatenablog.com/entry/2019/10/26/003032
    """
    logger = getLogger(__name__).getChild("stop_watch")

    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()

        result = func(*args, **kargs)

        elapsed_time = time.time() - start

        logger.debug(f"{elapsed_time * 1000} ms in {func.__name__}")
        return result

    return wrapper


def on_mouse(event, x, y, flags, params) -> None:
    img: np.ndarray = params["image"].copy()
    wname: str = params["window_name"]
    plist: list[tuple[int, int]] = params["point_list"]

    # add point
    if event == cv2.EVENT_LBUTTONDOWN:
        plist.append((x, y))

    # delete point
    if event == cv2.EVENT_RBUTTONDOWN:
        plist.pop(-1)

    # show cross
    if event == cv2.EVENT_MOUSEMOVE:
        h, w, _ = img.shape
        cv2.line(img, (x, 0), (x, h - 1), (0, 255, 0))
        cv2.line(img, (0, y), (w - 1, y), (0, 255, 0))

    # draw points and lines
    for i in range(len(plist)):
        cv2.circle(img, plist[i], 3, (0, 0, 255), 1)
        if 0 < i:
            cv2.line(img, plist[i], plist[i - 1], (0, 255, 0), 1)

    if 0 < len(plist):
        cv2.line(img, (x, y), plist[len(plist) - 1], (0, 255, 0), 1)

    # output text
    cv2.putText(
        img,
        f"({x}, {y})",
        (0, 20),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )

    cv2.imshow(wname, img)


def put_text_on_image(
    image: np.ndarray,
    text: str,
    position: tuple[int, int] = (40, 40),
    font_face: int = cv2.FONT_HERSHEY_SIMPLEX,
    font_scale: float = 1.0,
    color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 1,
    line_type: int = 1,
    bg_color: tuple[int, int, int] | None = None,
) -> np.ndarray:
    _img = image.copy()

    if bg_color is not None:
        x, y = position
        (text_w, text_h), _ = cv2.getTextSize(
            text, font_face, font_scale, thickness
        )
        cv2.rectangle(_img, (x, y - text_h), (x + text_w, y), bg_color, -1)
    cv2.putText(
        _img,
        text=text,
        org=position,
        fontFace=font_face,
        fontScale=font_scale,
        color=color,
        thickness=thickness,
        lineType=line_type,
    )
    return _img


def put_stacked_texts_on_image(
    image: np.ndarray,
    texts: list[str],
    font_face: int = cv2.FONT_HERSHEY_SIMPLEX,
    font_scale: float = 1.0,
    color: tuple[int, int, int] = (255, 255, 255),
    thickness: int = 1,
    line_type: int = 1,
    start_position: tuple[int, int] = (40, 40),
    stack_height: int = 40,
    bg_color: tuple[int, int, int] | None = None,
) -> np.ndarray:
    _img = image.copy()
    for i, text in enumerate(texts):
        _img = put_text_on_image(
            _img,
            text=text,
            position=(start_position[0], start_position[0] + i * stack_height),
            font_face=font_face,
            font_scale=font_scale,
            color=color,
            thickness=thickness,
            line_type=line_type,
            bg_color=bg_color,
        )
    return _img


def draw_grid(image: np.ndarray, grid_width: int) -> None:
    _img = image.copy()
    height, width = _img.shape[:2]

    # Draw vertical grid lines
    for x in range(0, width, grid_width):
        cv2.line(_img, (x, 0), (x, height), (0, 255, 0), 1)

    # Draw horizontal grid lines
    for y in range(0, height, grid_width):
        cv2.line(_img, (0, y), (width, y), (0, 255, 0), 1)

    cv2.imshow("grid", _img)
    cv2.waitKey()
