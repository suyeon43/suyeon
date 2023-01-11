''' i = 0
while i < 5:
    print(i,'종속 문장')
    i += 1
print('다음 문장') '''

''' i = 1                   # range 함수의 시작값과 비슷
odd,even = 0,0
while i <= 10:          # range 함수의 끝값과 비슷
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1              # range 함수의 증감값과 비슷
print('1 ~ 10 짝수의 합 :',even,'\n1 ~ 10 홀수의 합 :',odd) '''

''' i = 0
while i < 5:
    print(i,'종속 문장')
    i += 1
else:
    print('조건식이 거짓일 경우 :',i)
print('다음 문장') '''

''' for i in range(5):
    print(i,'종속 문장')
print('for문이 끝난 후 i :',i)
print('다음 문장') '''

''' # 무한 반복 1
i = 1
while True:
    print(i,'종속 문장',end=' ')
    i += 1 '''

''' # 무한 반복 2
i = 1
while 1:
    print(i,'종속 문장',end=' ')
    i += 1 '''

''' # 무한 반복 3
i = 1
while i < 5:
    print(i,'종속 문장',end=' ') '''

''' i = 1
flag = True
while flag:
    print(i,'종속 문장',end=' ')
    if i == 10:
        flag = False
    i += 1 '''

'''
    실습 1
    10 ~ 20 범위의 숫자를 입력 받아 1부터 입력 받은 수 까지의 합을 출력
'''
''' Sum = 0; num = 0; i = 1; f = True
while f:
    num = int(input('10 ~ 20 숫자 입력 : '))
    if num < 10 or num > 20:
        print('다시 입력하세요')
    else:
        f = False
while i <= num:
    Sum += i
    i += 1
print('1 ~',num,'까지의 합 :',Sum) '''

''' i = 0
while True:
    if i == 3:
        break
        print('3 --- 출력')
    print(i,'출력')
    i += 1
print('다음 문장') '''

''' i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
        print('3 --- 출력')
    print(i,'출력')
print('다음 문장') '''

'''
    실습 2
    for i in range(3):
        for j in range(5):
            if j == 3:
                break
            print('(i : %d\tj : %d)'%(i,j))
    
    위의 중첩 for문과 똑같이 동작하는 코드를 while문으로 작성해보기
'''
''' i = 0
while i < 3:
    j = 0
    while j < 5:
        if j == 3:
            break
        print('(i : %d\tj : %d)'%(i,j))
        j += 1
    i += 1 '''

'''
    실습 3
    커피 자판기 만들어 보기
     조건 1. 메뉴 : 커피(200원), 코코아(250원), 반환/종료
     조건 2. 요금을 투입하고 음료 선택
             음료가 나오면 잔액 확인을 하고 메뉴를 추가로 선택 가능하도록
             (잔액이 부족하면 '잔액 부족' 띄워주기)
     조건 3. 종료를 선택하기 전까지는 계속 동작하는 코드로 작성
'''
''' coffee = 200; cocoa = 250
money = int(input('요금을 투입하세요 : '))
while True:
    print('현재 잔액 : {:,}원'.format(money))
    print('1. 커피(200원)\n2. 코코아(250원)\n3. 종료')
    cho = int(input('메뉴를 선택하세요 >>>'))
    if cho > 3 or cho < 1:
        print('잘못 선택하셨습니다')
        continue
    elif cho == 3:
        print('잔액 {:,}원이 반환됩니다\n이용해 주셔서 감사합니다'.format(money))
        break
    elif cho == 1 and money >= coffee:
        print('커피 한 잔 나왔습니다')
        money -= coffee
    elif cho == 2 and money >= cocoa:
        print('코코아 한 잔 나왔습니다')
        money -= cocoa
    else:
        print('잔액이 부족합니다') '''

'''
    실습 4
    쌀 100통이 저장된 창고에 암수 한 쌍의 쥐가 들어왔다.
    쥐 한 마리가 하루에 20g의 쌀을 먹고, 10일마다(10,20,30 ...) 쥐가 2배로 늘어난다면
    창고의 쌀이 며칠 만에 다 떨어질까요? 그리고 그 때의 쥐는 총 몇 마리 일까요?
    (쌀 한 통 = 1kg, 쌀을 먹은 후 쥐가 2배로 증가)
'''
''' rice = 100000; mouse = 2; day = 1
while True:
    rice -= mouse * 20
    if day % 10 == 0:
        mouse *= 2
    if rice <= 0:
        break
    day += 1
print(day,'일',mouse,'마리') '''

'''
    실습 5
    1 ~ 1000까지의 자연 수 중 완전수(자기 자신을 제외한 모든 약수의 합이 자신과 같아지는 수)를
    찾는 코드를 작성해서 완전수를 찾아보세요
      ex. 6의 약수 : 1, 2, 3, 6  >>>  1 + 2 + 3 = 6(완전수)
          8의 약수 : 1, 2, 4, 8  >>>  1 + 2 + 4 = 7(완전수 X)
'''
''' for i in range(1,1001):
    Sum, j = 0,1
    while j < i:
        if i % j == 0:
            Sum += j
        j += 1
    if i == Sum:
        print(i,': 완전수') '''