#--- geome series  
#--- evaluate:  3⋅(−2)**n−1
#--- (You are finding S10 for the series 3−6+12−24+... , 
#--- whose common ratio is −2 .)
#--- Sn=a1(1−rn)/1−r


sn = 0
print("hallo")
for q in range(1,11):
  g = 3*(-2)**(q-1)
  gg = (-2)**(0)
  
  sn +=  g
  print(g, gg)
ggg = (-2)**9
print(ggg, "ggg")
print(sn)