import numpy as np

import cvstruct.contours.utils as cnt_utils
import cvstruct.typedef.contours as cnt_type


def merge_two_contours(
    cnt1: cnt_type.ContourType,
    cnt2: cnt_type.ContourType,
) -> cnt_type.ContourType:
    if not is_clockwise(cnt1):
        cnt1 = cnt1[::-1]
    if is_clockwise(cnt2):
        cnt2 = cnt2[::-1]

    idx1, idx2 = cnt_utils.get_closest_point_idx(cnt1, cnt2)

    cnt1 = np.squeeze(cnt1)
    cnt2 = np.squeeze(cnt2)

    cnt_merged = []
    cnt_merged.append(cnt1[0:idx1])
    cnt_merged.append(cnt2[idx2:-1])
    cnt_merged.append(cnt2[0:idx2])
    cnt_merged.append(cnt1[idx1:-1])

    cnt_merged = np.concatenate(cnt_merged, axis = 0)
    cnt_merged = np.expand_dims(cnt_merged, 1)
    
    return cnt_merged

def merge_contour_group(
    cnt_group: cnt_type.ContourGroupType
) -> cnt_type.ContourType:
    cnt_merge = cnt_group["parent"]

    for child_cnt in cnt_group["children"]:
        cnt_merge = merge_two_contour(cnt_merge, child_cnt)
    
    return cnt_merge