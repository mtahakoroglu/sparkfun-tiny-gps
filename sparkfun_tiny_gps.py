# receive GPS latitude & longitude data and print them with packet number in console
import numpy as np
import serial
import matplotlib.pyplot as plt
import keyboard
import datetime
import os

# Create data directory if it doesn't exist
data_dir = 'gps_data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create filename with datetime format similar to MATLAB's datestr(now)
current_time = datetime.datetime.now()
filename = f"gps data {current_time.strftime('%d-%b-%Y %H-%M-%S')}.txt"
file_path = os.path.join(data_dir, filename)

# Open file for recording data
data_file = None

ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM8'
ser.open()
if (ser.is_open):
    print('Serial port %s with %i baudrate is open.' %(ser.port, ser.baudrate))
    
startByte = b'\x68'  # 'h' in hex
packetLength = 9  # number of bytes after the startByte
packetByteArray = bytearray(packetLength)
coordinate = np.zeros(2, dtype='float32')  # latitude, longitude
i = 0  # packet number

while True:
    # Check if ESC key is pressed
    if keyboard.is_pressed('esc') or keyboard.is_pressed('q'): # ESC key (ASCII 27)
        print("ESC or 'q' key pressed. Terminating...")
        break
    
    if ser.read() == startByte: # corresponds to 'h'
        if i == 0:
            ser.flush()
            print('The serial port buffer is flushed. Data transfer begins now.')
            # Open the data file when we start receiving actual data
            data_file = open(file_path, 'w')
            data_file.write("Packet,Latitude,Longitude\n")  # Write header
            print(f"Recording data to: {filename}")
        else:
            # Read in the packet bytes one by one
            for j in range(packetLength):
                packetByteArray[j] = ser.read(1)[0]  # Read one byte and get its value
            
            # Calculate checksum
            checksum = 0
            for j in range(packetLength - 1):
                checksum = checksum ^ packetByteArray[j]  # XOR operation
            checksum = checksum ^ ord(startByte)  # XOR with startByte
            
            # Verify checksum
            if checksum == packetByteArray[8]:  # packetLength-1 = 8
                # Convert bytes to coordinates
                coordinate[0] = np.frombuffer(packetByteArray[0:4], dtype='float32')[0]
                coordinate[1] = np.frombuffer(packetByteArray[4:8], dtype='float32')[0]
                
                print(f'NumBytesAvailable = {ser.in_waiting}    Packet = {i}    Latitude = {coordinate[0]:.7f}    Longitude = {coordinate[1]:.7f}')
                
            
                # Write data to file
                if data_file:
                    data_file.write(f"{i},{coordinate[0]},{coordinate[1]}\n")
                    
                if (i > 1):
                    plt.plot(coordinate[1], coordinate[0], 'r.')
                    plt.xlabel("Longitude")
                    plt.ylabel("Latitude")
                    plt.title(f"Packet #{i}")
                    plt.draw()
                    plt.pause(0.01)
            else:
                print(f"Checksum error in packet {i}: calculated {checksum}, received {packetByteArray[8]}")
        
        i += 1 # next packet

# Clean up
if data_file:
    data_file.close()
    print(f"Data saved to {file_path}")
    
ser.close()
if (not ser.is_open):
    print('Serial port is terminated.')