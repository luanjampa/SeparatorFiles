import glob,os,shutil,sys

def separete(location,ext,arqPorPasta):
	files = glob.glob(location + '/' +'*.'+ ext)
	size = len(files)
	cont = 0
	cont2 = '0'
	while(cont < size):
		files = glob.glob(location + '/' +'*.'+ ext)
		os.mkdir(cont2)
		for i in range(0,int(arqPorPasta)):
			shutil.move(files[i],os.getcwd()+'/'+cont2)
		cont+=1
		cont2 = (int(cont2) + 1)
		cont2 = str(cont2)

if __name__ == "__main__":
	try:
		if os.path.isdir(sys.argv[1]):
			separete(sys.argv[1],sys.argv[2],sys.argv[3])
		else:
			print("Location:"+ sys.argv[1] +"\nNOT FOUND")

	except IndexError:
		print("Necessary to fill the arguments correctly\nExemple: python3.4 SEPARATOR.py /home/user/pictures/ jpg 100")

