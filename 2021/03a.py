

input = open('input3.txt').read().split('\n')


uns = [0 for x in range(12)]
zeros = [0 for x in range(12)]
for ligne in input :
	for indice in range(12) :
		if ligne[indice]=="1" :
			uns[indice] += 1
		else :
			zeros[indice] +=1


print(uns)			
print(zeros)

gamma = []
epsilon = []

for indice in range(12) :
	if uns[indice]>zeros[indice] :
		gamma.append(1)
		epsilon.append(0)
	else : 	
		gamma.append(0)
		epsilon.append(1)

gamma = [str(x) for x in gamma]
epsilon = [str(x) for x in epsilon]
print("".join(gamma))
print(int("".join(gamma),2))
print(int("".join(gamma),2)*int("".join(epsilon),2))	