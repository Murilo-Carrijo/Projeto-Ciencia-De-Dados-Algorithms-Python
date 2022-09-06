def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None

    for entrice, exit in permanence_period:
        if (
            entrice is None
            or exit is None
            or not isinstance(exit, int)
            or not isinstance(entrice, int)
        ):
            return None

        elif entrice <= target_time <= exit:
            counter += 1

    return counter

