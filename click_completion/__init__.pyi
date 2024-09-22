from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import click
from click import ParamType

__version__: str
_initialized: bool

def init(
    complete_options: bool = False,
    match_incomplete: Optional[Callable[[str, str], bool]] = None,
) -> None: ...

class DocumentedChoice(ParamType):
    name: str
    def __init__(self, choices: Union[Dict[str, str], Enum]) -> None: ...
    def get_metavar(self, param: Any) -> str: ...
    def get_missing_message(self, param: Any) -> str: ...
    def convert(self, value: str, param: Any, ctx: click.Context) -> Optional[str]: ...
    def __repr__(self) -> str: ...
    def complete(
        self, ctx: click.Context, incomplete: str
    ) -> List[Tuple[str, str]]: ...
