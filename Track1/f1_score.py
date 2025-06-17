import pandas as pd
import sklearn
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

print(sklearn.__version__)

# Load the files
ground_truth = pd.read_csv(r"C:\Users\Nabasree\OneDrive\Desktop\openaimer\Track1\Test Data Reference.csv")
predictions = pd.read_csv(r"C:\Users\Nabasree\OneDrive\Desktop\openaimer\Track1\inceptionV3.csv")

# Extract label columns
y_true = ground_truth['label']
y_pred = predictions['label']

# Calculate metrics
f1 = f1_score(y_true, y_pred, average='macro')
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')

# Print results
print(f"F1 Score (Macro): {f1:.4f}")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision (Macro): {precision:.4f}")
print(f"Recall (Macro): {recall:.4f}")