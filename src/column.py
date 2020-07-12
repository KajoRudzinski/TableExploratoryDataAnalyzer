import pandas as pd

dimension = "dimension"
measure = "measure"


class Column:
    def __init__(self, column: pd.Series):
        self.data = column
        self.name = column.name
        self.type = self.get_type()
        self.count = column.size
        self.count_distinct = column.nunique(dropna=False)
        self.count_null = column.isna().sum()

    def get_position_dataframe_base_0(self, df: pd.DataFrame):
        return df.columns.get_loc(self.name)

    def get_position_dataframe_base_1(self, df: pd.DataFrame):
        return df.columns.get_loc(self.name) + 1

    def get_type(self):
        if self.data.dtype == "float64" or self.data.dtype == "int64":
            return measure
        else:
            return dimension


class Dimension(Column):
    def __init__(self, column: pd.Series):
        super().__init__(column)
        self.test = "test"
