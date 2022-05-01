import tensorflow.keras as tf
import tensorflow.keras.layers as ly
import numpy as np
import datetime
from post_preprocessing import post_preprocessing

post_preprocessing("taula_final.csv", train = True)