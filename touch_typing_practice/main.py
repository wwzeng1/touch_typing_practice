## main.py
import curses
from touch_typing_practice.typing_practice import TypingPractice
from touch_typing_practice.user import User

def main(stdscr):
    # Clear screen
    typing_practice = initialize_user_session(stdscr)

    while True:
        print("1. Start new session\r")
        print("2. View statistics\r")
        print("3. Exit\r\n")
        try:
            choice = int(stdscr.getstr(0,0,3))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            conduct_typing_session(stdscr, typing_practice)
        elif choice == 2:
            display_user_statistics(typing_practice)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

def initialize_user_session(stdscr):
    """
    Initialize a user session.

    This function clears the screen, prompts the user for their username, loads the user's data,
    and initializes a TypingPractice session for the user.

    Parameters
    ----------
    stdscr : _curses.window
        The window object in which the user session is to be initialized.

    Returns
    -------
    TypingPractice
        The initialized TypingPractice session for the user.
    """
    # Clear screen
    stdscr.clear()
    curses.echo()
    print("Enter your username: \n\r")
    username = stdscr.getstr(0,0,15)
    user = User.load(username)
    typing_practice = TypingPractice(user)
    return typing_practice

def conduct_typing_session(stdscr, typing_practice):
    """
    Conduct a typing session.

    This function prompts the user for the text for the session, starts the session,
    prompts the user to start typing, ends the session when the user is done typing,
    and informs the user that the session has ended and their progress has been recorded.

    Parameters
    ----------
    stdscr : _curses.window
        The window object in which the typing session is to be conducted.
    typing_practice : TypingPractice
        The TypingPractice session in which the typing is to be conducted.
    """
    print("Enter text for the session: ")
    text = stdscr.getstr(0, 0, 100)
    typing_practice.start_session(text)
    print("Start typing: ")
    typed_text = stdscr.getstr(0, 0, 100)
    typing_practice.end_session(typed_text)
    print("Session ended. Your progress has been recorded.")

def display_user_statistics(typing_practice):
    """
    Display the user's typing statistics.

    This function retrieves the user's typing statistics from the TypingPractice session,
    and displays them in the console.

    Parameters
    ----------
    typing_practice : TypingPractice
        The TypingPractice session from which the user's typing statistics are to be retrieved.
    """
    statistics = typing_practice.get_user_statistics()
    for session_time, session_statistics in statistics.items():
        print(f"Session at {session_time}:")
        for stat, value in session_statistics.items():
            print(f"  {stat}: {value}")

if __name__ == "__main__":
    curses.wrapper(main)
