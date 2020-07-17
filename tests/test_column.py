import pandas as pd
import numpy as np
from src import column as c

test_df = pd.DataFrame(
    {"pear": [1, 2, 3],
     "apple": [2, 3, 4],
     "orange": [3, 4, 5]})

test_df_col_1 = test_df.iloc[:, 1]





def test_store_column_as_series():
    assert c.Column(test_df_col_1).data.all() == test_df_col_1.all()


def test_store_column_name():
    assert c.Column(test_df_col_1).name == test_df_col_1.name


def test_column_position_base_0():
    t = c.Column(test_df_col_1)
    assert test_df.columns.get_loc("apple") == \
           t.get_position(test_df)


def test_column_position_base_1():
    t = c.Column(test_df_col_1)
    assert test_df.columns.get_loc("apple") + 1 == \
           t.get_position(test_df, start_at=1)


def test_column_values_distinct_count_include_null():
    t = pd.DataFrame({"test": [3, 1, 2, 3, 1, 4, np.nan]})
    assert c.Column(get_first_col(t)).count_distinct == 5


def get_first_col(t):
    return t.iloc[:, 0]


def test_column_values_count_include_null():
    t = pd.DataFrame({"test": [3, 1, 2, 3, 1, 4, np.nan]})
    assert c.Column(get_first_col(t)).count == 7


def test_column_count_nulls():
    t = pd.DataFrame({"test": [3, 1, 2, np.nan, 1, 4, np.nan]})
    assert c.Column(get_first_col(t)).count_null == 2


def test_measure_is_str_measure():
    assert c.measure == "measure"


def test_dimension_is_str_dimension():
    assert c.dimension == "dimension"


def test_column_type_given_int_only_returns_measure():
    t = pd.DataFrame({"test": [3, 1]})
    assert c.Column(get_first_col(t)).type == c.measure


def test_column_type_given_int_null_returns_measure():
    t = pd.DataFrame({"test": [3, np.nan]})
    assert c.Column(get_first_col(t)).type == c.measure


def test_column_type_given_not_int_only_returns_dimension():
    t = pd.DataFrame({"test": ["a", "b"]})
    assert c.Column(get_first_col(t)).type == c.dimension


def test_column_type_given_not_int_null_returns_dimension():
    t = pd.DataFrame({"test": ["a", np.nan]})
    assert c.Column(get_first_col(t)).type == c.dimension


def test_column_type_given_not_int_and_int_returns_dimension():
    t = pd.DataFrame({"test": ["a", 1]})
    assert c.Column(get_first_col(t)).type == c.dimension


def test_dimension_inheritance_using_count_from_column_class():
    t = pd.DataFrame({"test": ["a", np.nan]})
    assert c.Dimension(get_first_col(t)).count == 2


def test_dimension_group_by_normal_size():
    t = pd.DataFrame({"test": [np.nan, "a", "b", "b", np.nan]})
    dt = c.Dimension(get_first_col(t))
    assert dt.group_by() == [('_None_', 2), ('a', 1), ('b', 2)]


def test_dimension_group_by_normal_size_normalized():
    t = pd.DataFrame({"test": [np.nan, "a", "b", "b", np.nan]})
    dt = c.Dimension(get_first_col(t))
    assert dt.group_by(normalize=True) == [
        ('_None_', 0.4), ('a', 0.2), ('b', 0.4)]


def test_dimension_group_by_limit_group_size():
    t = pd.DataFrame({"test": [np.nan, "a", "b", "b", np.nan, "c"]})
    dt = c.Dimension(get_first_col(t))
    dt.max_groups_allowed = 2
    test = dt.group_by()
    assert len(test) == dt.max_groups_allowed


def test_measure_mean():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.mean == 3.4285714285714284


def test_measure_std_dev():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.std_dev == 1.7182493859684491


def test_measure_min():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.min == 1


def test_measure_max():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.max == 6


def test_measure_q1():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.q1 == 2.5


def test_measure_median():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.median == 3


def test_measure_q3():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.q3 == 4.5


def test_measure_iqr():
    t = pd.DataFrame({"test": [np.nan, 1, 2, 3, 3, 4, 5, 6]})
    dt = c.Measure(get_first_col(t))
    assert dt.iqr == 2

