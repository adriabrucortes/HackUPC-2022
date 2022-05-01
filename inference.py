import tensorflow.keras as tf
import tensorflow.keras.layers as ly
import numpy as np
import pandas as pd

test_ID = np.load("test.npz")["ID"].astype(np.str)
test_in = np.load("test.npz")["inputs"].astype(np.float)

model = tf.models.load_model("frozen_model.tf")

prediction = model.predict (test_in)

results = pd.DataFrame({"ID": test_ID, "Prediction": prediction})

results.to_csv("results.csv", index=False)