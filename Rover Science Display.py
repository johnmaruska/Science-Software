# Author: John Maruska
# Created: May 2016
# Updated: May 2016
# For use with MRDT 2016-2017 Rover 

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt

def genGraph():
    # if Data-File selected and no file exist, print error and try again
    pass

root = tk.Tk()
root.title("MRDT Science Display")

##############################################################################################
#           Source Input Frame                                                               #
##############################################################################################

source = ttk.Frame(root, padding="3 3 12 12")
source.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

input_type = tk.StringVar()

file_name = tk.StringVar()
file_entry = ttk.Entry(source, width=90, textvariable=file_name)
file_entry.grid(column=3, row=0, sticky=(tk.W, tk.E))

realtime = ttk.Radiobutton(source, text='Real-Time', variable=input_type,
                           value='realtime', command=(file_entry.config(state="DISABLED")))
realtime.grid(column=1, row=0, sticky=tk.W)

data_file = ttk.Radiobutton(source, text='Data-File', variable=input_type,
                            value='datafile', command=(file_entry.config(state="NORMAL")))
data_file.grid(column=2, row=0, sticky=tk.W)

begin_button = ttk.Button(source, text='Graph', command=genGraph) #generate graph function required
begin_button.grid(column=4, row=0, sticky=tk.W)


##############################################################################################
#           Graph Input Frame                                                                #
##############################################################################################

# Main graph frame
graph_frame = ttk.Frame(root, padding="3 3 12 12")
graph_frame.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))

# Tablature
tabs = ttk.Notebook(graph_frame)
t1 = ttk.Frame(tabs)
t2 = ttk.Frame(tabs)
tabs.add(t1, text='Temp/Humid')
tabs.add(t2, text='CCD')
tabs.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Temp/Humid Graph area
graph_area_TH = ttk.Frame(t1, padding="3 3 12 12")
graph_area_TH.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
# Temperature Figure
figTH = plt.figure(1)
plt.subplots_adjust(hspace=0.27, wspace=0.27, top=0.88, bottom=0.06)
plt.suptitle("Soil Temperature Readings", fontsize=17)
# Temperature Subplot
plt.subplot(2,2,1)
plt.title("Temperature Readings")
plt.ylabel("Temperature (Celsius)")
plt.grid(True)
# Temperature Distribution
plt.subplot(2,2,2)
plt.title("Temperature Distribution")
plt.ylabel("Occurances")
plt.grid(True)
# Humidity Subplot
plt.subplot(2,2,3)
plt.title("Moisture Readings")
plt.ylabel("Moisture Content (%)")
plt.grid(True)
# Humidity Distribution
plt.subplot(2,2,4)
plt.title("Moisture Distribution")
plt.ylabel("Occurances")
plt.grid(True)

canvas = FigureCanvasTkAgg(figTH, master=graph_area_TH)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg(canvas, graph_area_TH)

# Temp/Humid Graph Options
graph_options_TH = ttk.Frame(t1, padding="3 3 12 12")
graph_options_TH.grid(column=2, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
graph_label_TH = ttk.Label(graph_options_TH, text="Display Sensors:")
graph_label_TH.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Create sensor checkbuttons
show_temp1  = tk.BooleanVar()
show_temp2  = tk.BooleanVar()
show_temp3  = tk.BooleanVar()
show_temp4  = tk.BooleanVar()
show_humid1 = tk.BooleanVar()
show_humid2 = tk.BooleanVar()
show_humid3 = tk.BooleanVar()
show_humid4 = tk.BooleanVar()
show_temp1.set(False)
show_temp2.set(False)
show_temp3.set(False)
show_temp4.set(False)
show_humid1.set(False)
show_humid2.set(False)
show_humid3.set(False)
show_humid4.set(False)

temp1  = ttk.Checkbutton(graph_options_TH, var=show_temp1, text='Temperature 1')
temp2  = ttk.Checkbutton(graph_options_TH, var=show_temp2, text='Temperature 2')
temp3  = ttk.Checkbutton(graph_options_TH, var=show_temp3, text='Temperature 3')
temp4  = ttk.Checkbutton(graph_options_TH, var=show_temp4, text='Temperature 4')
humid1 = ttk.Checkbutton(graph_options_TH, var=show_humid1, text='Humidity 1')
humid2 = ttk.Checkbutton(graph_options_TH, var=show_humid2, text='Humidity 2')
humid3 = ttk.Checkbutton(graph_options_TH, var=show_humid3, text='Humidity 3')
humid4 = ttk.Checkbutton(graph_options_TH, var=show_humid4, text='Humidity 4')

# Attach checkbuttons to frame
temp1.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
temp2.grid(column=0, row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
temp3.grid(column=0, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))
temp4.grid(column=0, row=4, sticky=(tk.N, tk.W, tk.E, tk.S))
humid1.grid(column=0, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
humid2.grid(column=0, row=6, sticky=(tk.N, tk.W, tk.E, tk.S))
humid3.grid(column=0, row=7, sticky=(tk.N, tk.W, tk.E, tk.S))
humid4.grid(column=0, row=8, sticky=(tk.N, tk.W, tk.E, tk.S))


# CCD Graph
graph_area_CCD = ttk.Frame(t2, padding="3 3 12 12")
graph_area_CCD.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

figCCD = plt.figure(2)
plt.title("Raman Spectrometer Reading")
plt.grid(True)

canvas = FigureCanvasTkAgg(figCCD, master=graph_area_CCD)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg(canvas, graph_area_CCD)
toolbar.update()
