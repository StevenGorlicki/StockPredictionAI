from data_preprocessing import load_data, normalize_data, create_sequences
from lstm_model import LSTMStockPredictor
from train_model import train_model
from plot import predict_and_plot

if __name__ == "__main__":
    file_name = "Stock_Data/AAPL.csv"

    # Load and split data
    train_df, test_df = load_data(file_name, test_size=0.2)
    test_df = test_df.reset_index(drop=True)

    seq_length = 5
    # Train model
    model, scaler = train_model(train_df, input_size=1, hidden_layer_size=75, output_size=1, epochs=100)

    # Prepare test data

    test_df['Close'] = scaler.transform(test_df['Close'].values.reshape(-1, 1))
    if len(test_df) > seq_length:
        x_test, y_test = create_sequences(test_df['Close'], seq_length)
        predict_and_plot(model, x_test, y_test, scaler)
