import numpy as np
import xarray as xr
from glob import glob

def data_adjust(data):
    
    data = data.transpose()

    return data

def create_sequences(data, input, output):

    data = np.expand_dims(data, axis=-1)

    w, h = data.shape[1:3]

    M = len(data)

    X = np.zeros((M-(input+output), w, h, input))
    y = np.zeros((M-(input+output), w, h, output))

    finish = 0

    i = 0
    while finish<M-input-output:

        X[i, :, :, :] = np.swapaxes(data[i:input+i, :, :, :], 0, 3)
        y[i, :, :, :] = np.swapaxes(data[input+i:input+i+output, :, :, :], 0, 3)
        
        i += 1
        finish += 1

    return X, y

def get_sequences(data_path, input=12, output=8):

    day_list = sorted(glob(data_path))

    # First day
    day = day_list[0]
    files = sorted(glob(f'{day}/*.nc4'))

    nc_files = [xr.open_dataset(nc) for nc in files]

    data = np.array([data_adjust(nc.precipitationCal.values[0]) for nc in nc_files])

    X, y = create_sequences(data, input=input, output=output)

    # Rest of days
    for day in day_list[1:]:
        
        files = sorted(glob(f'{day}/*.nc4'))
        nc_files = [xr.open_dataset(nc) for nc in files]
        data = np.array([data_adjust(nc.precipitationCal.values[0]) for nc in nc_files])
        Xtemp, ytemp = create_sequences(data, input=input, output=output)

        X = np.concatenate((X, Xtemp), axis=0)
        y = np.concatenate((y, ytemp), axis=0)

    return X, y