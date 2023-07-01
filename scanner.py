import tkinter as tk
import requests
import json

class IPTraceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Tracer")

        # create frame
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # create IP entry
        self.ip_entry = tk.Entry(frame, width=30)
        self.ip_entry.pack(padx=10, pady=10)

        # create trace button
        self.trace_button = tk.Button(frame, text="Trace IP", command=self.trace_ip)
        self.trace_button.pack()

        # create result label
        self.result_label = tk.Label(frame)
        self.result_label.pack(pady=10)

    def trace_ip(self):
        ip = self.ip_entry.get()
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = json.loads(response.text)

        if "bogon" in data and data["bogon"] == True:
            result = f"{ip} is a Bogon IP"
        else:
            result = f"IP: {data['ip']}\n"
            result += f"City: {data['city']}\n"
            result += f"Region: {data['region']}\n"
            result += f"Country: {data['country']}\n"
            result += f"Location: {data['loc']}\n"
            if 'org' in data:
                result += f"Organisation: {data['org']}\n"

        self.result_label['text'] = result

root = tk.Tk()
app = IPTraceGUI(root)
root.mainloop()
