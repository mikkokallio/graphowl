from tkinter import Frame, Tk, ttk
from constants import COLOR_DARK, COLOR_DARKER, COLOR_BRITE, COLOR_LITE
from ui.dashboardpage import DashboardPage
from ui.editconfigpage import EditConfigPage
from ui.editgraphspage import EditGraphsPage
from ui.editsourcespage import EditSourcesPage


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        leftpane = Frame(self, bg=COLOR_DARK)
        main = Frame(self, bg=COLOR_DARKER)
        leftpane.pack(side='left')
        main.pack(side='right')

        self.pages = {}

        for Page in (DashboardPage, EditConfigPage, EditGraphsPage, EditSourcesPage):
            page = Page(main, self)
            self.pages[Page] = page
            page.grid(row = 0, column = 0, sticky ="nsew")

        self.show_page(DashboardPage)

        style = ttk.Style()
        style.configure('W.TButton',
                        background=COLOR_DARK, foreground=COLOR_BRITE,
                        font=('Arial', 11), activebackground=COLOR_LITE)

        ttk.Button(leftpane, text='Main', style='W.TButton',
                       command = lambda : self.show_page(DashboardPage)).pack(padx=10, pady=15)
        ttk.Button(leftpane, text='config', style='W.TButton',
                       command = lambda : self.show_page(EditConfigPage)).pack(padx=5, pady=15)
        ttk.Button(leftpane, text='graphs', style='W.TButton',
                       command = lambda : self.show_page(EditGraphsPage)).pack(padx=5, pady=15)
        ttk.Button(leftpane, text='sources', style='W.TButton',
                       command = lambda : self.show_page(EditSourcesPage)).pack(padx=5, pady=15)

    def show_page(self, controller):
        page = self.pages[controller]
        page.tkraise()
