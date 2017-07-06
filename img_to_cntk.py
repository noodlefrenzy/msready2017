
# Convert images into CNTK map files for training and testing

import os
import numpy as np
import pandas as pd

# pip install Pillow - we use this to filter to only valid images since some might be corrupted
from PIL import Image

# Install opencv 3 from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
# pip install <the appropriate wheel file>
# Since CNTK uses OpenCV under the covers and has _terrible_ error reporting, 
#  we need to filter out bad images in a pre-filtering step.
import cv2

# Could use Pandas sampling, but want to do a stratified split
# Pandas doesn't easily support this.
from sklearn.model_selection import train_test_split

def is_img(x):
    try:
        Image.open(x)
        cv_img = cv2.imread(x)
        if cv_img is None:
            print('Image {} is not openable by OpenCV'.format(x))
            return False
        return True
    except:
        print('Failed to open {}'.format(x))
        return False

images = pd.read_csv('./images/images.tsv', sep='\t')
valid_images = images[images.Path.apply(lambda x: os.path.isfile(x) and is_img(x))]
# Convert "hot dog" to 1, anything else to 0
labels = np.array(valid_images['Label'] == 'hot dog', dtype=np.int)

# Split the data into 70/30 for training and testing.
# Use stratification to make sure that the "hot dog" class has roughly the
#  same ratio of samples in the training and the test sets.
X_train, X_test, y_train, y_test = train_test_split(labels, valid_images['Path'], 
                                                    test_size=0.3, random_state=1337, stratify=labels)

# Output the results to the tab-delimited format expected by CNTK
train_df = pd.DataFrame(np.array([y_train, X_train]).T, columns=['path', 'label'])
train_df.to_csv('./images/train.tsv', sep='\t', header=False, index=False)
test_df = pd.DataFrame(np.array([y_test, X_test]).T, columns=['path', 'label'])
test_df.to_csv('./images/test.tsv', sep='\t', header=False, index=False)
