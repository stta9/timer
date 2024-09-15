import time
import re


word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "a": 1, "an": 1
}


def word_to_seconds(word):
    word = word.lower().strip()

    # regex for short input
    short_regex = r"(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?"

    # regex for natural input
    time_regex = r"(?:(\d+|\w+)\s*hours?)?\s*(?:(\d+|\w+)\s*minutes?)?\s*(?:(\d+|\w+)\s*seconds?)?"

    # match short natural
    match_short = re.match(short_regex, word)
    if match_short and any(match_short.groups()):
        hours = match_short.group(1)
        minutes = match_short.group(2)
        seconds = match_short.group(3)
        total_seconds = 0
        if hours:
            total_seconds += int(hours) * 3600
        if minutes:
            total_seconds += int(minutes) * 60
        if seconds:
            total_seconds += int(seconds)
        return total_seconds

    # match regex natural
    match_natural = re.match(time_regex, word)
    if match_natural and any(match_natural.groups()):
        hours = match_natural.group(1)
        minutes = match_natural.group(2)
        seconds = match_natural.group(3)
        total_seconds = 0
        if hours:
            total_seconds += convert_to_number(hours) * 3600
        if minutes:
            total_seconds += convert_to_number(minutes) * 60
        if seconds:
            total_seconds += convert_to_number(seconds)
        return total_seconds

    try:
        h, m, s = map(int, word.split(':'))
        return h * 3600 + m * 60 + s
    except ValueError:
        pass
    raise ValueError("Invalid input. Please provide a valid time format like '1h:20m' or '0:5:32'.")


def convert_to_number(word):
    word = word.lower().strip()
    if word.isdigit():
        return int(word)
    elif word in word_to_num:
        return word_to_num[word]
    # if the number consists of two digits
    if "-" in word:
        parts = word.split("-")
        return word_to_num[parts[0]] + word_to_num.get(parts[1], 0)
    raise ValueError(f"Unknown number format: {word}")


def countdown_timer(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


try:
    user_input = input("Insert time to count down (e.g., '1h:20m', 'a minute 45 seconds', or '0:5:32'): ")
    countdown_time = word_to_seconds(user_input)
    countdown_timer(countdown_time)
except ValueError as e:
    print(e)
