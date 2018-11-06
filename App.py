#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 05, 2018 04:37:00 AM CAT  platform: Windows NT

from tkinter.filedialog import askopenfilename
import sys
import os
import main as m
import utilities as ut

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("972x696+491+97")
        top.title("Hybrid Algorithm for 0-1 Knapsack Problem")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.01, rely=0.014, relheight=0.97, relwidth=0.983)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=955)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.136, rely=0.03, height=51, width=744)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Hybrid IGA-SA Approach for the 0-1 Knapsack Problem''')
        self.Label1.configure(width=744)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.031, rely=0.237, relheight=0.421, relwidth=0.423)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=404)
        self.Text1.configure(wrap=WORD)

        self.Text1_1 = Text(self.Frame1)
        self.Text1_1.place(relx=0.565, rely=0.237, relheight=0.421
                , relwidth=0.392)
        self.Text1_1.configure(background="white")
        self.Text1_1.configure(font="TkTextFont")
        self.Text1_1.configure(foreground="black")
        self.Text1_1.configure(highlightbackground="#d9d9d9")
        self.Text1_1.configure(highlightcolor="black")
        self.Text1_1.configure(insertbackground="black")
        self.Text1_1.configure(selectbackground="#c4c4c4")
        self.Text1_1.configure(selectforeground="black")
        self.Text1_1.configure(width=374)
        self.Text1_1.configure(wrap=WORD)
        
        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.178, rely=0.133, height=31, width=105)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Dataset Items''')
        self.Label2.configure(width=105)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.712, rely=0.148, height=21, width=88)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Knapsack Items''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.042, rely=0.193, height=21, width=34)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Value''')
        self.Label4.configure(width=34)

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.408, rely=0.193, height=21, width=44)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Weight''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.576, rely=0.193, height=21, width=35)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Value''')

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.89, rely=0.193, height=21, width=44)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Weight''')

        self.Text2 = Text(self.Frame1)
        self.Text2.place(relx=0.293, rely=0.681, relheight=0.273, relwidth=0.674)

        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=644)
        self.Text2.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1,command=self.getfile)
        self.Button1.place(relx=0.052, rely=0.8, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Select Dataset''')
        self.Button1.configure(width=197)

    def add_data(self,data):
        self.Text1.config(state=NORMAL)
        self.Text1.delete('1.0',END)
        for i in range(1,len(data)):
            self.Text1.insert('1.0',str(data[i][0])+'\t\t\t\t\t\t'+str(data[i][1])+'\n')
        self.Text1.config(state=DISABLED)

    def add_bottom(self,dataset,maxw,finw,finv):
        self.Text2.config(state=NORMAL)
        self.Text2.delete('1.0',END)
        self.Text2.insert('1.0','Dataset: '+'\t\t\t\t\t\t'+dataset+'\n')
        self.Text2.insert('1.0','Maximum Knapsack Weigth: '+'\t\t\t\t\t\t'+str(maxw)+'\n')
        self.Text2.insert('1.0','Final Knapsack Weight: '+'\t\t\t\t\t\t'+str(finw)+'\n')
        self.Text2.insert('1.0','Final Knapsack Value: '+'\t\t\t\t\t\t'+str(finv)+'\n')
        self.Text2.config(state=DISABLED)
        
    def add_solution(self,sol,vs,ws):
        self.Text1_1.config(state=NORMAL)
        self.Text1_1.delete('1.0',END)
        for i in range(len(sol)):
            if sol[i]==1:
                self.Text1_1.insert('1.0',str(vs[i])+'\t\t\t\t\t\t'+str(ws[i])+'\n')
        self.Text1_1.config(state=DISABLED)
        
    def getfile(self):
        filename = askopenfilename()
        filename_w_ext = os.path.basename(filename)
        data = ut.readfile(filename)
        self.add_data(data)
        myMain = m.Main(dataset=filename,num_iterations=1)
        v,w,s,mw,myKnapSack = myMain.Run()
        self.add_bottom(filename_w_ext,mw,w,v)
        self.add_solution(s,myKnapSack.getValues(),myKnapSack.getWeights())

if __name__ == '__main__':
    vp_start_gui()