from pandas._typing import (
    FrameOrSeries as FrameOrSeries,
    FrameOrSeriesUnion as FrameOrSeriesUnion,
    Scalar as Scalar,
    AxisType as AxisType,
    KeysArgType,
)
from pandas.core.base import PandasObject as PandasObject, SelectionMixin as SelectionMixin
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import ops as ops
from pandas.core.indexes.api import Index as Index
from pandas.core.series import Series as Series
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, Union

class GroupByPlot(PandasObject):
    def __init__(self, groupby) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, name: str): ...

class _GroupBy(PandasObject, SelectionMixin):
    level = ...
    as_index = ...
    keys = ...
    sort = ...
    group_keys = ...
    squeeze = ...
    observed = ...
    mutated = ...
    obj = ...
    axis = ...
    grouper = ...
    exclusions = ...
    def __init__(
        self,
        obj: NDFrame,
        keys: Optional[KeysArgType] = ...,
        axis: int = ...,
        level=...,
        grouper: Optional[ops.BaseGrouper] = ...,
        exclusions=...,
        selection=...,
        as_index: bool = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: bool = ...,
        observed: bool = ...,
        mutated: bool = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    @property
    def groups(self) -> Dict[str, str]: ...
    @property
    def ngroups(self): ...
    @property
    def indices(self) -> Dict[str, Index]: ...
    def __getattr__(self, attr: str): ...
    def pipe(self, func: Callable, *args, **kwargs): ...
    plot = ...
    def get_group(self, name, obj: Optional[DataFrame] = ...) -> DataFrame: ...
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]: ...
    def apply(self, func: Callable, *args, **kwargs) -> FrameOrSeriesUnion: ...
    def transform(self, func: Callable, *args, **kwargs): ...

class GroupBy(_GroupBy):
    def count(self) -> FrameOrSeriesUnion: ...
    def mean(self, **kwargs) -> FrameOrSeriesUnion: ...
    def median(self, **kwargs) -> FrameOrSeriesUnion: ...
    def std(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def var(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def sem(self, ddof: int = ...) -> FrameOrSeriesUnion: ...
    def size(self) -> Series: ...
    def ohlc(self) -> DataFrame: ...
    def describe(self, **kwargs) -> FrameOrSeriesUnion: ...
    def resample(self, rule, *args, **kwargs): ...
    def rolling(self, *args, **kwargs): ...
    def expanding(self, *args, **kwargs): ...
    def pad(self, limit: Optional[int] = ...): ...
    def ffill(self, limit: Optional[int] = ...) -> FrameOrSeriesUnion: ...
    def backfill(self, limit: Optional[int] = ...) -> FrameOrSeriesUnion: ...
    def bfill(self, limit: Optional[int] = ...) -> FrameOrSeriesUnion: ...
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> FrameOrSeriesUnion: ...
    def quantile(self, q=..., interpolation: str = ...): ...
    def ngroup(self, ascending: bool = ...) -> Series: ...
    def cumcount(self, ascending: bool = ...) -> Series: ...
    def rank(
        self,
        method: str = ...,
        ascending: bool = ...,
        na_option: str = ...,
        pct: bool = ...,
        axis: int = ...,
    ) -> DataFrame: ...
    def cummax(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> FrameOrSeriesUnion: ...
    def shift(self, periods: int = ..., freq=..., axis: int = ..., fill_value=...): ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: str = ...,
        limit=...,
        freq=...,
        axis: AxisType = ...,
    ) -> FrameOrSeriesUnion: ...
    def head(self, n: int = ...) -> FrameOrSeriesUnion: ...
    def tail(self, n: int = ...) -> FrameOrSeriesUnion: ...
    # Surplus methodss from original pylance stubs; should they go away?
    def first(self, **kwargs) -> FrameOrSeriesUnion: ...
    def last(self, **kwargs) -> FrameOrSeriesUnion: ...
    def max(self, **kwargs) -> FrameOrSeriesUnion: ...
    def min(self, **kwargs) -> FrameOrSeriesUnion: ...
    def prod(self, **kwargs) -> FrameOrSeriesUnion: ...
    def sum(self, **kwargs) -> FrameOrSeriesUnion: ...

def get_groupby(
    obj: NDFrame,
    by: Optional[KeysArgType] = ...,
    axis: int = ...,
    level=...,
    grouper: Optional[ops.BaseGrouper] = ...,
    exclusions=...,
    selection=...,
    as_index: bool = ...,
    sort: bool = ...,
    group_keys: bool = ...,
    squeeze: bool = ...,
    observed: bool = ...,
    mutated: bool = ...,
) -> GroupBy: ...
