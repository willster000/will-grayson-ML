import pandas as pd
import glob
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Grayson's path
#train_folder = "C:\\Users\\grays\\Downloads\\train\\train\\"
#test_folder = "C:\\Users\\grays\\Downloads\\test\\test\\"
'''
# Will's path
train_folder = "C:\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\train\\"
test_folder = "C:\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\test\\"

# List all CSV files in the train folder
train_files = glob.glob(train_folder + "*.csv")
test_files = glob.glob(test_folder + "*.csv")

# Function to load and concatenate CSV files from a list of file paths
def load_and_concat(files):
    df_list = []
    for file in files:
        df = pd.read_csv(file)
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

# Load and concatenate training and testing data
train_df = load_and_concat(train_files)
test_df = load_and_concat(test_files)

def label_data(df):
    df['label'] = (df['ack_flag_number'] < 0.4).astype(int)
    return df

# Label the training and testing data
train_df = label_data(train_df)
test_df = label_data(test_df)

# Separate features and labels
X_train = train_df.drop(columns=['label'])
y_train = train_df['label']
X_test = test_df.drop(columns=['label'])
y_test = test_df['label']

# Create a scaler object
scaler = MinMaxScaler()

# Fit the scaler to the training features and transform both training and testing features
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert the scaled features to DataFrames
X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test.columns)

model = LogisticRegression()

# Train the model
model.fit(X_train_scaled_df, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled_df)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(model, X_train_scaled_df, y_train, cv=5, scoring='accuracy')

print(cv_scores)
print(cv_scores.mean())
'''
# Load the CSV file
df = pd.read_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\two-class\\data\\test\\Benign_test_modified.pcap.csv')

# Drop the 46th column
df = df.drop(df.columns[45], axis=1)

# Save the DataFrame back to CSV
df.to_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\two-class\\data\\test\\Benign_test.pcap.csv', index=False)