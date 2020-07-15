import pandas as pd
import numpy as np
from src import column as c

test_df = pd.DataFrame(
    {"pear": [1, 2, 3],
     "apple": [2, 3, 4],
     "orange": [3, 4, 5]})

test_df_col_1 = test_df.iloc[:, 1]


def list_and_sort_dict(d: dict):
    d = d.items()
    d = sorted(d)
    return d


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


def test_dimension_count_distinct_abs_dict():
    t = pd.DataFrame({"test": ["a", "b", "b", np.nan]})
    dt = c.Dimension(get_first_col(t))
    test = dt.group_by_distinct()
    expected = {"_None_": 1, "b": 2, "a": 1}
    assert list_and_sort_dict(expected) == list_and_sort_dict(test)


def test_dimension_count_distinct_rel_dict():
    t = pd.DataFrame({"test": ["a", "b", "b", np.nan]})
    dt = c.Dimension(get_first_col(t))
    test = dt.group_by_distinct(relative=True)
    expected = {"_None_": 0.25, "b": 0.5, "a": 0.25}
    assert list_and_sort_dict(expected) == list_and_sort_dict(test)


def test_dimension_count_distinct_abs_dict_top_2():
    t = pd.DataFrame({"test": ["a", np.nan, "b", "b", np.nan]})
    dt = c.Dimension(get_first_col(t))
    test = dt.group_by_distinct(top_n=2)
    expected = {"_None_": 2, "b": 2}
    assert list_and_sort_dict(expected) == list_and_sort_dict(test)