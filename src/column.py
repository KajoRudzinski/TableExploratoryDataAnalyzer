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

    def group_by_distinct(self, rel_or_abs="abs", top_n=None) -> dict:
        if top_n is None:
            return self._group_by(rel_or_abs=rel_or_abs)
        else:
            return self._group_by_top_n(rel_or_abs, top_n)

    def _group_by_top_n(self, rel_or_abs, top_n):
        d = self._group_by(rel_or_abs=rel_or_abs)
        return hq.nlargest(top_n, d, key=d.get)

    def _group_by(self, rel_or_abs="abs"):
        if rel_or_abs == "abs":
            return self.data_filled_na.value_counts()
        if rel_or_abs == "rel":
            return self.data_filled_na.value_counts(normalize=True)

