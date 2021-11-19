from tkinter import Tk, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import patheffects
from confighandler import ConfigHandler
from graphwidget import GraphWidget
from constants import *

class UI:
    def __init__(self, root):
        self._root = root

    def draw_graph_widget(self):
        pass

    def draw_coordinates(self, ax, data):
        """Draw background for the graph widget"""
        ax.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        ax.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [ax.spines.top, ax.spines.bottom, ax.spines.left, ax.spines.right]]

        if data is not None:
            ax.set_title(data['title'], fontdict={'color':'white','size':10})
            smallest = min([min(plot[1]) for plot in data['plots'].values()])

            for title, plot in data['plots'].items():
                ax.plot(plot[0], plot[1], marker='', markersize=1.0, path_effects=[patheffects.SimpleLineShadow(),
                    patheffects.Normal()], label=title)
                ax.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.025)
            ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), labelcolor='white', facecolor='black', framealpha=0.3, edgecolor='none', ncol=3)
        return ax

    def draw_graphs(self, rows, cols, graphdata):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 8), dpi=100, facecolor=COLOR_DARKER, edgecolor=COLOR_GRID, linewidth=1.0)
        fig.autofmt_xdate()
        gs = fig.add_gridspec(cols, rows, hspace=0.5)

        graph_gen = (graph for graph in graphdata)

        for y in range(rows):
            for x in range(cols):
                ax = fig.add_subplot(gs[y, x], frameon=True, facecolor=COLOR_DARK)
                self.draw_coordinates(ax, next(graph_gen, None))
        return FigureCanvasTkAgg(fig, master=self._root)


    def start(self):
        logo_label = ttk.Label(master=self._root, text="G")
        left_pane1_label = ttk.Label(master=self._root, text="1")
        left_pane2_label = ttk.Label(master=self._root, text="2")
        left_pane3_label = ttk.Label(master=self._root, text="3")
        left_pane4_label = ttk.Label(master=self._root, text="4")
        left_pane5_label = ttk.Label(master=self._root, text="5")

        loader = ConfigHandler('config/dashboard.yaml')
        dashboard = loader.load()
        canvas = self.draw_graphs(dashboard.layout['y'], dashboard.layout['x'], dashboard.load_all())
        canvas.draw()

        # Layout

        logo_label.grid(row=1, column=1, padx=5, pady=5)
        left_pane1_label.grid(row=2, column=1, padx=5, pady=5)
        left_pane2_label.grid(row=3, column=1, padx=5, pady=5)
        left_pane3_label.grid(row=4, column=1, padx=5, pady=5)
        left_pane4_label.grid(row=5, column=1, padx=5, pady=5)
        left_pane5_label.grid(row=6, column=1, padx=5, pady=5)
        canvas.get_tk_widget().grid(row=1, rowspan=6, column=3, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=100)
