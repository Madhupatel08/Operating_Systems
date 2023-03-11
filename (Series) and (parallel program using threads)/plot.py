#keep input files same and increase the workers 
# 0.946364,0.09723,0.752384,0.995733,0.922075,0.665446,0.926835,0.716374,0.725476,0.765133
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plotdata = pd.DataFrame({

    "time":[0.946364,0.09723,0.752384,0.995733,0.922075,0.665446,0.926835,0.716374,0.725476,0.765133]},

    )

plotdata.plot(kind="line",figsize=(15, 8),color=["#808080","#0000FF"])


plt.xlabel("Number of workers")

plt.ylabel("time")
plt.show()