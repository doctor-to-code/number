import random

r = random. randint(1, 100)
i = 0
while True:
	i = i + 1
	x = input('請輸入數字')
	x = int(x) 
	if x == r:
		print('you win')
		break
	elif x > r:
		print('比答案大')
	elif x < r:
		print('比答案小')
	print('已經猜第', i,'次')