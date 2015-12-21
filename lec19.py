import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = DataFrame(np.arange(25).reshape((5,5)),
                    index=['NYC','LA','SF','DC','Chi'],
                    columns=['A','B','C','D','E'])

print(dframe)
