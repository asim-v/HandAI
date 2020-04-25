import numpy as np

import pandas as pd
import scipy.signal as ss
import matplotlib.pylab as plt

import random

def sample_generator(yrange = 1,amount = 6):
	RES = ''
	for n in range(yrange):
		res = ''
		for x in range(amount):
			if x < amount-1: 
				res += str(random.randrange(100))
				res += ','
			else: res += str(random.randrange(100))
		RES += res
		RES += '\n'
	return RES

def piece_generator(amount = 6):
	res = ''
	for x in range(amount):
		if x < amount-1: 
			res += str(random.randrange(100))
			res += ','
		else: res += str(random.randrange(100))
	return res




file = open('mem.txt','r').read()


res = []
l = [x.split(',') for x in [i for i in file.split('\n')]] #Separa nuevas lineas y separa las comas
l = l[:len(l)-1] #Elimina el ultimo valor generado vacio
for m in l: #Convierte los valores en numeros
	L = []
	for n in m: L.append(int(n))
	res.append(L)

res = np.array(res)
res = np.transpose(res)

out = []
print(res)
for x in range(6):
	unfiltered = res[x]
	sg_filtered = ss.savgol_filter(unfiltered,7,3)
	out.append(int(sg_filtered[-1]))

print(out)
