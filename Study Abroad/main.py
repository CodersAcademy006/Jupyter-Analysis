# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from scipy import stats
import warnings
warnings.filterwarnings(action='ignore')

# Load dataset
data = pd.read_csv('abroad  - Sheet1.csv')

# Data Cleaning
data['FEES'] = pd.to_numeric(data['FEES'], errors='coerce')
data.dropna(inplace=True)

# Descriptive Statistics
print(data.describe().T)

# Better Color Palettes and Font Sizes
sns.set_palette('coolwarm')
plt.style.use('ggplot')

# 1. Distribution of Course Fees (Enhanced with Better Color and Font)
plt.figure(figsize=(10, 6))
sns.histplot(data['FEES'], bins=20, kde=True, color='#4C72B0')
plt.title('Distribution of Course Fees', fontsize=20, fontweight='bold')
plt.xlabel('Fees', fontsize=15)
plt.ylabel('Density', fontsize=15)
plt.show()

# 2. Number of Courses by Country
plt.figure(figsize=(14, 8))
sns.countplot(data=data, x='COUNTRY', order=data['COUNTRY'].value_counts().index, palette='Spectral')
plt.title('Number of Courses by Country', fontsize=22, fontweight='bold')
plt.xlabel('Country', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# 3. Distribution of Course Types (Enhanced with custom colors)
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='COURSE TYPE', order=data['COURSE TYPE'].value_counts().index, palette='Blues')
plt.title('Distribution of Course Types', fontsize=22, fontweight='bold')
plt.xlabel('Course Type', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# 4. Course Fees Distribution by Country (Boxplot)
plt.figure(figsize=(14, 8))
sns.boxplot(x='COUNTRY', y='FEES', data=data, palette='coolwarm')
plt.title('Course Fees Distribution by Country', fontsize=22, fontweight='bold')
plt.xlabel('Country', fontsize=18)
plt.ylabel('Fees', fontsize=18)
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# 5. Course Fees by Course Type
plt.figure(figsize=(10, 6))
sns.barplot(x='COURSE TYPE', y='FEES', data=data, palette='BuGn_r')
plt.title('Course Fees by Course Type', fontsize=22, fontweight='bold')
plt.xlabel('Course Type', fontsize=18)
plt.ylabel('Fees', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# 6. Correlation Matrix (Only Numeric Columns)
# Select only numeric columns for the correlation matrix
numeric_columns = data.select_dtypes(include=[np.number])

plt.figure(figsize=(10, 8))
corr_matrix = numeric_columns.corr()  # Compute correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix (Numeric Data)', fontsize=22, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# 7. Linear Regression with Extra Metrics
# Encoding categorical features
label_encoder = LabelEncoder()
data['COURSE TYPE'] = label_encoder.fit_transform(data['COURSE TYPE'])
data_encoded = pd.get_dummies(data, columns=['COUNTRY', 'COURSE (SPECIALIZATION)'], drop_first=True)

# Features (X) and target (y)
X = data_encoded.drop(columns='FEES')
y = data_encoded['FEES']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predictions
y_pred_lr = lr_model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred_lr)
mse = mean_squared_error(y_test, y_pred_lr)
r2 = r2_score(y_test, y_pred_lr)

print('Linear Regression Results:')
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Bonus: Outlier Detection using Z-scores (Show outliers for better analysis)
data['z_score'] = np.abs(stats.zscore(data['FEES']))
outliers = data[data['z_score'] > 3]

print("Outliers detected based on z-score method:")
print(outliers[['COUNTRY', 'COURSE (SPECIALIZATION)', 'FEES', 'z_score']])

# 8. Cluster Analysis (Clustering countries based on fees)
from sklearn.cluster import KMeans

# For simplicity, we only use fees and encoded course type
X_cluster = data[['COURSE TYPE', 'FEES']]
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_cluster)

# Plot clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='COURSE TYPE', y='FEES', hue='Cluster', data=data, palette='Set1')
plt.title('Clustering Countries Based on Fees', fontsize=22, fontweight='bold')
plt.xlabel('Course Type (Encoded)', fontsize=18)
plt.ylabel('Fees', fontsize=18)
plt.show()