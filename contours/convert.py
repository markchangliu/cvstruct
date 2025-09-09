import os
from typing import Union, Tuple

import cv2
import numpy as np
import numpy.typing as npt
import pycocotools.mask as pycocomask

from typedef.contours import ContoursType, ContourType
from typedef.polys import PolyLabelmeType, PolysLabelmeType, PolyCocoType, PolysCocoType
from typedef.masks import RLEType, RLEsType, MaskType, MasksType


def contour_to_poly_labelme(
    cnt: ContourType
) -> PolyLabelmeType:
    poly_labelme = np.squeeze(cnt).tolist()
    return poly_labelme

def contours_to_polys_labelme(
    cnts: ContoursType
) -> PolysLabelmeType:
    polys_labelme = []

    for cnt in cnts:
        polys_labelme = contour_to_poly_labelme(cnt)
        polys_labelme.append(polys_labelme)

    return polys_labelme

def contour_to_poly_coco(
    cnt: ContourType
) -> PolyCocoType:
    poly_coco = cnt.flatten().tolist()
    return poly_coco

def contours_to_polys_coco(
    cnts: ContoursType
) -> PolysCocoType:
    polys_coco = []

    for cnt in cnts:
        poly_coco = contour_to_poly_coco(cnt)
        polys_coco.append(poly_coco)
    
    return polys_coco

def contour_to_rle(
    cnt: ContourType,
    img_hw: Tuple[int, int]
) -> RLEType:
    poly_coco = contour_to_poly_coco(cnt)
    rle = pycocomask.frPyObjects([poly_coco], img_hw[0], img_hw[1])[0]
    return rle

def contours_to_rles(
    cnts: ContoursType,
    img_hw: Tuple[int, int]
) -> RLEsType:
    polys_coco = contours_to_polys_coco(cnts)
    rles = pycocomask.frPyObjects(polys_coco, img_hw[0], img_hw[1])
    return rles

def contours_to_rle_merge(
    cnts: ContoursType,
    img_hw: Tuple[int, int]
) -> RLEType:
    rles = contours_to_rles(cnts, img_hw)
    rle_merge = pycocomask.merge(rles, False)
    return rle_merge
    
def contour_to_mask(
    cnt: ContourType,
    img_hw: Tuple[int, int]
) -> MaskType:
    rle = contour_to_rle(cnt, img_hw)
    mask = pycocomask.decode(rle).astype(np.bool_)
    return mask

def contours_to_masks(
    cnts: ContoursType,
    img_hw: Tuple[int, int]
) -> MasksType:
    rles = contours_to_rles(cnts, img_hw)
    masks = pycocomask.decode(rles).astype(np.bool_)
    masks = np.transpose(masks, (2, 0, 1))
    return masks

def contours_to_mask_merge(
    cnts: ContoursType,
    img_hw: Tuple[int, int]
) -> MaskType:
    rle_merge = contours_to_rle_merge(cnts, img_hw)
    mask_merge = pycocomask.decode(rle_merge).astype(np.bool_)
    return mask_merge