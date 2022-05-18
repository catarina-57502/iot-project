import pickle
import sys

data = sys.argv[1]
data = data.replace(',', '')

dataR = data.split(" ")

listInt = [float(x) for x in dataR]
dataN = [listInt]
fileC = 'modelC.pkl'
with open(fileC,"rb") as file:
    pc = pickle.load(file)

print(pc.predict(dataN))