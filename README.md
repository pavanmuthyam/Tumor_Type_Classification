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

Data Visualization
The script sets the style of the plot to "whitegrid" and specifies the figure size. It then uses the sns.countplot() function to create a count plot of the 'diagnosis' column in the DataFrame, with different colors for benign and malignant cases.

Plot Customization
The plot is titled 'Distribution of Malignant (1) and Benign (0) Cases' to clearly convey the information being presented. The x-axis is labeled 'Diagnosis (0: Benign, 1: Malignant)' and the y-axis is labeled 'Count' to provide context for the data.

Output
The output of the script is a visual representation of the distribution of cancer diagnoses in the dataset. This plot helps in quickly understanding the balance between benign and malignant cases and can provide insights for further analysis or model development.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/a0cd8334-1054-4d13-923d-9405cf4bb7bc)

Pair Plot
The script generates a pair plot of selected features ('area_worst' and 'area_mean') colored by the 'diagnosis' category. This visualization helps in understanding the distribution of these features in benign and malignant cases and the relationships between them.

Correlation Heatmap
The script also creates a heatmap to visualize the correlation between the selected features and the diagnosis. This heatmap provides insights into how these features are related to each other and their association with the diagnosis.

Output
The output of the script includes a pair plot and a correlation heatmap, which together offer a comprehensive view of the selected features in relation to the diagnosis. These visualizations are crucial for identifying patterns and guiding further analysis or model development.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/f593e8a8-0d19-458f-af0d-7b1ef477bbb7)

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/72b04bd7-b0a4-4fd0-a178-6fbdc05fd82f)

Box Plots
The script generates two box plots side by side for a comparative view:

Box Plot of 'area_worst' by Diagnosis: This plot shows the distribution of the 'area_worst' feature for benign and malignant cases, highlighting the differences in their median values and variability.
Box Plot of 'area_mean' by Diagnosis: Similarly, this plot visualizes the distribution of the 'area_mean' feature, providing insights into how this feature varies between benign and malignant tumors.
Output
The output of the script is a set of box plots that offer a clear visualization of the distribution of key features by diagnosis. These plots are valuable for identifying potential patterns and outliers in the data, which can inform further analysis or model development.


![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/3ac3cd53-afb2-4173-9363-6a634c99d145)

Evaluating Model Performance with ROC Curve and AUC:
ROC Curve and AUC
The script calculates the predicted probabilities of the positive class (malignant tumors) and uses these probabilities to compute the ROC curve and AUC. The ROC curve plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at various threshold settings, while the AUC provides a single numerical value summarizing the overall performance of the model.

Output
The output of the script is a plot of the ROC curve with the AUC value displayed in the legend. The ROC curve provides insights into the trade-off between sensitivity (TPR) and specificity (1 - FPR) at different thresholds, while the AUC value indicates the model's ability to distinguish between benign and malignant tumors. A higher AUC value suggests better model performance.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/3797df5b-9bb8-47d2-b634-d48b0ef7f257)

Visualizing Model Accuracy with a Confusion Matrix:

Confusion Matrix
The script computes the confusion matrix, which summarizes the number of true positive, true negative, false positive, and false negative predictions made by the model. This matrix provides a detailed breakdown of the model's performance in classifying benign and malignant tumors.

Heatmap Visualization
The confusion matrix is visualized as a heatmap, with the actual labels on the y-axis and the predicted labels on the x-axis. The cells of the heatmap are annotated with the counts of each category, providing a clear and intuitive representation of the model's accuracy.

Output
The output of the script is a heatmap of the confusion matrix, which offers a comprehensive view of the model's performance in diagnosing cancer. This visualization is crucial for understanding the model's strengths and weaknesses in classification and can guide further improvements or adjustments to the model.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/8c65562b-bebc-441e-a40d-7d8b8ae293be)

Analyzing Model Performance with Precision-Recall Curve:

Precision-Recall Curve
The script calculates precision and recall values at various thresholds and uses these values to plot the Precision-Recall curve. The average precision score is also computed to provide a single numerical summary of the curve, representing the overall quality of the model's precision and recall.

Output
The output of the script is a plot of the Precision-Recall curve with the average precision score displayed in the legend. This curve provides insights into the balance between precision (the ability of the model to correctly identify positive cases) and recall (the ability of the model to capture all positive cases). The average precision score serves as a summary metric for the curve, with higher values indicating better model performance.

![image](https://github.com/pavanmuthyam/Tumor_Type_Classification/assets/87929903/630d8a45-116f-4f94-a19d-206be329b4c9)




















































