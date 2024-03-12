# PRODIGY_CS_05
Prodigy Cyber Security Internship - Task 5 - Network Packet Analyzer

Develop a packet sniffer GUI tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

Here’s a simple example of how you might develop a packet sniffer GUI tool using Python and the libraries pyshark for packet capture and analysis, and tkinter for the GUI. This is a basic example and may need to be adjusted based on your specific needs.

[Please do check out the attached packet_sniffer_GUI.py file.]

This script creates a simple GUI with a button to start the packet capture. When the button is clicked, it starts capturing packets on the ‘Ethernet’ interface (you may need to adjust this based on your network configuration) and displays some information about each packet in the text box.

Please note that you’ll need to have the pyshark and tkinter libraries installed, and you may need to run this script with administrative privileges to capture packets. Also, please be aware that packet sniffing can have legal and ethical implications depending on the context in which it’s used. Always respect privacy and use this tool responsibly.

This is a very basic example and there’s a lot more you could do with this, such as adding more detailed packet analysis, filtering options, etc. But this should give you a good starting point.
