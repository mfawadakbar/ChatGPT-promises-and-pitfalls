Sure! Here's a Python script that displays a timer:

```python
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Timer completed!")

if __name__ == '__main__':
    # Get user input for the duration of the timer
    minutes = input("Enter the number of minutes for the timer: ")
    seconds = input("Enter the number of seconds for the timer: ")

    # Calculate the total time in seconds
    total_time = int(minutes) * 60 + int(seconds)

    # Start the countdown timer
    countdown(total_time)
```

This script uses the `time` module to create a countdown timer. It asks the user for the duration of the timer in minutes and seconds, calculates the total time in seconds, and then starts the countdown. The timer is displayed in the format MM:SS and updates every second until the timer reaches zero.