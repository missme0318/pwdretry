# -*- coding: utf-8-sig -*-
password = 'a123456'
password = str(password)
'''
times = 3
while times <= 3 and times >= 0:
	login = input("請輸入密碼(最多輸入3次)：")
	if login == password:
		print('登入成功')
		break
	else:
		times -= 1
		print('登入失敗！還有', times, '次機會')
		if times == 0:
			print('登入三次失敗，請與客服聯繫')
			break

'''


times = 3
while times > 0:
	login = input("請輸入密碼(最多輸入3次)：")
	if login == password:
		print("登入成功")
		break
	else:
		times -= 1
		print("登入失敗！還有", times, "次機會")
		if times == 0:
			print("登入三次失敗，請與客服聯繫")
