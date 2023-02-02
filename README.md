
# Load Duration Curve Tool

The load duration curve is a vital tool that plays a significant role in the analysis and planning of electric utility operations. It is a graphical representation of the frequency of the electricity load (or demand) over a specific period of time, typically a year. The curve provides a clear picture of the pattern of electricity usage and is used to determine the peak demand times, average energy consumption, and energy requirements during off-peak hours. This information is crucial in ensuring efficient operation of the power system and in making informed decisions about future power infrastructure investments. The load duration curve is widely used by electric utilities for resource planning, system design, and capacity expansion planning, among other things.

This tool provides the ability to generate both load duration curves and load profile for a given load. You are required to input three files and a folder location (load data, regional capacity and output sheet). 



## FAQ

#### What files do i need?


the following (in order of request) are the data files you will need to run the code:
- An CSV file with the data extracted from SCADA
- An excel file with the Regional Capacity Capability
- An excel file where the output can be exported (original content will be deleted)
you will aslo need to specify a folder/filepath where the output images can be saved.

#### What do i input for itterations?

the itterations variable refers to the itterations per hour, a variable of 12 would mean that there are 12 itterations within a 60 minute period. 12 itterations relates to a dataset of 5 minute data
## Installation

Required Modules
-  [pandas](http://pandas.pydata.org/)
-  [numpy](http://numpy.org)
-  [matpotlib](http://matplotlib.org/)
-  [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)
-  [time](https://docs.python.org/3/library/time.html)
-  [datetime](https://docs.python.org/3/library/datetime.html)

## Application User Interface

![App Screenshot](Testing/UI.PNG)

## Acknowledgements

 - [Plotting a Load-Duration Curve with Python](https://blog.finxter.com/plotting-a-load-duration-curve-with-python/)
