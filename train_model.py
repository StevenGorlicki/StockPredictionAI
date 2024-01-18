import torch

from lstm_model import LSTMStockPredictor
from data_preprocessing import load_data, normalize_data, create_sequences
import torch.optim as optim
import torch.nn as nn

def train_model(train_df, input_size=1, hidden_layer_size=100, output_size=1, epochs=50):
    # Normalize data
    train_df, scaler = normalize_data(train_df)

    # Create sequences
    seq_length = 5
    x, y = create_sequences(train_df['Close'], seq_length)

    # Initialize model
    model = LSTMStockPredictor(input_size, hidden_layer_size, output_size)
    loss_function = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    for epoch in range(epochs):
        for seq, labels in zip(x, y):
            optimizer.zero_grad()
            model.reset_hidden_state()  # Reset hidden state at the beginning of each sequence

            seq_tensor = torch.FloatTensor(seq).unsqueeze(0)  # Shape: [1, seq_length, input_size]
            labels_tensor = torch.tensor([labels], dtype=torch.float32)

            y_pred = model(seq_tensor)
            single_loss = loss_function(y_pred, labels_tensor)
            single_loss.backward()
            optimizer.step()

        if epoch % 2 == 0:
            print(f'epoch: {epoch:3} loss: {single_loss.item():10.8f}')

    return model, scaler
