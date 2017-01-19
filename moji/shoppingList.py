def izpisi_pomoc():
	print('')
def izpisi_seznam(seznam):
	print('Na seznamu je {} artiklov:'.format(len(seznam)))
	for artikel in seznam:
		print(artikel)

def main():
	nakupovalniSeznam=[]
	while True:
		artikel=input('>>>)
		if artikel = 'KONEC':
			break
		elif artikel = 'IZPIS':
			izpisi_seznam(nakupovalniSeznam)
			continue
		elif artikel = 'POMOC':
			izpisi_pomoc()
			continue
		dodaj_na_seznam()
		
