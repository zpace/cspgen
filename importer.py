import os, sys, matplotlib

# add manga RC location to path, and import config
if os.environ['MANGA_CONFIG_LOC'] not in sys.path:
    sys.path.append(os.environ['MANGA_CONFIG_LOC'])

import mangarc

if mangarc.tools_loc not in sys.path:
    sys.path.append(mangarc.tools_loc)

fsps_loc = '/usr/data/minhas/zpace/.fsps/python-fsps'
if fsps_loc not in sys.path:
    sys.path.append(fsps_loc)

pcalib_loc = '/usr/data/minhas/zpace/stellarmass_pca'
if pcalib_loc not in sys.path:
    sys.path.append(pcalib_loc)

basedir = '/usr/data/minhas2/zpace/CSPs/CSPs_CKC14_MaNGA_20190215-1/'

matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['text.usetex'] = True
