from tkinter import Frame, Tk, PhotoImage, Button
from constants import COLOR_DARK, COLOR_DARKER, COLOR_DARKEST
from ui.dashboardpage import DashboardPage
from ui.editconfigpage import EditConfigPage
from ui.editgraphspage import EditGraphsPage
from ui.editsourcespage import EditSourcesPage
from confighandler import ConfigHandler


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self._loader = ConfigHandler('config/dashboard.yaml')

        leftpane = Frame(self, bg=COLOR_DARK)
        main = Frame(self, bg=COLOR_DARKER)
        leftpane.grid(row=0, column=0)
        main.grid(row=0, column=1)
        self.grid_columnconfigure(0, weight=1, minsize=0.0)
        self.grid_columnconfigure(1, weight=20, minsize=0.1)

        self.pages = {}

        for Page in (DashboardPage, EditConfigPage, EditGraphsPage, EditSourcesPage):
            page = Page(main, self._loader)
            self.pages[Page] = page
            page.grid(row = 0, column = 0, sticky ="nsew")

        self.show_page(DashboardPage)

        buttons = [('owl', DashboardPage), ('cog', EditConfigPage),
                   ('graph', EditGraphsPage), ('plug', EditSourcesPage)]

        for button in buttons:
            img = PhotoImage(file=f'src/ui/{button[0]}.png')
            img = img.subsample(6,6)
            btn = Button(leftpane, image=img, border=0, height=60, width=60,
                         background=COLOR_DARKER,
                         highlightcolor='blue',
                         activebackground=COLOR_DARKEST,
                         command = lambda button=button: self.show_page(button[1]))
            btn.pack(padx=10, pady=15)
            btn.image = img # Necessary

    def show_page(self, controller):
        page = self.pages[controller]
        page.tkraise()
