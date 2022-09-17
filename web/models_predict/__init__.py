import pickle
import os

# https://towardsdatascience.com/serving-prophet-model-with-flask-predicting-future-1896986da05f


def load_model_bitcoin():
    dir_model = os.path.abspath(__name__)
    path_model = os.path.join(dir_model, "model_btc.pckl")
    with open(path_model, 'rb') as model:
        model_btc = pickle.load(model)
    return model_btc
