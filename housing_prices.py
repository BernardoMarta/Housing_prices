import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Get data
train_path = "train.csv"
test_path = "test.csv"
train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)

# Select data
target = "SalePrice"
features = ["LotArea", "OverallQual", "YearBuilt", "TotalBsmtSF", "GrLivArea"]
X = train_data[features]
y = train_data[target]
X_test = test_data[features]

# Split data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions calculation
y_pred = model.predict(X_valid)
y_test_pred = model.predict(X_test)

# Evaluate performance of model
mae = mean_absolute_error(y_valid, y_pred)
print("Mean Absolute Error:", mae)

# Make predictions (with other data)
output = pd.DataFrame({"Id": test_data["Id"], "SalePrice": y_test_pred})
output.to_csv("submission.csv", index=False)
