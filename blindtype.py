import os
import curses
from playsound import playsound

script_dir = os.path.dirname(os.path.abspath(__file__))
audio_dir = os.path.join(script_dir, 'alfabet')

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr("Press 'escape' to quit\n")
    while True:
        key = stdscr.getch()
        if key != -1:
            try:
                stdscr.addstr(chr(key))
                playsound(os.path.join(audio_dir, f'{chr(key)}.mp3'))
            except:
                playsound(os.path.join(audio_dir, 'click.mp3'))
            if key == 27:
            	break
        stdscr.refresh()

curses.wrapper(main)
