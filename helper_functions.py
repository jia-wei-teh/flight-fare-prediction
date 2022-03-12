def convert_duration_to_minute(duration_string):
    """
    Converts a duration string to minutes
    """
    if duration_string == "":
        return 0
    else:
        duration_list = duration_string.split(" ")  # split the string by space [ "1h", "30m" ]

        if len(duration_list) != 2:
            duration_list.append("0m") if "h" in duration_list[0] else duration_list.insert(0, "0h")

        hours = int(duration_list[0].split("h")[0])
        minutes = int(duration_list[1].split("m")[0])

    return hours * 60 + minutes
