x = 1 #第一次輸入
while x < 4:  #只能輸入三次
	password = input('請輸入密碼：')
	i = 3 - x #剩餘次數
	if password == 'a123456':
		print('登入成功!')
		break
	else: 
		print('密碼錯誤!還有', i, '次機會')
	x = x + 1
