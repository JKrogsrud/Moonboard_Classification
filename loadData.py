import pandas as pd
import numpy as np
from IPython.display import display
import os
from Helpers.gradeConversion import font_to_v

def load_data():
    path = os.path.join('Data', 'moonboard_problems_setup_2016.json')
    climbing_df = pd.read_json(path).transpose()
    climbing_data = climbing_df[['Grade', 'Moves']].copy()
    display(climbing_data)
    climb_data = {'Grade': [], 'Climb': []}
    for climb_row in climbing_data.itertuples():
        climb_matrix = np.zeros((18, 11))
        for move in climb_row.Moves:
            col = ord(move['Description'][0].lower()) - 96
            row = (int)(move['Description'][1:])
            climb_matrix[row - 1][col - 1] = 1
        climb_data['Grade'].append(font_to_v(climb_row.Grade))
        climb_data['Climb'].append(climb_matrix)
    climbing_ml_data = pd.DataFrame(climb_data)
    display(climbing_ml_data)
    path = os.path.join('Data', 'moonboard_problems_cleaned.csv')
    climbing_ml_data.to_csv(path)

load_data()

        




