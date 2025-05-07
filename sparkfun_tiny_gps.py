# receive GPS latitude & longitude data and print them with packet number in console
import numpy as np
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import os
import sys

# Create data directory if it doesn't exist
data_dir = 'data'  # Changed to match MATLAB version
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create filename with datetime format similar to MATLAB's datestr(now)
current_time = datetime.datetime.now()
filename = f"gps data {current_time.strftime('%d-%b-%Y %H-%M-%S')}.csv"
file_path = os.path.join(data_dir, filename)

# Setup the plot first
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("GPS Trajectory")
ax.grid(True, linestyle='--')
points, = ax.plot([], [], 'r.', markersize=3)
lats = []
lons = []

# Key press handler
def on_key_press(event):
    if event.key == 'q' or event.key == 'escape':
        print("Termination key pressed. Cleaning up...")
        plt.close('all')  # Close all figures
        if 'ser' in globals() and ser.is_open:
            ser.close()
        if 'data_file' in globals() and data_file and not data_file.closed:
            data_file.close()
        print(f"Data saved to {file_path}")
        print('Serial port is terminated.')
        sys.exit(0)  # Exit the program cleanly

# Connect the key press event
fig.canvas.mpl_connect('key_press_event', on_key_press)

# Open serial port
try:
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM14'
    ser.open()
    if (ser.is_open):
        print('Serial port %s with %i baudrate is open.' %(ser.port, ser.baudrate))
except Exception as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)
    
startByte = b'\x68'  # 'h' in hex
packetLength = 9  # number of bytes after the startByte
packetByteArray = bytearray(packetLength)
coordinate = np.zeros(2, dtype='float32')  # latitude, longitude
i = 0  # packet number

# Open the data file
data_file = open(file_path, 'w')
data_file.write("Packet,Latitude,Longitude\n")  # Write header
print(f"Recording data to: {filename}")

try:
    while True:
        plt.pause(0.01)  # Allow GUI events to be processed
        
        if ser.in_waiting > 0 and ser.read() == startByte: # corresponds to 'h'
            if i == 0:
                ser.flush()
                print('The serial port buffer is flushed. Data transfer begins now.')
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
                    data_file.write(f"{i},{coordinate[0]},{coordinate[1]}\n")
                    data_file.flush()  # Ensure data is written even if program crashes
                    
                    # Update the plot
                    lats.append(coordinate[0])
                    lons.append(coordinate[1])
                    points.set_data(lons, lats)
                    
                    # Adjust axes limits if needed
                    if len(lons) > 1:
                        ax.set_xlim(min(lons) - 0.0001, max(lons) + 0.0001)
                        ax.set_ylim(min(lats) - 0.0001, max(lats) + 0.0001)
                    
                    # Update the plot title
                    ax.set_title(f"GPS Trajectory - Packet #{i}")
                    fig.canvas.draw_idle()
                else:
                    print(f"Checksum error in packet {i}: calculated {checksum}, received {packetByteArray[8]}")
            
            i += 1 # next packet

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

finally:
    # Clean up resources
    if 'data_file' in locals() and data_file and not data_file.closed:
        data_file.close()
        print(f"Data saved to {file_path}")
    
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print('Serial port is terminated.')
    
    plt.close('all')