class Dashboard:
    """Contains all graphs and other configuration and data"""

    def __init__(self, title, timespan, interval, sources, graphs):
        self.title = title
        self.timespan = timespan
        self.interval = interval

        # sources
        # graphs