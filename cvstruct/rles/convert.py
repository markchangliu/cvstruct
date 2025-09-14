
import cv2
import pycocotools.mask as pycocomask

import cvstruct.contours.merge as cnt_merge
from cvstruct.typedef.masks import MaskType, MaskImgType
from cvstruct.typedef.rles import RLEType
from cvstruct.typedef.contours import ContourType, ContoursType


def rle_to_mask(
    rle: RLEType,
) -> MaskType:
    mask = pycocomask.decode(rle)
    return mask

def rle_to_contours(
    rle: RLEType,
    approx_flag: bool
) -> ContoursType:
    mask = rle_to_mask(rle).astype(np.uint8) * 255
    cnts, _ = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
    
    if not approx_flag:
        return cnts
    
    cnts_approx = []
    for cnt in cnts:
        eps = 0.001 * cv2.arcLength(contour, True)
        cnt_approx = cv2.approxPolyDP(cnt, eps, True)
        cnts_approx.append(cnt_approx)
    
    return cnts_approx

def rle_to_contour_merge(
    rle: RLEType,
    approx_flag: bool
) -> ContourType:
    mask = rle_to_mask(rle).astype(np.uint8) * 255
    cnts, hierarchies = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
    
    if approx_flag:
        cnts_approx = []
        for cnt in cnts:
            eps = 0.001 * cv2.arcLength(contour, True)
            cnt_approx = cv2.approxPolyDP(cnt, eps, True)
            cnts_approx.append(cnt_approx)
        
        cnts = cnts_approx
    
    if len(cnts) == 0:
        return cnts[0]
    
    cnt = cnt_merge.merge_contours(cnts, hierarchies)

    return cnt
    

