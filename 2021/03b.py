#NB_BIT=5
NB_BIT=13


input = open('input03.txt').read().split('\n')


oxygen_generator= ''

for i in range(NB_BIT) :
	uns = 0
	zeros = 0
	ligneExemple = ''
	for ligne in input :
		if not ligne.startswith(oxygen_generator) :
			continue
		ligneExemple =  ligne
		if ligne[i]=='1' : 
			uns += 1
		elif ligne[i]=='0' :
			zeros += 1
		else :
			print(ligne[i],"inconnu")
	print("oxygen",oxygen_generator,uns,zeros)			
	if uns==1 and zeros==0:
		print("exemple : ",ligneExemple[i:])
		oxygen_generator += ligneExemple[i:]
		break
	elif uns==1 and zeros==1:
		print("exemple : ",ligneExemple[i:])
		oxygen_generator += ligneExemple[i:]
		break
	elif uns==zeros :
		oxygen_generator += '0'
	elif uns>zeros :
		oxygen_generator += '1'	
	else :
		oxygen_generator += '0'
	
print(oxygen_generator)
print("oxygen en entier :",int(oxygen_generator,2))	

co2 = ''
for i in range(NB_BIT) :
	uns = 0
	zeros = 0
	ligneExemple = ''
	for ligne in input :
		if not ligne.startswith(co2) :
			continue
		ligneExemple =  ligne
		if ligne[i]=='1' : 
			uns += 1
		elif ligne[i]=='0' :
			zeros += 1
		else :
			print(ligne[i],"inconnu")
	print("co2",co2,uns,zeros)				
	if uns==1 and zeros==0:
		print("exemple : ",ligneExemple[i:])
		co2 += ligneExemple[i:]
		break
	elif uns==0 and zeros==1:
		print("exemple : ",ligneExemple[i:])
		co2 += ligneExemple[i:]
		break
	elif uns == zeros :
		co2 += '0'
	elif uns>zeros :
		co2 += '0'	
	else :
		co2 += '1'
	



print("co2 :",co2)
print("co2 :",int(co2,2))
print(int(co2,2)*int(oxygen_generator,2))