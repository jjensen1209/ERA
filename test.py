import numpy as np
import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt

# subject file
#generic = "subject2_031023_1700.acq"
generic = "subject_l_041423.acq"
# read data from acq graph files
data_rest, rest_samp_rate = nk.read_acqknowledge("rest_"+generic)
data_read, read_samp_rate = nk.read_acqknowledge("read_"+generic)
data_video, video_samp_rate = nk.read_acqknowledge("video_"+generic)
data_game, game_samp_rate = nk.read_acqknowledge("game_"+generic)

eeg_list = [ # organized by horizontal row, front to back
    "Fp1","Fp2",
    "F7 ","F8 ","F3 ","Fz ","F4 ",
    "T3 ",
    #"C3 ", # issues with C3 grabbing multiple things, i think
    "Cz ","C4 ","T4 ",
    "T5 ","P3 ","Pz ","P4 ","T6 ",
    "O1 ","POz","O2 "
]

if False:
    # listing the channels we got from the set
    for a in data_rest.columns:
        print(a)
        print("\""+a[:3]+"\",")
    # seeing if i got the names properly
    #for a in eeg_list:
    #    print("is "+a+" found?\t", a in dlist)
    #print(eeg_list == dlist)

dlist = [a for a in data_rest.columns if a[:3] in eeg_list]

if False:
    print("dlist")
    for a in dlist:
        print(a)

# plotting the signals, independently (makes a lot of figures)
if False:
    for a in dlist:
        nk.signal_plot(data_rest[a])
    plt.show()

if False:
    import math
    # Using Numpy to create an array X
    X = np.arange(0, math.pi*2, 0.05)
  
    # Assign variables to the y axis part of the curve
    y = np.sin(X)
    z = np.cos(X)
  
    # Plotting both the curves simultaneously
    plt.plot(X, y, color='r', label='sin')
    plt.plot(X, z, color='g', label='cos')
  
    # Naming the x-axis, y-axis and the whole graph
    #plt.xlabel("Angle")
    #plt.ylabel("Magnitude")
    #plt.title("Sine and Cosine functions")
  
    # Adding legend, which helps us recognize the curve according to it's color
    #plt.legend()
  
    # To load the display window
    plt.show()


count = 0

#plt.figure(figsize=(8,6))
loglog_x = 0

for a in dlist:
    print("trying to process", a)
    orig = data_rest[a]

    #orig_powerline = nk.signal_filter(orig, rest_samp_rate, method='powerline', powerline=60)

    #b = nk.signal_smooth(orig, size=100)

    if(False):
        plt.plot(original)
        #plt.show()
        plt.plot(orig_powerline)
        #plt.show()
        plt.plot(b)
        #plt.ylim(-1000,1000)    
        #plt.show()

    thing = nk.signal_psd(orig, sampling_rate=rest_samp_rate, show=True, max_frequency=100)#, method="fft")

    #thing = nk.signal_filter(orig_psd, sampling_rate=rest_samp_rate, method='powerline', powerline=60)

    # keeping the largest x axis
    if type(loglog_x) != "Series":
        loglog_x = thing["Frequency"]
    elif len(loglog_x) != (thing["Frequency"]):
        old_len = len(loglog_x)
        new_len = len(thing["Frequency"])
        loglog_x = max(len(loglog_x), len(thing["Frequency"]))
        print("old length: ", old_len, "new length: ", new_len, 
              " keeping: ", len(loglog_x))

    plotme = nk.signal_filter(thing["Power"], rest_samp_rate, method='powerline', powerline=60)

    #plt.plot(loglog_x, thing["Power"])#, c="blue")
    plt.loglog( #loglog_x,
                thing["Frequency"], 
                plotme,
                #thing["Power"], 
                label=a[:3])#, c="blue")
    #count += 1
    #if count == 2:

#plt.grid(True)
    plt.show()
print("we are out")

# just a simple list
# eeg stuff
"Fp1","Fp2",
"F7 ","F8 ","F3 ","Fz ","F4 ",
"T3 ","C3 ","Cz ","C4 ","T4 ",
"T5 ","P3 ","Pz ","P4 ","T6 ",
"POz",
"O1 ","O2 ",
# ??
"ECG","Mov","Til","Til","Til",
"Lea","Lea",
# ecg stuff
"V1 ","V2 ","V3 ","V4 ","V5 ","V6 ",
# ??
"EMG","C0 ","C1 ","C2 ","C3 ",