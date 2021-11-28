from tkinter import Frame, Tk, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import patheffects
from confighandler import ConfigHandler
from constants import *


class DashboardPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self._root = root
        loader = ConfigHandler('config/dashboard.yaml')
        dashboard = loader.load()
        canvas = self.draw_layout(dashboard.layout['y'], dashboard.layout['x'], dashboard.load_all(), self)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0, sticky ="nsew")
            
    def draw_graph(self, ax, data):
        """Draw one graph widget"""
        ax.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        ax.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [ax.spines['top'], ax.spines['bottom'], ax.spines['left'], ax.spines['right']]]

        if data is not None:
            ax.set_title(data['title'], fontdict={'color':'white','size':10})
            smallest = min([min(plot[1]) for plot in data['plots'].values()])
            
            color_gen = (color for color in COLORS)

            for title, plot in data['plots'].items():
                color = next(color_gen, None)
                ax.plot(plot[0], plot[1], marker='', markersize=1.0, linewidth=0.75, path_effects=[patheffects.Normal()], label=title, color=color)
                [ax.plot(plot[0], plot[1], marker='', alpha=0.025, linewidth=2+1.15*n, color=color) for n in range(8)]
                ax.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.035, color=color)
            ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), labelcolor='white', facecolor='black', framealpha=0.3, edgecolor='none', ncol=3)
        return ax

    def draw_layout(self, rows, cols, graphdata, master):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 8), dpi=100, facecolor=COLOR_DARK, edgecolor=COLOR_GRID, linewidth=1.0)
        fig.autofmt_xdate()
        gs = fig.add_gridspec(cols, rows, hspace=0.5)

        graph_gen = (graph for graph in graphdata)

        for y in range(rows):
            for x in range(cols):
                ax = fig.add_subplot(gs[y, x], frameon=True, facecolor=COLOR_DARKEST)
                self.draw_graph(ax, next(graph_gen, None))
        return FigureCanvasTkAgg(fig, master)
