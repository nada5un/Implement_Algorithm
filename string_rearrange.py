a = input()

str1 = []
sum = 0

for i in a:
  if i.isalpha():
    str1.append(i)
  else:
    sum += int(i)
  
str1.sort()

for i in str1:
  print(i,end='')
print(sum,end='')