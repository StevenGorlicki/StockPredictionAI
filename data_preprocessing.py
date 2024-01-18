import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def load_data(file_name, test_size=0.2):
    df = pd.read_csv(file_name)
    train_size = int(len(df) * (1 - test_size))
    train_df = df[:train_size]
    test_df = df[train_size:]
    return train_df, test_df

def normalize_data(df):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    df['Close'] = scaler.fit_transform(df['Close'].values.reshape(-1,1))
    return df, scaler

def create_sequences(data, seq_length):
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        # Ensure there's enough data to create a complete sequence
        if i + seq_length < len(data):
            x = data[i:(i + seq_length)]
            y = data[i + seq_length]
            xs.append(x)
            ys.append(y)
    return np.array(xs, dtype=np.float32), np.array(ys, dtype=np.float32)