import pandas as pd
import glob

# Assuming df is your DataFrame
# move DoS ICMP before DDoS ICMP

for file in glob.glob('\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\unlabeled\\train\\*.csv'):
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'Benign' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([1]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'MQTT-DDoS-Connect_Flood' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([1]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'MQTT-DoS-Connect_Flood' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([1]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'MQTT-DDoS-Publish_Flood' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([1]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'MQTT-DoS-Publish_Flood' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([1]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
        
    if 'MQTT-Malformed_Data' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([1]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
        
    if 'Recon-OS_Scan' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([1]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'Recon-Ping_Sweep' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([1]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'Recon-Port_Scan' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([1]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([0]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'Recon-VulScan' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
        df = df.assign(benign=pd.Series([0]*len(df)).values)

        df = df.assign(MQTT_DDoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Connect_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DDoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_DoS_Publish_Flood=pd.Series([0]*len(df)).values)
        df = df.assign(MQTT_Malformed_Data=pd.Series([0]*len(df)).values)
        
        df = df.assign(Recon_OS_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Ping_Sweep=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_Port_Scan=pd.Series([0]*len(df)).values)
        df = df.assign(Recon_VulScan=pd.Series([1]*len(df)).values)
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
   
    if 'DoS-ICMP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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

        df = df.assign(DoS_ICMP=pd.Series([1]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DoS-SYN' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([1]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DoS-TCP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([1]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DoS-UDP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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

        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([1]*len(df)).values)
    
        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DDoS-ICMP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([1]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DDoS-ICMP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([1]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DDoS-SYN' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([1]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)

    if 'DDoS-TCP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([1]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([0]*len(df)).values)
    
    if 'DDoS-UDP' in file_name:
        df = pd.read_csv(file)

        df = df.assign(spoofing=pd.Series([0]*len(df)).values)
        
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
        
        df = df.assign(DoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DoS_UDP=pd.Series([0]*len(df)).values)

        df = df.assign(DDoS_ICMP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_SYN=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_TCP=pd.Series([0]*len(df)).values)
        df = df.assign(DDoS_UDP=pd.Series([1]*len(df)).values)

    df.to_csv(f'\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\nineteen-class\\data\\train\\{file_name}', index=False)
