intervals = (
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),  # 60 * 60 * 24
    ('h', 3600),  # 60 * 60
    ('m', 60),
    ('s', 1),
)



def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

intervals_dict = {
    'w': 604800000000,  # 60 * 60 * 24 * 7 * 1000000
    'd': 86400000000,  # 60 * 60 * 24 * 1000000
    'h': 3600000000,  # 60 * 60 * 1000000
    'm': 60000000,
    's': 1000000,
}

def get_microseconds(timerecord):
    res = 0;
    for interval in timerecord.split(' '):

        amount = float(interval[:-1])
        period = interval[-1:]
        duration = intervals_dict[period]

        print("amount", amount)
        print("period", period)
        print("duration", duration)

        res += amount * duration
    return res

print(get_microseconds('1m'))