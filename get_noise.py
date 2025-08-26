from cryosparc.tools import Dataset
import pandas as pd
#import matplotlib.pyplot as plt
import plotext as plt


# Load the .cs file
ds = Dataset.load("../CS-cryosparc-tutorial/J9/J9_020_particles.cs")

# Convert to DataFrame manually
df = pd.DataFrame(ds.rows())

print(df.head())
print(df.columns[:20])  # show some column names


plt.hist(df["alignments2D/cross_cor"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
plt.title("Distribution of per-particle alignment scores")
plt.show()


plt.hist(df["alignments2D/error"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
plt.title("Distribution of per-particle alignment scores")
plt.show()

plt.hist(df["alignments2D/ncc_score"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
plt.title("Distribution of per-particle alignment scores")
plt.show()

plt.hist(df["alignments2D/fit_quality"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
plt.title("Distribution of per-particle alignment scores")
plt.show()