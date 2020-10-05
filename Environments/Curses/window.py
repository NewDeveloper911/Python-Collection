import curses
import time

print("Initialising")
screen = curses.initscr()
screen.addstr(5, 10, "Sup, my code-y homie? how you doing?")
print("Initialises window")
screen.refresh()
curses.napms(2000)
curses.endwin()
print("Window has ended")
time.sleep(3)
