

import sys
import csv

# TODO
# compile PV analysis, or strip it back and just use it here
sys.path.append(r'D:\Dropbox\CommonCode\analysis\src')
# sys.path.append(r'/home/shanoot/Dropbox/CommonCode/analysis/src')

import PV_analysis.lifetime.QSSPC.IO as IO


def load(fname):
    return IO.load_lifetime_sinton(fname)


def save(fname, samples):
    '''
    Saves a csv file with the name fname,
    and the data in data
    '''
    # test to see if can open the file
    try:
        with open(fname, 'w', newline='') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(
                f,
                fieldnames=list(samples.values())[0].keys())
            w.writeheader()

            for sample in samples.keys():
                w.writerow(samples[sample])

    except IOError:
        print("Could not open output file {0}! Please check if it open and close!".format(
            fname))
