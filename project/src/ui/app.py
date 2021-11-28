from tkinter import Frame, Tk, ttk, PhotoImage, Button
from PIL import Image
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
        
        buttons = [('owl', DashboardPage), ('cog', EditConfigPage), ('graph', EditGraphsPage), ('plug', EditSourcesPage)]
        for button in buttons:
            print(button[1])
            img = PhotoImage(file=f'src/ui/{button[0]}.png')
            img = img.subsample(5,5)
            btn = Button(leftpane, image=img, border=0, height=80, width=80, 
                         background=COLOR_DARKER, highlightcolor='blue', activebackground='black',
                         command = lambda button=button: self.show_page(button[1]))
            btn.pack(padx=10, pady=15)
            btn.image = img # Necessary

    def show_page(self, controller):
        page = self.pages[controller]
        page.tkraise()
