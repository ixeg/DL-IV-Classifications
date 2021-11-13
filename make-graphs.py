import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

df = pd.read_csv('temp.csv')

print(df.columns[4])
df.plot(x="Gate",y="Current")

#"Image ecause of that, images in the training and test sets are resized
# to 120 × 120 pixels while preserving their aspect ratio. 
# We determined this size value based on trial and error tests. 
# Images with sizes larger than 120 × 120 pixels did not 
# increase test accuracy and caused much longer training times 
# since the input size was increased. 
# Smaller sizes than that also reduced classification accuracies. - Multi-label
#  cassifcation of line chart images using CNN
plt.savefig('graph.png', figsize=(1,1),dpi=50 ,metadata={'Title': 'VgId'})