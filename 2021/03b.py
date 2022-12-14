

input = open('input3.txt').read().split('\n')


oxygen_generator= ''

for i in range(12) :
	uns = 0
	zeros = 0
	for ligne in input :
		if not ligne.startswith(oxygen_generator) :
			continue
		if ligne[i]=='1' : 
			uns += 1
		elif ligne[i]=='0' :
			zeros += 1
		else :
			print(ligne[i],"inconnu")
	if uns>=zeros :
		oxygen_generator += '1'	
	else :
		oxygen_generator += '0'
	print(oxygen_generator,uns,zeros)	
	

co2 = ''
for i in range(12) :
	uns = 0
	zeros = 0
	for ligne in input :
		if not ligne.startswith(co2) :
			continue
		if ligne[i]=='1' : 
			uns += 1
		elif ligne[i]=='0' :
			zeros += 1
		else :
			print(ligne[i],"inconnu")
	if uns>zeros :
		co2 += '0'	
	else :
		co2 += '1'


print(oxygen_generator)
print(int(oxygen_generator,2))
print(co2)
print(int(co2,2))
print(int(co2,2)*int(oxygen_generator,2))