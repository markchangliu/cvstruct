
import numpy as np

from cvstruct.typedef.contours import ContourType, ContoursType
from cvstruct.contours.utils import is_clockwise, get_closest_point_idx


def merge_two_contour(
    cnt1: ContourType,
    cnt2: ContourType,
) -> ContourType:
    if not is_clockwise(cnt1):
        cnt1 = cnt1[::-1]
    if is_clockwise(cnt2):
        cnt2 = cnt2[::-1]

    idx1, idx2 = get_closest_point_idx(cnt1, cnt2)

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

def merge_contours_parent_children(
    parent_cnt: ContourType,
    child_cnts: ContoursType
) -> ContourType:
    cnt_merge = parent_cnt

    for child_cnt in child_cnts:
        cnt_merge = merge_two_contour(cnt_merge, child_cnt)
    
    return cnt_merge

def merge_contours(
    cnts: ContoursType
) -> ContourType:
    cnt_merge = cnts[0]
    
    for cnt in cnts[1:]:
        cnt_merge = merge_two_contour(cnt_merge, cnt)
    
    return cnt_merge

