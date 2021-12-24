from tkinter import Frame, Button, OptionMenu, StringVar, ttk, constants
from services import resolve_path
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC


class Form(Frame):
    """Generic form with entry rows to populate with data"""
    def __init__(self, root, rows, loader, path):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        self._loader = loader
        self._rows = rows
        self._path = path
        self._vars = []

        config = self._loader.load()

        for i, row in enumerate(self._rows):
            rowpath = self._path + row['var']
            try:
                var = resolve_path(rowpath, config)
            except TypeError:
                var = None
            except KeyError:
                var = None
            self._vars.append(StringVar(self, value=var))
            label = ttk.Label(master=self, text=row['label'],
                              background=COLOR_DARK, foreground=COLOR_BRITE)
            entry = ttk.Entry(self, textvariable=self._vars[i]) if row['options'] is None else OptionMenu(self, self._vars[i], *row['options'])
            label.grid(row=i+1, column=1, padx=100, pady=5)
            entry.grid(row=i+1, column=2, padx=100, pady=5, sticky=(constants.E, constants.W))

        button = Button(master=self, text='Save', background=COLOR_BRITE,
                        activebackground=NEON_ELECTRIC, command=self._save_config)
        button.grid(row=len(self._rows)+1, column=1, columnspan=2,
                    sticky=(constants.E, constants.W), padx = 100, pady = 5)

    def _save_config(self):
        config = self._loader.load()
        for i, row in enumerate(self._rows):
            value = self._vars[i].get() if not row['numeric'] else int(self._vars[i].get())
            path = self._path + row['var']
            resolve_path(path, config, value=value)
        self._loader.save(config)
