from typing import Tuple

import numpy as np
import pycocotools.mask as pycocomask

from cvstruct.typedef.polys import PolyLabelmeType, PolyCocoType
from cvstruct.typedef.contours import ContourType
from cvstruct.typedef.masks import RLEType


def poly_labelme_to_contour(
    poly: PolyLabelmeType
) -> ContourType:
    cnt = np.asarray(poly, dtype = np.int32)
    cnt = np.expand_dims(cnt, 1)
    return cnt

def poly_labelme_to_coco(
    poly: PolyLabelmeType
) -> PolyCocoType:
    poly = np.asarray(poly).flatten().tolist()
    return poly

def poly_labelme_to_rle(
    poly: PolyLabelmeType,
    img_hw: Tuple[int, int]
) -> RLEType:
    poly = poly_labelme_to_coco(poly)
    rle = pycocomask.frPyObjects([poly], img_hw[0], img_hw[1])[0]
    return rle