from bot.crowded import CrowdedInfo


def handle_user_input(args):
    if args[0] == "jetzt":
        location = args[1]

        crowded_info = CrowdedInfo(location)
        response = crowded_info.get_current_crowded()
    else:
        weekday = args[0]
        time = args[1]
        location = args[2]

        crowded_info = CrowdedInfo(location)
        response = crowded_info.get_crowded(weekday, time)

    return response
