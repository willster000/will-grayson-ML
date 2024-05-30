import pandas as pd
import glob

# Assuming df is your DataFrame

'''df = pd.read_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class\\data\\test\\Benign_test.pcap.csv')
df = df.drop(df.columns[45], axis=1)

    # Save the DataFrame to a new csv file
df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class\\data\\test\\Benign_test.pcap.csv', index=False)
'''

# Load the CSV file
df = pd.read_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class\\data\\test\\Benign_test.pcap.csv')

# Drop the 46th column
df = df.drop(df.columns[45], axis=1)

# Save the DataFrame back to CSV
df.to_csv('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class\\data\\test\\Benign_test.pcap.csv', index=False)




'''for file in glob.glob('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\train\\*.csv'):
    file_name = file.split('\\')[-1]

    if 'Spoofing' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([1]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)
    
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
    
    df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class-labeled-data\\test\\{file_name}', index=False)
'''
    
'''
df = pd.read_csv(file)
df = df.assign(benign=pd.Series([0]*len(df)).values)
df = df.assign(attack=pd.Series([1]*len(df)).values)

# Save the DataFrame to a new csv file
df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\six-class-labeled-data\\train\\{file_name}', index=False)
'''