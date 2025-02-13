import socket
import os
import time
import tkinter as tk
from tkinter import filedialog, Tk, Label, Entry, Button, messagebox
import threading
import multiprocessing


class Fxg(Tk):
    def __init__(udp):
        super(Fxg, udp).__init__()
        
        
        udp.title("UDP Nav Sender")
        udp.minsize(150, 70)
        udp.Ip()
        udp.Ipe()
        udp.Port()
        udp.Porte()
        udp.Start()
        udp.Quit()
        
        
       
    def Ip(udp):
        
        udp.Ip_l = Label(udp, text="Enter IP adress:")
        udp.Ip_l.grid(column = 1, row = 1)
        
    def Ipe(udp):
        
        udp.Ip_e = tk.Entry(udp)
        udp.Ip_e.grid(column = 2, row = 1)
        udp.Ip_e.insert(0,"10.146.144.63")

    def Port(udp):
        
        udp.Port_l = Label(udp, text="Enter port:")
        udp.Port_l.grid(column = 1, row = 2)
        
    def Porte(udp):
        
        udp.Port_e = tk.Entry(udp)
        udp.Port_e.grid(column = 2, row = 2)
        udp.Port_e.insert(0,"1111")

        
    def Quit(udp):
        udp.exit = tk.Button(width = 16,text = "Exit ", command=udp.Exit )
        udp.exit.grid(column = 2, row = 3)

        

    def Run(udp):
        
      
        try:
            IP_ADDRESS = udp.Ip_e.get()
        except ValueError:
            messagebox.showinfo("failed to get IP")
            return
        try:
            PORT_set = int(udp.Port_e.get())
        except ValueError:
            messagebox.showinfo("failed to get Port number")
            return
        try:
            FILE_NAME = filedialog.askopenfilename(title="Select text file to be output")
        except ValueError:
            return
        except FileNotFoundError:
            return

        try:
            open(FILE_NAME, 'r')
        except FileNotFoundError:
             messagebox.showinfo("no file")
             
        except ValueError:
             messagebox.showinfo("failed to read file")
             
        
        with open(FILE_NAME, 'r') as file:
            try:
                lines = file.readlines()
            except ValueError:
                messagebox.showinfo("failed to read file")
                return
            except FileNotFoundError:
                messagebox.showinfo("failed to read file")
                return
            
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    

            while True:
                
               
                for line in lines:
                    try:
                        sock.sendto(line.encode(), (IP_ADDRESS, PORT_set))
                        print(f'{line.strip()}')
                        time.sleep(0.25)
                        
                        
                    except ValueError:
                        messagebox.showinfo("failed to read file")
                        return
                    except RuntimeError:
                        messagebox.showinfo("test")
                        return
                       
            
                        
                                 
                                                                                                                                
                
    def Start(udp):
        
        t1 = threading.Thread(target=udp.Run)
        udp.start = tk.Button(width = 16,text = "Start", command=t1.start )
        udp.start.grid(column = 1, row = 3)
        
        
            
       

    def Exit(udp):
        
        udp.destroy
        os._exit(1)
        
        
        

fxg = Fxg()
fxg.mainloop()

