def main():
    time = input("What time is it? ")
    print(convert(time))


def convert(time):
    hours, minutes = map(int, time.split(":"))
    total_minutes = hours * 60 + minutes
    if 0 <= total_minutes < 720:
        return "breakfast time"
    elif 720 <= total_minutes < 1020:
        return "lunch time"
    elif 1020 <= total_minutes < 1440:
        return "dinner time"
    else:
        raise ValueError("Time must be between 00:00 and 23:59")

main()