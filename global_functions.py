
from time import sleep
from msvcrt import kbhit, getwch # import kbhit to check for keyboard input

typewrite = True  #variable to control typewriter effect
type_delay = 0.05  #Time to sleep between each character
wait_time = 0.5  # Delay after the entire string is printed

def skip_typewriter(): # this function checks if a key has been pressed to skip the typewriter effect
    if kbhit(): # Check if a key has been pressed
        getwch() # Read the key press to clear the buffer
        return True # Return True to indicate that the typewriter effect should be skipped
    return False # Return False to indicate that the typewriter effect should continue

def typewriter_print(string): # this function prints the string with a typewriter effect, with time between each character and a delay after the entire string is printed

    if not typewrite:
        print(string)
        return
    else:
        for i, char in enumerate(string): # Loop through each character in the string. I will store the index for skipping the typewriter effect
            if skip_typewriter(): # if a key has been pressed, print the rest of the string without delay
                print(string[i:]) # print everything from the current index to the end of the string
                return
            print(char, end="", flush=True) # Print the character without a newline and flush the output buffer to ensure immediate display
            sleep(type_delay) # the time to sleep between each character is controlled by the type_delay variable

    sleep(wait_time) # the time to sleep after the entire string is printed is controlled by the wait_time variable
    print()

def get_valid_int(prompt, min_value= 1, max_value= 100): # Check if the input is a valid integer within the specified range, default range is 1 to 100, but can be changed through arguments
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

def get_valid_float(prompt, min_value= 0.01, max_value= 2.0): # check if the input is a valid float within the specified range, default range is 0.01 to 2.0, but can be changed through arguments
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def set_typewriter_delay(delay):
    global type_delay
    type_delay = delay

def set_typewriter_wait(wait):
    global wait_time
    wait_time = wait

def set_typewriter_effect(enabled):
    global typewrite
    typewrite = enabled
    


