import curses

def menu(stdscr):
    curses.curs_set(0)
    options = ["PRINT STATEMENTS", "VARIABLES", "OPERATORS", "QUIT"]
    current = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for i, text in enumerate(options):
            x = w//2 - len(text)//2
            y = h//2 - len(options)//2 + i

            if i == current:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, text)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, text)

        key = stdscr.getch()

        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(options) - 1:
            current += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current]

        stdscr.refresh()

curses.wrapper(menu)
