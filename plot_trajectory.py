import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def list_gps_files():
    """List all GPS data files in the gps_data directory"""
    data_dir = 'gps_data'
    if not os.path.exists(data_dir):
        print(f"Error: Directory '{data_dir}' not found.")
        return []
    
    files = glob.glob(os.path.join(data_dir, "gps data *.txt"))
    files.sort(key=os.path.getmtime)  # Sort by modification time
    return files

def get_latest_file():
    """Get the most recently created GPS data file"""
    files = list_gps_files()
    if not files:
        return None
    return files[-1]  # Return the most recent file

def select_file():
    """Allow user to select a file to plot"""
    files = list_gps_files()
    
    if not files:
        print("No GPS data files found.")
        return None
    
    print("\nAvailable GPS data files:")
    for i, file in enumerate(files):
        filename = os.path.basename(file)
        print(f"{i+1}. {filename}")
    
    print(f"\n{len(files)+1}. Latest file ({os.path.basename(files[-1])})")
    
    try:
        choice = int(input(f"\nSelect file to plot (1-{len(files)+1}), or press Enter for latest: ") or len(files)+1)
        if choice == len(files)+1:
            return files[-1]
        elif 1 <= choice <= len(files):
            return files[choice-1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def plot_trajectory(file_path):
    """Plot GPS trajectory from the specified file"""
    try:
        # Read the data file
        data = pd.read_csv(file_path)
        
        # Extract file name for the plot title
        filename = os.path.basename(file_path)
        
        # Create plot
        plt.figure(figsize=(10, 8))
        plt.plot(data['Longitude'], data['Latitude'], 'k.')
        plt.grid(True, linestyle='--')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title(f"GPS Trajectory: {filename}")
        
        # Make the plot a bit nicer
        plt.tight_layout()
        plt.show()
        
        print(f"Plotted {len(data)} GPS points from {filename}")
        
    except Exception as e:
        print(f"Error plotting data: {e}")

def main():
    # Allow user to select a file or use a specific file name
    file_path = select_file()
    
    if file_path:
        plot_trajectory(file_path)
    else:
        print("No file selected. Exiting.")

if __name__ == "__main__":
    main()