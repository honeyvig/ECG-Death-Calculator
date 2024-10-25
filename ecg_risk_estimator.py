import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from sklearn.linear_model import LogisticRegression

class ECGRiskEstimator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = self.create_model()

    def initUI(self):
        self.setWindowTitle("AI-ECG Risk Estimator")

        layout = QVBoxLayout()

        self.label = QLabel("Enter ECG parameters (comma-separated):")
        layout.addWidget(self.label)

        self.input_line = QLineEdit(self)
        layout.addWidget(self.input_line)

        self.predict_button = QPushButton("Predict Risk", self)
        self.predict_button.clicked.connect(self.predict_risk)
        layout.addWidget(self.predict_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def create_model(self):
        # Dummy model for demonstration purposes
        # Replace this with a trained model in practice
        X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6]])  # Dummy features
        y_train = np.array([0, 0, 1, 1])  # Dummy labels (0: low risk, 1: high risk)

        model = LogisticRegression()
        model.fit(X_train, y_train)
        return model

    def predict_risk(self):
        try:
            # Parse input data
            input_data = self.input_line.text().strip()
            features = np.array([float(x) for x in input_data.split(",")]).reshape(1, -1)

            # Make prediction
            risk_prediction = self.model.predict(features)[0]

            if risk_prediction == 1:
                self.result_label.setText("High Risk!")
            else:
                self.result_label.setText("Low Risk!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    estimator = ECGRiskEstimator()
    estimator.show()
    sys.exit(app.exec_())
