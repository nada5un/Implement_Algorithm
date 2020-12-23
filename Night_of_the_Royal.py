point =input()
point_c = point[0:1]
point_r = point[1:2]
count =0 

col_list = ['a','b','c','d','e','f','g','h']
row_list = [1,2,3,4,5,6,7,8]

#이동 총 8가지 경우의 수 
d1 = [-1,1]
d2 = [-2,2]

t1 = [-2,2]
t2 = [-1,1]

for idx,col in enumerate(col_list):
  if col == point_c:
    c_index = idx+1 # 열 위치 인덱스 

for i in d1:
  for j in d2:
    tx = c_index + i
    ty = int(point_r) + j

    if tx>8 or tx<=0 or ty>8 or ty<=0:
      continue
    else:
      count+=1
  
for i in t1:
  for j in t2:
    tx = c_index + i
    ty = int(point_r) + j
    if tx>8 or tx<=0 or ty>8 or ty<=0:
      continue
    else:
      count+=1
  
print(count)


