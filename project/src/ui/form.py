from tkinter import Frame, Button, OptionMenu, StringVar, ttk, constants
from constants import COLOR_DARK, COLOR_BRITE, NEON_ELECTRIC, FORM_ROWS


class Form(Frame):
    def __init__(self, root, rows, loader):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        self._loader = loader
        self._config = self._loader.load()
        self._rows = rows
        self._vars = []

        for i, row in enumerate(self._rows):
            var = self._resolve_path(row['var'], self._config)
            #var = self._config[row['var'][0]] if len(row['var']) == 1 else self._config[row['var'][0]][row['var'][1]]
            self._vars.append(StringVar(self, value=var))
            label = ttk.Label(master=self, text=row['label'],
                              background=COLOR_DARK, foreground=COLOR_BRITE)
            entry = ttk.Entry(self, textvariable=self._vars[i]) if row['options'] is None else OptionMenu(self, self._vars[i], *row['options'])
            label.grid(row=i+1, column=1, padx=100, pady=5)
            entry.grid(row=i+1, column=2, padx=100, pady=5, sticky=(constants.E, constants.W))

        button = Button(master=self, text="Save", background=COLOR_BRITE, activebackground=NEON_ELECTRIC, command=self.save_config)
        button.grid(row=len(self._rows)+1, column=1, columnspan=2,
                    sticky=(constants.E, constants.W), padx = 100, pady = 5)

    # Move to service or something!
    def _resolve_path(self, path, data):
        if len(path) == 1:
            return data[path[0]]
        else:
            return self._resolve_path(path[1:], data[path[0]])

    def save_config(self, *args):
        for i, row in enumerate(self._rows):
            value = self._vars[i].get() if not row['numeric'] else int(self._vars[i].get())
            if len(row['var']) == 1:
                self._config[row['var'][0]] = value
            else:
                self._config[row['var'][0]][row['var'][1]] = value
        self._loader.save(self._config)
