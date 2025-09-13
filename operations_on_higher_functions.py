from functools import reduce
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55),
            ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]


def long_songs(param):
    length = param[1]
    if length > 5.00:
        return length


def seconds(param):
    duration = param[1]
    length = int(duration)
    secs = (duration - length) * 100
    full_length = (length * 60) + round(secs)
    return full_length


def total(tot, param):
    length = param[1]
    return tot + length


print(list(filter(long_songs, playlist)))
print(list(map(seconds, playlist)))
print(reduce(total, playlist, 0))
