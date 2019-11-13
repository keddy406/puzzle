import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字:\n')
	num = int(num)
	if num == r:
		print('恭喜答對')
		break
	elif num > r:
		print('猜錯了 你猜的數字太大')
	elif num < r:
		print('猜錯了 你猜的數字太小')
		