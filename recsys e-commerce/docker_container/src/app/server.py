import pickle
import pandas as pd
from flask import Flask


# model upload
with open('./SVD_model.pickle', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

app = Flask(__name__)


# test message if server runs at ./
@app.route('/')
@app.route('/index/')
def index():
    msg = "Hi, it's a test message. Server is started!"
    return msg


# upload data
events = pd.read_csv('events.csv')


# posting recommendations at ./predict
@app.route('/predict')
def recommend_3():
    """Returns 3 recommendations of item-id for user with input id"""
    user_id = input('Enter visitor id, please:')
    print("user id:", user_id)
    try:
        user_id = int(user_id)
        # make predictions for user for each item
        uid_predictions = []
        for item in events.itemid.unique():
            prediction = model.predict(user_id, item)
            if prediction.details['was_impossible'] == False:
                uid_predictions.append(prediction)
        if len(uid_predictions) == 0:
            return "No visitor with this Id"
        else:
            uid_predictions.sort(key=lambda x: x.est, reverse=True)
            recommendations = [i.iid for i in uid_predictions[:3]]
            recommendations = ' '.join(str(i) for i in recommendations)
            print('recommended items:', recommendations)
        return recommendations
    except TypeError:
        print("Please, check the value inserted. It must be integer.")
        return "Please, check the value inserted. It must be integer."


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
#127.0.0.1