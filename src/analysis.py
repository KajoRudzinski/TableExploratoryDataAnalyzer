def get_column_summary(df):
    summary = []
    title = "\n\tColumns:\n\n"
    summary.append(title)
    for c in df.columns:
        x = "\t{}.\t{}{}\n".format(
            df.columns.get_loc(c) + 1,
            get_simple_type_from_dtype(str(df[c].dtype)),
            c)
        summary.append(x)
    summary = "".join(summary)
    return summary


def get_simple_type_from_dtype(dt: str):
    if dt == "float64" or dt == "int64":
        return "(measure):   "
    else:
        return "(dimension): "
