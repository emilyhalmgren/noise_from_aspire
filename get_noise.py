from cryosparc.tools import Dataset
import pandas as pd
#import matplotlib.pyplot as plt
import plotext as plt
import numpy as np


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

plt.subplots(2, 2)

plt.subplot(1)
plt.hist(df["alignments2D/cross_cor"], bins=50)
plt.xlabel("2D alignment cross-correlation")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")

plt.subplot(2)
plt.hist(df["alignments2D/class_posterior"], bins=50)
plt.xlabel("Probability of assignment to the chosen class")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")

plt.subplot(3)
plt.hist(df["alignments2D/weight"], bins=50)
plt.xlabel("Weight given by cryoSPARC")
plt.ylabel("Number of particles")
#plt.title("Distribution of per-particle alignment scores")

# Model-vs-residual SNR
snr_slice = df["alignments2D/slice_pow"] / df["alignments2D/resid_pow"]
snr_slice = np.clip(snr_slice, 0, None)
plt.subplot(4)
plt.hist(snr_slice, bins=80)
plt.xlabel("Per-particle SNR (slice/residual)"); plt.ylabel("Count"); plt.title("SNR_slice")
plt.show()

