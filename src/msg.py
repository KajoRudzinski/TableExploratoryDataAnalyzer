def get_initial_status():
    status = "Status: "
    return "{}Ready for work".format(status)


def get_initial_text_response():
    return "\n\tHi stranger!\n\n" \
        "\tOpen a csv / txt file to start the analysis :-)"


def start_app_msg():
    return "\nTEDA started"


def close_app_msg():
    return "\nTEDA closed"


def get_app_name():
    return "Table Exploratory Data Analysis"
