import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Assuming df is your loaded DataFrame
df['diagnosis'].replace(['M', 'B'], [1, 0], inplace=True)

# Select top 2 features based on chi2 scores
selected_features = features_scores.nlargest(2, 'Score')['Features'].tolist()

# Create a new DataFrame with only the top 2 features and the target variable
X_selected = df[selected_features]
Y = df['diagnosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, Y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Add a new column for predicted diagnosis to the original DataFrame
df['predicted_diagnosis'] = model.predict(X_selected)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{classification_rep}")

# Display the DataFrame with actual and predicted diagnosis columns
df[[selected_features[0],selected_features[0],'diagnosis', 'predicted_diagnosis']]
