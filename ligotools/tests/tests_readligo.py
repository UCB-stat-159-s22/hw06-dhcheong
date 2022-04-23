from ligotools import readligo as rl
import h5py

def test_dimension_H1():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	assert (len(strain_H1) == 131072) & (len(time_H1) == 131072) & (len(chan_dict_H1) == 13)

def test_dimension_L1():
	strain_L1, time_L1, chan_dict_L1 = rl.loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')
	assert (len(strain_L1) == 131072) & (len(time_L1) == 131072) & (len(chan_dict_L1) == 13)

def test_F_template():
	f_template = h5py.File('data/GW150914_4_template.hdf5', "r")
	assert (f_template is not None)

def test_read_hdf5():
	assert rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)[2] == 0.000244140625