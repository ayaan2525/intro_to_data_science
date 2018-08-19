import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        
        passenger_class = passenger['Pclass']
        passenger_gender = passenger['Sex']
        passenger_age = passenger['Age']
        if passenger_gender == 'female' or (passenger_class == 1 and passenger_age < 18):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
        # 
        # your code here
        # for example, assuming that passengers who are male
        # and older than 18 surived:
        #     if passenger['Sex'] == 'male' or passenger['Age'] < 18:
        #         predictions[passenger_id] = 1
        # 
    return predictions
