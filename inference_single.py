def inference (model_name, data):

    import tensorflow.keras as tf
    import tensorflow.keras.layers as ly
    import numpy as np

    from post_preprocessing import post_preprocessing

    data = post_preprocessing(data, train = False)[1]

    model = tf.models.load_model(model_name)

    prediction = model.predict (data)
    
    return prediction
   
