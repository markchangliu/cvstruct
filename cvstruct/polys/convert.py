
import numpy as np

from cvstruct.typedef.polys import PolyLabelmeType
from cvstruct.typedef.contours import ContourType


def poly_labelme_to_contour(
    poly: PolyLabelmeType
) -> ContourType:
    cnt = np.asarray(poly, dtype = np.int32)
    cnt = np.expand_dims(cnt, 1)
    return cnt