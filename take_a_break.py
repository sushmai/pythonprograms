import webbrowser
import time

times = 0
print("This program started on " + time.ctime())
while times < 3:
    # sleep function takes in seconds
    # to print in one hour
    time.sleep(10*60)
    webbrowser.open("https://www.youtube.com/")
    times = times + 1 
