from threading import Timer
from time import sleep
from tkinter import Frame, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from matplotlib import patheffects
from matplotlib.ticker import MaxNLocator
from dashboard import Dashboard
from ui.coolbutton import CoolButton
from constants import COLOR_BRITE, COLOR_DARK, COLOR_DARKEST, COLOR_LITE, COLOR_GRID, COLORS, MAXTICKS, LEGENDCOLS, TIME_EXP


class DashboardPage(Frame):
    def __init__(self, root, loader):
        Frame.__init__(self, root, bg=COLOR_DARK)
        self._loader = loader
        self._legends = []
        self._hovering = None
        self._dboard = Dashboard(**self._loader.load())
        label = Label(master=self, text=self._dboard.title, font=("Arial", 25),
                          background=COLOR_DARK, foreground='white')
        label.grid(row=0, column=1, padx=100, pady=10)

        CoolButton(self, imgfile='recycle', imgsize=6, size=60,
                   cmd=self._draw_canvas).grid(row=0, column=2, padx=10, pady=15)

        self._fig = Figure(figsize=(12, 7), dpi=100,
                          facecolor=COLOR_DARK, edgecolor=COLOR_GRID, linewidth=1.0)
        self._fig.canvas.mpl_connect("motion_notify_event", self._on_hover)
        self._gridspec = self._fig.add_gridspec(self._dboard.layout['x'], self._dboard.layout['y'],
                                                left=0.075, right=0.925, top=0.925, bottom=0.075,
                                                wspace=0.20, hspace=0.35)
        self._canvas = FigureCanvasTkAgg(self._fig, self)
        self._canvas.get_tk_widget().grid(row = 1, column = 0, columnspan=3, sticky="nsew")
        self._draw_canvas()
        Timer(10.0, self._refresher)
        Timer(20.0, self._refresher)
        Timer(30.0, self._refresher)
        #self._refresher()

    def _draw_canvas(self):
        self._draw_layout(self._dboard.layout['y'], self._dboard.layout['x'], self._dboard.load_all())
        self._canvas.draw()

    def _refresher(self):
        while True:
            self._draw_canvas()
            sleep(10)

    def _draw_layout(self, rows, cols, graphdata):
        """Uses a generator to yield one graph at a time to put into the layout"""
        graph_gen = (graph for graph in graphdata)
        time_or_date = lambda span : '%m-%d' if not span or span > 2 * TIME_EXP['days'] else '%H:%M'
        xformatter = DateFormatter(time_or_date(self._dboard.timespan))

        [ax.clear() for ax in self._fig.get_axes()]
        [self._fig.delaxes(ax) for ax in self._fig.get_axes()]
        for y in range(rows):
            for x in range(cols):
                axl = self._fig.add_subplot(self._gridspec[y, x], facecolor=COLOR_DARKEST)
                axl = self._draw_graph(axl, next(graph_gen, None), cols)
                axl.xaxis.set_major_formatter(xformatter)
                axl.xaxis.set_major_locator(MaxNLocator(MAXTICKS[cols]))

    def _draw_graph(self, axl, data, cols):
        """Draw one graph widget"""
        axl.tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
        axl.grid(color=COLOR_GRID)
        [spine.set_color(COLOR_LITE) for spine in axl.spines.values()]

        if data is not None:
            axl.set_title(data['title'], fontdict={'color':'white','size':10})
            error = None if data['plots'] is None or '_error_' not in data['plots'] else data['plots']['_error_']
            #if error or 'plots' not in data or data['plots'] in [None, {}]:
            if error or 'plots' not in data:
                axl.axis([0, 10, 0, 10])
                axl.text(5, 5, error if error else 'no data', style='italic',
                         verticalalignment='center', horizontalalignment='center',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
                return axl

            smallest = data['plots'].min(numeric_only=True).min()

            color_gen = (color for color in COLORS)

            for title, plot in data['plots'].items():
                plot = plot.dropna()
                color = next(color_gen, None)
                axl.plot(plot, marker='', markersize=1.0, linewidth=0.75, label=title, color=color)
                for n in range(8):
                    axl.plot(plot, marker='',
                             alpha=0.025, linewidth=2+1.15*n, color=color)
                axl.fill_between(x=plot.index, y1=plot, y2=smallest, alpha=0.035, color=color)
            if self._dboard._legend and cols in LEGENDCOLS:
                #cols in LEGENDCOLS and LEGENDCOLS[cols] is not None:
                lgd = axl.legend(loc='lower center',
                                labelcolor='white', facecolor='black',
                                framealpha=0.5, edgecolor='none', ncol=LEGENDCOLS[cols])
                self._legends.append(lgd)
        return axl

    def _on_hover(self, event):
        pass
        #if event.inaxes is None and self._hovering is not False:
        #    self._hovering = False
        #    [leg.set_visible(True) for leg in self._legends]
        #    self._canvas.draw()
        #if event.inaxes is not None and self._hovering is not True:
        #    self._hovering = True
        #    [leg.set_visible(False) for leg in self._legends]
        #    self._canvas.draw()
