import numpy as np

rng = np.random.default_rng()

waves = rng.random(100) * 1.7 * 1216 + 2.8*1216

with open("wavelength.dat", 'w') as outfile:
    outfile.write("# ID\tWavelength\n")
    for i,w in enumerate(waves):
        outfile.write(f'{i+1}\t{w:.4f}\n')