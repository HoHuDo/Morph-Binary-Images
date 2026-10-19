import numpy as np
import pytest
from scipy import ndimage

from src.morphology import dilate, erode, make_structuring_element

IMG = np.zeros((7, 7), dtype=np.uint8)
IMG[2:5, 2:5] = 1


def test_structuring_element_shapes():
    assert make_structuring_element("square", 3).sum() == 9
    assert make_structuring_element("cross", 3).sum() == 5


@pytest.mark.skip(reason="waiting for erode() implementation")
def test_erode_matches_scipy():
    se = make_structuring_element("square", 3)
    expected = ndimage.binary_erosion(IMG, structure=se).astype(np.uint8)
    assert np.array_equal(erode(IMG, se), expected)


@pytest.mark.skip(reason="waiting for dilate() implementation")
def test_dilate_matches_scipy():
    se = make_structuring_element("square", 3)
    expected = ndimage.binary_dilation(IMG, structure=se).astype(np.uint8)
    assert np.array_equal(dilate(IMG, se), expected)
