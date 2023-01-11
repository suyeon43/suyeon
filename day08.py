''' tp1 = (10,20,30,40)
tp2 = tp1[0] + tp1[1] + tp1[2] + tp1[3]
print('튜플 요소 합 :',tp2)
print('tp1[1:3] :',tp1[1:3])
print('tp1[1:] :',tp1[1:])
print('tp[:3] :',tp1[:3]) '''

''' a = 1,2,3
b = 4,5,6
c = a + b
print('a :',a)
print('b :',b)
print('c :',c) '''

''' pack = 1,2,'패킹'
print('packing\npack :',pack)

a,b,c = pack
print('unpacking\na :',a,'b :',b,'c :',c) '''

''' student = {'학번':1234,'이름':'홍길동','학과':'IT학과'}
print(student)

mobile = {'품명':'갤럭시','가격':100,'크기':10}
print(mobile) '''

''' impo = {}
impo['파이썬']='www.python.org'
impo['네이버']='www.naver.com'
impo['구글']='www.google.com'

print(impo)
print('파이썬 :',impo['파이썬'])
print('네이버 :',impo['네이버'])
print('구글 :',impo['구글']) '''

'''
    python 3.6 까진 딕셔너리에 들어간 데이터는 순서 없이 저장되었고,
    내부 데이터의 순서를 유지하기 위해 OrderedDict() 함수를 사용하여 딕셔너리 생성
'''
''' import collections
impo = collections.OrderedDict() '''

''' impo = {}
name = input('키 입력 : ')
val = input('값 입력 : ')
impo[name] = val

print(name,':',impo[name]) '''

''' num = {1:'일',2:'이',3:'삼',4:'사'}

print('keys() 키 :',num.keys())
print('list(keys()) :',list(num.keys()))
print('\nvalues() 값 :',num.values())
print('list(values()) :',list(num.values())) '''

''' singer = {}
singer['이름']=input('가수 이름 입력 : ')
singer['구성원']=int(input('인원수 입력 : '))
singer['대표곡']=input('대표곡 입력 : ')
for i in singer.keys():
    print('{} : {}'.format(i,singer[i]))
print(singer) '''

''' student = {'학번':1234,'이름':'홍길동','학과':'IT학과'}
print(student['학번'])
print(student['이름'])
print(student['학과'])
print(student.items())
print(student) '''

''' name={'이순신':'거북선','세종대왕':'훈민정음','파이썬':'프로그래밍'}
for key,value in name.items():
    print(key,':',value)

print('삭제 :',name.clear())
print('삭제 후 dict :',name) '''

''' num = {1:'일',2:'이',3:'삼',4:'사',5:'오'}
print('변경 전 값 :',num)
print('num.setdefault(9) :',num.setdefault(9,'구~우'))
"""
num[5] = '다섯'            : 5라는 키에 매핑된 값을 변경
num.setdefault(5,'다섯')   : 5라는 키가 존재하기 때문에 값을 변경하지 않는다
"""
print('변경 후 값 :',num)
#print('num.get(9) value :',num.get(9))
"""
print('존재하지 않는 key 7 :',num.get(7))   : 없는 키가 입력되면 None 출력
print('존재하지 않는 key 7 :',num[7])       : 없는 키가 입력되면 error
"""
 '''

''' dic = {}; dic2 = {}; ls = []

ls.append(input('등록할 첫번째 키 입력 : '))
ls.append(input('등록할 두번째 키 입력 : '))
ls.append(input('등록할 세번째 키 입력 : '))

dic = dic.fromkeys(ls)
print('dic 키 설정 :',dic)

dic2 = dic2.fromkeys(ls,0)
print('dic2 키&값 설정 :',dic2) '''

''' num = {1:'일',2:'이',3:'삼',4:'사',5:'오'}
aaa = {6:'육',7:'칠',8:'팔'}
print('update 전 num :',num)
num.update(aaa)
#num = num + aaa
print('update 후 num :',num) '''

''' num = {1:'일',2:'이',3:'삼',4:'사',5:'오'}
print('popitem() 전 num :',num)
print('popitem 실행 결과 ->',end=' ')
print(num.popitem())
print('popitem() 후 num :',num)
print('popitem 실행 결과 ->',end=' ')
print(num.popitem())
print('popitem() 후 num :',num) '''

''' num = {1:'일',2:'이',3:'삼',4:'사'}
print('pop 전 num :',num)
print('pop(3) 실행 :',num.pop(3))
print('pop 실행 후 num :',num) '''

''' Str = 'Have a nice day'
print('Str :',Str)
print('Str[0] :',Str[0])
print('Str[1] :',Str[1])
print('Str[2] :',Str[2])
print('Str[3] :',Str[3]) '''

''' st = 'Have a nice day'
for i in range(len(st)):
    print('st[%d] : %s'%(i,st[i])) '''

''' st = 'Have a nice day'
arr = st[7:11]
print('st :',st)
print('arr :',arr) '''

''' st = '즐거운 파이썬'
print('st\t:',st)
print('st[0]\t:',st[0])
print('st[1:3]\t:',st[1:3])
print('st[3:]\t:',st[3:]) '''

''' st = 'Have a'
print('변경 전 st :',st)
st += ' nice day'
print('변경 후 st :',st)
print('st * 3 :',st*3)
print('st 길이 :',len(st)) '''

''' st = 'Python is Easy. 그리고 programming 할만하다'
print('st :',st)
print('st.upper() :',st.upper())
print('st.lower() :',st.lower())
print('st.swapcase() :',st.swapcase())
print('st.title() :',st.title()) '''

''' st = 'Have a nice day'
print('st :',st)
print('st 안에 "a"문자 개수 :',st.count('a'))
print('st 안에 "day"문자열 개수 :',st.count('day')) '''

''' st = 'Have a nice day'
print('st :',st)
print('st안에 "day" 위치 :',st.find('day'))
print('st안에 "day" 위치 :',st.index('day'))
print('st안에 "kkk" 위치 :',st.find('kkk'))
print('st안에 "kkk" 위치 :',st.index('kkk')) '''

''' st = 'test1234'
print('st :',st)
print('st.startswith 결과 :',st.startswith('t'))
print('st.startswith 결과 :',st.startswith('k'))
print('st.endswith 결과 :',st.endswith('4'))
print('st.endswith 결과 :',st.endswith('1'))
print('st.endswith 결과 :',st.endswith('t')) '''

''' st = '파이썬파'
print('st\t\t:',st)
print('st.strip("파")\t:',st.strip('파'))
print()
st = '파이썬'
print('st\t\t:',st)
print('st.strip("썬")\t:',st.strip('썬')) '''

''' st = '---파---이---썬---'
print('st\t\t:',st)
print('st.strip("-")\t:',st.strip('-'))
print('st.rstrip("-")\t:',st.rstrip('-'))
print('st.lstrip("-")\t:',st.lstrip('-')) '''

''' st = '즐거운 파이썬 수업'
print('st\t\t:',st)
print('st.replace()\t:',st.replace('즐거운','장난 아니지'))
print('st.replace()\t:',st.replace(st[0],'장난 아니지'))
print('st\t\t:',st) '''

''' st = 'Never ever give up'
print('st\t\t:',st)
print('st.split()\t:',st.split()) '''

''' st = '하나^둘:셋'
print('st\t\t:',st)
print('st.split(":")\t:',st.split(':'))

st = '일:1,이,삼'
print('st\t\t:',st)
print('st.split(",")\t:',st.split(',')) '''

''' st = 'Never ever give up'
print(st)
print('st.splitlines() :',st.splitlines())
st = '하나\n둘\n셋'
print(st)
print('st.splitlines() :',st.splitlines())
st = '하나\n둘셋'
print(st)
print('st.splitlines() :',st.splitlines()) '''

''' st = '%'
print('st.join\t:',st.join('1234'))
st = 'Never ever give up'
print('st.join\t:',st.join('123')) '''

''' st = 'python'
print('st\t\t:',st)
print('st.center(10)\t:',st.center(10))
print('st.center(10,"-"):',st.center(10,'-'))
print('st.ljust(10)\t:',st.ljust(10),st.ljust(10))
print('st.rjust(10)\t:',st.rjust(10),st.rjust(10))
print('st.zfill(10)\t:',st.zfill(10)) '''

''' st = 'python test 1234'
print('st.isdigit() :',st.isdigit())
print('st.isalpha() :',st.isalpha())
print('st.isalnum() :',st.isalnum())
print('st.islower() :',st.islower())
print('st.isupper() :',st.isupper())
print('st.isspace() :',st.isspace()) '''

