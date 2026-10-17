
from time import sleep

def typewriter_print(string, sleep_time=0.05 , delay=0.5):
    for char in string:
        print(char, end="", flush=True)
        sleep(sleep_time)
    sleep(delay)
    print()