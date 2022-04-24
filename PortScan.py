from tkinter import *
from socket import *
import ipaddress

# define window element
root = Tk()
root.iconbitmap('F:\PythonProjects\intranet.ico')
root.title('Port Scan v1.1    (c) 2022    J.Knight')

# Take input of IP, port, and timeout
myLabel1 = Label(root, text='                              Enter IP address, or CIDR notation:                              ')             
myLabel1.pack()
e1 = Entry(root, width=20, bg='light gray')
e1.pack(side = TOP)
e1.insert(0,'192.168.1.0/24')

myLabel2 = Label(root, text='Enter port to scan:')             
myLabel2.pack()
e2 = Entry(root, width=7, bg='light gray')
e2.pack()
e2.insert(0,'9100')

myLabel3 = Label(root, text='Enter timout in seconds:')             
myLabel3.pack()
e3 = Entry(root, width=4, bg='light gray')
e3.pack()
e3.insert(0,'0.1')

# Define function that builds a broadcast tcp/ip packet
# Sequentially arp ping every address in CIDR range or a single IP
def myClick():
    ip = e1.get()
    port = int(e2.get())
    net4 = ipaddress.ip_network(ip)
    to = float(e3.get())

    for x in net4.hosts():
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(to)
        conn = s.connect_ex((str(x), port))

        if (conn == 0):
            myLabel5 = Label(root, text=f'IP: {x}  Port %d: OPEN' % port)             
            myLabel5.pack()
        else:   
            s.close()
            
    myLabel6 = Label(root, text='****Finished****') 
    myLabel6.pack()

# Search button function call
myButton = Button(root, text='Scan Now', padx=25, bg='light gray', command=myClick)
myButton.pack(pady=5)

myLabel4 = Label(root, text='Results:')             
myLabel4.pack()

root.mainloop()