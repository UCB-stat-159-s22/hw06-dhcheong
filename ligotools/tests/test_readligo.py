from ligotools import loaddata, dq_channel_to_seglist, read_hdf5, FileList
import numpy as np

def test_loaddata():
	strain_H1, time_H1, chan_dict_H1 = loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
	assert (len(strain_H1) == 131072) & (len(time_H1) == 131072) & (len(chan_dict_H1) == 13)

def test_dq_channel_to_seglist():
	c = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assert np.array_equal(dq_channel_to_seglist(c),[slice(0, 131072, None)])

def test_read_hdf5():
	assert read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)[1] == 1126259446

def test_FileList_searchdir():
	hdf5_files = FileList().searchdir('ligotools/')
	assert np.array_equal(hdf5_files, [])




