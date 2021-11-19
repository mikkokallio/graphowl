import time


class Connector:
    """Abstract connector class for actual connectors to inherit"""
    
    def __init__(self, name):
        self.name = name
    
    def get_start_time(self, timespan: int) -> int:
        return 1000 * (time.time()-timespan)
    
    def get_data(self, *args):
        return {'plot1': ([1,2,3,4],[1,2,3,4]), 'plot2': ([1,2,3,4],[4,3,2,1])}