#keep input files same and increase the workers 
# 0.946364,0.09723,0.752384,0.995733,0.922075,0.665446,0.926835,0.716374,0.725476,0.765133
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plotdata = pd.DataFrame({

    "time":[0.628911,0.751396,0.652037,0.711983,0.668413,0.756237,0.798838,0.833765,0.909753,0.827005]},

    )

plotdata.plot(kind="line",figsize=(15, 8),color=["#808080","#0000FF"])


plt.xlabel("Number of files")

plt.ylabel("time")
plt.show()