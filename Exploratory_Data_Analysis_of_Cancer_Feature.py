# Create a pair plot
sns.pairplot(df, hue='diagnosis', vars=['area_worst', 'area_mean'], palette='crest')
plt.suptitle('Pair Plot of Selected Features by Diagnosis', y=1.02)
plt.show()

# Create a heatmap of correlations
plt.figure(figsize=(12, 8))
sns.heatmap(df[['area_worst', 'area_mean', 'diagnosis']].corr(), annot=True, cmap='crest')
plt.title('Correlation Heatmap of Selected Features')
plt.show()
