
import numpy as np

import cvstruct.merge.utils as utils
import cvstruct.merge.subs as subs
import cvstruct.typedef.contours as cnt_type


def merge_contours(
    cnts: cnt_type.ContoursType,
    hierarchies: cnt_type.HierarchiesType
) -> cnt_type.ContourType:
    cnt_groups = utils.get_contour_groups(cnts, hierarchies)

    cnts_group_merge = []
    for cnt_group in cnt_groups:
        cnt_group_merge = subs.merge_contour_group(cnt_group)
        cnts_group_merge.append(cnt_group)
    
    cnt_merge = cnts_group_merge[0]
    for cnt in cnts_group_merge[1:]:
        cnt_merge = subs.merge_two_contours(cnt_merge, cnt)
    
    return cnt

