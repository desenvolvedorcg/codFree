#coding: utf-8
import numpy as np
np.set_printoptions(threshold='nan')
import random


def criarNoise(matrizDeCriacao):
	loc=0.0
	scale=1.0
	noise_factor = 0.001
	noiseCriado = matrizDeCriacao + noise_factor * np.random.normal(loc, scale, size=matrizDeCriacao.shape)
	return noiseCriado


ValoresValence =  np.genfromtxt("/home/jefferson/Documents/codsArtigosEmocoes/arquivo_Valence.csv", delimiter=',')
ValoresArousal =  np.genfromtxt("/home/jefferson/Documents/codsArtigosEmocoes/arquivo_Arousal.csv", delimiter=',')


print len(ValoresValence)
print ValoresValence[1][2020]

print ValoresValence[54][2020]
print ValoresArousal[54][1], ValoresArousal[54][3]
#ValoresValence =  np.genfromtxt("/home/jefferson/AMG1608/valence.csv", delimiter=',')

for i in range(len(ValoresArousal)):
	if len(ValoresValence[i]) != 2021:
		print "achei"
		print len(ValoresArousal[i])
	
#apenas os das caracteristica de arousal e valence
valencesCorreto = ValoresValence[1:,1:2020]
arousalCorreto = ValoresArousal[1:,1:2020]
#apenas os valores de arousal e valence
apenasArousal = ValoresArousal[1:,2020]
apenasValence = ValoresValence[1:,2020]


print len(valencesCorreto[0]), "valor final"


serao = 0
serao2 = 0
valenceCl1 = []
valenceCl2 = []
valenceCl3 = []
valenceCl4 = []

arousalCl1 = []
arousalCl2 = []
arousalCl3 = []
arousalCl4 = []
for i in range(194):
	if apenasValence[i] >= 0 and apenasValence[i] < 1 and apenasArousal[i] >= 0 and apenasArousal[i] < 1:
		serao+=1
		valenceCl1.append(valencesCorreto[i])
		#print serao
	elif apenasValence[i] > -1 and apenasValence[i] < 0 and apenasArousal[i] > 0 and apenasArousal[i] < 1:
		#serao2+=1
		valenceCl2.append(valencesCorreto[i])
		#print serao2
	elif apenasValence[i] > -1 and apenasValence[i] < 0 and apenasArousal[i] > -1 and apenasArousal[i] <= 0:
		#serao2+=1
		valenceCl3.append(valencesCorreto[i])
		#print serao2
	else:
		serao2+=1
		valenceCl4.append(valencesCorreto[i])
		#print serao2, i





print arousalCorreto[0][76], valencesCorreto[0][76]

print "observe a quantidade\n"

print len(valenceCl1), len(valenceCl2), len(valenceCl3), len(valenceCl4) 


#criando os noises
valenceCl2 = np.array(valenceCl2)
noiseC2p1 = criarNoise(valenceCl2)
noiseC2p2 = criarNoise(valenceCl2)
noiseC2p3 = criarNoise(valenceCl2)

valenceCl3 = np.array(valenceCl3)
noiseC3 = criarNoise(valenceCl3)

valenceCl4 = np.array(valenceCl4)
noiseC4 = criarNoise(valenceCl4)



print valenceCl2[0][45],noiseC2p1[0][45], noiseC2p2[0][45], noiseC2p3[0][45]


#importante para criar o vetor de 0 ou 1.
#raramdom =  [random.randrange(0, 2) for _ in range(0, 61)]
