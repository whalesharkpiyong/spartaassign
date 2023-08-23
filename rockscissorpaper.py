import random

list = ['가위','바위', '보']
com = random.choice(list)
print(com)

print('가위, 바위, 보 게임을 시작합니다.')
user= str(input("가위~ 바위~ 보!"))

if user not in list:
    print("가위, 바위, 보 중 하나를 내시오")
else:
    if com == user: 
        print('비겼습니다.')
    elif (com == '바위' and user == '가위') or (com =='가위' and  user == '보') or (com =='보' and user=='바위'):
        print('졌습니다.')
    else:
        print('이겼습니다.')

    
