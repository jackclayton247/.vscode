from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Iterator
from typing import Any, overload

class BaseRow:
    def __init__(
        self,
        __parent,
        __processors: Iterable[Callable[[Any], Any]] | None,
        __keymap: dict[Incomplete, Incomplete],
        __key_style: int,
        __row: Iterable[Any],
    ) -> None: ...
    def __reduce__(self) -> tuple[Incomplete, tuple[Incomplete, Incomplete]]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self, __key: str | int) -> tuple[Any, ...]: ...
    @overload
    def __getitem__(self, __key: slice) -> tuple[tuple[Any, ...]]: ...

def safe_rowproxy_reconstructor(__cls, __state): ...
