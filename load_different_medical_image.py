import nibabel as nib
import numpy as np

def _load_medical_volume(filename, ext, verbose=False):
    """
    load a medical volume from one of a number of file types
    """
    with timer.Timer('load_vol', verbose >= 2):
        if ext == '.npz':
            vol_file = np.load(filename)
            vol_data = vol_file['vol_data']
        elif ext == 'npy':
            vol_data = np.load(filename)
        elif ext == '.mgz' or ext == '.nii' or ext == '.nii.gz':
            vol_med = nib.load(filename)
            vol_data = vol_med.get_data()
        else:
            raise ValueError("Unexpected extension %s" % ext)

    return vol_data
