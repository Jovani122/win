import curses
import time
import datetime
import random

def draw_logo(stdscr):
    logo = """
    ██████╗ █████╗ ██╗     ██╗   ██╗███████╗
    ██╔══██╗██╔══██╗██║     ██║   ██║██╔════╝
    ██████╔╝███████║██║     ██║   ██║███████╗
    ██╔═══╝ ██╔══██║██║     ██║   ██║╚════██║
    ██║     ██║  ██║███████╗╚██████╔╝███████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
    """
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 2, logo)
    stdscr.attroff(curses.color_pair(1))

def draw_datetime(stdscr):
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    stdscr.addstr(curses.LINES - 2, curses.COLS - len(dt_string) - 2, dt_string)

def display_user_info(stdscr, email, password, balance):
    color = 1  # Rouge
    stdscr.attron(curses.color_pair(color))
    stdscr.addstr(16, 2, f"Email: {email}", curses.color_pair(color))
    stdscr.addstr(17, 2, f"Password: {password}", curses.color_pair(color))
    stdscr.addstr(18, 2, f"User: {email}", curses.color_pair(color))
    stdscr.addstr(20, 2, f"BTC Balance: {balance:.8f}", curses.color_pair(color))
    stdscr.attroff(curses.color_pair(color))

def display_history(stdscr, history):
    max_entries = min(20, len(history))
    border_win = curses.newwin(24, curses.COLS - 4, 1, 2)
    border_win.box()
    border_win.addstr(0, 2, "BTC MULTIPLY history:")
    for index, entry in enumerate(history[-max_entries:], start=1):
        border_win.addstr(index, 2, f"{index}. {entry}", curses.color_pair(1))  # Rouge

    stdscr.refresh()

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)  # Définit la couleur rouge

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    stdscr.addstr(10, 2, "TanoraTech", curses.color_pair(1))  # Rouge
    stdscr.addstr(14, 2, "Welcome to my application!", curses.color_pair(1))  # Rouge
    stdscr.refresh()

    stdscr.addstr(16, 2, "Enter your email: ", curses.color_pair(1))  # Rouge
    email = ""
    while True:
        draw_datetime(stdscr)
        stdscr.addstr(16, 22, email, curses.color_pair(1))  # Rouge
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            break
        elif key == curses.KEY_BACKSPACE:
            email = email[:-1]
        else:
            email += chr(key)

    stdscr.addstr(17, 2, "Enter your password: ", curses.color_pair(1))  # Rouge
    password = ""
    while True:
        draw_datetime(stdscr)
        stdscr.addstr(17, 25, "*" * len(password), curses.color_pair(1))  # Rouge
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            break
        elif key == curses.KEY_BACKSPACE:
            password = password[:-1]
        else:
            password += chr(key)

    user_balance = 0.12345678
    time.sleep(1)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, password, user_balance)
    stdscr.refresh()
    time.sleep(2)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, password, user_balance)
    display_history(stdscr, [])  # Commence avec un historique vide
    stdscr.refresh()

    history = []

    while True:
        draw_datetime(stdscr)
        entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: You won 0.00000092 BTC!"
        history.append(entry)
        user_balance += 0.00000092  # Créditer le montant gagné de BTC à l'utilisateur
        display_user_info(stdscr, email, password, user_balance)
        display_history(stdscr, history)
        stdscr.refresh()
        
        # L'utilisateur peut entrer "Run bot" pour démarrer le crédit de l'historique
        user_input = stdscr.getstr(22, 2, 8).decode('utf-8')
        if user_input == "Run bot":
            entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Starting bot to credit history..."
            history.append(entry)
            for _ in range(20):  # Créditer 20 fois l'historique
                time.sleep(2)
                user_balance += 0.00000092
                entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: You won 0.00000092 BTC!"
                history.append(entry)
            display_user_info(stdscr, email, password, user_balance)
            display_history(stdscr, history)
            stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
