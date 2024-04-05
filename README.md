# Tumor_Type_Classification
This repository contains a Python script for analyzing a dataset of cancer cases and selecting the most significant features for predicting tumor malignancy. The dataset includes various measurements related to tumor characteristics, and the goal is to identify the features that are most indicative of malignant tumors.

Data Preprocessing
The script starts by loading the cancer data from a CSV file into a pandas DataFrame. The 'diagnosis' column, which contains labels 'M' (malignant) and 'B' (benign), is converted to binary values (1 for malignant and 0 for benign) to facilitate analysis.

Feature Selection
The script employs the chi-squared (χ²) statistical test to select the top 5 features that have the highest scores, indicating their importance in relation to the target variable 'diagnosis'. This feature selection process helps in identifying the most relevant features for building predictive models in cancer diagnosis.

Output
The output is a DataFrame containing the feature names and their corresponding chi-squared scores, sorted in descending order of scores. This output provides insights into which features are crucial for distinguishing between benign and malignant tumors.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/f6229270-0993-417f-84de-2369b59afb25)

Model Training and Prediction
The script splits the data into training and testing sets, then creates and trains a logistic regression model on the training data. It makes predictions on the testing data and adds a new column to the original DataFrame to store these predicted diagnoses.

Model Evaluation
The script evaluates the model's performance by calculating the accuracy, confusion matrix, and classification report. These metrics provide insights into the model's effectiveness in correctly classifying tumors as benign or malignant.

Output
The final output is the DataFrame with the selected features, actual diagnosis, and predicted diagnosis, along with the model evaluation metrics. This output helps in understanding the model's predictions and its accuracy in diagnosing cancer.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/e11ffa27-f1ef-440b-befb-963f505bd5b4)














