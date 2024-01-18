import matplotlib.pyplot as plt
import torch
import numpy as np

def predict_and_plot(model, x_test, y_test, scaler):
    model.eval()  # Set the model to evaluation mode
    predictions = []

    for seq in x_test:
        seq_tensor = torch.FloatTensor(seq).unsqueeze(0)
        with torch.no_grad():
            prediction = model(seq_tensor)
            predictions.append(prediction.item())

    # Inverse transform the predictions and actuals (if they were normalized)
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    actuals = scaler.inverse_transform(np.array(y_test).reshape(-1, 1))

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(actuals, label='Actual Prices')
    plt.plot(predictions, label='Predicted Prices')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

    return predictions, actuals