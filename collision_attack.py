import TinySHA
import sys

oldMessages = []
oldHashes = []
numHashes = 0

while True:

    currentHash = TinySHA.getTinySHA1(int(sys.argv[1]))
    numHashes += 1
    #print("testing hash: " + currentHash + "\n")

    if currentHash in oldHashes:

        #print("Found a match!\n")
        oldIndex = oldHashes.index(currentHash)
        #print(oldMessages[oldIndex] + ":" + oldHashes[oldIndex] + "\n")
        #print(TinySHA.getCurrentSeed() + ":" + currentHash + "\n")
        print(str(sys.argv[1]) + "\t" + str(numHashes))
        exit(0)

    else:

        oldHashes.append(currentHash)
        oldMessages.append(TinySHA.getCurrentSeed())
