def post_preprocessing (data_name, train = False):
    
    import pandas as pd
    import numpy as np
    from sklearn import preprocessing

    raw = pd.read_csv(data_name)

    if train == True:
        

        sh_train = raw.copy().sample(frac = 1).reset_index(drop = True)


        rw_tr_in = sh_train.drop("sales", axis = 1)
        rw_tr_out = sh_train.filter(["sales"], axis = 1)


        input_samples = rw_tr_in.copy()
        target_samples = rw_tr_out.copy()

        n_train = int(0.8 * len(rw_tr_in))

        b_tr_in = input_samples[:n_train]
        b_tr_out = target_samples[:n_train]

        b_val_in = input_samples[n_train:]
        b_val_out = target_samples[n_train:]


        # IDS
        tr_ID = b_tr_in.filter(["ID"], axis = 1)
        val_ID = b_val_in.filter(["ID"], axis = 1)
        

        # FEATURES
        s_tr_in = b_tr_in.drop("ID", axis = 1)
        s_val_in = b_val_in.drop("ID", axis = 1)


        tr_in = preprocessing.scale(s_tr_in)
        tr_out = preprocessing.scale(b_tr_out)

        val_in = preprocessing.scale(s_val_in)
        val_out = preprocessing.scale(b_val_out)



        np.savez ("train", id = tr_ID, inputs = tr_in, targets = tr_out)
        np.savez ("val", id = val_ID, inputs = val_in, targets = val_out)


    if test == False:
        
        test_ID = raw.filter(["ID"], axis = 1)
        rw_test_in = raw.drop(["ID"], axis = 1)

        test_ID = raw.filter(["ID"], axis = 1)

        s_test = rw_test_in.drop("ID", axis = 1)

        test = preprocessing.scale(s_test)

        np.savez ("test", id = test_ID, inputs = test)