from cryosparc.tools import Dataset
import pandas as pd
#import matplotlib.pyplot as plt
import plotext as plt


# Load the .cs file
ds = Dataset.load("../CS-cryosparc-tutorial/J9/J9_020_particles.cs")

# Convert to DataFrame manually
df = pd.DataFrame(ds.rows())

print(df.head())
print(df.columns)  # show some column names

cross_corr = df["alignments2D/cross_cor"]
print(cross_corr[:10])

error = df["alignments2D/error"]
print(error[:10])

ncc_score = df["pick_stats/ncc_score"]
print(ncc_score[:10])   

fit_quality = df["ctf/fit_quality"]
print(fit_quality[:10])

plt.hist(df["alignments2D/cross_cor"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")
plt.show()


plt.hist(df["alignments2D/error"], bins=50)
plt.xlabel("Error")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")
plt.show()

plt.hist(df["pick_stats/ncc_score"], bins=50)
plt.xlabel("NCC Score")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")
plt.show()

plt.hist(df["ctf/fit_quality"], bins=50)
plt.xlabel("Fit Quality")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")
plt.show() 