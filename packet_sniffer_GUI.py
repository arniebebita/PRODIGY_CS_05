import tkinter as tk
import pyshark

class PacketSnifferGUI:
    def __init__(self, master):
        self.master = master
        master.title("Packet Sniffer")

        self.capture_button = tk.Button(master, text="Start Capture", command=self.start_capture)
        self.capture_button.pack()

        self.output_text = tk.Text(master)
        self.output_text.pack()

    def start_capture(self):
        capture = pyshark.LiveCapture(interface='Ethernet')
        for packet in capture.sniff_continuously(packet_count=10):
            self.output_text.insert(tk.END, f"Packet: {packet}\n")
            self.output_text.insert(tk.END, f"Source IP: {packet.ip.src}\n")
            self.output_text.insert(tk.END, f"Destination IP: {packet.ip.dst}\n")
            self.output_text.insert(tk.END, f"Protocol: {packet.transport_layer}\n")
            self.output_text.insert(tk.END, f"Payload: {packet}\n\n")

root = tk.Tk()
gui = PacketSnifferGUI(root)
root.mainloop()