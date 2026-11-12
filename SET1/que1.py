n=6
a=[120,45,80,200,35,150]
T=235
d={}
for i in range(n):
  c=T-a[i]
  if c in d:
    print(d[c],i)
    break
  d[a[i]]=i
