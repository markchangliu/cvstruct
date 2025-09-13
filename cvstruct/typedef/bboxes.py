from typing import Tuple

try:
    from typing import TypeAlias
except:
    from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt


BBoxesXYXYType: TypeAlias = npt.NDArray[np.number]
"""
`BBoxesXYXYType`
    `NDArray[np.number]`, `(num_bboxes, 4)`, `[[x1, y1, x2, y2], ...]`
"""

BBoxesXYWHType: TypeAlias = npt.NDArray[np.number]
"""
`BBoxesXYWHType`
    `NDArray[np.number]`, `(num_bboxes, 4)`, `[[x1, y1, w, h], ...]`
"""

BBoxLabelmeType: TypeAlias = Tuple[Tuple[float, float], Tuple[float, float]]
"""
`BBoxLabelmeType`
    `Tuple[Tuple[float, float], Tuple[float, float]], `(2, (2, ))`, `[[x1, y1], [x2, y2]], ...]`
"""

BBoxCOCOType: TypeAlias = Tuple[float, float, float, float]
"""
`BBoxCOCOType`
    `Tuple[float, float, float, float]`, `(4, )`, `[x1, y1, w, h]`
"""