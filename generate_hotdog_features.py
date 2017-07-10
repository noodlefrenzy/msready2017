import numpy as np
import pandas as pd

def gen_hotdogs(n_hotdogs):
    hd = pd.DataFrame(columns=['label', 'length', 'width', 'is_cylinder', 'meatiness'])
    hd['label'] = [1.] * n_hotdogs
    hd['length'] = np.random.rand(n_hotdogs) * 4. + 4. # Between 4 & 8
    hd['width'] = np.random.rand(n_hotdogs) * 0.4 + 0.6 # Between .6 & 1
    hd['is_cylinder'] = np.random.rand(n_hotdogs) > 0.15 # High chance of cylindrical shape
    hd['meatiness'] = np.random.rand(n_hotdogs) * 0.3 + 0.7 # Between .7 and 1
    return hd

def gen_not_hotdogs(n_not_hotdogs):
    nhd = pd.DataFrame(columns=['label', 'length', 'width', 'is_cylinder', 'meatiness'])
    nhd['label'] = [0.] * n_not_hotdogs
    nhd['length'] = np.random.rand(n_not_hotdogs) * 10. + 0.2 # Between .2 & 10.2
    nhd['width'] = np.random.rand(n_not_hotdogs) * 10. + 0.2 # Between .2 & 10.2
    nhd['is_cylinder'] = np.random.rand(n_not_hotdogs) > 0.65 # Low chance of cylindrical shape
    nhd['meatiness'] = np.random.rand(n_not_hotdogs) # Between 0 and 1
    return nhd

def gen_records(n_records):
    n_hotdogs = np.random.randint(0, 2, size=n_records).sum()
    return pd.concat([gen_hotdogs(n_hotdogs), gen_not_hotdogs(n_records - n_hotdogs)])

if __name__ == '__main__':
    np.random.seed(1337)
    gen_records(5000).to_csv('./hotdog_features.csv', index=False)
