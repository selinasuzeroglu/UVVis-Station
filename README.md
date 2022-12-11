# **UVVis-Station**

Python script that automates the execution and analysis of UVVis spectroscopy.


The final code is located in the 'Main' folder in the 'Position' file. In this file the positioning of the Zaber devices is determined and functions for the communication with the MicroSwitch, the InProcess system as well as SQL are used, which can be found in the respective other files. 

The respective codes for the Arduino boards can be found in the 'Arduino_code' folder. For the Microswitch Trigger, file 'Microswitch Control' was used. To trigger the measurements in InProcess, another Arduino board is controlled via Python with the Microswitch. Relays are connected to the second Arduino board and depending on the type of the relays "low level/high level trigger", we upload the corresponding InProcess input trigger to this Arduino board. To extract the results from SQL after the measurement, a signal is sent from the InProcess device to a third Arduino board. For this third board the code 'InProcess Output Trigger is used'.
