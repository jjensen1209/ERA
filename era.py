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
# grab full name of V1 column (should be the same across all files)
V1_name = [a for a in data_rest.columns if a[:2] == "V1"][0]
# smooth the signal
smoothed_rest = nk.signal_smooth(data_rest[V1_name], size=150)
smoothed_read = nk.signal_smooth(data_read[V1_name], size=150)
smoothed_video = nk.signal_smooth(data_video[V1_name], size=150)
smoothed_game = nk.signal_smooth(data_game[V1_name], size=150)
# basic ecg processing ( remember squeeze() is necessary to get it into 1-dimension )
signal_rest, info_rest = nk.ecg_process(smoothed_rest.squeeze(), sampling_rate=rest_samp_rate)
signal_read, info_read = nk.ecg_process(smoothed_read.squeeze(), sampling_rate=read_samp_rate)
signal_video, info_video = nk.ecg_process(smoothed_video.squeeze(), sampling_rate=video_samp_rate)
signal_game, info_game = nk.ecg_process(smoothed_game.squeeze(), sampling_rate=game_samp_rate)
# plot the signals separately, can't customize the titles on these
# figure 1: rest
plot_ecg_rest = nk.ecg_plot(signal_rest, rpeaks=info_rest["ECG_R_Peaks"], sampling_rate=rest_samp_rate)
# figure 2: reading notes
plot_ecg_read = nk.ecg_plot(signal_read, rpeaks=info_read["ECG_R_Peaks"], sampling_rate=read_samp_rate)
# figure 3: watching video
plot_ecg_video = nk.ecg_plot(signal_video, rpeaks=info_video["ECG_R_Peaks"], sampling_rate=video_samp_rate)
# figure 4: playing game (fruit ninja, ideally)
plot_ecg_game = nk.ecg_plot(signal_game, rpeaks=info_game["ECG_R_Peaks"], sampling_rate=game_samp_rate)
# last figure: plot heart rate together
data_fig_rate = pd.DataFrame({  "rest_rate": signal_rest["ECG_Rate"],   "read_rate": signal_read["ECG_Rate"],
                                "video_rate": signal_video["ECG_Rate"], "game_rate": signal_game["ECG_Rate"]})
nk.signal_plot(data_fig_rate, labels=["rest", "read", "video", "game"], standardize=False)
plt.show()



Fp1_name = [a for a in data_rest.columns if a[:3] == "Fp1"][0]

print(Fp1_name)

nk.signal_plot(data_rest[Fp1_name])
plt.show()

psd_fp1_rest = nk.signal_psd(data_rest[Fp1_name], sampling_rate=rest_samp_rate, 
                             show=True, max_frequency=100)#, method="fft")
plt.loglog(psd_fp1_rest["Frequency"], psd_fp1_rest["Power"], c="blue")
plt.show()


# not using EMG data for now
#cheek_name = [a for a in data_rest.columns if a[:4] == "EMG"]
#print(cheek_name)
#print([a for a in data_rest.columns])
#for a in data_rest.columns:
#    print(a)
