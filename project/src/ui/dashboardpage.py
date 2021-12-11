from tkinter import Frame, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib import patheffects
from dashboard import Dashboard
from constants import COLOR_BRITE, COLOR_DARK, COLOR_DARKEST, COLOR_LITE, COLOR_GRID, COLORS


class DashboardPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK)
        self._root = root
        self._loader = loader
        self._axes = []
        self._legends = []
        self._hovering = None
        self._dboard = Dashboard(**self._loader.load())
        label = ttk.Label(master=self, text=self._dboard.title, font=("Arial", 25),
                              background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=1, padx=100, pady=10)
        #self.canvas = self.draw_layout(dboard.layout['y'], dboard.layout['x'],
        #                               dboard.load_all(), self)
        #self.canvas.draw()
        self._refresh()
        self.canvas.get_tk_widget().grid(row = 1, column = 0, columnspan=3, sticky ="nsew")

    def _refresh(self):
        self.canvas = self.draw_layout(self._dboard.layout['y'], self._dboard.layout['x'],
                                       self._dboard.load_all(), self)
        self.canvas.draw()
        #self.after(1000, self._refresh)

    def draw_graph(self, axl, data):
        """Draw one graph widget"""
        axl.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        axl.grid(color=COLOR_GRID)
        [spine.set_color(COLOR_LITE) for spine in axl.spines.values()]

        if data is not None:
            axl.set_title(data['title'], fontdict={'color':'white','size':10})
            if data['plots'] in [None, {}]:
                axl.axis([0, 10, 0, 10])
                axl.text(5, 5, 'no data', style='italic',
                         verticalalignment='center', horizontalalignment='center',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
                return axl

            smallest = min([min(plot[1]) for plot in data['plots'].values()])

            color_gen = (color for color in COLORS)

            for title, plot in data['plots'].items():
                color = next(color_gen, None)
                axl.plot(plot[0], plot[1], marker='', markersize=1.0, linewidth=0.75,
                         path_effects=[patheffects.Normal()], label=title, color=color)
                for n in range(8):
                    axl.plot(plot[0], plot[1], marker='',
                             alpha=0.025, linewidth=2+1.15*n, color=color)
                axl.fill_between(x=plot[0], y1=plot[1], y2=smallest, alpha=0.035, color=color)
            lgd = axl.legend(loc='lower center',
                             labelcolor='white', facecolor='black',
                             framealpha=0.5, edgecolor='none', ncol=3)
            self._legends.append(lgd)
        return axl

    def draw_layout(self, rows, cols, graphdata, master):
        """Uses a generator to yield one graph at a time to put into the layout"""
        fig = Figure(figsize=(12, 6), dpi=100,
                     facecolor=COLOR_DARK, edgecolor=COLOR_GRID, linewidth=1.0)
        gridspec = fig.add_gridspec(rows, cols, left=0.075, right=0.925, top=0.925, bottom=0.075,
                                    wspace=0.20, hspace=0.35)
        graph_gen = (graph for graph in graphdata)
        xformatter = mdates.DateFormatter('%H:%M')

        fig.canvas.mpl_connect("motion_notify_event", self._on_hover)

        for y in range(rows):
            for x in range(cols):
                axl = fig.add_subplot(gridspec[y, x], frameon=True, facecolor=COLOR_DARKEST)
                axl = self.draw_graph(axl, next(graph_gen, None))
                axl.xaxis.set_major_formatter(xformatter)
                self._axes.append(axl)
        return FigureCanvasTkAgg(fig, master)

    def _on_hover(self, event):
        if event.inaxes is None and self._hovering is not False:
            self._hovering = False
            [leg.set_visible(True) for leg in self._legends]
            self.canvas.draw()
        if event.inaxes is not None and self._hovering is not True:
            self._hovering = True
            [leg.set_visible(False) for leg in self._legends]
            self.canvas.draw()
