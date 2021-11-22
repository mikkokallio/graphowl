from tkinter import Frame, Tk, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import patheffects
from confighandler import ConfigHandler
from constants import *

  
class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        leftpane = Frame(self)
        main = Frame(self)
        leftpane.pack(side='left')
        main.pack(side='right')        
        
        self.pages = {} 
  
        for Page in (DashboardPage, EditConfigPage, EditGraphsPage, EditSourcesPage):
            page = Page(main, self)
            self.pages[Page] = page
            page.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_page(DashboardPage)
        
        ttk.Button(leftpane, text='Main',
                       command = lambda : self.show_page(DashboardPage)).pack(padx=5, pady=15)
        ttk.Button(leftpane, text='config',
                       command = lambda : self.show_page(EditConfigPage)).pack(padx=5, pady=15)
        ttk.Button(leftpane, text='graphs',
                       command = lambda : self.show_page(EditGraphsPage)).pack(padx=5, pady=15)
        ttk.Button(leftpane, text='sources',
                       command = lambda : self.show_page(EditSourcesPage)).pack(padx=5, pady=15)

    def show_page(self, controller):
        page = self.pages[controller]
        page.tkraise()

class DashboardPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self._root = root
        loader = ConfigHandler('config/dashboard.yaml')
        dashboard = loader.load()
        canvas = self.draw_graphs(dashboard.layout['y'], dashboard.layout['x'], dashboard.load_all(), self)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0, sticky ="nsew")

    def draw_coordinates(self, ax, data):
        """Draw background for the graph widget"""
        ax.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        ax.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [ax.spines['top'], ax.spines['bottom'], ax.spines['left'], ax.spines['right']]]

        if data is not None:
            ax.set_title(data['title'], fontdict={'color':'white','size':10})
            smallest = min([min(plot[1]) for plot in data['plots'].values()])

            for title, plot in data['plots'].items():
                ax.plot(plot[0], plot[1], marker='', markersize=1.0, path_effects=[patheffects.SimpleLineShadow(),
                    patheffects.Normal()], label=title)
                ax.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.025)
            ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), labelcolor='white', facecolor='black', framealpha=0.3, edgecolor='none', ncol=3)
        return ax

    def draw_graphs(self, rows, cols, graphdata, master):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 8), dpi=100, facecolor=COLOR_DARKER, edgecolor=COLOR_GRID, linewidth=1.0)
        fig.autofmt_xdate()
        gs = fig.add_gridspec(cols, rows, hspace=0.5)

        graph_gen = (graph for graph in graphdata)

        for y in range(rows):
            for x in range(cols):
                ax = fig.add_subplot(gs[y, x], frameon=True, facecolor=COLOR_DARK)
                self.draw_coordinates(ax, next(graph_gen, None))
        return FigureCanvasTkAgg(fig, master)


class EditConfigPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        label = ttk.Label(self, text ='This page is for editing the configuration of the dashboard.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)


class EditSourcesPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        label = ttk.Label(self, text ='Here you can configure data sources.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)


class EditGraphsPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        label = ttk.Label(self, text ='And here you can configure the graphs to be shown in the dashboard.')
        label.grid(row = 0, column = 0, padx = 100, pady = 100)
