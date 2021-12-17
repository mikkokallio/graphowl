from tkinter import Frame, Button, messagebox, PhotoImage
from constants import COLOR_DARK, COLOR_DARKER, COLOR_DARKEST
from ui.coolbutton import CoolButton
from services import resolve_path
from ui.form import Form


class Carousel(Frame):
    """View component that loops through all items in array"""
    def __init__(self, root, loader, rows, path):
        Frame.__init__(self, root, bg=COLOR_DARK, border=1)
        self._rows = rows
        self._loader = loader
        self._path = path

        nav = Frame(self, bg=COLOR_DARK)
        nav.grid(row=1, column=1)

        buttons = [('left', self._show_prev), ('plus', self._add_new),
                   ('cross', self._delete), ('right', self._show_next)]

        for i, button in enumerate(buttons):
            btn = CoolButton(nav, imgfile=button[0], imgsize=10, size=40, cmd=button[1])
            btn.grid(row=0, column=i, padx=6, pady=6)
  
        self._forms = self._update_forms()
        self._current = 0

        self._indicator = None

        self._show_form()
    
    def _update_indicator(self):
        if self._indicator:
            self._indicator.destroy()
        self._indicator = Frame(self, bg=COLOR_DARK)
        self._indicator.grid(row=2, column=1)

        for i in range(len(self._forms)):
            icon = 'on' if i == self._current else 'off'
            size = 12 if i == self._current else 8
            img = PhotoImage(file=f'src/ui/icons/box_{icon}.png')
            img = img.subsample(2,2)
            btn = Button(self._indicator, image=img, border=0, height=size, width=size,
                         background=COLOR_DARKER,
                         activebackground=COLOR_DARKEST,
                         command = lambda i=i: self._show_clicked(i))
            btn.grid(row=0, column=i, padx=8-size/2, pady=8-size/2)
            btn.image = img # Necessary

    def _update_forms(self):
        items = self._loader.load()[self._path]
        forms = [Form(self, self._rows, self._loader, [self._path, n]) for n in range(len(items))]
        for form in forms:
            form.grid(row=3, column=1)
        return forms

    def _show_form(self):
        form = self._forms[self._current]
        form.tkraise()
        self._update_indicator()

    def _add_new(self):
        new_item = {}
        for row in self._rows:
            resolve_path(row['var'], new_item, 'add')
        config = self._loader.load()
        config[self._path].insert(self._current + 1, new_item)
        self._loader.save(config)
        self._forms = self._update_forms()
        self._show_next()

    def _delete(self):
        config = self._loader.load()
        confirm = messagebox.askquestion('Delete',
                                         f'Do you want to delete this entry from {self._path}?')
        if confirm == 'yes':
            del config[self._path][self._current]
            self._loader.save(config)
            self._forms = self._update_forms()
            self._show_prev()

    def _show_clicked(self, n):
        self._current = n
        self._show_form()

    def _show_next(self):
        self._current += 1
        if self._current >= len(self._forms):
            self._current = 0
        self._show_form()

    def _show_prev(self):
        self._current -= 1
        if self._current <= -1:
            self._current = len(self._forms) - 1
        self._show_form()
