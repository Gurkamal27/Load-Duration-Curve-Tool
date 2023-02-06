
<img src="Source/Logo.jpg"  width="225" height="112.5">


# Load Duration Curve Tool

The load duration curve is a vital tool that plays a significant role in the analysis and planning of electric utility operations. It is a graphical representation of the frequency of the electricity load (or demand) over a specific period of time, typically a year. The curve provides a clear picture of the pattern of electricity usage and is used to determine the peak demand times, average energy consumption, and energy requirements during off-peak hours. This information is crucial in ensuring efficient operation of the power system and in making informed decisions about future power infrastructure investments. The load duration curve is widely used by electric utilities for resource planning, system design, and capacity expansion planning, among other things.

## Functionality 

This tool provides the ability to generate both load duration curves and load profile for a given load. You are required to input three files and a folder location (load data, regional capacity and output sheet). 

The load duration curve helps determine seasonal patterns of electricity demand, enabling the best time for maintenance or installations. It can be adjusted by season, year, and month, providing a comprehensive understanding of demand patterns. 

The "clean data" function requires further development to meet the manual cleaning standards. However, the automatic correction of zero values is currently in place. By improving the accuracy and efficiency of the "clean data" function, the quality and reliability of the data used for analysis and decision making will be ensured.

The user has the option to input low, middle, and high demand test points, providing flexibility in analyzing electricity demand patterns. This allows for a more detailed understanding of the electricity usage and provides a more accurate representation of the demand.

## Output (example)

The output file that is gernerated is in the following format, with 11 coloumns and as many rows as loads in the dataset.

|     Feeder     |  Limit | Percentage Over   Limit (%) | Time Over Limit   (hrs) |  low  |  mid  |  high |   Max  |  Min  |                                     Dates Over Limit                                    | Magnitude over   limit |
|:--------------:|:------:|:---------------------------:|:-----------------------:|:-----:|:-----:|:-----:|:------:|:-----:|:---------------------------------------------------------------------------------------:|:----------------------:|
| GRM_CB9_A_Amps | 115.00 | 0.57                        | 59.39                   | 64.27 | 61.80 | 59.69 | 131.62 | 34.84 | ['August 2019', 'September 2019', 'March 2020'] | 16.62                  |

The first image saved is the Load Profile, a graphical representation of load usage over a period of time. It shows consumption trends and patterns, with a limit indicated to determine if the load exceeds the limit.

<img src="Source/example_load_profile.png"  width="800" height="385">

The second image is the Load Duration Curve, which displays the limit, the percentage at which the limit is exceeded (if exceeded), and the testpoint percentages (if selected).

<img src="Source/example_load-duration_curve.png"  width="800" height="385">

## FAQ

#### What files do i need?

the following (in order of request) are the data files you will need to run the code:
- An CSV file with the data extracted from SCADA
- An excel file with the Regional Capacity Capability
- An excel file where the output can be exported (original content will be deleted)
Additionally, you will need to specify a folder/file path to save the output images.

#### What do i input for itterations?

The "iterations" variable represents the sampling rate, where a value of 12 means the data is sampled 12 times per hour, yielding 5-minute data intervals. The sampling rate affects data accuracy, with a higher rate leading to more detailed analysis of electricity demand patterns. The ability to adjust the sampling rate provides flexibility in data collection and analysis.

## Installation

Required Modules, most of which should already be installed in the standard installtion of python
-  [pandas](http://pandas.pydata.org/) (used for its dataframe object) 
-  [numpy](http://numpy.org) (general mathematical functions)
-  [matpotlib](http://matplotlib.org/) (used to plot the end result) 
-  [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) (used to create pop out windows for user inputs)
-  [time](https://docs.python.org/3/library/time.html) (used to record the time taken for the program to run)
-  [datetime](https://docs.python.org/3/library/datetime.html) (used to interpret and minipulate the dataset)

## Application User Interface

Upon launching the application, you'll be presented with a user-friendly interface. The tool is set up so that no input is required and the default sampling is set to 5-minute data. Percentage testpoints and data manipulation are not necessary to run the program. Data manipulation is only enabled if a specific option is selected, such as "Summer in 2021" or "January in 2019." However, it's important to note that the chosen dates must be present in the data file, or errors may occur.

![App Screenshot](Source/UI.PNG)

After entering the initial parameters, you'll be presented with several pop-up windows requesting file/folder selections. The red indicator shows where the pop-up will indicate what needs to be selected, in this case, it will indicate a .csv data file.

<img src="Source/interface.PNG"  width="800" height="385">

## Acknowledgements

 - [Plotting a Load-Duration Curve with Python](https://blog.finxter.com/plotting-a-load-duration-curve-with-python/)
