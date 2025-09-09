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