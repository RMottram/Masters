#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os, sys

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.5f}'.format
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(precision = 5, suppress = True)

## splits, encodes and equalizes the data

data = str(sys.argv[1])
split = float(sys.argv[2])

def split_dataset(dataset = str(data), train_split = float(split)):
    df = pd.read_csv(dataset)
    master_copy = df.copy()
    
    ## removes these features to level out dataset
    df = df.query("service != 'aol'")
    df = df.query("service != 'harvest'")
    df = df.query("service != 'http_2784'")
    df = df.query("service != 'http_8001'")
    df = df.query("service != 'red_i'")
    df = df.query("service != 'urh_i'")
    df = df.query("service != 'printer'")
    df = df.query("service != 'rje'")
    df = df.query("service != 'printer'")
    df = df.query("service != 'rje'")
    
    ## changes all the attack types to simply 'attack'
    df.loc[df.attack_type != 'normal', 'attack_type'] = 'attack'
    
    ## OHE protocol, service and flag features
    proto_ohe = pd.get_dummies(df['protocol_type'])
    service_ohe = pd.get_dummies(df['service'])
    flag_ohe = pd.get_dummies(df['flag'])
    
    df = df.drop(['protocol_type', 'service', 'flag'], axis = 1)
    df = pd.concat([df, proto_ohe, service_ohe, flag_ohe], axis = 1)
    
    ## makes sure there are no NaNs
    for column in df:
        if df[column].isna().any():
            df[column] = float(0)
    
    ## drop the 'attack_type' column so it does not get normalises
    df_labels = df['attack_type']
    df = df.drop(['attack_type'], axis = 1)
    df = 255 * df / df.max(numeric_only = True)
    
    df['attack_type'] = df_labels
    
    train = df.sample(frac = train_split)
    test = df.drop(train.index)
    
    return train, test

train, test = split_dataset(dataset = data, train_split = split)

train.to_csv(f'train_{int(split*100)}{int(100-split*100)}.csv', index = 0)
test.to_csv(f'test_{int(split*100)}{int(100-split*100)}.csv', index=0)