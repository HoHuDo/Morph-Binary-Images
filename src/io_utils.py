"""Helpers for loading, binarizing and saving images."""
import cv2
import numpy as np


def load_binary(path: str, threshold: int = 127) -> np.ndarray:
    """Load an image as grayscale and binarize to {0, 1} (uint8)."""
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise FileNotFoundError(path)
    return (gray > threshold).astype(np.uint8)


def save_binary(path: str, img: np.ndarray) -> None:
    """Save a {0, 1} image as a 0/255 PNG."""
    cv2.imwrite(path, (img * 255).astype(np.uint8))
