
from time import sleep

def typewriter_print(string, sleep_time=0.05 , delay=0.5):
    for char in string:
        print(char, end="", flush=True)
        sleep(sleep_time)
    sleep(delay)
    print()

def get_valid_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")