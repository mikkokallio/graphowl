from tkinter import Tk
from tester_app import UI


def main():
    window = Tk()
    window.title('GraphOwl')

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
