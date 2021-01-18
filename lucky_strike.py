n = input()

# 자릿수 기준으로 반으로 나누기 
l = len(n)//2

suma = 0
sumb = 0

for i in range(2*l):
  if i<l:
    suma += int(n[i])
  else:
    sumb += int(n[i])

if suma == sumb:
  print("LUCKY")
else:
  print("READY")