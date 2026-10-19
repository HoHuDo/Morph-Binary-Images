"""Core morphological operations on binary images (to be implemented).

Conventions:
- Binary image: 2D numpy array, dtype uint8, values in {0, 1} (foreground = 1).
- Structuring element (SE): 2D numpy array of {0, 1} with odd dimensions, origin at center.
"""
import numpy as np


def make_structuring_element(shape: str = "square", size: int = 3) -> np.ndarray:
    """Create a structuring element: 'square', 'cross' or 'disk'."""
    if size % 2 == 0:
        raise ValueError("size must be odd")
    if shape == "square":
        return np.ones((size, size), dtype=np.uint8)
    if shape == "cross":
        se = np.zeros((size, size), dtype=np.uint8)
        se[size // 2, :] = 1
        se[:, size // 2] = 1
        return se
    if shape == "disk":
        r = size // 2
        y, x = np.ogrid[-r:r + 1, -r:r + 1]
        return (x * x + y * y <= r * r).astype(np.uint8)
    raise ValueError(f"unknown shape: {shape}")


def erode(img: np.ndarray, se: np.ndarray) -> np.ndarray:
    """Binary erosion. TODO: implement from scratch."""
    raise NotImplementedError


def dilate(img: np.ndarray, se: np.ndarray) -> np.ndarray:
    """Binary dilation. TODO: implement from scratch."""
    raise NotImplementedError


def opening(img: np.ndarray, se: np.ndarray) -> np.ndarray:
    """Opening = erosion followed by dilation."""
    return dilate(erode(img, se), se)


def closing(img: np.ndarray, se: np.ndarray) -> np.ndarray:
    """Closing = dilation followed by erosion."""
    return erode(dilate(img, se), se)
