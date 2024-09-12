import tkinter as tk
from tkinter import messagebox
import requests
import json
import re

class IPTraceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Tracer Tool")
        self.root.geometry("500x400")  # Set window size
        self.root.configure(bg="#f4f4f9")

        # Title label
        title_label = tk.Label(self.root, text="IP Address Tracer", font=('Arial', 18, 'bold'), bg="#f4f4f9")
        title_label.pack(pady=10)

        # Create frame for input
        input_frame = tk.Frame(self.root, bg="#f4f4f9")
        input_frame.pack(pady=10)

        # Label for instruction
        self.instruction_label = tk.Label(input_frame, text="Enter IP Address:", font=('Arial', 12), bg="#f4f4f9")
        self.instruction_label.pack(pady=5)

        # Entry for IP
        self.ip_entry = tk.Entry(input_frame, width=30, font=('Arial', 14))
        self.ip_entry.pack(pady=5)

        # Create trace button
        self.trace_button = tk.Button(input_frame, text="Trace IP", command=self.trace_ip, font=('Arial', 12), bg='lightblue')
        self.trace_button.pack(pady=10)

        # Create help button
        self.help_button = tk.Button(input_frame, text="Help", command=self.show_help, font=('Arial', 12), bg='lightgreen')
        self.help_button.pack(pady=5)

        # Create frame for results
        self.result_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.result_frame.pack(pady=20)

        # Create result label
        self.result_label = tk.Label(self.result_frame, text="IP Information will appear here.", justify="left", font=('Arial', 10), wraplength=400, bg="#f4f4f9")
        self.result_label.pack(pady=10)

        # Footer
        footer_label = tk.Label(self.root, text="© 2024 TACHY | www.tachy.in | info@tachy.in", font=('Arial', 10), bg="#f4f4f9", fg="gray")
        footer_label.pack(side="bottom", pady=10)
    
    def trace_ip(self):
        ip = self.ip_entry.get()

        # Validate IP address format
        if not self.is_valid_ip(ip):
            messagebox.showerror("Invalid IP", "Please enter a valid IP address.")
            return
        
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            data = json.loads(response.text)
        except requests.exceptions.RequestException:
            messagebox.showerror("Network Error", "Failed to connect to the IP information service.")
            return
        
        if "bogon" in data and data["bogon"] == True:
            result = f"{ip} is a Bogon IP"
        else:
            result = f"IP: {data.get('ip', 'N/A')}\n"
            result += f"City: {data.get('city', 'N/A')}\n"
            result += f"Region: {data.get('region', 'N/A')}\n"
            result += f"Country: {data.get('country', 'N/A')}\n"
            result += f"Location (Lat, Lon): {data.get('loc', 'N/A')}\n"
            if 'org' in data:
                result += f"Organisation: {data.get('org', 'N/A')}\n"
            result += f"Postal Code: {data.get('postal', 'N/A')}\n"

        # Display result in label
        self.result_label.config(text=result)
    
    def is_valid_ip(self, ip):
        # Simple IP address validation (IPv4 only)
        pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        return bool(pattern.match(ip))

    def show_help(self):
        help_text = """
        How to use the IP Tracer Tool:
        1. Enter a valid IP address in the input box.
        2. Click the "Trace IP" button to retrieve information about the IP address.
        3. The information will include city, region, country, and organization details.
        4. For Bogon IPs (internal or invalid IPs), you will receive a notification.
        5. Click the "Help" button anytime to get instructions on how to use this tool.
        """
        messagebox.showinfo("Help - User Manual", help_text)

root = tk.Tk()
app = IPTraceGUI(root)
root.mainloop()
