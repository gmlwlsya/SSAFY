# 파이썬 모듈과 패키지 (Python Modules & Packages)

---

## 1. 모듈의 정의

**모듈(Module)** | 한 파일로 묶인 변수와 함수의 모음  
> 특정한 기능을 하는 코드가 작성된 파이썬 파일 (`.py`)

---

## 2. 직접 정의한 모듈 사용하기

* `my_math.py`를 생성하여 두 수의 합을 구하는 `add` 함수를 작성

```python
# my_math.py
def add(x, y):
    return x + y
```

* 같은 위치에 `sample.py` 파일을 생성하고 `my_math` 모듈의 `add` 함수 import 후 `add` 함수 호출

```python
# sample.py
import my_math

print(my_math.add(10, 20))  # 30
```

---

## 3. import 문 사용

* 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
* **`.` (dot) 연산자**: "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라"라는 의미

```python
import math

print(math.pi)       # 모듈명.변수명
print(math.sqrt(4))  # 모듈명.함수명
```

* **단점**: 자칫 코드가 길어질 수 있음

---

## 4. from 절 사용

* 필요한 것만 콕 집어서 가져오는 방식

```python
from math import pi, sqrt

print(pi)       # 변수명
print(sqrt(4))  # 함수명
```

* **실무에서 from 절이 표준인 대표 사례**

```python
from datetime import datetime  # datetime.datetime.now() 는 너무 장황
from collections import Counter
from django.shortcuts import render, redirect
```

---

## 5. import 문과 from 절 비교

| 방식 | 이럴 때 적합 |
| :--- | :--- |
| `import 모듈` | 모듈 이름이 짧고, 어디서 온 함수인지 드러내고 싶을 때 (예: `math.pi`) |
| `from 모듈 import 대상` | 특정 함수/변수를 자주 반복 호출할 때, 모듈 경로가 깊을 때 |

> 💡 **TIP**
> * 둘 중 무엇이 옳고 그른 것이 아니라, **"이 이름의 출처를 코드에 남길 것인가"**를 선택하는 문제입니다.
> * `math.sqrt(4)`는 출처가 보이고, `sqrt(4)`는 간결합니다.
> * 팀 컨벤션에 따르되, 한 파일 안에서는 방식을 통일하는 것이 좋습니다.

---

## 6. import 시 이름 충돌 다루기

* **같은 이름을 두 번 가져오면 나중 것이 이깁니다.**

```python
from math import sqrt     # math.sqrt
from my_math import sqrt  # my_math.sqrt 가 덮어씀

result = sqrt(9)          # my_math.sqrt 가 호출됨
```

---

## 7. 'as' 키워드

* `as` 키워드를 사용하여 **별칭(alias)**을 부여
* 두 개 이상의 모듈에서 동일한 이름의 변수, 함수, 클래스 등을 가져올 때 발생하는 **이름 충돌 해결**

```python
from math import sqrt
from my_math import sqrt as my_sqrt  # 별칭으로 공존

sqrt(4)     # math
my_sqrt(4)  # my_math
```

---

## 8. import * 는 별개의 문제입니다

* 이름 충돌은 `as`로 해결되지만, `*`는 무엇을 가져왔는지 코드에 적혀 있지 않아 충돌이 일어나도 원인을 찾을 수 없음
* 에디터의 자동완성과 코드 검사 도구도 무력해짐

> ➢ `from`은 자유롭게 쓰되, `*` 하나만 피하면 됨

```python
from math import *

e = 300  # math의 자연상수 e가 조용히 사라짐
```

---

## 9. 패키지의 정의

**패키지 (Package)** | 연관된 **모듈**들을 하나의 디렉토리에 **모아 놓은 것**

* 패키지는 이미 누군가가 잘 만들어둔 **코드 꾸러미**라고 생각하면 됩니다.
* 마치 가구를 조립할 때 공구 세트가 있으면 편한 것처럼, 파이썬도 사용자가 모든 기능을 다 만들기 어렵습니다. 그래서 잘 만들어진 유용한 도구(모듈)를 모아서 하나로 묶은 것이 패키지입니다.
* 패키지는 여러 기능을 쉽게 사용할 수 있도록 도와주는 역할을 합니다.


---

## 10. 직접 패키지 만들어 보기

* 다음과 같은 구조로 폴더와 파일을 생성
* `sample.py` 파일을 생성
* `my_package` 폴더를 생성
* `my_package` 폴더 내부에 `math` 폴더와 `statistics` 폴더 생성
* `my_package / math` 폴더 내부에 `my_math.py` 파일 생성 후 다음 코드 작성



```python
# my_package/math/my_math.py
def add(x, y):
    return x + y

```

* `my_package / statistics` 폴더 내부에 `tools.py` 파일 생성 후 다음 코드 작성

```python
# my_package/statistics/tools.py
def mod(x, y):
    return x % y

```

---

## 11. 직접 만든 패키지 사용하기

* `sample.py` 에 다음 코드를 작성해서 실행 결과 확인

```python
# sample.py

from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))    # 출력: 3
print(tools.mod(1, 2))      # 출력: 1

```

> 💡 **TIP**
> * 너무 많은 기능이 한 파일에 몰려 있으면 사용자가 헷갈릴 수 있습니다.
> * 비슷한 기능은 묶고, 관련 없는 것은 나누는 것이 사용하기 편합니다.
> * 폴더/파일 명은 소문자 + 언더스코어(`_`)를 쓰는 게 깔끔하고 표준적입니다.
> 
> 

---

## 12. 패키지 사용 목적

> **패키지 사용 목적**
> * 모듈들의 이름공간(Namespace)을 구분하여 **충돌을 방지**
> * 모듈들을 **효율적으로 관리**하고 사용할 수 있도록 돕는 역할
> 
> 

---

## 13. 라이브러리 > 패키지 > 모듈

```text
Library (라이브러리)
│
└── Package (패키지) = 모듈들을 담은 폴더
    │
    └── Module (모듈) = my_math.py (변수 + 함수)

```

| 단위 | 실체 | 크기 비유 | 예시 |
| --- | --- | --- | --- |
| **모듈** | `.py` 파일 하나 | 책 한 권 | `math`, `random`, `my_math.py` |
| **패키지** | 모듈이 든 폴더 | 책장 하나 | `json`, `email`, `my_package` |
| **라이브러리** | 패키지들의 묶음 | 도서관 | 파이썬 표준 라이브러리 |

---

## 14. 파이썬 표준 라이브러리의 정의

> **파이썬 표준 라이브러리 (Python Standard Library)**
> 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
> 🔗 [https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

---

## 15. 라이브러리의 구성

### 1) 파이썬 표준 라이브러리 (PSL, Python Standard Library)

* 파이썬을 설치하면 자동으로 사용할 수 있는 기본 라이브러리
* 다양한 기능이 들어 있어 복잡한 작업도 쉽게 처리할 수 있음
* `'math'`, `'random'`, `'sys'`(모듈) 및 `'json'`, `'email'`(패키지) 등 다양한 모듈과 패키지가 포함됨
* 별도 설치 없이 바로 `import` 해서 사용 가능

### 2) 파이썬 외부 패키지 (Third-party Packages)

* 필요한 기능을 사용하기 위해 직접 설치해서 쓰는 패키지
* 전 세계 개발자들이 만든 다양한 패키지들이 존재
* **예시:** 엑셀 파일 조작(`pandas`, `openpyxl`) / 데이터 시각화(`matplotlib`) / 웹 데이터 수집(`requests`) 등


* 사용할 패키지를 설치할 때는 `pip` 명령어를 사용

---

## 16. pip 란?

> **pip**
> 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
> 🔗 [https://pypi.org/](https://pypi.org/)
> **PyPI(Python Package Index)**에 저장된 외부 패키지들을 설치하는 것입니다.
> 직접 만든 패키지도 이곳에 등록해서 배포할 수 있습니다.

---

## 17. 패키지 설치

* 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음

```bash
$ pip install SomePackage
$ pip install SomePackage==1.0.5
$ pip install SomePackage>=1.0.4

```

> 💡 **TIP**
> * 다양한 패키지 버전이 존재하기 때문에 개발 시 호환성 이슈가 생기지 않는지 확인이 필요합니다.
> * 설치한 패키지는 `pip freeze > requirements.txt` 명령어로 버전 정보를 기록해 두는 것이 좋습니다.
> * `requirements.txt` 파일은 협업 시 개발 환경을 통일하는 데 큰 도움이 됩니다.
> 
> 

---

## 18. requests 외부 패키지 설치 및 사용 예시

### 1) requests 패키지

* 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 외부 패키지

### 2) pip 를 통해 requests 패키지를 설치

```bash
$ pip install requests

```

### 3) requests 를 import 하여 웹에 데이터 요청

```python
import requests

# 공휴일 정보 API
url = "https://date.nager.at/api/v3/publicholidays/2025/KR"
response = requests.get(url).json()
print(response)

```

> 💡 **참고 메서드 설명**
> * `.get(url)`: 주어진 url로 요청하는 requests 패키지 메서드
> * `.json()`: 응답 본문(문자열)에 담긴 JSON 데이터를 대응하는 Python 객체(`dict`, `list` 등)로 변환해주는 requests 응답(`Response`) 객체의 메서드
> 
> 
> ※ 메서드는 OOP에서 진행



---

# 제어문 (Control Statement)

코드의 실행 흐름을 제어하는 데 사용되는 구문입니다. **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행합니다.

---

## 1. 조건문과 반복문의 개요

### 조건문

* `if`, `elif`, `else`

```python
if score >= 90:
    message = "축하합니다! 최고입니다!"
elif score >= 70:
    print("멋져요! 잘하셨어요!")
else:
    print("조금 더 노력해보세요!")

```

### 반복문

* **for 반복**
```python
for i in range(3):
    print('반짝')

```


* **while 반복**
```python
count = 1

while count <= 3:
    print(count)
    count = count + 1

print('끝')

```



---

## 2. 조건문 (Conditional Statement)

주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜁니다.

### 조건문의 기본 구조

#### `if` 문

* 조건문의 기본 형태
* `if` 문에 작성된 조건을 만족할 때 내부 코드 실행
* 작성되는 조건은 **표현식**(하나의 '값'으로 평가될 수 있는 모든 코드)으로 작성

#### `elif` 문

* 이전의 조건을 만족하지 못하고 추가로 다른 조건이 필요할 때 사용
* 여러 개의 `elif` 문을 사용할 수 있음

#### `else` 문

* 모든 조건들을 만족하지 않으면 실행됨

```python
# 조건 작성은 반드시 표현식

if 조건1:
    조건1을 만족할 때 실행할 코드
elif 조건2:
    조건2를 만족할 때 실행할 코드
elif 조건3:
    조건3을 만족할 때 실행할 코드
else:
    모든 조건을 만족하지 않으면 실행할 코드

```

---

## 3. 조건문의 네 가지 형태

### ① `if` 단독 — 특정 상황에만 무언가를 덧붙일 때

* 조건이 거짓이면 그냥 넘어감
* `else`가 필요 없는 가장 흔한 형태

```python
temperature = 33

if temperature >= 30:
    print('폭염 주의보')

print('오늘 기온:', temperature)

```

**[출력 결과]**

```text
폭염 주의보
오늘 기온: 33

```

### ② `if-else` — 반드시 둘 중 하나

```python
age = 17

if age >= 19:
    print('입장 가능')
else:
    print('입장 불가')

```

### ③ `if-elif` (`else` 없음)

* 해당 없으면 아무 일도 안 함

```python
rank = 5

if rank == 1:
    print('금메달')
elif rank == 2:
    print('은메달')
elif rank == 3:
    print('동메달')

print('경기 종료')

```

**[출력 결과]**

```text
경기 종료

```

### ④ `if-elif-else` — 모든 경우를 빠짐없이 처리

```python
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(grade)  # B

```

---

## 4. 독립 `if` 여러 개 vs `elif`

> 같아 보이지만 결과가 완전히 다릅니다.

### A. 독립된 `if` 세 개

```python
score = 95

# 독립된 if 세 개
if score >= 60:
    print('합격')
if score >= 80:
    print('우수')
if score >= 90:
    print('최우수')

```

**[출력 결과]**

```text
합격
우수
최우수

```

### B. `if - elif` 로 연결

```python
score = 95

# if - elif 로 연결
if score >= 60:
    print('합격')
elif score >= 80:
    print('우수')
elif score >= 90:
    print('최우수')

```

**[출력 결과]**

```text
합격

```

---

## 5. 중첩 조건문

* 조건문(`if`) 내부에 또 다른 조건문(`if`) 작성 가능

```python
dust = 480  # 출력: 매우 나쁨 / 위험해요! 나가가지 마세요!

if dust > 150:
    print('매우 나쁨')
    
    # 중첩된 조건문
    if dust > 300:
        print('위험해요! 나가가지 마세요!')

elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

```


---

# 반복문 (Loop Statement)

주어진 코드 블록을 여러 번 반복해서 실행하는 구문입니다.

---

## 1. 반복문의 종류

### `for` 문

* 반복 가능(iterable)한 객체의 요소들을 반복하는 데 주로 사용
* 주로 반복 가능(iterable)한 객체 요소의 개수만큼 반복
* **특징:** 반복 횟수가 정해져 있음

```python
student_list = ['Alice', 'Bob', 'Charlie']

for student in student_list:
    print(f"Hello, {student}!")

```

### `while` 문

* `while` 조건이 참(True)인 동안 반복
* 반복 횟수가 정해지지 않은 경우 주로 사용

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1

print('끝')

```

**[출력 결과]**

```text
1
2
3
끝

```

---

## 2. for 반복문

반복 가능한(iterable) 객체의 요소들을 반복하는 데 사용되며, 반복 가능한 객체의 요소 개수만큼 반복이 수행됩니다.

### 기본 구문

```python
for 변수 in 반복 가능 객체:
    코드 블록

```

---

## 3. 반복 가능한 객체 (iterable)

요소를 하나씩 반환할 수 있는 모든 객체 (반복문에서 순회할 수 있는 객체)

> **💡 시퀀스 자료형:** 요소가 순서대로 나열된 자료형
> ※ 시퀀스 자료형(`list`, `tuple`, `str`)뿐만 아니라 비시퀀스 자료형(`dict`, `set`) 등도 반복 가능한 객체입니다.

---

## 4. for문 작동 원리와 주요 순회 패턴

### for문 작동 원리

* 리스트 내 첫 항목이 반복 변수(`item`)에 할당되고 코드 블록이 실행됨
* 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드 블록이 다시 실행됨
* ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드 블록이 실행됨
* 더 이상 반복 변수에 할당할 값이 없으면 반복 종료

> ※ **팁:** 반복 변수는 단수형으로 작성하는 것을 권장합니다.

```python
item_list = ['apple', 'banana', 'coconut']

for item in item_list:  # item: 반복 변수
    print(item)

# 출력 결과:
# apple
# banana
# coconut

```

### 문자열 순회

* 문자열은 문자로 구성된 시퀀스 자료형
* 문자열 반복 시 문자가 반복 변수에 할당되어 반복 수행

```python
country = 'Korea'

for char in country:
    print(char)

# 출력 결과:
# K
# o
# r
# e
# a

```

### range 순회

* 특정 숫자 범위만큼 반복을 하고 싶을 때 `range` 함수를 사용

```python
for i in range(5):
    print(i)

```

### 딕셔너리 순회

* `dict` 자료형은 비시퀀스 자료형으로 반복 순서가 보장되지 않음에 유의

```python
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])

# 출력 결과:
# x
# 10
# y
# 20
# z
# 30

```

---

## 5. 인덱스로 리스트 순회 및 중첩 반복문

### 인덱스로 리스트 순회

* 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
* 인덱스를 사용하면 리스트의 원하는 위치에 있는 값을 읽거나 변경할 수 있음

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]

```

### 중첩된 반복문 (1/2)

* 중첩된 반복문에서의 출력 예상해보기

```python
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 출력 결과:
# A c
# A d
# B c
# B d

```
---

# 파이썬 제어문: 반복문 (Loop Statement)

---

## 1. 중첩 리스트 순회 (Nested List Iteration)

안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회합니다.

### 1-1. 바깥 리스트 순회 (1차원)

```python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)

# 출력 결과:
# ['A', 'B']
# ['c', 'd']

```

### 1-2. 중첩 반복을 통한 요소 순회 (2차원)

```python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)

# 출력 결과:
# A
# B
# c
# d

```

---

## 2. while 반복문

주어진 조건식이 참(True)인 동안 코드를 반복해서 실행하며, 조건식이 거짓(False)이 될 때까지 반복을 수행합니다.

### 기본 구문

```python
while 조건식:
    코드 블록

```

### while문의 반복 원리

1. **while의 조건식 확인:**
* 조건식이 참(True)이면 코드 블록 실행
* 조건식이 거짓(False)이면 반복 종료


2. 코드 블록 실행이 마무리되면 다시 while 조건식 확인

### 활용 예시

#### 예시 1: 기본 반복

```python
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

# 출력 결과:
# 0
# 1
# 2
# 끝

```

#### 예시 2: 사용자 입력에 따른 반복

```python
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

# [실행 예시]
# 양의 정수를 입력해주세요.: 0
# 0은 양의 정수가 아닙니다.
# 양의 정수를 입력해주세요.: -1
# 음수를 입력했습니다.
# 양의 정수를 입력해주세요.: 1
# 잘했습니다!

```

### while문의 특징 및 주의사항

> **⚠️ 반드시 종료 조건이 필요**
> 종료 조건이 없는 경우 **무한 반복**에 빠지게 되어 원하는 동작을 하지 않게 되므로 반드시 종료 조건을 설정해야 합니다.

* **TIP:**
* 조건이 언젠가는 반드시 `False`가 되도록 반복문 내부에서 변수 값을 변화시켜야 합니다.
* `while`문을 시작하기 전에 조건에서 사용할 변수를 반드시 초기화해야 오류를 방지할 수 있습니다.
* 예상치 못한 상황에 대비해 `break`문을 활용하면 반복문을 안전하게 종료할 수 있습니다.



---

## 3. for 반복문 vs while 반복문 비교

| 구분 | for 반복문 | while 반복문 |
| --- | --- | --- |
| **작동 방식** | iterable 요소를 하나씩 순회하며 반복 | 주어진 조건식이 참(True)인 동안 반복 |
| **유용한 상황** | **반복 횟수가 명확하게 정해져 있는 경우**<br>

<br>• 리스트, 튜플, 문자열 등 시퀀스 형식 처리<br>

<br>• `range()` 함수를 사용해 일정 횟수 반복 작업 수행 | **반복 횟수가 불명확하거나 조건에 따라 종료해야 할 경우**<br>

<br>• 사용자 입력을 받아 특정 조건이 충족될 때까지 반복<br>

<br>• 특정 조건이 만족될 때까지 반복해야 하는 경우 |

> **💡 TIP:**
> * 문제의 반복 조건과 목적에 따라 더 적합한 반복문을 선택하는 것이 중요합니다.
> * 필요하다면 두 반복문을 중첩하거나 상황에 따라 자유롭게 바꿔 쓸 수 있습니다.
> * 한 가지 방식에만 얽매이지 않고 다양한 문제에 맞게 융통성 있게 활용하는 것이 좋습니다.
> 
> 

---

## 4. 반복 제어 (Loop Control)

`for`문과 `while`문은 매 반복마다 본문 내 모든 코드를 실행하지만, 때때로 일부만 실행하는 것이 필요할 때 제어 키워드를 사용합니다.

### 4-1. 제어 키워드 종류

* **`break`:** 해당 키워드를 만나게 되면 남은 코드를 무시하고 **반복을 즉시 종료** (반복을 끝내야 할 명확한 조건이 있을 때 사용)
* **`continue`:** 해당 키워드를 만나게 되면 다음 코드는 무시하고 **다음 반복을 수행**

```python
# break 예시
for i in range(10):
    if i == 5:
        break
    print(i)  # 출력: 0 1 2 3 4

# continue 예시
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 출력: 1 3 5 7 9

```

### 4-2. 상세 활용 예시

#### break 예시 (1): 리스트에서 첫 번째 짝수만 찾은 후 반복 종료

```python
numbers = [1, 3, 5, 6, 7, 9, 10, 11]

for num in numbers:
    print('확인 중...', num)
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        break

# 출력 결과:
# 확인 중... 1
# 확인 중... 3
# 확인 중... 5
# 확인 중... 6
# 첫 번째 짝수를 찾았습니다: 6

```

#### break 예시 (2): 프로그램 종료 조건 만들기

```python
number = int(input('양의 정수를 입력해주세요. (종료: 0): '))

while number <= 0:
    if number == 0:
        print('프로그램을 종료합니다.')
        break
    print('음수는 입력할 수 없습니다.')
    number = int(input('양의 정수를 입력해주세요. (종료: 0): '))

print('반복문을 빠져나왔습니다.')

```

#### continue 예시: 리스트에서 홀수만 출력하기

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# 출력 결과:
# 1
# 3
# 5
# 7
# 9

```

> **💡 TIP:**
> * 반복 제어문은 반드시 반복문 내에서만 사용해야 합니다.
> * 중첩 반복문인 경우 해당 키워드가 작성된 **코드 블록의 반복 흐름만 제어**한다는 것을 잊지 마세요.
> * 과도하게 사용하면 가독성이 떨어지므로 필요한 상황에서만 사용하는 것이 좋습니다.
> 
> 

---

## 5. 빈 코드 블록 키워드 (`pass`)

'아무 동작도 하지 않음'을 명시적으로 나타내는 키워드입니다.

* 반복 제어가 아닌 **코드를 틀을 유지하거나 나중에 내용을 채우기 위한 용도**로 사용합니다.
* 코드를 비워두면 구문 오류(IndentationError 등)가 발생하기 때문에 `pass` 키워드를 사용합니다.
* 반복문뿐만 아니라 함수, 조건문에서도 사용 가능합니다.

```python
# 1. 반복문 및 조건문에서 예시
while True:
    if condition1:
        break
    elif condition2:
        pass  # 빈 코드를 의미
    else:
        print('출력')

# 2. 조건문 구조 잡기
if condition:
    pass  # 아무런 동작도 수행하지 않음
else:
    pass  # 구조를 잡을 뿐

# 3. 함수 정의 시 틀 잡기
def my_function():
    pass  # 없으면 오류 발생

```


---

## 1. map 함수

### 개념

`map(function, iterable)`

* 반복 가능한 데이터구조(iterable)의 모든 요소에 **function**을 적용하고, 그 결과 값들을 **map object**로 묶어서 반환합니다.

> **💡 map object**
> 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형. 전체 값을 확인하려면 `list`나 `tuple`로 형변환을 해줘야 함.

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)        # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']

```

---

### map 함수 활용 1: SWEA 문제 등 입력 처리 예시

SWEA 문제의 input 처럼 문자열 `'1 2 3'`이 입력 되었을 때 활용 예시:

```python
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]

```

> **💡 split 메서드**
> 문자열을 지정한 기준 문자(기본은 공백)를 기준으로 잘라서, 잘린 문자들을 리스트로 반환해주는 문자열 메서드.

> **TIP**
> * 입력이 `'1 2 3'`과 같이 공백으로 구분되어 있는지, `'123'`처럼 연속된 문자형태인지 확인을 잘해주세요.
> * 만약 문자열이 공백으로 구분된다면 문자열의 `split()` 메서드를 통해 분리해서 `map` 함수에 넣어야 해요.
> * 만약 `'123'`과 같이 연속된 문자 형태이면 `split()` 하지 않고 문자열 그대로 `map` 함수에 넣어야 해요.
> 
> 

---

### map 함수 활용 2 (with 람다 표현식)

```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x ** 2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]

```

---

## 2. 파이썬의 조금 특별한 문법, `for-else`

### 개념

* `for` 루프가 `break`를 만나 중단되지 않고, **끝까지 정상적으로 완료되었을 때만** `else` 블록이 실행됩니다.
* `break` 문을 만나 반복문이 종료되면 `else`의 코드 블록은 실행되지 않습니다.

```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print('짝수를 찾았습니다:', num)
        break
else:
    # break 없이 끝까지 돌았을 때만 실행
    print('짝수를 찾지 못했습니다')

```

**# 출력**

```text
짝수를 찾지 못했습니다.

```

> **TIP**
> * `for-else` 문의 경우 `if-else` 문과 혼동되지 않도록 작성해야 해요.
> * 모든 반복을 정상적으로 수행해야 `else` 블록이 실행되므로 검색, 검증 로직에서 활용해요.
> * `while-else` 문도 존재하며, 동작 규칙도 `for-else`와 동일하게 `break`로 반복이 종료되는 경우 `else` 블록이 실행되지 않아요.
> 
> 

---

### for-else 예시 1: 중복 아이디를 찾았을 경우

*(break 실행 → else 실행 안 됨)*

* `id_to_check`와 동일한 `'guest'`를 목록에서 발견하는 순간 `break`가 실행되어 `for` 루프가 중간에 멈춤
* 따라서 `else` 블록은 실행되지 않음

```python
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest'  # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break  # 중복 아이디를 찾았으므로 확인 절차를 중단
else:
    # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
    print('사용 가능한 아이디입니다.')

print('아이디 확인 절차를 종료합니다.')

```

**# 출력**

```text
이미 사용 중인 아이디입니다.
아이디 확인 절차를 종료합니다.

```

---

### for-else 예시 2: 중복 아이디를 찾지 못한 경우

*(break 실행 안 됨 → else 실행됨)*

* `'new_user'`는 `registered_ids` 목록 끝까지 확인해도 존재하지 않음
* `for` 루프가 모든 항목을 확인한 뒤 정상적으로 종료되었으므로, `else` 블록이 실행

```python
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'new_user'  # 리스트에 없는 새로운 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break
else:
    # for 루프가 break 없이 마무리 되어 else 블록 실행
    print('사용 가능한 아이디입니다.')

```

**# 출력**

```text
사용 가능한 아이디입니다.

```

---

## 3. enumerate 함수

### 개념

`enumerate(iterable, start=0)`

* iterable 객체의 각 요소에 대해 **인덱스와 값을 함께 반환**하는 내장함수.

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

```

**# 출력**

```text
0 apple
1 banana
2 cherry

```

---

### enumerate 함수 활용

#### 1) enumerate의 index 정보를 이용해 넘버링으로 사용

* `start`에 시작 값을 설정할 수 있음

```python
movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']

for idx, title in enumerate(movies, start=1):
    print(f"{idx}위: {title}")

```

**# 출력**

```text
1위: 인터스텔라
2위: 기생충
3위: 인사이드 아웃
4위: 라라랜드

```

#### 2) 인덱스 정보를 이용해 요소의 위치를 확인할 수 있음

```python
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")

```

**# 출력**

```text
은지 미제출
소민 미제출

```

---

## 4. zip 함수

### 개념

`zip(*iterables)`

* zip 함수는 여러 개의 반복 가능한 데이터 구조를 묶어서, **같은 위치에 있는 값들을 하나의 tuple로 만든 뒤** 그것들을 모아 **zip object**로 반환하는 함수.

> **💡 zip object**
> 짝지어진 결과(tuple)를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형. 전체 값을 확인하려면 `list`나 `tuple`로 형변환을 해줘야 함.

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)        # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

```

---

### zip 함수 활용 1: 여러 개의 리스트를 동시에 조회할 때

```python
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

```

**# 출력**

```text
(10, 20, 40)  # 0번 인덱스 값
(20, 40, 20)  # 1번 인덱스 값
(30, 50, 30)  # 2번 인덱스 값
(50, 70, 50)  # 3번 인덱스 값

```

> **TIP**
> * 반복 가능한 자료형의 길이가 다른 경우 **가장 짧은 길이를 기준**으로 묶어서 반환해요.
> * 반드시 반복 가능한 자료형만 인자로 넣을 수 있어요.
> * zip object는 언패킹을 활용하여 변수에 바로 tuple 요소를 할당할 수 있어요.
> 
> 

---

### zip 함수 활용 2: 2차원 리스트의 같은 컬럼(열) 요소를 동시에 조회할 때

* 실행 결과가 **전치 행렬**과 동일함

> **💡 전치 행렬**
> $(i, j)$의 값을 $(j, i)$ 위치로 옮긴 행렬. 즉, 행을 열로, 열을 행으로 뒤집은 행렬.

```python
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)

```

**# 출력**

```text
(10, 40, 20)
(20, 50, 40)
(30, 39, 50)

```