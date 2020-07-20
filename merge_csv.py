import os
import pandas as pd

extension = ".csv"
dflist=[]

for dffile in [f for f in os.listdir("./") if f.endswith(extension) and f.startswith('test_chunk')]:
	dflist.append(pd.read_csv(dffile))

dataframe = pd.concat(dflist,ignore_index=True)
dataframe.to_csv(os.path.join(output_dir,"train"+extension),index=False)
