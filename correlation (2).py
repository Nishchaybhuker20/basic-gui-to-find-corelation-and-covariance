from tkinter import *
import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog as fd 
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr
from researchpy.correlation import corr_case

df = pd.read_excel (r'D:\Project 3\student.xlsx')
def browse():
    global loc
    loc = fd.askopenfilename()
    lab_3 = Label(root, text = loc)
    lab_3.place(x=300, y=45)

def loaddata():
    print (df)
    
#def karl_pearson():
 #   data = pd.read_excel (r'D:\Project 3\student.xlsx') 
  #  df = pd.DataFrame(data)
  #  df[['seasonal','Marks']]
  #  ans=corr_case(df[['seasonal','marks']])    
  #  print(ans)
    
def rank_correlation():
    data = pd.read_excel (r'D:\Project 3\student.xlsx') 
    df = pd.DataFrame(data)
    df[['seasonal','Marks']]
    corelation = df.corr(method="spearman")
    print(corelation)
    
def data_visualizatin():
    df.plot(x='seasonal',y='Marks')
    plt.show()
    
# creating Main window 
root = Tk() 
root.title("GUI APP - Correlation in Python")
root.minsize(600, 400) 
root.wm_iconbitmap("1.ico")
root.configure(background="grey")

# Adding widgets to the Main window 

lab_1 = Label(root, text = 'Correlation Project', font =('Bold', 18))

browseBt = Button(root, text = 'Browse', command=browse)
loadBt = Button(root, text = 'Load Data', command=loaddata)
kpCor_Bt = Button(root, text = 'Karl Pearson', command=browse)
rankCor_Bt = Button(root, text = 'Rank Correlation', command=rank_correlation)
dataVis_Bt = Button(root, text = 'Data Visualization', command=data_visualizatin)

quitBt = Button(root, text = 'Quit from System',command=root.destroy)

lab_1.place(x=190, y=5)
browseBt.place(x=450, y=45, width=100)
loadBt.place(x=450, y=85, width=100)

kpCor_Bt.place(x=450, y=125, width=100) 
rankCor_Bt.place(x=450, y=165, width=100) 
dataVis_Bt.place(x=450, y=205, width=100)

quitBt.place(x=450, y=350, width=100) 

mainloop()        