status_file_read_ok = "File read correctly"


def get_response_text_initial():
    return "\n\tHi stranger!\n\n" \
        "\tOpen a csv / txt file to start the analysis :-)"


def get_response_text_file_read_ok(file: str):
    return "\n\tGreat!\n\n" \
        "\tClick 'Analyse' to get insights " \
           "about the dataset inside the file '{}'.".format(file)


def get_response_text_error():
    return "\n\tOops!\n\n" \
        "\tSomething went wrong :( Check the status."


def format_status(s: str, error=False):
    if not error:
        return "Status [OK]: {}".format(s)
    else:
        return "Status [ERROR]: {}".format(s)


def start_app_msg():
    return "\nTEDA started"


def close_app_msg():
    return "\nTEDA closed"


def get_app_name():
    return "Table Exploratory Data Analysis"
