import random

r = random. randint(1, 5)
while True:
	x = input('請輸入數字')
	x = int(x) 
	if x == r:
		print('you win')
		break
	else:
		print('retry it')
