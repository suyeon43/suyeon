'''
    실습 1
    숫자를 입력 받아 1부터 입력 받은 숫자 까지 홀수의 합과 짝수의 합을 각각 출력
'''
''' oddSum = 0
evenSum = 0
num = int(input('숫자 입력 : '))
for f in range(1,num+1,1):
    if f % 2 == 0:
        evenSum += f
    else:
        oddSum += f
print('1 ~',num,'까지의\n홀수의 합 :',oddSum,'\n짝수의 합 :',evenSum) '''

''' print('출력 내용',end='-')
print('이어서 출력') '''

''' for g in range(1,11,1):
    print(g,end='*') '''

'''
    실습 2
    for문 하나만 사용하여 아래와 같이 출력

    1       2       3       4       5  
    6       7       8       9       10
    11      12      13      14      15
    16      17      18      19      20
    21      22      23      24      25
    26      27      28      29      30
'''
''' for h in range(1,31,1):
    print(h,end='\t')
    if h % 5 == 0:
        print() '''

''' Sum = 0
Start = int(input('시작값 입력 : '))
en = int(input('끝값 입력 : '))
grow = int(input('증감값 입력 : '))
for i in range(Start,en+1,grow):
    Sum += i
print('{}에서 {}까지 {}씩 증가한 값의 합 : {}'.format(Start,en,grow,Sum)) '''

''' Sum = 0
num = int(input('값 입력 : '))
for i in range(num+1):      # range에 끝값 입력, 시작값은 0으로 증감값은 1로 자동 입력
    print(i)
    Sum += i
print('0에서 %d까지 합 : %d'%(num,Sum)) '''

''' for i in range(0,10):       # range(0,10,1)
    print(i) '''

''' i = 10                  # i 변수에 10을 넣고 시작했지만
for i in range(10):     # range(0,10,1) 과 같은 의미가 되면서
    print(i)            # 기존 i 값과 상관 없이 0 부터 시작 '''

''' i = 0
for i in range(10,2):       # range 함수는 증감값 -> 시작값 순서로만 생략 가능
    print(i)                # range(10,2,1)     <- 생성되는 데이터 X

a = list(range(10,2))
print(a)
b = list(range(0,10,2))
print(b) '''

''' for i in range(0,10,2):
    print(i) '''

'''
    실습 3
    시작값과 끝값을 입력 받아 그 사이의 7의 배수 출력
    (증감값은 생략하여 사용)
'''
''' startNum = int(input('시작값 입력 : '))
endNum = int(input('끝값 입력 : '))
for su in range(startNum+1,endNum):
    if su % 7 == 0:
        print(su) '''

'''
    실습 4
    두 수를 입력 받아 각각 시작값과 끝값으로 사용하여
    시작값부터 끝값까지의 합을 출력
    (먼저 입력된 숫자가 큰 숫자일때와 작은 숫자일때 전부 동작가능한 코드 작성)
'''
#실습 4 - 풀이 1
''' Sum = 0
su1 = int(input('숫자1 입력 : '))
su2 = int(input('숫자2 입력 : '))
if su1 > su2:
    for s in range(su2,su1+1):
        Sum += s
    print(su2,'~',su1,'까지의 합 :',Sum)
else:
    for s in range(su1,su2+1):
        Sum += s
    print(su1,'~',su2,'까지의 합 :',Sum) '''

# 실습 4 - 풀이 2
''' Sum = 0
su1 = int(input('숫자1 입력 : '))
su2 = int(input('숫자2 입력 : '))
if su1 > su2:       # 여러 프로그래밍 언어에서 사용하는 swap 코드 예시
    num = su2
    su2 = su1
    su1 = num
for s in range(su1,su2+1):
    Sum += s
print(su1,'~',su2,'까지의 합 :',Sum) '''

# 실습 4 - 풀이 3
''' Sum = 0
su1 = int(input('숫자1 입력 : '))
su2 = int(input('숫자2 입력 : '))
if su1 > su2:       # python에서 사용 가능한 swap 코드
    su1,su2 = su2,su1
for s in range(su1,su2+1):
    Sum += s
print(su1,'~',su2,'까지의 합 :',Sum) '''

'''
    실습 5
    첫 날에 10원을 예금하고, 다음날부터는 전날의 2배를 예금하는 방식으로
    한 달(30일)동안 저축을 하게되면 총 얼마까지 모을 수 있을까요?
    (1일차 : 10원, 2일차 : 20원, 3일차 : 40원 ...)
'''
''' result = 0
money = 10
for Day in range(1,31):
    #result += money * 2 ** (Day-1)     # 이 수식 사용 or 아래 if문 사용
    if Day == 1:
        money = 10
    else:
        money = money * 2
    result += money
    #print(Day, money, result)           # 중간 확인을 위한 코드
print('총 저축 금액 : {:,}원'.format(result)) '''

''' for i in [1,2,3,4,5,6,7,8,9,10]:    # 변수에 넣을 데이터를 list로 제시
    print('i :',i) '''

''' for i in [3,4,5,8,2,1,5,4,7,9]:
    print('i :',i) '''

''' for c in "Hello Python":        # 문자열을 직접 사용
    print('c :',c) '''

''' st = 'Hello Python'
for c in st:                    # 문자열을 변수에 넣어서 사용
    print('c :',c) '''

''' for i in range(3):
    for k in range(2):
        print('이중 for문(i : %d\tk : %d)'%(i,k)) '''

'''
    실습 6
    중첩 for문을 이용하여 아래의 내용을 똑같이 출력하세요

    상위포문 0 일때 하위포문 : 0 0 0 0 0
    상위포문 1 일때 하위포문 : 0 1 2 3 4
    상위포문 2 일때 하위포문 : 0 2 4 6 8
    상위포문 3 일때 하위포문 : 0 3 6 9 12
    상위포문 4 일때 하위포문 : 0 4 8 12 16
'''
''' for a in range(5):
    print('상위포문',a,'일때 하위 포문 : ',end='')
    for b in range(5):
        print(a*b,end=' ')
    print() '''

'''
    실습 7
    중첩 for문을 이용하여 아래와 같이 출력

    1       2       3       4       5  
    6       7       8       9       10
    11      12      13      14      15
    16      17      18      19      20
    21      22      23      24      25
'''
for c in range(5):
    for d in range(1,6):
        print(c * 5 + d, end='\t')
    print()