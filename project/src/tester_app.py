from tkinter import Tk, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import patheffects
from mongodbconnector import MongoDbConnector
from confighandler import ConfigHandler
from graphwidget import GraphWidget
from constants import *

class UI:
    def __init__(self, root):
        self._root = root

    def draw_graph_widget(self):
        pass

    def draw_coordinates(self, ax):
        ax.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        ax.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [ax.spines.top, ax.spines.bottom, ax.spines.left, ax.spines.right]]
        return ax

    def draw_graphs(self, dashboard):
        layout = {'x': dashboard.layout['x'], 'y': dashboard.layout['y']}

        fig = Figure(figsize=(12, 8), dpi=100, facecolor=COLOR_DARKER, edgecolor=COLOR_GRID, linewidth=1.0)
        gs = fig.add_gridspec(layout['y'], layout['x'], hspace=0.5)
        axs = [[None for _ in range(layout['x'])] for _ in range(layout['y'])]

        data = dashboard.load_all()

        graph_n = 0

        for y in range(layout['y']):
            for x in range(layout['x']):
                #ax[y][x] = self.draw_graph_widget()
                ax = fig.add_subplot(gs[y, x], polar=False, frameon=True, facecolor=COLOR_DARK)
                if graph_n >= len(data): continue
                ax.set_title(data[graph_n][0], fontdict={'color':'white','size':10})
                ax = self.draw_coordinates(ax)

                mini, maxi = 100000, 0
                for plot in data[graph_n][1].values():
                    if min(plot[1]) < mini: mini = min(plot[1])
                    if max(plot[1]) > maxi: maxi = max(plot[1])

                for graph in data[graph_n][1]:
                    plot = data[graph_n][1][graph]
                    ax.plot(plot[0], plot[1], marker='o', markersize=2.5, path_effects=[patheffects.SimpleLineShadow(),
                       patheffects.Normal()], label=graph)
                    ax.fill_between(x=plot[0], y1=plot[1], y2=mini, alpha=0.025)
                ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), labelcolor='white', facecolor='black', framealpha=0.3, edgecolor='none', ncol=3)
                axs[y][x] = ax
                graph_n += 1


        return FigureCanvasTkAgg(fig, master=self._root)


    def start(self, dashboard):
        logo_label = ttk.Label(master=self._root, text="G")
        left_pane1_label = ttk.Label(master=self._root, text="1")
        left_pane2_label = ttk.Label(master=self._root, text="2")
        left_pane3_label = ttk.Label(master=self._root, text="3")
        left_pane4_label = ttk.Label(master=self._root, text="4")
        left_pane5_label = ttk.Label(master=self._root, text="5")

        canvas = self.draw_graphs(dashboard)
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

loader = ConfigHandler('config/dashboard.yaml')
dashboard = loader.load()

db_data = dashboard.load_all()
#for x in db_data:
#    print(x)

window = Tk()
window.title("GraphOwl")

ui = UI(window)
ui.start(dashboard)

window.mainloop()
