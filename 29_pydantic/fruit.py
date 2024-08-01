from typing import Annotated, Dict, List, Literal, Tuple

from annotated_types import Gt

from pydantic import BaseModel


class Fruit(BaseModel):
    name: str  
    color: Literal['red', 'green']  
    weight: Annotated[float, Gt(0)]  
    bazam: Dict[str, List[Tuple[int, bool, float]]]  

