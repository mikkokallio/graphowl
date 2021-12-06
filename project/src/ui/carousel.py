from tkinter import Frame, Button
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC
from ui.form import Form


class Carousel(Frame):
    """View component that loops through all items in array"""
    def __init__(self, root, loader, rows, path):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
                
        nav = Frame(self)
        nav.grid(row=1, column=1)

        prev = Button(master=nav, text="<", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self._show_prev)
        prev.grid(row=0, column=0)
        next = Button(master=nav, text=">", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self._show_next)
        next.grid(row=0, column=1)

        items = loader.load()[path]

        self._forms = [Form(self, rows, loader, [path, n]) for n in range(len(items))]
        [form.grid(row=2, column=1) for form in self._forms]
        self._current = 0
        self._show_form(0)

    def _show_form(self, current):
        form = self._forms[current]
        form.tkraise()

    def _show_next(self):
        self._current += 1
        if self._current == len(self._forms):
            self._current = 0
        self._show_form(self._current)

    def _show_prev(self):
        self._current -= 1
        if self._current == -1:
            self._current = len(self._forms) - 1
        self._show_form(self._current)
