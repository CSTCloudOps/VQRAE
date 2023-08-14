import json
import os
import pandas as pd
import numpy as np
import sys
from datetime import datetime
def read_NAB_dataset(file_name, normalize=True):
    print(file_name)
    with open('../NAB/labels/combined_windows.json') as data_file:
        json_label = json.load(data_file)
    abnormal = pd.read_csv(file_name, header=0,index_col=0)
    abnormal['label'] = 0
    parent_dir = os.path.basename(os.path.dirname(file_name))
    list_windows = json_label.get(parent_dir+'/'+os.path.basename(file_name))
    input_format = '%Y-%m-%d %H:%M:%S.%f'
    output_format = '%Y-%m-%d %H:%M:%S'
    for window in list_windows:
        start = window[0]
        end = window[1]
        start = datetime.strptime(start, input_format)
        start = datetime.strftime(start, output_format)
        end = datetime.strptime(end, input_format)
        end = datetime.strftime(end, output_format)
        abnormal.loc[start:end, 'label'] = 1
    print('ab',np.sum(abnormal['label']))
    abnormal_data = abnormal['value'].values.astype(dtype='float32')
    # abnormal_preprocessing_data = np.reshape(abnormal_preprocessing_data, (abnormal_preprocessing_data.shape[0], 1))
    abnormal_label = abnormal['label'].values
    
    abnormal = abnormal.reset_index(drop=False)
    # abnormal_data = np.expand_dims(abnormal_data, axis=1)
    # abnormal_label = np.expand_dims(abnormal_label, axis=1)
    df = pd.DataFrame()
    import time
    timestamp = pd.to_datetime(abnormal['timestamp'])
    timestamp = timestamp.apply(lambda x: x.timestamp())
    print('unique',np.unique(np.diff(timestamp),return_counts=True,return_index=True))
    df['timestamp'] = timestamp
    df['value'] =  abnormal_data
    df['label'] = abnormal_label
    df = df.drop_duplicates()
    print('unique',np.unique(np.diff(df['timestamp']),return_counts=True,return_index=True))
    if(not os.path.exists('./data/NAB/data/{}'.format(parent_dir))):
        os.mkdir('./data/NAB/data/{}'.format(parent_dir))
    df.to_csv('./data/NAB/data/{}/{}'.format(parent_dir,os.path.basename(file_name)),index=False)
    # if normalize == True:
    #     scaler = MinMaxScaler(feature_range=(0, 1))
    #     abnormal_data = scaler.fit_transform(abnormal_data)

    # Normal = 1, Abnormal = -1
    return abnormal_data, abnormal_label



if __name__ =='__main__':
    file_list = os.listdir(sys.argv[1])
    for f in file_list:
        read_NAB_dataset(os.path.join(sys.argv[1],f))