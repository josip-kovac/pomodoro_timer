# Basic Timer

Console application developed in Python.

Developed for Pomodoro based Study, but it can be used for any other purpose.

Usage:
1. Open up the terminal.
2. Navigate to the directory where the script is located.
3. General use case is: "python timer.py hours minutes seconds ticks"
    * So, if timer is to be set to 25 minutes, and you would like to see the progress of the timer every second, the command is: "python timer.py 0 25 0 1".

After the timer finishes, new window will pop up that will notify you that the timer is over. If you are in deep focused study, and you would **not** like to take a break, hitting OK will measure the total time passed.

# Example - timer of 5 seconds:

>   12:11:34 | 00:00:05 | 00:00:00
>   12:11:35 | 00:00:04 | 00:00:01
>   12:11:36 | 00:00:03 | 00:00:02
>   12:11:37 | 00:00:02 | 00:00:03
>   12:11:38 | 00:00:01 | 00:00:04
>   12:11:39 | 00:00:00 | 00:00:05

First column = current time, second column = time left, third column = total time passed.

After timer is over, new window will pop up notifying you that the timer is over. After you hit OK, following information will be printed to the console:

> Current Time: 12:11:41 | Timer was over 00:00:01 ago | Total time passed: 00:00:07
> Current Time: 12:11:42 | Timer was over 00:00:02 ago | Total time passed: 00:00:08
> Current Time: 12:11:43 | Timer was over 00:00:03 ago | Total time passed: 00:00:09
> Current Time: 12:11:44 | Timer was over 00:00:04 ago | Total time passed: 00:00:10
> Current Time: 12:11:45 | Timer was over 00:00:05 ago | Total time passed: 00:00:11

Have fun!