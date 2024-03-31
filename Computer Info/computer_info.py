import tkinter as tk
from tkinter import ttk
import platform
import subprocess
import psutil
import socket
import datetime

# Function to get CPU information
def get_cpu_info():
    cpu_info = {
        'CPU': platform.processor(),  # Get CPU model
        'Cores': psutil.cpu_count(logical=False),  # Get number of physical cores
        'Threads': psutil.cpu_count(logical=True),  # Get number of logical cores
        'Clock Speed': f"{psutil.cpu_freq().current:.2f} MHz"  # Get current CPU frequency
    }
    return cpu_info

# Function to get GPU information
def get_gpu_info():
    gpu_info = {}
    try:
        gpus = psutil.virtual_memory().available
        if gpus:
            gpu_info['GPU Name'] = 'Integrated GPU'  # If integrated GPU, set name
            gpu_info['GPU Memory'] = f"{gpus / (1024 ** 3):.2f} GB"  # Calculate GPU memory
            gpu_info['Driver Version'] = 'N/A'  # No driver version for integrated GPU
        else:
            # If NVIDIA GPU, get name, memory, and driver version using subprocess
            result = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
                encoding="utf-8")
            gpu_name, memory, driver_version = result.strip().split(',')
            gpu_info['GPU Name'] = gpu_name
            gpu_info['GPU Memory'] = f"{int(memory.strip().split()[0]) / 1024:.2f} GB"
            gpu_info['Driver Version'] = driver_version.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Handle errors if NVIDIA GPU not found
        gpu_info = {'GPU Name': 'N/A', 'GPU Memory': 'N/A', 'Driver Version': 'N/A'}
    return gpu_info

# Function to get battery status
def get_battery_status():
    battery_status = {}
    try:
        battery = psutil.sensors_battery()
        battery_status['Charge Percentage'] = f"{battery.percent}%"  # Get battery charge percentage
        battery_status['Power Plugged'] = "Yes" if battery.power_plugged else "No"  # Check if power is plugged in
        battery_status['Remaining Time'] = "Unknown" if battery.power_plugged else f"{battery.secsleft // 60} minutes"  # Get remaining time if not plugged in
    except AttributeError:
        # Handle errors if battery information not available
        battery_status = {'Charge Percentage': 'N/A', 'Power Plugged': 'N/A', 'Remaining Time': 'N/A'}
    return battery_status

# Function to get network interface information
def get_network_info():
    network_info = {}
    try:
        interfaces = psutil.net_if_addrs()
        for interface_name, addresses in interfaces.items():
            # Get IPv4 addresses for each network interface
            network_info[interface_name] = [address.address for address in addresses if address.family == socket.AF_INET]
    except Exception as e:
        # Handle errors if network information cannot be fetched
        print(f"Error fetching network information: {e}")
    return network_info

# Function to get system temperature
def get_system_temperature():
    temp_info = {}
    try:
        # Get current system temperature
        temp_info = psutil.sensors_temperatures()['coretemp'][0].current
    except Exception as e:
        # Handle errors if system temperature cannot be fetched
        print(f"Error fetching system temperature: {e}")
        temp_info = {'Temperature': 'N/A'}
    return temp_info

# Function to get installed software
def get_installed_software():
    software_list = {}
    try:
        # Use subprocess to get list of installed software
        process = subprocess.Popen(["wmic", "product", "get", "Name"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        software_list['Installed Software'] = [line.strip() for line in stdout.split('\n') if line.strip()]
    except Exception as e:
        # Handle errors if installed software cannot be fetched
        print(f"Error fetching installed software: {e}")
        software_list = {'Installed Software': 'N/A'}
    return software_list

# Function to get connected USB devices
def get_usb_devices():
    usb_devices = []
    try:
        # Get list of connected USB devices
        devices = psutil.disk_partitions(all=True)
        usb_devices = [device.device for device in devices if "removable" in device.opts]
    except Exception as e:
        # Handle errors if USB devices cannot be fetched
        print(f"Error fetching USB devices: {e}")
    return usb_devices

# Function to get display information
def get_display_info():
    display_info = {}
    try:
        # Use subprocess to get display information
        process = subprocess.Popen(["wmic", "desktopmonitor", "get", "ScreenHeight,ScreenWidth",
                                    "/format:list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)
        stdout, stderr = process.communicate()
        lines = [line.strip() for line in stdout.split('\n') if line.strip()]

        # Extract screen resolution, color depth, and refresh rate
        display_info['Screen Resolution'] = lines[0].split('=')[1] + 'x' + lines[1].split('=')[1] if len(lines) >= 2 else 'N/A'
        display_info['Color Depth'] = lines[2].split('=')[1] + ' bits' if len(lines) >= 3 else 'N/A'
        display_info['Refresh Rate'] = lines[3].split('=')[1] + ' Hz' if len(lines) >= 4 else 'N/A'

    except Exception as e:
        # Handle errors if display information cannot be fetched
        print(f"Error fetching display information: {e}")
    return display_info

# Function to get audio devices information
def get_audio_devices_info():
    audio_devices_info = {}
    try:
        # Use PowerShell to get audio devices information
        process = subprocess.Popen(["powershell", "(Get-WmiObject -Class Win32_SoundDevice).Name"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()
        audio_devices_info['Audio Devices'] = [line.strip() for line in stdout.split('\n') if line.strip()]
    except Exception as e:
        # Handle errors if audio devices information cannot be fetched
        print(f"Error fetching audio devices information: {e}")
        audio_devices_info = {'Audio Devices': 'N/A'}
    return audio_devices_info

# Function to check internet connectivity
def check_internet_connectivity():
    try:
        # Use subprocess to ping Google to check internet connectivity
        subprocess.check_call(["ping", "-c", "1", "www.google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception as e:
        # Handle errors if internet connectivity cannot be checked
        print(f"Error checking internet connectivity: {e}")
        return False

# Function to get current date and time
def get_current_date_time():
    try:
        # Get current date and time
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        # Handle errors if current date and time cannot be fetched
        print(f"Error getting current date and time: {e}")
        return 'N/A'

# Function to get memory and disk space information
def get_memory_disk_space_info():
    try:
        # Get memory and disk space information using psutil
        svmem = psutil.virtual_memory()
        total_memory_gb = svmem.total / (1024 ** 3)
        available_memory_gb = svmem.available / (1024 ** 3)

        total_disk = psutil.disk_usage('/')
        total_disk_gb = total_disk.total / (1024 ** 3)
        available_disk_gb = total_disk.free / (1024 ** 3)

        return {
            'Total Memory (RAM)': total_memory_gb,
            'Available Memory (RAM)': available_memory_gb,
            'Total Disk Space': total_disk_gb,
            'Available Disk Space': available_disk_gb
        }
    except Exception as e:
        # Handle errors if memory and disk space information cannot be fetched
        print(f"Error fetching memory and disk space information: {e}")
        return {
            'Total Memory (RAM)': 'N/A',
            'Available Memory (RAM)': 'N/A',
            'Total Disk Space': 'N/A',
            'Available Disk Space': 'N/A'
        }

# Class for creating the GUI
class SystemInformationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Information")
        self.geometry("800x600")
        self.resizable(True, True)
        self.configure(bg="#F0F0F0")

        # Set style for GUI elements
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), foreground="#333333")
        style.configure("Section.TLabel", font=("Arial", 16, "bold"), foreground="#333333")
        style.configure("Key.TLabel", font=("Arial", 14), foreground="#333333")
        style.configure("Value.TLabel", font=("Arial", 14), foreground="#333333")

        # Create main frame and canvas for scrolling
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        system_info_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=system_info_frame, anchor="nw")

        # Add sections for different system information
        self.add_section(system_info_frame, "CPU Information", get_cpu_info())
        self.add_section(system_info_frame, "GPU Information", get_gpu_info())
        self.add_section(system_info_frame, "Battery Status", get_battery_status())
        self.add_section(system_info_frame, "Network Interface Information", get_network_info())
        self.add_section(system_info_frame, "System Temperature", get_system_temperature())
        self.add_section(system_info_frame, "Installed Software", get_installed_software())
        self.add_section(system_info_frame, "Connected USB Devices", {"Connected USB Devices": get_usb_devices()})
        self.add_section(system_info_frame, "Display Information", get_display_info())
        self.add_section(system_info_frame, "Audio Devices Information", get_audio_devices_info())
        self.add_section(system_info_frame, "Internet Connectivity",
                         {"Internet Connectivity": "Connected" if check_internet_connectivity() else "Disconnected"})
        self.add_section(system_info_frame, "Current Date and Time", {"Current Date and Time": get_current_date_time()})
        self.add_section(system_info_frame, "RAM and Disk Space Information", get_memory_disk_space_info())

    # Function to add a section with labels and values
    def add_section(self, parent_frame, section_title, section_data):
        section_frame = ttk.Frame(parent_frame, padding=10)
        section_frame.pack(fill="x")

        section_label = ttk.Label(section_frame, text=section_title, style="Section.TLabel")
        section_label.pack(pady=5)

        for key, value in section_data.items():
            key_label = ttk.Label(section_frame, text=f"{key}:", style="Key.TLabel")
            key_label.pack(side="left", padx=5)

            value_text = "\n".join(value) if isinstance(value, list) else str(value)

            value_label = ttk.Label(section_frame, text=value_text, style="Value.TLabel")
            value_label.pack(side="left", fill="x", expand=True)


if __name__ == "__main__":
    if platform.system() != 'Windows':
        # Check if the script is running on Windows
        print("Sorry, the script is currently available only for Windows Operating System")
    else:
        # Create and run the GUI application
        app = SystemInformationGUI()
        app.mainloop()
