
columns = None





def get_column_summary(df):
    described_columns = []
    title = "\n\tColumns:\n\n"
    described_columns.append(title)
    get_all_columns_basic_info(described_columns, df)
    described_columns = "".join(described_columns)
    return described_columns


def get_all_columns_basic_info(described_columns, df):
    for column in df.columns:
        current_column = get_column_basic_info(column, df)
        described_columns.append(current_column)


def get_column_basic_info(column, df):

    col_position = get_column_loc_base_1(column, df)

    col_type = get_simple_type_from_dtype(
        convert_dtype_to_string(column, df))

    current_column = "\t{}.\t{}{}\n".format(
            col_position, col_type, column)

    return current_column


def get_column_loc_base_1(column, df):
    return df.columns.get_loc(column) + 1


def convert_dtype_to_string(column, df):
    return str(df[column].dtype)


def get_simple_type_from_dtype(dt: str):
    if dt == "float64" or dt == "int64":
        return "(measure):   "
    else:
        return "(dimension): "
