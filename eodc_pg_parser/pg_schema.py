# generated by datamodel-codegen:
#   filename:  https://openeo.org/documentation/1.0/developers/api/assets/pg-schema.json
#   timestamp: 2022-07-08T11:29:33+00:00

from __future__ import annotations

import json
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, Extra, Field, constr


class ResultReference(BaseModel, extra=Extra.forbid):
    from_node: str
    node: ProcessNode


class ParameterReference(BaseModel, extra=Extra.forbid):
    from_parameter: str


class ProcessArgument(BaseModel):
    __root__: Union[
        ResultReference,
        ParameterReference,
        ProcessGraph,
        List[Any],
        Dict[str, Any],
        float,
        bool,
        str,
    ]

    # TODO: get rid of this?
    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]


class ProcessNode(BaseModel):
    process_id: constr(regex=r'^\w+$')
    namespace: Optional[Optional[str]] = None
    result: Optional[bool] = False
    description: Optional[Optional[str]] = None
    arguments: Dict[str, Optional[ProcessArgument]]

    def __str__(self):
        return json.dumps(self.dict(), indent=4)


class ProcessGraph(BaseModel, extra=Extra.forbid):
    process_graph: Dict[str, ProcessNode]
    uid: UUID = Field(default_factory=uuid4)


class PGEdgeType(str, Enum):
    ResultReference = "result_reference"
    Callback = "callback"


ResultReference.update_forward_refs()
ProcessArgument.update_forward_refs()
