from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import patheffects
from dashboard import Dashboard
from constants import COLOR_BRITE, COLOR_DARK, COLOR_DARKEST, COLOR_LITE, COLOR_GRID, COLORS


class DashboardPage(Frame):
    def __init__(self, root, controller, loader):
        Frame.__init__(self, root)
        self._root = root
        self._loader = loader
        dboard = Dashboard(**self._loader.load())
        canvas = self.draw_layout(dboard.layout['y'], dboard.layout['x'], dboard.load_all(), self)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0, sticky ="nsew")

    def draw_graph(self, axl, data):
        """Draw one graph widget"""
        axl.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        axl.grid(color=COLOR_GRID)
        [x.set_color(COLOR_LITE) for x in [
            axl.spines['top'], axl.spines['bottom'], axl.spines['left'], axl.spines['right']
            ]]

        if data is not None:
            axl.set_title(data['title'], fontdict={'color':'white','size':10})
            smallest = min([min(plot[1]) for plot in data['plots'].values()])

            color_gen = (color for color in COLORS)

            for title, plot in data['plots'].items():
                color = next(color_gen, None)
                axl.plot(plot[0], plot[1], marker='', markersize=1.0, linewidth=0.75,
                         path_effects=[patheffects.Normal()], label=title, color=color)
                [axl.plot(plot[0], plot[1], marker='', alpha=0.025, linewidth=2+1.15*n, color=color) for n in range(8)]
                axl.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.035, color=color)
            axl.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35),
                       labelcolor='white', facecolor='black',
                       framealpha=0.3, edgecolor='none', ncol=3)
        return axl

    def draw_layout(self, rows, cols, graphdata, master):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 8), dpi=100,
                     facecolor=COLOR_DARK, edgecolor=COLOR_GRID, linewidth=1.0)
        fig.autofmt_xdate()
        gridspec = fig.add_gridspec(rows, cols, hspace=0.5)

        graph_gen = (graph for graph in graphdata)

        for y in range(rows):
            for x in range(cols):
                axl = fig.add_subplot(gridspec[y, x], frameon=True, facecolor=COLOR_DARKEST)
                self.draw_graph(axl, next(graph_gen, None))
        return FigureCanvasTkAgg(fig, master)
