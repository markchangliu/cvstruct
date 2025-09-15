import numpy as np

from cvstruct.typedef.insts import Insts


def sort_by_conf(insts: Insts) -> Insts:
    sort_idx = np.argsort(insts.confs)[::-1]
    confs = insts.confs[sort_idx]
    cat_ids = insts.cat_ids[sort_idx]
    bboxes = insts.bboxes[sort_idx, ...]

    if insts.masks is not None:
        insts.masks = insts.masks[sort_idx, ...]

    return insts