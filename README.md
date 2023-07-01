# ipscanner
A simple GUI tool developed in Python that provides an easy-to-use interface for tracing the geographical location and other details of an IP address. The tool makes use of Python's built-in tkinter library to render the GUI, and the requests library to fetch the information.

A simple GUI tool developed in Python that provides an easy-to-use interface for tracing the geographical location and other details of an IP address. The tool makes use of Python's built-in tkinter library to render the GUI, and the requests library to fetch the information.

Features:

IP Entry Field: This field allows users to input the IP address they want to trace.

Trace Button: After entering the IP address, clicking on the "Trace IP" button triggers the tracing process.

Result Label: The information retrieved from the tracing process, including the IP's city, region, country, GPS location, and organization (if applicable) is displayed here.

The tool makes use of the ipinfo.io API for IP address information. For Bogon IP addresses (fake or non-routable IPs), it informs the user that the IP is a Bogon IP.

Please note that the tool uses the free tier of ipinfo.io, which has a rate limit of 50,000 requests per month. As such, the tool is best suited for light to moderate usage.

Installation:

You need Python 3.x and the requests library to run this tool. You can install requests via pip:

bash
Copy code
pip install requests
Usage:

Run the script with Python 3.x.
In the GUI, enter the IP address you want to trace.
Click the "Trace IP" button.
View the traced IP's information in the result box.
Important: Always make sure you have the appropriate permissions and are respectful of privacy and ethical considerations when tracing IP addresses.

Future Improvement:

Extend functionality to include more detailed information about IP addresses.
Implement error handling for rate-limited or otherwise unsuccessful requests to the ipinfo.io API.
Implement better support for edge cases, such as reserved IP addresses.
Disclaimer: This project is intended for educational and legitimate purposes. The author is not responsible for any misuse of this tool.
