# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:22:48 2022

@author: gws

This is a Load Duration Curve program. This program takes in data, cleans it if
needed, and provides two graphs for each circuit breaker, one for overall load
over time and the other is the load over the percentage. It also calculates the
point of intercept between the max capacity and the load-over-percentage curve 
as well as calculating the load at three different chosen percentage points 
alongside the max and the min. It prints a table with all of the information 
in the console, it also exports it to a desired excel output file.

Note: This program uses multiple data frames form pandas, dictionaries
and tkinter for the pop out windows. For more information about them,
look at the standard python Library (https://docs.python.org/3/library/index.html)
"""



#load the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.filedialog as fl
import time
from tkinter import *
import tkinter.ttk as ttk
import tkinter.tix as tix
import datetime

#Setting the output display
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

    
#Changed Variables                                         
printing = []                                           #Initializing the printing list
export_data = []
yLabel = "Demand (A)"                                   #The Y axis label



#Getting requeried values from user using pop out window

def on_tick1():
    if tick_var1.get() == 1:
        selection_combo1.config(state='readonly')
    else:
        selection_combo1.config(state='disabled')

def on_tick2():
    if tick_var2.get() == 1:
        selection_combo2.config(state='readonly')
        selection_combo3.config(state='disabled')
        tick3.config(state='disabled')
    else:
        selection_combo2.config(state='disabled')
        tick3.config(state='enable')
        
def on_tick3():
    if tick_var3.get() == 1:
        selection_combo3.config(state='readonly')
        selection_combo2.config(state='disabled')
        tick2.config(state='disabled')
    else:
        selection_combo3.config(state='disabled')
        tick2.config(state='enable')


root = tix.Tk()
root.geometry("400x300")

tick_var1 = IntVar()
tick1 = ttk.Checkbutton(root, variable=tick_var1, command=on_tick1)
tick_var2 = IntVar()
tick2 = ttk.Checkbutton(root, variable=tick_var2, command=on_tick2)
tick_var3 = IntVar()
tick3 = ttk.Checkbutton(root, variable=tick_var3, command=on_tick3)
tick_var4 = IntVar()
tick4 = ttk.Checkbutton(root, variable=tick_var4)


options1 = [f'{i+2015}' for i in range(11)]
selection_combo1 = ttk.Combobox(root, values=options1, state='readonly')
selection_combo1.set(options1[0])
selection_combo1.config(state='disabled')

options2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
selection_combo2 = ttk.Combobox(root, values=options2, state='readonly')
selection_combo2.set(options2[0])
selection_combo2.config(state='disabled')

options3 = ['Summer', 'Autumn', 'Winter', 'Spring']
selection_combo3 = ttk.Combobox(root, values=options3, state='readonly')
selection_combo3.set(options3[0])
selection_combo3.config(state='disabled')

L_tip = tix.Balloon(root)
L_tip.label.config(fg="yellow", bd=-100)
M_tip = tix.Balloon(root)
M_tip.label.config(fg="yellow", bd=-100)
H_tip = tix.Balloon(root)
H_tip.label.config(fg="yellow", bd=-100)

label = ttk.Label(root, text = "Sampling Iterations")
label.grid(column = 0, row = 0)  
label = ttk.Label(root, text = "Clean Data")
label.grid(column = 0, row = 1) 
label = ttk.Label(root, text = "Low Percentage")
label.grid(column = 0, row = 2)
label = ttk.Label(root, text = "Mid Percentage")
label.grid(column = 0, row = 3)
label = ttk.Label(root, text = "High Percentage")
label.grid(column = 0, row = 4)
label = ttk.Label(root, text = "Enable Yearly Data")
label.grid(column = 0, row = 5)
label = ttk.Label(root, text = "Enable Monthly Data")
label.grid(column = 0, row = 7)
label = ttk.Label(root, text = "Enable Seasonal Data")
label.grid(column = 0, row = 9)
label = ttk.Label(root, text = "Export Load Duration Curve")
label.grid(column = 0, row = 11)

IR = ttk.Combobox(root)
IR['values']= (12, 2, 1)
IR.current(0)

chk_state = BooleanVar()
chk_state.set(False)
C = ttk.Checkbutton(root, text='', var=chk_state)
C.config(state='disabled')

L = ttk.Entry(root)
L_tip.bind_widget(L,balloonmsg="% of Time Test Point (TTP)")
M = ttk.Entry(root)
M_tip.bind_widget(M,balloonmsg="% of Time Test Point (TTP)")
H = ttk.Entry(root)
H_tip.bind_widget(H,balloonmsg="% of Time Test Point (TTP)")

IR.grid(row = 0, column = 1)
C.grid(row = 1, column = 1)
L.grid(row = 2, column = 1)
M.grid(row = 3, column = 1)
H.grid(row = 4, column = 1)
tick1.grid(row = 5, column = 1)
selection_combo1.grid(row = 6, column = 1)
tick2.grid(row = 7, column = 1)
selection_combo2.grid(row = 8, column = 1)
tick3.grid(row = 9, column = 1)
selection_combo3.grid(row = 10, column = 1)
tick4.grid(row = 11, column = 1)

def getInput():
    a = IR.get()
    b = chk_state.get()
    c = L.get()
    if L.get() == '':
        c = 0
    d = M.get()
    if M.get() == '':
        d = 0
    e = H.get()
    if H.get() == '':
        e = 0
    f = tick_var1.get()
    g = selection_combo1.get()
    h = tick_var2.get()
    i = selection_combo2.get()
    j = tick_var3.get()
    k = selection_combo3.get()
    l = tick_var4.get()
    
    root.destroy()
    global params
    params = [a,b,c,d,e,f,g,h,i,j,k,l]


Button(root, text = "submit", command = getInput).grid(row = 20, sticky = W)

mainloop()   
                                               
ir_hour = int(params[0])                                    #number of iterations in an hour
clean = params[1]
low = int(params[2])                                        #Lowest Percentage of interist
mid = int(params[3])                                        #Middel Percentage of interist
high = int(params[4])                                       #Highest Percentage of interist
year_var = int(params[5])
year = int(params[6])
month_var = int(params[7])
month = str(params[8])
season_var = int(params[9])
season = str(params[10])
export = str(params[11])




#Reading the Data file and setting the dataframes
reader = Tk()
filename = fl.askopenfilename(filetype=[("Comma Separated Values (CSV)", ".csv")], title = 'Open Data File in CSV')
filename2 = fl.askopenfilename(title = 'Open Regional Capacity Capability')
filename3 = fl.askopenfilename(title = 'Open an Excel Output File')
if export == "1":
    filename4 = fl.askopenfilename(title = 'Open CSV for exporting LDC')
picture_location = fl.askdirectory(title = "Select a folder to save images")
reader.destroy()
start = time.time()
df_cap = pd.read_excel(filename2, "Switching Diagram Tables-Major") 
df_main_file = pd.read_csv(filename, parse_dates=['DateTime'], dayfirst=True)

df_main_file['DateTime'] = pd.to_datetime(df_main_file['DateTime'], format='%d/%m/%Y %H:%M')

df_main_file['Season'] = "Summer"
df_main_file.loc[df_main_file['DateTime'].dt.month.isin([3, 4, 5]), 'Season'] = "Autumn"
df_main_file.loc[df_main_file['DateTime'].dt.month.isin([6, 7, 8]), 'Season'] = "Winter"
df_main_file.loc[df_main_file['DateTime'].dt.month.isin([9, 10, 11]), 'Season'] = "Spring"

datetime_object = datetime.datetime.strptime(month, "%B")

if season_var:    
    df_main_file = df_main_file[df_main_file['Season'].isin([season])]
if year_var:
    df_main_file = df_main_file[df_main_file['DateTime'].dt.year.isin([year])]
if month_var:
    df_main_file = df_main_file[df_main_file['DateTime'].dt.month.isin([datetime_object.month])]

df_main_file_num = df_main_file.select_dtypes(include=np.number)

if month_var:
    if year_var:
        date_range = month + " " + str(year)
    else:
        date_range = month + str(df_main_file["DateTime"].tolist()[0])[:4] + " to " + str(df_main_file["DateTime"].tolist()[-1])[:4]
elif season_var:
    if year_var:
        date_range = season + " " + str(year)
    else:
        date_range = season + str(df_main_file["DateTime"].tolist()[0])[:4] + " to " + str(df_main_file["DateTime"].tolist()[-1])[:4]
else:
    date_range = str(df_main_file["DateTime"].tolist()[0])[:10] + " to " + str(df_main_file["DateTime"].tolist()[-1])[:10]

#getting the name of station used and the number of circuit breakers
if "Twizel" in filename:
    station = "TWIZEL"
elif "Temuka" in filename:
    station = "TEMUKA"
elif "Tekapo" in filename:
    station = "TEKAPO"
elif "Timaru" in filename:
    station = "TIMARU"
elif "Bells" in filename:
    station = "BELLS POND"
elif "Studholme" in filename:
    station = "STUDHOLME"
elif "Albury" in filename:
    station = "ALBURY"
elif "Fairlie" in filename:
    station = "FAIRLIE"
elif "Cooney" in filename:
    station = "COONEY'S ROAD"
elif "Grasmere" in filename:
    station = "GRASMERE"
elif "Hunt" in filename:
    station = "HUNT"
elif "North" in filename:
    station = "NORTH"
elif "Pareora" in filename:
    station = "PAREORA"  
elif "Pleasant" in filename:
    station = "PLEASANT"  
elif "Unwin" in filename:
    station = "UNWIN" 
elif "Old" in filename:
    station = "OLD" 
elif "Haldon" in filename:
    station = "HALDON" 
elif "Geraldine" in filename:
    station = "GERALDINE" 
elif "Rangitata" in filename:
    station = "RANGITATA" 
elif "Canal" in filename:
    station = "CANAL" 
elif "Clandeboye1" in filename:
    station = "CLANDEBOYE NO. 1" 
elif "Clandeboye2" in filename:
    station = "CLANDEBOYE NO. 2" 

if station == "TIMARU": 
    num_of_feeders = len(df_main_file.columns) + 100
elif station == "TEMUKA":
    num_of_feeders = len(df_main_file.columns) + 20
else:
    num_of_feeders = len(df_main_file.columns) + 2





#Main loop to iterate over all the columns in the data sheet
for i in range(len(df_main_file_num.columns)):    
    yData = df_main_file_num.columns[i]
    xData = df_main_file.columns[0]
    df_filter = df_main_file.filter([xData, yData]) 
    df_filter = df_filter[df_filter[yData] != 0]
    #Getting the index to start searching from 
    num = 0
    for row in df_cap[df_cap.columns[1]]:
        if station in str(row):
            index = num
            break
        num += 1
    
    #Getting the max load for the circuit breaker 
    for u in range(index + 4, index + num_of_feeders + 2): 
        if "MW" in yData or "MVA" in yData:
            limit = 0.111
            break
        elif str(df_cap.iat[u, 1]) in yData and (df_cap.iat[u, 4]) == (df_cap.iat[u, 4]): 
            limit = df_cap.iat[u, 4]
            break
        else:
            limit = 0.111
    if limit == 0.111:
        continue   
    
    #Cleaning the data if required   
    if clean == "yes":
        length = int(len(df_filter[yData]) / 67)
        trial = df_filter
        for n in range(30):
            r = trial[yData].rolling(length)
            m = r.mean().shift(0)
            s = r.std(ddof=0).shift(0)
            z = (trial[yData]-m)/s
            df_filter2 = trial[(np.abs(z) < 3.5)]
        frames = [df_filter[:(length - 2)], df_filter2[(length - 1):]]
        df_filter = pd.concat(frames)
    
    #Convert dictionary to a DataFrame
    loadData = df_filter.to_dict()
    c_load_df = pd.DataFrame(loadData)
    
    
    # Getting Dates for when limit is exceded 
    exc = c_load_df.loc[c_load_df[yData] > limit, 'DateTime']
    exc = exc.dt.strftime('%B %Y')
    exc = exc.drop_duplicates()
    exc = exc.tolist()
    
    #Add a column for the time interval for which the loads were recorded
    c_load_df['interval'] = 1
    
    #Sort the DataFrame by the loads, in descending order of magnitude
    load_df_sorted = c_load_df.sort_values(by=[yData], ascending = False)
    
    #Use the cumsum() function to to add a column with the duration for which the system load is greater than or equal to each load
    load_df_sorted['duration'] = load_df_sorted['interval'].cumsum()
    
    #Calculate the percentage of time for which the system load is greater than or equal to each load
    num_of_data = len(c_load_df[yData])
    if num_of_data == 0:
        continue
    load_df_sorted['percentage'] = load_df_sorted['duration']*(100/num_of_data)
    
# =============================================================================
#     #Plot the load profile
#     p = df_filter.plot(x = xData, y = yData,figsize=(16,7), legend=False)
#     p.axhline(limit, color='r')
#     p.set_title(yData, fontsize = 30)
#     p.set_xlabel("Time (Hrs)", fontsize = 20)
#     p.set_ylabel(yLabel, fontsize = 20)
#     plt.xticks(rotation=90)
#     plt.show()
#     
#     #Plot the load_duration curve (Load vs Percentage of time)
#     p = load_df_sorted.plot(x = "percentage",y = yData,figsize=(16,7), legend=False)
#     p.axhline(limit, xmin=0.00, xmax=0.80, color='r')
#     plt.ylim(0, None)
#     plt.xlim(0, None)
#     p.set_title("{} Load-Duration Curve".format(yData), fontsize = 30)
#     p.set_xlabel("Time (%)", fontsize = 20)
#     p.set_ylabel(yLabel, fontsize = 20)
#     p.xaxis.grid()
#     p.yaxis.grid()
#     plt.show()
# =============================================================================
    
    
            
    ##Getting points of interist 
    Demand = load_df_sorted[yData]
    percent = load_df_sorted['percentage']
    max_p = max(Demand)
    min_p = min(Demand)
    
    #Getting the percentage of intersection 
    if limit < min_p:
        per = 100
    elif limit> max_p:
        per = 0
    else:
        try: 
            load_df_sorted2 = load_df_sorted.round(decimals = 0)
            #load_df_sorted2 = load_df_sorted.apply(np.ceil)
            dic2 = load_df_sorted.to_dict()
            dic = load_df_sorted2.to_dict()  
            per_d = list(dic[yData].keys())[list(dic[yData].values()).index(int(limit))]
            per = dic2["percentage"][per_d]
        except ValueError:
            per = 0
    #Getting the low, mid and high points
    load_df_sorted_new = load_df_sorted.sort_values(by = yData, axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=True, key=None)
    low_p = (len(percent)/100)*low
    low_p = load_df_sorted_new.loc[int(low_p)].at[yData]
    mid_p = (len(percent)/100)*mid
    mid_p = load_df_sorted_new.loc[int(mid_p)].at[yData]
    high_p = (len(percent)/100)*high
    high_p = load_df_sorted_new.loc[int(high_p)].at[yData]
    per = "{:.2f}".format(per)
    


    
    #Getting total number of hours over
    per2 = float(per)/100
    hours_over = per2 * (num_of_data/ir_hour)
    hours_over = "{:.2f}".format(hours_over)

    #Plot the load profile
    p = df_filter.plot(x = xData, y = yData,figsize=(16,7), legend=False)
    p.axhline(limit, color='r')
    p.set_title(yData + " " + date_range, fontsize = 30)
    p.set_xlabel("Time (Hrs)", fontsize = 20)
    p.set_ylabel(yLabel, fontsize = 20)
    plt.xticks(rotation=90)
    plt.savefig(picture_location+'/{} load profile.png'.format(yData), dpi=300, bbox_inches='tight')
    plt.show()
    
    #Plot the load_duration curve (Load vs Percentage of time)
    p = load_df_sorted.plot(x = "percentage",y = yData,figsize=(16,7), legend=False)
    p.axhline(limit, xmin=0.00, color='r')
    p.vlines(per2*100, ymin=0, ymax=limit, color='r') 
    p.vlines(mid, ymin=0, ymax=mid_p, color='#FF5733', linestyle='--')
    p.hlines(mid_p, xmin=0, xmax=mid, color='#FF5733', linestyle='--')
    p.vlines(low, ymin=0, ymax=low_p, color='#C70039', linestyle='--')
    p.hlines(low_p, xmin=0, xmax=low, color='#C70039', linestyle='--')
    p.vlines(high, ymin=0, ymax=high_p, color='#FFC300', linestyle='--')
    p.hlines(high_p, xmin=0, xmax=high, color='#FFC300', linestyle='--')
    plt.ylim(0, None)
    plt.xlim(0, 100)
    p.set_title(("{} Load-Duration Curve " + date_range).format(yData), fontsize = 25)
    p.set_xlabel("Time (%)", fontsize = 20)
    p.set_ylabel(yLabel, fontsize = 20)
    p.xaxis.grid()
    p.yaxis.grid()
    plt.savefig(picture_location+'/{} Load-Duration Curve.png'.format(yData), dpi=300, bbox_inches='tight')
    plt.show()
    
    if export == "1":
        export_data.append(([yData] + load_df_sorted[yData].tolist()))  #########################################################################################
        export_df = pd.DataFrame(export_data)
    
    #Printing the outcome
    low_p = "{:.2f}".format(low_p)
    mid_p = "{:.2f}".format(mid_p)
    min_p = "{:.2f}".format(min_p)
    high_p = "{:.2f}".format(high_p)
    max_p = "{:.2f}".format(max_p)
    limit = "{:.2f}".format(limit)
    printing.append([yData, limit, per, hours_over, low_p, mid_p, high_p, max_p, min_p, exc])
    
if export == "1":
    export_df = export_df.T
    export_df.to_csv(filename4, index = False)


headers = ["Feeder", "Limit", "Percentage Over Limit (%)", "Time Over Limit (hrs)", "low", "mid", "high", "Max", "Min", "Dates Over Limit"]
table = pd.DataFrame(printing, columns = headers)
table["Magnitude over limit"] = table["Max"].astype(float) - table["Limit"].astype(float)
table['Magnitude over limit'] = np.where(table['Magnitude over limit'] < 0, 0, table['Magnitude over limit'])
table.to_excel(filename3, index = False)
print('                                         ')
print(table.iloc[:, [0,1,2,3,4,5,6,7,8,10]])
print('                                         ')
print('-----------------------------------------')
    

end = time.time()
time = "{:.2f}".format(end-start)
print("Time Taken:", time , "s")