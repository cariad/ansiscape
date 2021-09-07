from typing import List, Union


class AttributeError(ValueError):
    def __init__(self, msg: str, attr: Union[List[int], int]) -> None:
        suffix = "attributes" if isinstance(attr, list) else "attribute"
        super().__init__(f"{msg} ({suffix}={attr})")
