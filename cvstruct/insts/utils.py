
from typing import List

import numpy as np

from cvstruct.typedef.insts import Insts


def concat_insts(
    insts_list: List[Insts]
) -> Insts:
    confs_list = [i.confs for i in insts_list]
    cat_ids_list = [i.cat_ids for i in insts_list]
    bboxes_list = [i.bboxes for i in insts_list]
    masks_list = [i.masks for i in insts_list]

    new_confs = np.concatenate(confs_list)
    new_cat_ids = np.concatenate(cat_ids_list)
    new_bboxes = np.concatenate(bboxes_list, axis = 0)
    
    if None in masks_list:
        new_masks = None
    else:
        new_masks = np.concatenate(masks_list, axis = 0)

    new_insts = Insts(
        new_confs, new_cat_ids, new_bboxes, new_masks
    )

    return new_insts


def sort_by_conf(insts: Insts) -> Insts:
    sort_idx = np.argsort(insts.confs)[::-1]
    confs = insts.confs[sort_idx]
    cat_ids = insts.cat_ids[sort_idx]
    bboxes = insts.bboxes[sort_idx, ...]

    if insts.masks is not None:
        insts.masks = insts.masks[sort_idx, ...]

    return insts