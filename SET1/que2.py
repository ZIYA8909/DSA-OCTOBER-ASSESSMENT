n=8
a=[4021,3377,5120,3377,4021,9001,5120,7]
d={}
for i in range(n):
  if a[i] in d:
    print(a[i])
    break
  d[a[i]]=1

else:
  print(-1)
