# Vanity names for various colors
COLOR_DARKEST='#121A28'
COLOR_DARKER='#1A2340'
COLOR_DARK='#212946'
COLOR_GRID='#2A3449'
COLOR_LITE='#3A4469'
COLOR_BRITE='#7A84A9'

NEON_LIME='#CCFF00'
NEON_ELECTRIC='#0FF0FC'
NEON_SAFFRON='#FFCF09'
NEON_CHARTREUSE='#DFFF11'
NEON_PINK='#FE01B1'
NEON_TEAL='#01F9C6'
NEON_FUCHSIA='#FE4164'
NEON_YELLOW='#CFFF04'
NEON_GREEN='#66FF00'
NEON_CRIMSON='#FF003F'
NEON_BLUE='#04D9FF'
NEON_ORANGE='#FFCF00'
NEON_PURPLE='#BC13FE'

# Color array for graphs
COLORS = [NEON_GREEN, NEON_BLUE, NEON_CRIMSON, NEON_ORANGE, NEON_PURPLE, NEON_YELLOW]

# How many seconds go to minutes, hours, days, and weeks
TIME_EXP = {'minutes': 60, 'minute': 60, 'mins': 60, 'min': 60,
            'hours': 3600, 'hour': 3600, 'h': 3600,
            'days': 86400, 'day': 86400, 'd': 86400,
            'weeks': 604800, 'week': 604800, 'w': 604800}

# Options in form dropdowns
TIMESPANS = ['none', '5 minutes', '15 minutes', '30 minutes', '1 hour',
             '6 hours', '12 hours', '1 day', '2 days', '7 days', '30 days']
INTERVALS = ['none', '30 seconds', '1 minute', '2 minutes', '5 minutes',
             '10 minutes', '15 minutes', '30 minutes']
LAYOUTS = [1, 2, 3, 4]

# In the dashboard's main configuration view, show these rows in the form
FORM_ROWS = [{'label': 'Dashboard title', 'var': ['title'],
              'numeric': False, 'options': None},
             {'label': 'Time span', 'var': ['timespan'],
              'numeric': False, 'options': TIMESPANS},
             {'label': 'Refresh interval', 'var': ['interval'],
              'numeric': False, 'options': INTERVALS},
             {'label': 'Layout x', 'var': ['layout', 'x'],
              'numeric': True, 'options': LAYOUTS},
             {'label': 'Layout y', 'var': ['layout', 'y'],
              'numeric': True, 'options': LAYOUTS}]

# In the graph configuration view, show these rows in the form
GRAPH_ROWS = [{'label': 'Graph title', 'var': ['title'],
               'numeric': False, 'options': None},
              {'label': 'Source name', 'var': ['connector'],
               'numeric': False, 'options': None},
              {'label': 'Table / collection / endpoint', 'var': ['collection'],
               'numeric': False, 'options': None},
              {'label': 'Field: name', 'var': ['fields', 'name'],
               'numeric': False, 'options': None},
              {'label': 'Field: time', 'var': ['fields', 'time'],
               'numeric': False, 'options': None},
              {'label': 'Field: value', 'var': ['fields', 'value'],
               'numeric': False, 'options': None}]

# In the sources (connectors) configuration view, show these rows in the form
SOURCE_ROWS = [{'label': 'Source name', 'var': ['name'],
                'numeric': False, 'options': None},
               {'label': 'Connector type', 'var': ['connector'],
                'numeric': False, 'options': None},
               {'label': 'URI', 'var': ['uri'],
                'numeric': False, 'options': None},
               #{'label': 'Other properties', 'var': ['props'],
               # 'numeric': False, 'options': None}
               ]

# If the x dimension of the layout is n = 1...4,
# this is how many horizontal ticks and legend cols there'll be
MAXTICKS = {1:16, 2:8, 3:6, 4:4}
LEGENDCOLS = {1:7, 2:3, 3:None, 4:None}
