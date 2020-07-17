import pandas as pd

dimension = "dimension"
measure = "measure"


def to_sorted_list_of_tuples(series: pd.Series):
    return sorted(list(series.to_dict().items()))


class Column:
    """Given Pandas' Series (presumably a column) determines if this a
    numeric like column (measure) or categorical like column (dimension)
    and stores basic information."""
    def __init__(self, column: pd.Series):
        self.data = column
        self.name = str(column.name)
        self.type = self.get_type()
        self.count = column.size
        self.count_distinct = column.nunique(dropna=False)
        self.count_null = column.isna().sum()
        self.max_groups_allowed = 20    # for group by operations

    def get_position(self, df: pd.DataFrame, start_at=0):
        return df.columns.get_loc(self.name) + start_at

    def get_type(self):
        if self.data.dtype == "float64" or self.data.dtype == "int64":
            return measure
        else:
            return dimension


class Dimension(Column):
    """Given Pandas' Series with categorical data stores statistical
    statistical information on it."""
    def __init__(self, column: pd.Series):
        super().__init__(column)
        self.null_replacement = "_None_"
        self.data_without_nulls = column.fillna(value=self.null_replacement)

    def group_by(self, normalize=False):
        group = self.get_groups(normalize)
        return self.group_by_considering_size(group)

    def group_by_considering_size(self, group):
        if self.full_group_is_by_allowed(group):
            return to_sorted_list_of_tuples(group)
        else:
            return self.get_top_n_from_group(group)

    def get_top_n_from_group(self, group):
        return group.nlargest(self.max_groups_allowed, keep="all")

    def get_number_of_groups(self):
        return self.data_without_nulls.value_counts().len()

    def get_groups(self, normalize):
        return self.data_without_nulls.value_counts(normalize=normalize)

    def full_group_is_by_allowed(self, group):
        if len(group) <= self.max_groups_allowed:
            return True
        else:
            return False


class Measure(Column):
    """Given Pandas' Series with numerical data stores statistical
    statistical information on it."""
    def __init__(self, column: pd.Series):
        super().__init__(column)
        self.description = column.describe()
        self.mean = self.description.at["mean"]
        self.std_dev = self.description.at["std"]
        self.min = self.description.at["min"]
        self.max = self.description.at["max"]

        # refers to interquartile range (IQR)
        self.q1 = self.description.at["25%"]
        self.median = self.description.at["50%"]
        self.q3 = self.description.at["75%"]
        self.iqr = self.q3 - self.q1

