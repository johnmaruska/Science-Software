# Missouri University of Science and Technology: Mars Rover Design Team
# Author: John Maruska
# For use with MST-MRDT 2016-2017 Rover (as of yet unnamed)

# TODO:
# * Graph button command to generate graphs
# * Check to make sure non-existent or non-compatible files are sent in
# * Collect data code block
#   * Read through network from the rover
#   * Generate from CSV
# * Katie Request: Save digsite graphs
#   * Press button -> Create new tab -> Move graphs to new tab
# * Hide / Show data immediately on 

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib import pyplot as plt

root = tk.Tk()
root.title("MRDT Science Display")

digsites_tabs = ttk.Notebook(root)
current_site = tk.Frame(digsites_tabs)
digsites_tabs.add(current_site, text="Current Digsite")
digsites_tabs.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))

site_count = 0
site_temp1 = []
site_temp2 = []
site_temp3 = []
site_temp4 = []
site_humid1 = []
site_humid2 = []
site_humid3 = []
site_humid4 = []

################################################
#            Generate New Tabs                 #
################################################

def new_tab():
    
    global site_count
    global digsite_tabs
    global current_fig_th
    global current_fig_ccd
    global site_temp1
    global site_temp2
    global site_temp3
    global site_temp4
    global site_humid1
    global site_humid2
    global site_humid3
    global site_humid4
    site_count = site_count + 1
    
    # New main tab
    new_site = tk.Frame(digsites_tabs)
    digsites_tabs.add(new_site, text=("Digsite #" + str(site_count)))
    
    # Main graph frame
    new_graph_frame = ttk.Frame(new_site)
    new_graph_frame.grid(column=0, row=1)
    
    # Sensor Type Tabs
    new_tabs = ttk.Notebook(new_graph_frame)
    new_th = ttk.Frame(new_tabs)
    new_ccd = ttk.Frame(new_tabs)
    new_tabs.add(new_th, text='Temp/Humid')
    new_tabs.add(new_ccd, text='CCD')
    new_tabs.grid(column=0, row=0)
    
    # Temp/Humid Graph area
    new_graph_area_th = ttk.Frame(new_th, padding="3 3 12 12")
    new_graph_area_th.grid(column=0, row=0)
    
    # PyPlot Figures
    new_fig_th = current_fig_th
    
    # attach back to Tkinter interface
    canvas = FigureCanvasTkAgg(new_fig_th, master=new_graph_area_th)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, new_graph_area_th)
    
    # Temp/Humid Graph Options
    new_graph_options_th = ttk.Frame(new_th, padding="3 3 12 12")
    new_graph_options_th.grid(column=2, row=0)
    new_graph_label_th = ttk.Label(new_graph_options_th, text="Show Sensors:")
    new_graph_label_th.grid(column=0, row=0)
    
    # Sidebar of Options
    show_new_temp1 = tk.BooleanVar()
    show_new_temp2 = tk.BooleanVar()
    show_new_temp3 = tk.BooleanVar()
    show_new_temp4 = tk.BooleanVar()
    show_new_humid1 = tk.BooleanVar()
    show_new_humid2 = tk.BooleanVar()
    show_new_humid3 = tk.BooleanVar()
    show_new_humid4 = tk.BooleanVar()
    show_new_temp1.set(False)
    show_new_temp2.set(False)
    show_new_temp3.set(False)
    show_new_temp4.set(False)
    show_new_humid1.set(False)
    show_new_humid2.set(False)
    show_new_humid3.set(False)
    show_new_humid4.set(False)
    site_temp1.append(show_new_temp1)
    site_temp2.append(show_new_temp2)
    site_temp3.append(show_new_temp3)
    site_temp4.append(show_new_temp4)
    site_humid1.append(show_new_humid1)
    site_humid2.append(show_new_humid2)
    site_humid3.append(show_new_humid3)
    site_humid4.append(show_new_humid4)
    
    #Create checkbuttons
    new_temp1  = ttk.Checkbutton(new_graph_options_th,
                                 var=site_temp1[site_count-1],
                                 text='Temperature 1')
    new_temp2  = ttk.Checkbutton(new_graph_options_th,
                                 var=site_temp2[site_count-1],
                                 text='Temperature 2')
    new_temp3  = ttk.Checkbutton(new_graph_options_th,
                                 var=site_temp3[site_count-1],
                                 text='Temperature 3')
    new_temp4  = ttk.Checkbutton(new_graph_options_th,
                                 var=site_temp4[site_count-1],
                                 text='Temperature 4')
    new_humid1 = ttk.Checkbutton(new_graph_options_th,
                                 var=site_humid1[site_count-1],
                                 text='Humidity 1')
    new_humid2 = ttk.Checkbutton(new_graph_options_th,
                                 var=site_humid2[site_count-1],
                                 text='Humidity 2')
    new_humid3 = ttk.Checkbutton(new_graph_options_th,
                                 var=site_humid3[site_count-1],
                                 text='Humidity 3')
    new_humid4 = ttk.Checkbutton(new_graph_options_th,
                                 var=site_humid4[site_count-1],
                                 text='Humidity 4',
                                 padding="2 2 2 271")

    # Attach checkbuttons to frame
    new_temp1.grid(column=0, row=1)
    new_temp2.grid(column=0, row=2)
    new_temp3.grid(column=0, row=3)
    new_temp4.grid(column=0, row=4)
    new_humid1.grid(column=0, row=5, sticky=tk.W)
    new_humid2.grid(column=0, row=6, sticky=tk.W)
    new_humid3.grid(column=0, row=7, sticky=tk.W)
    new_humid4.grid(column=0, row=8, sticky=tk.W)

    # Create CCD Graph area
    new_graph_area_ccd = ttk.Frame(new_ccd, padding="3 3 12 12")
    new_graph_area_ccd.grid(column=0, row=0)
    new_fig_ccd = current_fig_ccd
    canvas = FigureCanvasTkAgg(new_fig_ccd, master=new_graph_area_ccd)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, new_graph_area_ccd)
    toolbar.update()
    
def save_graph():
    new_tab()

################################################
#           Source Input Frame                 #
################################################

source = ttk.Frame(current_site, padding="3 3 12 12")
source.grid(column=0, row=1)

input_type = tk.StringVar()

file_name = tk.StringVar()
file_entry = ttk.Entry(source, width=90, textvariable=file_name, state='disabled')
file_entry.grid(column=3, row=0, sticky=(tk.W, tk.E))

def entry_toggle():
    global input_type
    if input_type.get() == 'realtime':
        file_entry.config(state='disabled')
    elif input_type.get() == 'datafile':
        file_entry.config(state='active')

realtime = ttk.Radiobutton(source, text='Real-Time', variable=input_type,
                           value='realtime', command=entry_toggle)
realtime.grid(column=1, row=0, sticky=tk.W)
realtime.invoke()

data_file = ttk.Radiobutton(source, text='Data-File', variable=input_type,
                            value='datafile', command=entry_toggle)
data_file.grid(column=2, row=0, sticky=tk.W)

graph_button = ttk.Button(source, text='Graph') #generate graph function required
graph_button.grid(column=4, row=0, sticky=tk.W)

################################################
#           Graph Input Frame                  #
################################################

# Main graph frame
current_graph_frame = ttk.Frame(current_site, padding="3 3 12 12")
current_graph_frame.grid(column=0, row=2)

# Tablature
tabs = ttk.Notebook(current_graph_frame)
current_th = ttk.Frame(tabs)
current_ccd = ttk.Frame(tabs)
tabs.add(current_th, text='Temp/Humid')
tabs.add(current_ccd, text='CCD')
tabs.grid(column=0, row=0)

# Temp/Humid Graph area
graph_area_th = ttk.Frame(current_th, padding="3 3 12 12")
graph_area_th.grid(column=1, row=0)


################################################
#          Actual PyPlot Figures               #   
################################################

# Temperature Figure
current_fig_th = plt.figure(1)
plt.subplots_adjust(hspace=0.27, wspace=0.27, top=0.88, bottom=0.06)
plt.suptitle("Soil Readings", fontsize=17)
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

# Attach back to Tkinter interface
canvas = FigureCanvasTkAgg(current_fig_th, master=graph_area_th)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg(canvas, graph_area_th)

################################################
#          Sidebar of Options                  #   
################################################

# Temp/Humid Graph Options
current_graph_options_th = ttk.Frame(current_th, padding="3 3 12 12")
current_graph_options_th.grid(column=2, row=0)
graph_label_TH = ttk.Label(current_graph_options_th, text="Display Sensors:")
graph_label_TH.grid(column=0, row=0)

# Save Digsite Graphs Button
save_button = ttk.Button(current_graph_options_th, text='Store Graphs', command=save_graph)
save_button.grid(column=0, row=10, sticky=tk.S)

# Create sensor checkbuttons
show_current_temp1  = tk.BooleanVar()
show_current_temp2  = tk.BooleanVar()
show_current_temp3  = tk.BooleanVar()
show_current_temp4  = tk.BooleanVar()
show_current_humid1 = tk.BooleanVar()
show_current_humid2 = tk.BooleanVar()
show_current_humid3 = tk.BooleanVar()
show_current_humid4 = tk.BooleanVar()
show_current_temp1.set(False)
show_current_temp2.set(False)
show_current_temp3.set(False)
show_current_temp4.set(False)
show_current_humid1.set(False)
show_current_humid2.set(False)
show_current_humid3.set(False)
show_current_humid4.set(False)

current_temp1 = ttk.Checkbutton(current_graph_options_th,
                                var=show_current_temp1,
                                text='Temperature 1')
current_temp2 = ttk.Checkbutton(current_graph_options_th,
                                var=show_current_temp2,
                                text='Temperature 2')
current_temp3 = ttk.Checkbutton(current_graph_options_th,
                                var=show_current_temp3,
                                text='Temperature 3')
current_temp4 = ttk.Checkbutton(current_graph_options_th,
                                var=show_current_temp4,
                                text='Temperature 4')
current_humid1 = ttk.Checkbutton(current_graph_options_th,
                                 var=show_current_humid1,
                                 text='Humidity 1')
current_humid2 = ttk.Checkbutton(current_graph_options_th,
                                 var=show_current_humid2,
                                 text='Humidity 2')
current_humid3 = ttk.Checkbutton(current_graph_options_th,
                                 var=show_current_humid3,
                                 text='Humidity 3')
current_humid4 = ttk.Checkbutton(current_graph_options_th,
                                 var=show_current_humid4,
                                 text='Humidity 4',
                                 padding="2 2 2 271")

# Attach checkbuttons to frame
current_temp1.grid(column=0, row=1)
current_temp2.grid(column=0, row=2)
current_temp3.grid(column=0, row=3)
current_temp4.grid(column=0, row=4)
current_humid1.grid(column=0, row=5, sticky=tk.W)
current_humid2.grid(column=0, row=6, sticky=tk.W)
current_humid3.grid(column=0, row=7, sticky=tk.W)
current_humid4.grid(column=0, row=8, sticky=tk.W)

################################################
#             CCD GRAPH AREA                   #   
################################################

graph_area_ccd = ttk.Frame(current_ccd, padding="3 3 12 12")
graph_area_ccd.grid(column=0, row=0)

current_fig_ccd = plt.figure(2)
plt.title("Raman Spectrometer Reading")
plt.grid(True)

canvas = FigureCanvasTkAgg(current_fig_ccd, master=graph_area_ccd)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg(canvas, graph_area_ccd)
toolbar.update()
