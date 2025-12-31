import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("price_model.h5")

def predict_price(rating):
    return model.predict(np.array([[rating]]))[0][0]
