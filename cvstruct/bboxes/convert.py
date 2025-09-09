

import numpy as np

from cvstruct.typedef.bboxes import BBoxesXYXYType, BBoxesXYWHType


def bboxes_xyxy2xywh(
    bboxes_xyxy: BBoxesXYXYType
) -> BBoxesXYWHType:
    bboxes_xywh = bboxes_xyxy.copy()
    bboxes_xywh[:, [2, 3]] = bboxes_xyxy[:, [2, 3]] - bboxes_xyxy[:, [0, 1]]
    return bboxes_xywh

def bboxes_xywh2xyxy(
    bboxes_xywh: BBoxesXYWHType
) -> BBoxesXYXYType:
    bboxes_xyxy = bboxes_xywh.copy()
    bboxes_xyxy[:, [2, 3]] = bboxes_xywh[:, [0, 1]] + bboxes_xywh[:, [2, 3]]
    return bboxes_xyxy