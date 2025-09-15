import cvstruct.typedef.bboxes as bbox_type


def bboxes2bboxes_xyxy2xywh(
    bboxes_xyxy: bbox_type.BBoxesXYXYType
) -> bbox_type.BBoxesXYWHType:
    bboxes_xywh = bboxes_xyxy.copy()
    bboxes_xywh[:, [2, 3]] = bboxes_xyxy[:, [2, 3]] - bboxes_xyxy[:, [0, 1]]
    return bboxes_xywh

def bboxes2bboxes_xywh2xyxy(
    bboxes_xywh: bbox_type.BBoxesXYWHType
) -> bbox_type.BBoxesXYXYType:
    bboxes_xyxy = bboxes_xywh.copy()
    bboxes_xyxy[:, [2, 3]] = bboxes_xywh[:, [0, 1]] + bboxes_xywh[:, [2, 3]]
    return bboxes_xyxy