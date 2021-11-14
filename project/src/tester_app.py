from tkinter import Tk, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import patheffects
from mongodbconnector import MongoDbConnector
from confighandler import ConfigHandler

class UI:
    def __init__(self, root):
        self._root = root

    def draw_graph_widget(self):
        pass

    def draw_graphs(self, dashboard):
        COLOR_DARKER='#1E2744'
        COLOR_DARK='#212946'
        COLOR_GRID='#2A3459'
        COLOR_LITE='#3A4469'
        COLOR_BRITE='#7A84A9'
        layout = {'x': 2, 'y': 2}

        fig = Figure(figsize=(10, 7), dpi=80, facecolor=COLOR_DARKER, edgecolor=COLOR_GRID, linewidth=1.0)
        gs = fig.add_gridspec(layout['y'], layout['x'], hspace=0.4)
        ax = [[None for _ in range(layout['x'])] for _ in range(layout['y'])]

        data = dashboard.load_all()

        graph_n = 0

        for y in range(layout['y']):
            for x in range(layout['x']):
                ax[y][x] = fig.add_subplot(gs[y, x], polar=False, frameon=True, facecolor=COLOR_DARK)
                ax[y][x].tick_params(color=COLOR_LITE, labelcolor=COLOR_BRITE)
                ax[y][x].grid(color=COLOR_GRID)
                ax[y][x].spines.top.set_color(COLOR_LITE)
                ax[y][x].spines.bottom.set_color(COLOR_LITE)
                ax[y][x].spines.left.set_color(COLOR_LITE)
                ax[y][x].spines.right.set_color(COLOR_LITE)
                if graph_n >= len(data): continue
                ax[y][x].set_title(data[graph_n][0], fontdict={'color':'white','size':10})

                for plot in data[graph_n][1].values():
                    ax[y][x].plot(plot[0], plot[1], marker='o', path_effects=[patheffects.SimpleLineShadow(),
                       patheffects.Normal()])
                    ax[y][x].fill_between(x=plot[0], y1=plot[1], y2=min(plot[1]) * 0, alpha=0.045)
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

        self._root.grid_columnconfigure(1, weight=1, minsize=50)

loader = ConfigHandler('config/dashboard.yaml')
dashboard = loader.load()

db_data = dashboard.load_all()
for x in db_data:
    print(x)


window = Tk()
window.title("GraphOwl")

ui = UI(window)
ui.start(dashboard)

window.mainloop()
