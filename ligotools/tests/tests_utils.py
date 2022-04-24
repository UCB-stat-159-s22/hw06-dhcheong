import ligotools.readligo as rl
import ligotools.utils as u 

strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')

# both H1 and L1 will have the same time vector, so:
time = time_H1
# the time sample interval (uniformly sampled!)
dt = time[1] - time[0]

tevent = 1126259462.44
fs = 4096

def test_whiten():
	strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
	assert len(starin_H1_whiten) == 131072

def test_write_wavefile():

    strain_H1_whiten = u.whiten(strain_H1,psd_H1,dt)
    
    
    # We need to suppress the high frequency noise (no signal!) with some bandpassing:
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
    strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization
    strain_L1_whitenbp = filtfilt(bb, ab, strain_L1_whiten) / normalization
	deltat_sound = 2.                     
	indxd = np.where((time >= tevent-deltat_sound) & (time < tevent+deltat_sound))
	u.write_wavfile("audio/"+eventname+"_H1_whitenbp.wav",int(fs), strain_H1_whitenbp[indxd])

def test_reqshift():
	assert
  
def test_plot_changes():
	assert