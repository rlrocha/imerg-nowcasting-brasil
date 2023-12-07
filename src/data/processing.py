import numpy as np

class Scaler():

    def __init__(self, scaler='standard', range=(0,1)):
        
        if not scaler.lower() in ['minmax', 'standard']:
            raise ValueError('Incorrect scaler. Please choose between minmax and standard.')
        
        self.scaler = scaler.lower()
        self.min = range[0]
        self.max = range[1]

    def fit(self, X):
        
        if self.scaler == 'minmax':
            self.data_min = np.nanmin(X)
            self.data_max = np.nanmax(X)

        else:
            self.data_mean = np.nanmean(X)
            self.data_std = np.nanstd(X)
        
        return self

    def transform(self, X):

        X = X.copy()
        
        if self.scaler == 'minmax':
            X = (X-self.data_min)/(self.data_max - self.data_min)*(self.max-self.min) + self.min

        else:
            X = (X-self.data_mean)/self.data_std

        return X
    
    def inverse_transform(self, X):
        
        X = X.copy()
        
        if self.scaler == 'minmax':
            X = ((X-self.min)*(self.data_max-self.data_min)/(self.max-self.min)) + self.data_min

        else:
            X = X*self.data_std + self.data_mean
        
        return X