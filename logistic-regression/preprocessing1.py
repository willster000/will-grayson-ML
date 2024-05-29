import pandas as pd
import glob

# Assuming df is your DataFrame
''''
df = pd.read_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\train\\Benign_train.pcap.csv')
df = df.assign(benign=pd.Series([1]*len(df)).values)
df = df.assign(attack=pd.Series([0]*len(df)).values)

    # Save the DataFrame to a new csv file
df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\two-class-labeled-data\\train\\Benign_train.pcap.csv', index=False)
'''

for file in glob.glob('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\train\\*.csv'):
    file_name = file.split('\\')[-1]

    if 'Spoofing' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([1]*len(df)).values)
        df = df.assign(benign=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT=pd.Series([0]*len(df)).values)
        df = df.assign(recon=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS=pd.Series([0]*len(df)).values)
        df = df.assign(DoS=pd.Series([0]*len(df)).values)
    
    if 'Benign' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        df = df.assign(benign=pd.Series([1]*len(df)).values)
        df = df.assign(MQTT=pd.Series([0]*len(df)).values)
        df = df.assign(recon=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS=pd.Series([0]*len(df)).values)
        df = df.assign(DoS=pd.Series([0]*len(df)).values)
    
    if 'MQTT' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        df = df.assign(benign=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT=pd.Series([1]*len(df)).values)
        df = df.assign(recon=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS=pd.Series([0]*len(df)).values)
        df = df.assign(DoS=pd.Series([0]*len(df)).values)
    
    if 'Recon' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        df = df.assign(benign=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT=pd.Series([0]*len(df)).values)
        df = df.assign(recon=pd.Series([1]*len(df)).values)
        df = df.assign(DDoS=pd.Series([0]*len(df)).values)
        df = df.assign(DoS=pd.Series([0]*len(df)).values)
    
    if 'DoS' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        df = df.assign(benign=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT=pd.Series([0]*len(df)).values)
        df = df.assign(recon=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS=pd.Series([0]*len(df)).values)
        df = df.assign(DoS=pd.Series([1]*len(df)).values)

    if 'DDoS' in file_name:
        df = pd.read_csv(file)
        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        df = df.assign(benign=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT=pd.Series([0]*len(df)).values)
        df = df.assign(recon=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS=pd.Series([1]*len(df)).values)
        df = df.assign(DoS=pd.Series([0]*len(df)).values)
    
    df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class-labeled-data\\train\\{file_name}', index=False)

    
'''
df = pd.read_csv(file)
df = df.assign(benign=pd.Series([0]*len(df)).values)
df = df.assign(attack=pd.Series([1]*len(df)).values)

# Save the DataFrame to a new csv file
df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class-labeled-data\\train\\{file_name}', index=False)
'''