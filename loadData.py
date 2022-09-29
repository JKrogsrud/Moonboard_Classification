import pandas as pd
from IPython.display import display
import os
path = os.path.join('Data', 'moonboard_problems_setup_2016.json')
climbing_df = pd.read_json(path).transpose()
display(climbing_df)
