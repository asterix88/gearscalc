## -*- coding: utf-8 -*-
# gearcalc.py
##

from sys import argv as aa
from sys import exit
import math
import os

banner = """  
  ##                              #      
 #   ###  ## ###  ##     ###  ##  #  ### 
 # # ##  # # #    #      #   # #  #  #   
 # # ### ### #   ##      ### ###  ## ### 
  ##                                     

Usage: 
gearscalc.py -opt -m -z -L -Dt1 -Dt2 -mn -cos

< beri nilai 1 pada setiap argumen yang kosong >

OPTIONS:
	-l : roda gigi lurus
	-r : roda gigi rack
	-m : roda gigi miring
	
"""

strbanner = """  
                                           
  _ |_  _  _  .  _  |_  |_    _   _  _   _ 
 _) |_ |  (_| | (_) | ) |_   (_) (- (_| |  
                _/           _/            

"""

miringbanner = """
                                     
 |_   _ | .     _  |    _   _  _   _ 
 | ) (- | | )( (_| |   (_) (- (_| |  
                       _/            

"""

rackbanner = """
  __                            
 |__)  _   _ |     _   _  _   _ 
 | \  (_| (_ |(   (_) (- (_| |  
                  _/ 
"""


def gearcalc(opt,m,z,L,dt1,dt2,mn,coss):
	if opt == "-l" :
		os.system("clear")
		print(strbanner)
		print("Hasil Perhitungan >>> ")
		print()
		print("Diamter jarak bagi (Pt): ",float(m) * float(z))
		print("Diamter kepala gigi (Dh/Dk) : ",float(m) * (float(z)+2))
		print("Diameter kaki gigi (Df): ",float(m)*(float(z)-2.5))
		print("Tinggi kepala gigi (Hk): ",1 * float(m))
		print("Tinggi kaki gigi (Hf): ",1.25 * float(m))
		print("Tinggi gigi (H): ",(1*float(m))+(1.25*float(m)) )
		print("Jarak antar poros (T): ",(float(dt1)+float(dt2))/2)
		print("Angka Transmisi (i): ",float(dt1)/float(dt2))
		print("Lebar gigi (b): ",10 * float(m))
		print("Tebal pelek (k): ",1.5 * float(m))
		print()
	
	elif opt == "-m":
		ma = float(mn) / math.cos(math.radians(int(coss)))
		D = float(z) * ma
		b = 12 * float(mn)
		os.system("clear")
		print(miringbanner)
		print("Hasil perhitungan >> ")
		print()
		print("D : ",D)
		print("Ma : ",ma)
		print("Hk : ",1 * float(mn) )
		print("Hf : \n\tStandar NEN >> ",1.25 * float(mn),"\n\tStandar DIN >> ",1.16 * float(mn) )
		print("Dh : ",D + (2 * float(mn)) )
		print("Dk : ",D - (2.5 * float(mn)) )
		print("b : ",b)
		print("bn : ",b / math.cos(math.radians(int(coss))) )
		print("k : ", 1.6 * float(mn))
		print()
		
	
	
	elif opt == "-r":
		os.system("clear")
		print(rackbanner)
		print("Hasil perhitungan >>> ")
		print()
		pt = 3.14 * float(m)
		Z = float(L) / pt
		sisa = (Z % (float(L) // pt)) * pt
		X = ( float(sisa) + 4 ) / 2
		print("Ukuran pitch (pt) : ",pt)
		print("Banyak gigi sepanjang ",float(L)," : ",Z)
		print("Sisa gigi : ",sisa)
		print("Sisa gigi yang sama (X) : ",X)
		print("Tinggi gigi kepala (ha) : ", 1 * float(m) )
		print("Tinggal gigi kaki (hf) : ", 1.25 * float(m) )
		print("Tinggi gigi (H) : ", (1*float(m) ) + (1.25 * float(m) ) )
		print()
		
	else:
		print("Wrong input")
		exit()
	
	












if __name__ == "__main__":
	if len(aa) != 9:
		os.system("clear")
		print(banner)
	else:
		gearcalc(aa[1],aa[2],aa[3],aa[4],aa[5],aa[6],aa[7],aa[8] )
	
	
           


