from typing import List, Optional, Tuple

import click

def param_type_complete(
    self: click.ParamType, ctx: click.core.Context, incomplete: str
) -> List[Tuple[str, Optional[str]]]: ...
def choice_complete(
    self: click.Choice, ctx: click.core.Context, incomplete: str
) -> List[Tuple[str, Optional[str]]]: ...
def multicommand_get_command_short_help(
    self: click.MultiCommand, ctx: click.Context, cmd_name: str
) -> str: ...
def multicommand_get_command_hidden(
    self: click.MultiCommand, ctx: click.Context, cmd_name: str
) -> bool: ...
def _shellcomplete(
    cli: click.Command, prog_name: str, complete_var: Optional[str] = None
) -> None: ...
def patch() -> None: ...
