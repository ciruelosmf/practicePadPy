
def asd(a, l=[]):

  l.append(a)
  return l
ad = asd(3)
print(ad)

ad2 = asd(32)
print(ad, ad2)
def asd(a, l=None):
  if l==None:
    l = []
  l.append(a)
  return l
ad = asd(3)
ad2 = asd(32)

print(ad, ad2)