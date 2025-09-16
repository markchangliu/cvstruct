from typing import Tuple

import numpy as np
import pycocotools.mask as pycocomask

import cvstruct.typedef.polys as poly_type
import cvstruct.typedef.rles as rle_type


def poly2rle_labelme(
    poly: poly_type.PolyLabelmeType,
    img_hw: Tuple[int, int]
) -> rle_type.RLEType:
    poly = np.asarray(poly, dtype = np.int32).flatten().tolist()
    rle = pycocomask.frPyObjects([poly], img_hw[0], img_hw[1])[0]
    return rle

def poly2rle_coco(
    poly: poly_type.PolyLabelmeType,
    img_hw: Tuple[int, int]
) -> rle_type.RLEType:
    rle = pycocomask.frPyObjects([poly], img_hw[0], img_hw[1])[0]
    return rle

def poly2rle_yolo(
    poly: poly_type.PolyYoloType,
    img_hw: Tuple[int, int]
) -> rle_type.RLEType:
    poly = np.asarray(poly).reshape(-1, 2)
    img_wh = np.asarray((img_hw[1], img_hw[0])).reshape(-1, 2)
    poly = (poly * img_wh).astype(np.int32).flatten().tolist()
    rle = pycocomask.frPyObjects([poly], img_hw[0], img_hw[1])[0]
    return rle
