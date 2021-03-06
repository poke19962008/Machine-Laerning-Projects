from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

features = {
    'loudness': 1,
    'brightness': 2,
    'flatness': 3,
    'attack': 4,
    'b1': 5,
    'b2': 6,
    'b3': 7,
    'b4': 8,
    'b5': 9,
    'b6': 10,
    'b7': 11,
    'b8': 12,
}

def meanPlotter(ftr):
    with open('bin/trainMean.bin', 'r') as f:
        mean = np.load(f)
        plt.plot(mean[:,0], mean[:,features[ftr]], 'o', label="mean"+ftr)
        plt.xlabel('Year')
        plt.ylabel('Mean of average '+ftr)
        plt.title('Mean '+ftr)

def allFourMeanPlotter():
    meanPlotter('loudness')
    meanPlotter('brightness')
    meanPlotter('flatness')
    meanPlotter('attack')

def allBPlotter():
    ftrs = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8']

    for ftr in ftrs:
        plt.subplot(4, 2, ftrs.index(ftr)+1)
        meanPlotter(ftr)

def threeDFeaturePlot():
    with open('bin/trainMean.bin', 'r') as f:
        mean = np.load(f)
        with open('loudBrightFlat.txt', 'a') as f:
            for i in xrange(len(mean)):
                row = mean[i][1:4]
                row = ' '.join(str(x) for x in row)
                row += " "+str(i)+"\n"
                f.write(row)
        print "[SUCCESS] Saved to loudBrightFlat.txt "
        print "splot (\"loudBrightFlat.txt\") with points palette"

def clusterMapp():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    with open('bin/train.bin', 'r') as f:
        data = np.load(f)
        years = np.unique(data[:15,0])

        colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
        axis = ['brightness', 'flatness', 'b3']

        for year in years[:-1]:
            rowRng = (data[:,0] == year).nonzero()[0]

            x, y, z = [], [], []

            limit = 0
            for row in rowRng:
                limit += 1
                x.append(data[row][features[axis[0]]])
                y.append(data[row][features[axis[1]]])
                z.append(data[row][features[axis[2]]])

                if limit == 25:
                    break

            # Centroid Calculation
            x, y, z = np.array(x), np.array(y), np.array(z)
            cent_x = np.sum(x)/x.shape[0]
            cent_y = np.sum(y)/y.shape[0]
            cent_z = np.sum(z)/z.shape[0]

            ind = np.where(years == year)[0][0]
            ax.scatter(x, y, z, c=colors[ind], marker='o')
            ax.scatter(cent_x, cent_y, cent_z, marker='x')
            print year
            break

        ax.set_xlabel(axis[0])
        ax.set_ylabel(axis[1])
        ax.set_zlabel(axis[2])

if __name__ == '__main__':
    # meanPlotter('loudness')
    # allFourMeanPlotter()
    # allBPlotter()
    # threeDFeaturePlot()
    #
    clusterMapp()

    plt.legend()
    plt.show()
