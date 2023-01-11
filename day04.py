'''
    실습 1
    숫자를 입력 받아 짝수와 홀수를 구분하여 출력
'''
''' num = int(input('숫자 입력 : '))
if num % 2 == 0:
    print(num,': 짝수')
if num % 2 == 1:
    print(num,': 홀수') '''

'''
    실습 2
    숫자 세 개를 입력 받아 가장 큰 수를 출력
'''
''' su1 = int(input('첫번째 숫자 입력 : '))
su2 = int(input('두번째 숫자 입력 : '))
su3 = int(input('세번째 숫자 입력 : '))
if su1 >= su2 and su1 >= su3:
    print('첫번째 숫자가 가장 크다')
if su2 > su1 and su2 >= su3:
    print('두번째 숫자가 가장 크다')
if su3 > su1 and su3 > su2:
    print('세번째 숫자가 가장 크다') '''

'''
    실습 3
    숫자 두 개를 입력 받아 합이 짝수이면서 3의 배수이면 그 합을 출력
'''
''' su1 = int(input('첫번째 숫자 입력 : '))
su2 = int(input('두번째 숫자 입력 : '))
Sum = su1 + su2
if Sum % 2 == 0 and Sum % 3 == 0:
    print('두 수의 합 :',Sum) '''

''' num = int(input('숫자 입력 : '))
if num == 1:
    print('1 입력')
else:
    print('1이 아닌 값 입력') '''

''' num = int(input('숫자 입력 : '))
if num % 2 == 0:
    print(num,': 짝수')
else:
    print(num,': 홀수') '''

''' num = int(input('숫자 입력 : '))
if num % 3 == 0:
    if num % 2 == 0:
        print('입력한 숫자는 3의 배수이면서 짝수 입니다')
    else:
        print('입력한 숫자는 3의 배수이면서 홀수 입니다')
print('다음 문장 실행') '''

''' num = int(input('숫자 입력 : '))
if num > 0:
    if num % 2 == 0:
        print('num은 양의 짝수')
    else:
        print('num은 양의 홀수')
else:
    if num == 0:
        print('num은 0')
    else:
        print('num은 음수') '''

''' num = int(input('숫자 입력 : '))
if num > 0:
    print('0보다 큰 수 입력')
elif num < 0:
    print('0보다 작은 수 입력')
else:
    print('0과 같은 수 입력') '''

'''
    실습 4
    GB단위 용량을 입력 받아 byte, KB, MB 중 선택한 단위로 변환하여 출력
    (선택은 숫자로 진행; ex. 1. byte, 2. KB, 3. MB)
        * 용량 변환
            1024 byte = 1KB
            1024 KB = 1MB
            1024 MB = 1GB
'''
''' Size = int(input('용량 입력(GB) : '))
sel = int(input('변환할 단위 선택\n1. byte\n2. KB\n3. MB\n>>>'))
if sel == 1:
    print('{}GB는 {}byte 입니다'.format(Size,Size*1024**3))
elif sel == 2:
    print('{}GB는 {}KB 입니다'.format(Size,Size*1024**2))
elif sel == 3:
    print('{}GB는 {}MB 입니다'.format(Size,Size*1024)) '''

'''
    실습 5
    이름, 학번, 3개 과목의 성적을 입력 받아 합계와 평균을 구하고
    평균이 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D,
    60점 미만이면 F를 출력
'''
''' name = input('학생 이름 : ')
num = input('학번 : ')
sc1 = int(input('과목1 점수 : '))
sc2 = int(input('과목2 점수 : '))
sc3 = int(input('과목3 점수 : '))
Sum = sc1 + sc2 + sc3
aver = Sum / 3
if aver >= 90:    grade = 'A'
elif aver >= 80:    grade = 'B'
elif aver >= 70:    grade = 'C'
elif aver >= 60:    grade = 'D'
else:    grade = 'F'
print('{}님({})의 총 학점은 {} 입니다'.format(name,num,grade)) '''
'''
    실습 6
    정수를 입력 받아 아래의 내용 중 하나 출력
     - 3의 배수이면서 4의 배수입니다
     - 3의 배수입니다
     - 4의 배수입니다
     - 3의 배수도 4의 배수도 아닙니다
     - 0은 어떤 숫자의 배수도 아닙니다
'''
''' num = int(input('숫자 입력 : '))
if num == 0:
    print('0은 어떤 숫자의 배수도 아닙니다')
elif num % 3 == 0:
    if num % 4 == 0:
        print('3의 배수이면서 4의 배수입니다')
    else:
        print('3의 배수입니다')
elif num % 4 == 0:
    print('4의 배수입니다')
else:
    print('3의 배수도 4의 배수도 아닙니다') '''

'''
    실습 7
    커피 한 잔의 가격은 2000원이다.
    10잔을 초과하면 초과하는 양에 대해서만 한 잔에 1500원씩 받는다.
    커피의 잔 수를 입력 받아 지불할 금액을 출력
'''
''' coffee = int(input('커피 몇 잔? >> '))
price = 2000
dsc = 1500
if coffee <= 10:
    result = coffee * price
else:
    result = 10 * price + (coffee-10) * dsc
print('커피의 총 가격은 {:,}원 입니다'.format(result)) '''

''' for i in range(1,11,1):
    print(i)

print('다음 문장') '''

''' for i in range(0,3,1):
    print('i :',i,'for문 이해하기')

print('다음 문장 실행') '''

''' for i in range(1,11,1):
    if i % 2 == 0:
        print('i =',i,': 값 확인')

print('다음 문장') '''

''' for i in range(1,11,2):
    print('i =',i,': 값 확인') '''

''' for i in range(10,-1,-1):
    print(i,'10 ~ 0 까지 출력') '''

'''
    실습 8
    for문을 이용하여 1 ~ 10까지의 합을 출력
'''
''' Sum = 0
for num in range(1,11,1):
    Sum += num
print('1 ~ 10 전체 합 :',Sum) '''

'''
    실습 9
    숫자를 입력 받아 1부터 입력 받은 수 까지의 합을 출력
'''
''' su = int(input('숫자 입력 : '))
Sum = 0
for b in range(1,su+1,1):
    Sum += b

print('1 ~',su,'까지의 합 :',Sum) '''