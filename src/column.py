import pandas as pd
import heapq as hq

dimension = "dimension"
measure = "measure"


class Column:
    """Given Pandas' Series (presumably a column) determines if this a
    numeric like column (measure) or categorical like column (dimension)
    and stores basic information"""
    def __init__(self, column: pd.Series):
        self.data: pd.Series = column
        self.name: str = str(column.name)
        self.type: str = self.get_type()
        self.count: int = column.size
        self.count_distinct: int = column.nunique(dropna=False)
        self.count_null: int = column.isna().sum()

    def get_position(self, df: pd.DataFrame, start_at=0) -> int:
        return df.columns.get_loc(self.name) + start_at

    def get_type(self) -> str:
        if self.data.dtype == "float64" or self.data.dtype == "int64":
            return measure
        else:
            return dimension


class Dimension(Column):
    """Given Pandas' Series with categorical data stores statistical
    statistical information on it"""
    def __init__(self, column: pd.Series):
        super().__init__(column)
        self.data_filled_na: pd.Series = column.fillna(value="_None_")
        self.groups_allowed = 20

    def group_by_distinct(
            self, relative: bool = False, top_n: int = None) -> dict:
        if top_n is None:
            return self._group_by(relative=relative)
        else:
            return self._group_by_top_n(relative=relative, top_n=top_n)

    def _group_by_top_n(self, relative: bool, top_n: int):
        d = self._group_by(relative=relative)
        return hq.nlargest(top_n, d, key=d.get)

    def _group_by(self, relative: bool):
        if relative is True:
            groups = self.data_filled_na.value_counts(normalize=True)
        else:
            groups = self.data_filled_na.value_counts()
        if groups.len() > self.groups_allowed:
            return groups
        else:
            return {"Many values": 1}
