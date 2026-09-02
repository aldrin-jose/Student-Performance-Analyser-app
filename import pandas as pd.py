import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv('Student_Performance.csv')

print("Columns found in CSV:", df.columns.tolist())

# Select all numeric columns automatically
numeric_df = df.select_dtypes(include=['number'])

# Use all numeric columns except the last one as features; use last column as target
X = numeric_df.iloc[:, :-1]
y = numeric_df.iloc[:, -1]

print(f"Training features: {list(X.columns)}")
print(f"Target column: {y.name}")

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, predictions):.2f}")
print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")

# Export model artifact
joblib.dump(model, 'student_model.pkl')
print("\nSuccess! Model trained and saved as 'student_model.pkl'")