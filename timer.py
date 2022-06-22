import time
import os
import sys
import ctypes  # An included library with Python install.   


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def current_time():
    return time.strftime("%H:%M:%S", time.localtime())


def set_timer(hour=0, minute=0, second=0, print_every=1):
    os.system("cls")
    start_time = time.monotonic()
    total_time_second = (hour * 60 * 60) + (minute * 60) + (second)
    total_time_second_unchanged = (hour * 60 * 60) + (minute * 60) + (second)
    
    i = 0
    message = f" {current_time()} | {convert(total_time_second)} | {convert(i)}"
    print(message)
    
    while total_time_second > 0:
        time.sleep(1)
        i += 1
        total_time_second -= 1
        message = f" {current_time()} | {convert(total_time_second)} | {convert(i)}"
        
        if total_time_second % print_every == 0:
            print(message, end="\n")
    
    ctypes.windll.user32.MessageBoxW(0, f"{convert(total_time_second_unchanged)} has passed!", "Notification", 1)
    
    time_over_counter = 0
    
    while total_time_second <= 0:
        time.sleep(1)
        time_over_counter += 1
        message = f"Current Time: {current_time()} | Timer was over {convert(time_over_counter)} ago | Total time passed: {convert(time.monotonic() - start_time)}"
        if time_over_counter % print_every == 0 or time_over_counter == 1:
            print(message, end="\n")
        

all_args = sys.argv[1:]
all_args = list(map(int, all_args))


set_timer(
    hour=all_args[0],
    minute=all_args[1],
    second=all_args[2],
    print_every=all_args[3]
)


