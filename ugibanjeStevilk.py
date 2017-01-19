import random

def pripravi_igro(seznamIgralcev):
	steviloRund=int(input("Stevilo rund: "))
	minSt=int(input("Najmanjse mozno stevilo: "))
	maxSt=int(input("Najvecje mozno stevilo:"))
	while True:
		igralec=input("Ime igralca: ")
		if igralec == "":
			break
		seznamIgralcev.append([igralec,0,0])
	return (steviloRund, minSt, maxSt)

def igrajmo(seznamIgralcev, steviloRund, maxSt, minSt):
	print(steviloRund)
	print(minSt)
	print(maxSt)
	for i in range(steviloRund):
		print(i)
		print("Igralci pripravite se za {}. rundo.".format(i + 1))
		for igralec in seznamIgralcev:
			igralec[1]=1
			print("Na vrsti je {}. Ugani stevilko, ki jo imam v ramu.".format(igralec[0]))
			stevilo=random.randint(1, maxSt)
			while True:
				vnos=int(input(">>> "))
				if vnos > stevilo:
					print("Moja stevilka je manjsa!")
					igralec[1]+=1
				elif vnos < stevilo:
					print("Moja stevilka je vecja!")
					igralec[1]+=1
				else:
					print("Bravo! Stevilko si uganil v {}. poskusu".format(igralec[1]))
					break
			igralec[2]+=igralec[1]
		#seznamIgralcev.sort(igralec[2])
		print("Trenutni rezultat red")
		for igralec in seznamIgralcev:
			print(igralec[0] + ' '+ str(igralec[2]))
			

def main():
	seznamIgralcev=[]
	nastavitve = pripravi_igro(seznamIgralcev)
	
	igrajmo(seznamIgralcev, nastavitve[0], nastavitve[2], nastavitve[1])
	
main()
