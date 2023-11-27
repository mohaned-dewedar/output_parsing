from typing import List, Union, Any, Optional
from pydantic import BaseModel, Field

class Condition(BaseModel):
    field: str = Field(..., description="The field specified")
    operator: str = Field(..., description="The operator to use [==, !=, in, >, <, etc.]")
    value: Union[Any, List[Any]] = Field(..., description="The value or list of values to compare with")
    sub_conditions: List['Condition'] = Field(default_factory=list, description="Nested sub-conditions")

Condition.model_rebuild()

class Outcome(BaseModel):
    field: str = Field(..., description="Claims amount or somehting else")
    operator: str = Field(description="Mathematical operation to apply [+,-,*,/] or ==")
    value: Union[float, str] = Field(..., description="The value or factor to be applied in the operation")

class Rule(BaseModel):
    conditions: List[Condition] = Field(..., description="List of conditions")
    condition_operator: Optional[str] = Field(None, description="The operator to use [and, or, etc.]")
    outcome: Outcome

class Rules(BaseModel):
    rules: List[Rule] = Field(..., description="List of rules")
