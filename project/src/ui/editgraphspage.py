from tkinter import Frame, Button, ttk
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC, GRAPH_ROWS
from ui.form import Form


class EditGraphsPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        
        label = ttk.Label(master=self, text='Graph configuration', font=("Arial", 25),
                          background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=1, padx=100, pady=10)
        
        nav = Frame(self)
        nav.grid(row=1, column=1)

        prev = Button(master=nav, text="<", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self._show_prev)
        prev.grid(row=0, column=0)
        next = Button(master=nav, text=">", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self._show_prev)
        next.grid(row=0, column=1)

        graphs = loader.load()['graphs']

        self._forms = [Form(self, GRAPH_ROWS, loader, ['graphs', n]) for n in range(len(graphs))]
        [form.grid(row=2, column=1) for form in self._forms]
        self._current = 0
        self._show_form(0)

        self.grid_rowconfigure(0, weight=1, minsize=0.1)
        self.grid_rowconfigure(2, weight=1, minsize=0.1)

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
