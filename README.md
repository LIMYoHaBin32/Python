# Python
## Python Home
print("Hello, World!!!!!!")
##Python Syntax
### Python Indentation
### if 5 > 2:
### print("Five is greater than two!")
### 공백을 넣지 않으면 오류가 발생한다. 일반적으로 4개의 공백이 사용되지만 적어도 하는 있어야 한다. ex)
if 5 > 2:

print("Five is greater than two!") 

if 5 > 2:

print("Five is greater than two!") 
  ### Python Variables 변수에 값을 할당하면 변수가 생성된다.

x = 119

y = "Hello, World!"

###Coment #을 이용해 주석을 달 수 있다. #이것은 주석입니다

###print("Hello, World!!!!!!")

##Python Comments

###주석은 #으로 시작하며 그 뒤는 파이썬에서 무시된다.

###print("Hello, World!!!!!!") # 주석이다

##Python Variables

###x = 20

###y = "Ha Bin"


###print(x)

###print(y)

###다른 유형으로 변수를 설정할 수 있다 (int : 정수형 , str : 문자열)

x = 18       # 정수형으로 작성된 변수

x = "Cally" # 문자열로 작성된 변수

print(x)

문자열,정수형,실수형 등 원하는 데이터 유형으로 지정할 수 있다

x = str(9)    # x will be '9'

y = int(9)    # y will be 9

z = float(9)  # z will be 9.0

type() 함수를 사용하여 변수의 데이터 유형을 도출해낼 수 있다.

x = 19

y = "Tom"

print(type(x))

print(type(y))


위의 경우 아래처럼 데이터 유형이 값으로 나온다.

<class 'int'>

<class 'str'>

문자열 변수는 작은따옴표나 큰땅옵표를 사용하여 작성 가능 변수의 이름은 대소문자를 구분하기 때문에 a,A 처럼 두 개의 변수를 설정할 수 있다.

##Variable Names

변수 이름은 문자나 밑줄 문자로 시작해야 합니다.

변수 이름은 숫자로 시작할 수 없습니다.

변수 이름에는 영숫자와 밑줄(Az, 0-9 및 _)만 포함할 수 있습니다.

변수 이름은 대소문자를 구분합니다(age, Age 및 AGE는 세 가지 다른 변수입니다).

myvar = "HaBin"

my_var = "HaBin"

_my_var = "HaBin"

myVar = "HaBin"

MYVAR = "HaBin"

myvar2 = "HaBin"

여러 변수에 대한 많은 값 한 줄로 여러 변수에 값을 할당할 수 있다.

x, y, z = "Orange", "Banana", "Cherry"


print(x)

print(y)

print(z)

##목록 압축 풀기 :

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)

##Output Variables

##print()함수는 변수를 출력한다.

숫자의 경우 + 문자는 수학 연산자로 작동한다.

x = 1

y = 2

print(x + y)

##함수에서 print()문자열과 숫자를 + 연산자와 결합하려고 하면 Python에서 오류를 표시한다.


x = 5

y = "Tom"

print(x + y)

함수에서 여러 변수를 출력하는 가장 좋은 방법은 print()변수를 쉼표로 구분하는 것이다. 이는 다양한 데이터 유형도 지원한다.

x = 7

y = "HaBin"

print(x, y)

##Python Data Types

문자열 유형: str



숫자(정수,실수) 유형: int, float, complex



시퀀스 유형: list, tuple, range



매핑 유형: dict



세트 유형: set,frozenset



부울 유형: bool



바이너리 유형: bytes, bytearray, memoryview



없음 유형: NoneType

##데이터 유형 가져오기

type()함수를 사용해서 데이터 유형을 가져올 수 있다.

x = 5

print(type(x))

<class 'int'>

##Python Numbers

int 정수



float 실수



complex 복소수

##한 유형에서 다른 유형으로 변환:

x = 1    # int

y = 2.8  # float

z = 1j   # complex



#convert from int to float:

a = float(x)



#convert from float to int:

b = int(y)



#convert from int to complex:

c = complex(x)



print(a)

print(b)

print(c)



print(type(a))

print(type(b))

print(type(c))

##Python Strings

안녕하세요는 안녕하세요와 같다



#변수에 문자열 할당

a = "사랑해"

print(a)

##Strings are Arrays

#위치 1의 문자을 가져온다.(첫 번째 문자의 위치는 0임을 기억할것)

a = "안녕, 반가워

print(a[1])

=녕

#for 루프를 사용하여 문자열의 문자를 반복할 수 있다.

for x in "catia":

  print(x)
  
  ##문자열 길이
  
  #len()함수를 사용
  
  a = "Hello, World!!!!!!"
pr
int(len(a))

=13

##Check String

in과 not in을 사용하여 텍스트에 원하는 단어가 있는지 확인 가능하다

txt = "안녕하세요, 반갑습니다"

print("고마워요" not in txt)

= True

if 명령문을 통해 활용 가능

txt = "안녕하세요, 반갑습니다"

if "고마워요" not in txt:

    print("No, '고마워요' is NOT present.")









