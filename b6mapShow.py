import sys, collections, os
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

query = sys.argv[1]

line_dict = {}
line_list = []
i = 0
with open(query) as f:
    for line in f:
        if int(line.split()[8]) < int(line.split()[9]):
            start = int(line.split()[8])
            end = int(line.split()[9])
            line_list.extend(list(range(start, end)))
            i += 1
        else:
            start = int(line.split()[9])
            end = int(line.split()[8])
            line_list.extend(list(range(start, end)))
            i += 1

print(i, " sequences were loaded.")

count_dict = collections.Counter(line_list)
position = np.array(list(dict(count_dict).keys()))
reads = np.array(list(dict(count_dict).values()))
plt.bar(position, reads, width=1.0)
plt.ylabel("depth (reads)")
plt.xlabel(query)
plt.show()
# query = query + ".png"
# plt.savefig(query)
