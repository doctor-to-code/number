import random

r = random. randint(1, 100)
while True:
	x = input('請輸入數字')
	x = int(x) 
	if x == r:
		print('you win')
		break
	elif x > r:
		print('比答案大')
	elif x < r:
		print('比答案小')