import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL-win-loss_records'
webbrowser.open(website)
nfl_frame = pd.read_clipboard()
print(nfl_frame)
