# -*- coding: utf-8 -*-
# /usr/bin/python3

import socket
try:
    from Tkinter import *
except:
    from tkinter import *


def getMsg():
    """main loop getter function"""
    sin.setblocking(False)
    try:
        msg = sin.recv(1024)
        print("[log] msg!")
        log.config(state=NORMAL)
        log.insert(END, msg.decode('utf-8') + "\n")
        log.config(state=DISABLED)
        log.see(END)
        tk.after(1, getMsg)
        return
    except:
        tk.after(1, getMsg)
        return


def sendMsg(event):
    """send to"""
    if (text.get()) != '':
        msg = name.get() + ": " + text.get()
        msg = msg.encode('utf-8')
        sout.sendto(msg, ('255.255.255.255', 11719))
        text.set('')


# listening socket
sin = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sin.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sin.bind(('0.0.0.0', 11719))

# sending socket
sout = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sout.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


# GUI init
tk = Tk()
tk.title('ezchat')

iframe = Frame(tk, bd=1)  # input entries frame
oframe = Frame(tk, bd=1)  # log frame
iframe.pack(side='bottom', fill='x', expand='true')
oframe.pack(side='top', fill='x', expand='true')

text = StringVar()
name = StringVar()
name.set('Justus')
text.set('')

nick = Entry(iframe, textvariable=name)
msg = Entry(iframe, textvariable=text)
log = Text(oframe)

scroll = Scrollbar(oframe)
scroll.pack(side='right', fill='y', expand='true')
scroll['command'] = log.yview
log['yscrollcommand'] = scroll.set

msg.pack(side='right', fill='x', expand='true')
nick.pack(side='left', fill='x', expand='true')
log.pack(side='left', fill='x', expand='true')

log.config(state=DISABLED, wrap=WORD)

log.config(state=NORMAL)
log.insert(END, "Hello " + name.get() + "!\n")
log.config(state=DISABLED)

msg.bind('<Return>', sendMsg)
tk.after(1, getMsg)
tk.mainloop()
