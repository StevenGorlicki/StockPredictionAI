import torch
import torch.nn as nn


class LSTMStockPredictor(nn.Module):
    def __init__(self, input_size, hidden_layer_size=100, output_size=1):
        super(LSTMStockPredictor, self).__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size)
        self.linear = nn.Linear(hidden_layer_size, output_size)
        self.hidden_cell = None

    def reset_hidden_state(self):
        self.hidden_cell = (torch.zeros(1, 1, self.hidden_layer_size),
                            torch.zeros(1, 1, self.hidden_layer_size))

    def forward(self, input_seq):
        self.reset_hidden_state()
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(-1, 1, 1), self.hidden_cell)

        # Reshape the LSTM output before feeding it to the linear layer
        # We take the output of the last time step
        lstm_out_last_step = lstm_out[-1].view(-1)  # Reshape to [hidden_layer_size]
        predictions = self.linear(lstm_out_last_step)

        return predictions
