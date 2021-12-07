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

        items = self._loader.load()[path]

        self._forms = [Form(self, self._rows, loader, [path, n]) for n in range(len(items))]
        [form.grid(row=2, column=1) for form in self._forms]
        self._current = 0
        self._show_form(0)

    def _show_form(self, current):
        form = self._forms[current]
        form.tkraise()

    def _add_new(self):
        new_item = {}
        for row in self._rows:
            for step in row['var']:
                if step is not row['var'][-1]:
                    print('last')
                    resolve_path(row['var'], new_item, {})
                else:
                    print('not last')
                    resolve_path(row['var'], new_item, ' ')
            print(new_item)
        #self._forms.append(Form(self, self._rows, self._loader, [self._path, len(self._forms)]))

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
