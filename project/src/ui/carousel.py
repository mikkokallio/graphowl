from tkinter import Frame, Button
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC
from services import resolve_path
from ui.form import Form


class Carousel(Frame):
    """View component that loops through all items in array"""
    def __init__(self, root, loader, rows, path):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        self._rows = rows
        self._loader = loader
        self._path = path

        nav = Frame(self)
        nav.grid(row=1, column=1)

        prev_b = Button(master=nav, text="<", background=COLOR_BRITE,
                        activebackground=NEON_ELECTRIC, command=self._show_prev)
        prev_b.grid(row=0, column=0)
        new_b = Button(master=nav, text="+", background=COLOR_BRITE,
                       activebackground=NEON_ELECTRIC, command=self._add_new)
        new_b.grid(row=0, column=1)
        next_b = Button(master=nav, text=">", background=COLOR_BRITE,
                        activebackground=NEON_ELECTRIC, command=self._show_next)
        next_b.grid(row=0, column=2)

        self._forms = self._update_forms()
        self._current = 0
        self._show_form()

    def _update_forms(self):
        items = self._loader.load()[self._path]
        forms = [Form(self, self._rows, self._loader, [self._path, n]) for n in range(len(items))]
        [form.grid(row=2, column=1) for form in forms]
        return forms
    
    def _show_form(self):
        form = self._forms[self._current]
        form.tkraise()

    def _add_new(self):
        new_item = {}
        for row in self._rows:
            resolve_path(row['var'], new_item, 'add')
        config = self._loader.load()
        config[self._path].insert(self._current + 1, new_item)
        self._loader.save(config)
        self._forms = self._update_forms()
        self._show_next()

    def _show_next(self):
        self._current += 1
        if self._current == len(self._forms):
            self._current = 0
        self._show_form()

    def _show_prev(self):
        self._current -= 1
        if self._current == -1:
            self._current = len(self._forms) - 1
        self._show_form()
