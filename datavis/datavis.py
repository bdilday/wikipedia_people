
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

class wikipedia_people_datavis():

    def __init__(self, ifile='../data/all.csv', load=True):
        self.ifile = ifile
        self.running_bin_stride = 10
        self.running_bin_percentile = 99
        self.dt = [('length', 'i4'),
                    ('linkshere', 'i4'),
                    ('pagelinkshere', 'i4'),
                    ('year_birth', 'i4'),
                    ('year_demise', 'i4'),
                    ('name', 'S256')]
        if load:
            self.load()

    def load(self):
        self.data = np.genfromtxt(self.ifile, dtype=self.dt, delimiter=',', skip_header=1)
        self.df = pd.DataFrame(self.data)
        self.yrs = np.unique(self.data['year_birth'])

    def binned_percentiles(self, p=None, stride=None):
        p = p if p is not None else self.running_bin_percentile
        stride = stride if stride is not None else self.running_bin_stride

        yy = []
        for yr in self.yrs:
            cc = np.logical_and(self.data['year_birth']>=yr,
                                self.data['year_birth']<yr+stride)
            tmp = self.data[cc]['pagelinkshere']

            yy.append(np.percentile(tmp, p))
        plt.plot(self.yrs, yy)

    def max_by_year(self):

        yy = []
        for yr in self.yrs:
            cc = np.logical_and(self.data['year_birth']==yr,
                                True)
            tmp = self.data[cc]['pagelinkshere']

            yy.append(max(tmp))
        plt.plot(self.yrs, yy)

if __name__=='__main__':
    pass
