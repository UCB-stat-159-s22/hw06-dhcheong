import ligotools.readligo as rl
import ligotools.utils as u 
import numpy as np
from os.path import exists
from os import remove
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt

def test_whiten():
	fs = 4096
	NFFT = 4*fs
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
	psd_H1 = interp1d(freqs, Pxx_H1)
	time = time_H1
	dt = time[1] - time[0]
	strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
	assert (starin_H1_whiten is not None)


def test_write_wavfile():
	write_wavfile("audio/temp.wav", 4096, np.linspace(0,10,16000))
	assert exists("audio/temp.wav")
	remove("audio/temp.wav")

def test_reqshift():
	fs = 4096
	NFFT = 4*fs
	fband = [43.0, 300.0]
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
	psd_H1 = interp1d(freqs, Pxx_H1)
	time = time_H1
	dt = time[1] - time[0]
	strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
	bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
	normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
	strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
	strain_H1_shifted = u.reqshift(strain_H1_whitenbp,fshift=fshift,sample_rate=fs)
	assert (starin_H1_shifted is not None)

def test_plot_whitened():
	fs = 4096
	NFFT = 4*fs
	fband = [43.0, 300.0]
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
	psd_H1 = interp1d(freqs, Pxx_H1)
	time = time_H1
	dt = time[1] - time[0]
	strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
	bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
	normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
	strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
	timemax = time[6]
	u.plot_whitened(time = time, tevent = 1126259462.44, strain_H1_whitenbp, 'g', dets = 'H1',
					timemax = timemax, template_match = strain_H1_whitenbp, eventname = 'GW150914', plottype = "png")
	assert exists('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")
	remove('figures/'+'GW150914'+"_"+"H1"+"_matchtime."+"png")