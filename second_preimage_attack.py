import TinySHA
import sys

numHashes = 0

if len(sys.argv) < 2:

    print("You need to give me a number of bits")
    exit(0)

firstHash = TinySHA.getTinySHA1(int(sys.argv[1]))
firstSeed = TinySHA.getCurrentSeed()

while True:

    newHash = TinySHA.getTinySHA1(int(sys.argv[1]))
    numHashes += 1
    if newHash == firstHash:

        #print("found a match!\n")
        #print(firstSeed + ":" + firstHash + "\n")
        #print(TinySHA.getCurrentSeed() + ":" + newHash + "\n")
        print(str(sys.argv[1]) + "\t" + str(numHashes))
        exit(0)
