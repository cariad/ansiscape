from typing import Union

from ansiscape.types import Attributes


class AttributeError(ValueError):
    def __init__(self, msg: str, attr: Union[Attributes, int]) -> None:
        suffix = "attributes" if isinstance(attr, list) else "attribute"
        super().__init__(f"{msg} ({suffix}={attr})")
