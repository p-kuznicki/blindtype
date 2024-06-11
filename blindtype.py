import curses
from playsound import playsound

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr("Press 'escape' to quit\n")
    while True:
        key = stdscr.getch()
        if key != -1:
            try:
                stdscr.addstr(chr(key))
                playsound(f'/home/pk/code/blindtype/alfabet/{chr(key)}.mp3')
            except:
                playsound(f'/home/pk/code/blindtype/alfabet/click.mp3')
            if key == 27:
                break
        stdscr.refresh()

curses.wrapper(main)
