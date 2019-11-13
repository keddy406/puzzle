import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜數字:\n')
	num = int(num)
	count += 1
	print('這是你第',count,'幾次猜')
	if num == r:
		print('恭喜答對')
		break
	elif num > r:
		print('猜錯了 你猜的數字太大')
	elif num < r:
		print('猜錯了 你猜的數字太小')
