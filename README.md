# Count_down-App
This is a simple timer app

This code creates a GUI application using the Tkinter library in Python. The application is a timer that allows the user to set the duration of the timer in hours, minutes, and seconds.

The code starts by importing the necessary libraries, Tkinter and time. It then creates a window using the Tk() method and sets its title, size, and background color.

The application consists of two parts: a clock and a timer. The clock displays the current time in hours, minutes, and seconds. The timer allows the user to set the duration of the timer and start the countdown.

The clock is implemented using the time library and the after() method. The after() method schedules a function to be called after a certain amount of time has passed. In this case, the function updates the current time label every second.

The timer is implemented using a while loop and the sleep() method. The while loop counts down from the specified duration and updates the hours, minutes, and seconds labels accordingly. The sleep() method pauses the execution of the loop for one second to create the illusion of a countdown.

In addition to the timer and clock, the application also has three buttons that set the timer duration to predefined values. The buttons are implemented using images and the Button() method.

Finally, the application is started by calling the mainloop() method on the window. This method runs the application until the user closes the window.
