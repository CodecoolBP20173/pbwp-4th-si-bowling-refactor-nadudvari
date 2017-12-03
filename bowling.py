def score(game):        # Returns a score for given outcome of a bowling game

    result = 0
    frame = 1
    in_first_half = True

    for i, score in enumerate(game):
        if score == '/':
            result += 10 - get_value(game[i - 1])
        else:
            result += get_value(score)

        if frame < 10 and get_value(score) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif score.upper() == 'X':
                result += get_value(game[i + 1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])

        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if score.upper() == 'X':
            in_first_half = True
            frame += 1
    return result


def get_value(char):        # Gives value to the given characters

    if char.upper() == 'X' or char == '/':
        return 10
    elif char == '-':
        return 0
    elif int(char) in range(1, 10):
        return int(char)
    else:
        raise ValueError()
