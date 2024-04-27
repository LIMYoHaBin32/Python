#1-1
name = "BlockDMask"
if name == "BlockDMask":
 print("이름이 맞습니다.")
else:
 print("이름이 다릅니다.")

 #1-2
pocket = 1000
if pocket == 1000:
 print("복권 구매")
elif pocket == 500:
 print("껌 구매")
else:
 print("504나 가자")

 #2-1
a = '사과'
b = '바나나'
c = '치즈'
if a == '사과' or b == '안바나나':
  print('사과 이거나 바나나 입니다')
if a == '사과' and b == '안바나나':
  print('사과 이고 바나나 입니다')
if not a == '사과' :
  print('사과가 아니어야 여기 들어옵니다.')

  #2-2
a = [1,2,3,4,5,6,7,8]
if 1 in a:
  print("a 리스트에 1이 포함되어있습니다.")
elif 10 in a:
  print("a 리스트에 10이 포함되어있습니다.")

  #3
p_class = "Z"
sel_amount = 79900

if p_class == "A":
  sel_amount *= 0.7 # 55930.0
  print(sel_amount)
elif p_class == "B":
  sel_amount *= 0.85 # 67915.0
  print(sel_amount)
elif p_class == "C":
  sel_amount *= 0.92 # 84900
  print(sel_amount)
elif p_class == "Z":
  sel_amount += 5000 # 84900
  print(sel_amount)

  #4-1
p_class = "Z"
sel_amount = 79900

if p_class == "A":
  sel_amount *= 0.7 # 55930.0
  print(f'판매가는 {sel_amount}원 입니다.')
elif p_class == "B":
  sel_amount *= 0.85 # 67915.0
  print(f'판매가는 {sel_amount}원 입니다.')
elif p_class == "C":
  sel_amount *= 0.92 # 84900
  print(f'판매가는 {sel_amount}원 입니다.')
elif p_class == "Z":
  sel_amount += 5000 # 84900
  print(f'판매가는 {sel_amount}원 입니다.')

  #4-2
x = 11

if x< 10:
  print('x는 10보다 작아!!!!!')
else:
  print('x는 10보다 작아 않아!!!!!')

  #4-3
x = 2

if x%2 == 0:
  print('x는 짝수야!!!!!')
else:
  print('x는 홀수야!!!!!')

  #5
x = 3

if x < 10:
  print('x는 10보다 작아!!!!!')
  if x%2 == 0:
    print('x는 짝수야!!!!!')
  else:
    print('x는 홀수야!!!!!')
else:
  print('x는 10보다 커!!!!!')
  if x%2 == 0:
    print('x는 짝수야!!!!!')
  else:
    print('x는 홀수야!!!!!')

    #6
x = 3

if x<10 and x%2==0:
  print('x는 10보다 작으면서 짝수야!!!!!')
if x<10 and not x%2==0:
  print('x는 10보다 작으면서 홀수야!!!!!')
if not x<10 and x%2==0:
  print('x는 10보다 크면서 짝수야!!!!!')
if not x<10 and not x%2==0:
  print('x는 10보다 크면서 홀수야!!!!!')

  #while
treeHit = 0

while treeHit < 10:
  treeHit += 1
  print("나무를 %d번 찍었습니다."%treeHit)
  if treeHit == 10:
    print("나무 넘어갑니다.")

#break
coffee = 10
money = 300
while money:
  print("돈을 받았으니 커피를 줍니다.")
  coffee -= 1
  print("남은 커피의 양은 %d개 입니다."%coffee)
  if coffee == 0:
    print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
    break
  
  while True:
  print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

  #1번 방법
i = 0
result1 = 0
while i < 100:
  i += 1
  if i % 2 == 0:
    result1 += i

print('1번 방법 : {0}'.format(result1))

#2번 방법
j = 0
result2 = 0
while True:
  if j > 100:
    break

  j +=1
  if j % 2 == 0:
    result2 += j

print('2번 방법 (break) : {0}'.format(result2))

#3번 방법
k = 0
result3 = 0
while k < 100:
  k += 1
  if k % 2 != 0:
    continue

  result3 += k

print('3번 방법 (continue) : {0}'.format(result3))