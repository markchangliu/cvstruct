from typing import Dict, Any, List

try:
    from typing import TypeAlias
except:
    from typing_extensions import TypeAlias


RLEType: TypeAlias = Dict[str, Any]
"""
`RLEType`
    `Dict[str, Any]`, `{"size": [img_h, img_w], "counts": "XXXXX"}`
"""

RLEsType: TypeAlias = List[Dict[str, Any]]
"""
`RLEsType`
    `List[Dict[str, Any]]`, `[rle1, rle2, ...]`
"""