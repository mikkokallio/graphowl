from ui.app import App
from constants import *


def main():
    app = App()
    app.title('GraphOwl')
    app.configure(bg=COLOR_DARK)
    app.mainloop()

if __name__ == '__main__':
    main()
