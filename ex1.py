n= int(input())
x,y =1,1
tx,ty =1,1
plan_list =input().split()

move_list = ['L','R','U','D']
dy =[-1,1,0,0]
dx =[0,0,-1,1]

for plan in plan_list:
  for i in range(len(move_list)):
    if plan == move_list[i]:
      tx = x+dx[i]
      ty = y+dy[i]
    if tx>n or tx<=0 or ty>n or ty<=0:
      continue
    x,y = tx,ty

print(x,y) 

