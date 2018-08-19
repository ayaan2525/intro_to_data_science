import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
      
        # Your code here:
        sex = passenger['Sex']
        if sex == 'male':
            predictions[passenger_id] = 0
        elif sex == 'female':
            predictions[passenger_id] = 1
        else:
            continue
        # For example, let's assume that if the passenger
        # is a male, then the passenger survived.
        #     if passenger['Sex'] == 'male':
        #         predictions[passenger_id] = 1
        
    return predictions
