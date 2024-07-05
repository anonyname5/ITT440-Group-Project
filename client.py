import socket
import ssl
import json
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

SERVER_HOST = '10.0.191.27'  # Use your server's IP address
SERVER_PORT = 443
DATA_FILE = 'health_data.json'
CERT_FILE = 'private.crt'
KEY_FILE = 'private.key'

# Function to save health data locally
def save_data(data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f)

# Function to load health data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Function to send data to the server
def send_data_to_server(data):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    with socket.create_connection((SERVER_HOST, SERVER_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_HOST) as ssock:
            ssock.sendall(data.encode('utf-8'))

# Function to load and send data
def load_and_send_data():
    data = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "heart_rate": heart_rate_entry.get(),
        "blood_pressure": blood_pressure_entry.get(),
    }
    save_data(data)
    send_data_to_server(json.dumps(data))
    messagebox.showinfo("Info", "Data sent to server successfully")

# Function to add health data through the GUI
def add_health_data():
    data = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "heart_rate": heart_rate_entry.get(),
        "blood_pressure": blood_pressure_entry.get(),
    }
    save_data(data)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    heart_rate_entry.delete(0, tk.END)
    blood_pressure_entry.delete(0, tk.END)
    messagebox.showinfo("Info", "Data saved successfully")

# Function to view saved health data
def view_data():
    data = load_data()
    display.delete(1.0, tk.END)
    for entry in data:
        display.insert(tk.END, f"{entry}\n")

# Initialize the GUI application
app = tk.Tk()
app.title("Health Monitoring Client")

tk.Label(app, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(app, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(app, text="Heart Rate:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
heart_rate_entry = tk.Entry(app)
heart_rate_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(app, text="Blood Pressure:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
blood_pressure_entry = tk.Entry(app)
blood_pressure_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

tk.Button(app, text="Add Data", command=add_health_data).grid(row=4, column=1, padx=10, pady=5, sticky=tk.E)
tk.Button(app, text="View Data", command=view_data).grid(row=5, column=1, padx=10, pady=5, sticky=tk.E)

tk.Button(app, text="Send Data", command=load_and_send_data).grid(row=6, column=1, padx=10, pady=5, sticky=tk.E)

display = scrolledtext.ScrolledText(app, state=tk.NORMAL, wrap=tk.WORD, width=50, height=10)
display.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()