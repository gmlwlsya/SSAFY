## 1. 데이터 구조 (Data Structure)

### 개념

* **데이터 구조**: 여러 데이터를 효과적으로 사용·관리하기 위한 구조 (`str`, `list`, `dict` 등)
* **자료구조**: 컴퓨터 공학에서는 '자료 구조'라고 함
* 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것
* 단순히 데이터를 묶는 것을 넘어, 프로그램의 성능과 효율성, 유지보수성에 큰 영향을 미치는 핵심적인 개념

---

## 2. 공통 시퀀스 메서드

| 메서드 | 설명 |
| --- | --- |
| **`s.index(x)`** | 시퀀스 s에서 첫 번째로 일치하는 항목 x의 인덱스를 반환. 없으면 `ValueError` 발생 |
| **`s.count(x)`** | 시퀀스 s에서 등장하는 항목 x의 개수를 반환 |

### `.index(x)`

* 시퀀스에서 첫 번째로 일치하는 항목 x의 인덱스를 반환

```python
text = 'banana'
print(text.index('a'))  # 1

my_list = [1, 2, 3]
print(my_list.index(2))  # 1

```

### `.count(x)`

* 시퀀스에서 항목 x의 개수를 반환

```python
text = 'banana'
print(text.count('a'))  # 3

my_list = [1, 2, 2, 3, 3, 3]
print(my_list.count(3))  # 3

```

---

## 3. 문자열 탐색 및 검증 메서드 (불변 시퀀스)

| 메서드 | 설명 |
| --- | --- |
| **`s.find(x)`** | x의 첫 번째 위치를 반환. 없으면 `-1`을 반환 |
| **`s.isupper()`** | 문자열 내의 모든 케이스 문자가 대문자인지 확인 |
| **`s.islower()`** | 문자열 내의 모든 케이스 문자가 소문자인지 확인 |
| **`s.isalpha()`** | 문자열의 모든 문자가 알파벳이고 하나 이상의 문자가 포함되어 있으면 `True`를 반환<br>

<br>*(단순 알파벳이 아닌 유니코드 상 Letter(한국어 포함))* |

### `.find(x)`

* x의 첫 번째 위치를 반환. 없으면 `-1`을 반환
* x의 위치를 알아야 할 경우에 사용



```python
print('banana'.find('a'))  # 1
print('banana'.find('z'))  # -1

```

### `.isupper()`, `.islower()`

* 문자열 내의 모든 케이스 문자가 대문자/소문자로 이루어져 있는지 확인

```python
string1 = 'HELLO'
string2 = 'Hello'

print(string1.isupper())  # True
print(string2.isupper())  # False
print(string2.islower())  # False
print(string1.islower())  # False

```

### `.isalpha()`

* 문자열이 비어 있지 않고, 모든 글자가 문자(letter)일 때만 `True`를 반환

```python
string1 = 'Hello'
string2 = '123heis98576ssh'

print(string1.isalpha())  # True
print(string2.isalpha())  # False

```

> **※ 참고**
> 여기서 '문자'는 영문 알파벳뿐 아니라 한글·한자 등 유니코드상 문자로 분류되는 모든 글자를 포함합니다. 숫자, 공백, 특수문자가 하나라도 섞이면 `False`입니다.

---

## 4. 문자열 조작 메서드 (새로운 문자열 반환)

> **💡 Iterable**
> 순서대로 꺼내 쓸 수 있는 데이터들의 묶음

| 메서드 | 설명 |
| --- | --- |
| **`str.replace(old, new[, count])`** | 기존 문자열에서 "old"라는 부분 문자열이 "new"로 모두 바뀐 문자열을 반환 |
| **`str.strip([chars])`** | 선행과 후행 문자가 제거된 문자열의 복사본을 돌려줌 |
| **`str.split(sep=None, maxsplit=-1)`** | sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환 |
| **`str.join(iterable)`** | 구분자로 iterable의 문자열을 연결한 문자열을 반환 |
| **`str.capitalize()`** | 가장 첫 번째 글자를 대문자로 변경 |
| **`str.title()`** | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환 |
| **`str.upper()`** | 모두 대문자로 변경 |
| **`str.lower()`** | 모두 소문자로 변경 |
| **`str.swapcase()`** | 대 ↔ 소문자 서로 변경 |

### `.replace(old, new[, count])`

* 기존 문자열에서 "old"라는 부분 문자열이 "new"로 모두 바뀐 문자열을 반환

```python
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)

print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world

```

### `.strip([chars])`

* 선행과 후행 문자가 제거된 문자열의 복사본을 돌려줌
* `chars` 인자는 제거할 문자 집합을 지정하는 문자열
* 생략되거나 `None` 이라면, `chars` 인자의 기본값은 공백을 제거

```python
# 사용자 입력 등에서 불필요한 공백이 포함된 경우
text = '   Hello World   '

# 1. 아무것도 지정하지 않으면 '공백(띄어쓰기, 탭, 엔터)'을 제거
clean_text = text.strip()
print(clean_text)  # 'Hello World'
# (주의: 문자열 중간의 공백은 제거되지 않음)

# 2. 제거할 문자를 지정하는 경우
text = '!!!Hello World!!!'
print(text.strip('!'))  # 'Hello World'

# [심화] 문자열 집합으로 제거 (순서 상관 없음)
# 'w', '.', 'c', 'o', 'm' 중 하나라도 양쪽 끝에 있으면 계속 제거
url = 'www.example.com'
print(url.strip('w.com'))  # 'example'
# (왼쪽의 'www.' 과 오른쪽의 '.com' 이 모두 제거됨)

```

### `.split(sep=None, maxsplit=-1)`

* `sep`를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환
* `maxsplit` 이 주어지면 최대 `maxsplit` 번의 분할이 수행됨
* `sep`이 지정되지 않거나 `None` 이면, 연속된 공백 문자는 단일한 구분자로 간주하고, 문자열이 선행이나 후행 공백을 포함해도 결과는 시작과 끝에 빈 문자열을 포함하지 않음

```python
# 1. 공백을 기준으로 분리 (기본 동작)
# 여러 개의 공백도 하나로 처리하며, 앞뒤 공백은 무시함
text = '   Hello   Python   '
print(text.split())  # ['Hello', 'Python']

# 2. 특정 문자를 기준으로 분리
# 지정한 문자를 기준으로 '엄격하게' 분리함 (빈 문자열 발생 가능)
data = '10,20,,30'
print(data.split(','))  # ['10', '20', '', '30']

# 3. 분할 횟수 제한 (maxsplit)
# 앞에서부터 1번만 자르고 나머지는 그대로 둠
path = 'User/admin/documents'
print(path.split('/', maxsplit=1))  # ['User', 'admin/documents']

```

### `.join(iterable)`

* `iterable`의 문자열을 연결한 문자열을 반환

```python
words = ['Python', 'is', 'awesome']

sentence1 = ' '.join(words)
sentence2 = '-'.join(words)

print(sentence1)  # Python is awesome
print(sentence2)  # Python-is-awesome

```

### 기타 문자열 조작 메서드

```python
text = 'heLLo, woRld!'

new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.lower()
new_text5 = text.swapcase()

print(new_text1)  # Hello, world!
print(new_text2)  # Hello, World!
print(new_text3)  # HELLO, WORLD!
print(new_text4)  # hello, world!
print(new_text5)  # HELLO, WOrLD!

```

---

## 5. 가변 시퀀스 메서드 (리스트 값 추가 및 삭제)

| 메서드 | 설명 |
| --- | --- |
| **`L.append(x)`** | 리스트 마지막에 항목 x를 추가 |
| **`L.extend(iterable)`** | Iterable의 모든 항목들을 리스트 끝에 추가 (`+=`와 같은 기능) |
| **`L.insert(i, x)`** | 리스트 인덱스 i에 항목 x를 삽입 |
| **`L.remove(x)`** | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 (항목이 존재하지 않을 경우 `ValueError` 발생) |
| **`L.pop()`** | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거 |
| **`L.pop(i)`** | 리스트의 인덱스 i에 있는 항목을 반환 후 제거 |
| **`L.clear()`** | 리스트의 모든 항목 제거 |

### `.append(x)`

* 리스트 마지막에 항목 x를 추가

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

```

### `.extend(iterable)`

* 리스트에 다른 반복 가능한 객체의 모든 항목을 추가

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

```

> **⚠️ extend 주의사항**
> * **`append()`와의 비교**:
> ```python
> my_list = [1, 2, 3, 4, 5, 6]
> my_list.append([5, 6, 7])
> print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]
> 
> ```
> 
> 
> * **반복 가능한 객체(iterable)가 아니면 추가 불가**:
> ```python
> my_list.extend(100)
> # TypeError: 'int' object is not iterable
> 
> ```
> 
> 
> 
> 

### `.insert(i, x)`

* x를 지정한 인덱스 i 위치에 삽입

```python
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

```

### `.remove(x)`

* 리스트에서 첫 번째로 일치하는 항목을 삭제

```python
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

```

### `.pop()` 또는 `.pop(i)`

* 리스트에서 지정한 인덱스의 항목을 제거하고 반환
* 작성하지 않을 경우 **마지막 항목을 제거**

```python
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)    # 5
print(item2)    # 1
print(my_list)  # [2, 3, 4]

```

### `.clear()`

* 리스트의 모든 항목을 제거

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []

```

---

## 6. 리스트 정렬 및 순서 변경 (뒤집기) 메서드

| 문법 | 설명 |
| --- | --- |
| **`L.reverse()`** | 리스트의 순서를 역순으로 변경 (정렬 X) |
| **`L.sort()`** | 리스트를 정렬 (매개변수 이용가능) |

### `.reverse()`

* 리스트의 순서를 **역순으로 변경(정렬 X)**

```python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()

print(my_list.reverse())  # None (반환값이 없음)
print(my_list)            # [9, 1, 8, 2, 3, 1]

```

### `.sort()`

* 원본 리스트를 오름차순 또는 내림차순으로 정렬

```python
# 1. 오름차순 정렬
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# 2. 내림차순 정렬
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]

```

---

## 7. 가변/불변 객체와 메모리 참조

> 객체 복사의 핵심을 파악하려면, 파이썬 자료구조의 **가변(Mutable)**과 **불변(Immutable)** 두 가지 종류를 살펴봐야 합니다.

### 개념 분류

* **Mutable(가변) 객체**: 생성 후 내용을 변경할 수 있는 객체
* 예: `list`, `dict`, `set`


* **Immutable(불변) 객체**: 생성 후 내용을 변경할 수 없는 객체
* 예: `int`, `float`, `str`, `tuple`



### 변수 할당의 의미

* 파이썬에서 변수 할당은 **객체에 대한 참조(메모리 주소)를 생성하는 과정**
* 변수는 객체의 메모리 주소를 가리키는 **Label 역할**을 함
* `'='` 연산자를 사용하여 변수에 값을 할당할 때:
* **새로운 객체 생성 후 참조**: 할당되는 값이 새로운 객체일 경우 메모리에 만들고 변수가 가리키게 함
* **기존 객체에 대한 참조**: 이미 메모리에 존재하는 객체를 할당하면 새로운 객체를 만들지 않고 참이지만 생성함



### 가변 객체 예시

* 생성 후 내용을 변경할 수 있는 객체 (`list`)

```python
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)       # [100, 2, 3, 4]
print(b)       # [100, 2, 3, 4]
print(a is b)  # True (동일한 메모리 주소를 참조함)

```

### 불변 객체 예시

* 생성 후 내용을 변경할 수 없는 객체 (`int`)

```python
a = 20
b = a
b = 10

print(a)       # 20
print(b)       # 10
print(a is b)  # False (b에 새 값을 할당하는 순간 새로운 객체를 참조함)

```

### `id()` 함수를 사용한 메모리 주소 확인

* `id()` 함수를 사용하여 객체의 메모리 주소를 확인 가능
* `is` 연산자를 통해 두 변수가 같은 객체를 참조하는지 확인 가능

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')  # 예: 1682231207424
print(f'y의 id: {id(y)}')  # 예: 1682231207424
print(f'z의 id: {id(z)}')  # 예: 1682231224896

print(f'x와 y는 같은 객체인가? {x is y}')  # True
print(f'x와 z는 같은 객체인가? {x is z}')  # False

```

### 가변/불변 메모리 관리 방식과 이유

#### 1. 메모리 관리 방식

* **가변 객체**: 생성 후에도 그 내용을 수정할 수 있으며, 객체의 내용이 변경되어도 같은 메모리 주소를 유지함
* **불변 객체**: 생성 후 그 값을 변경할 수 없으며, 새로운 값을 할당하면 새로운 객체가 생성되고 변수는 새 객체를 참조하게 됨

#### 2. 메모리 관리 방식의 이유

* **성능 최적화**
* **가변 객체**: 내용 수정이 빈번할 때, 새로운 객체를 생성하는 대신 기존 객체를 직접 수정하여 객체 생성 및 삭제에 드는 비용을 절감함
* **불변 객체**: 변경이 불가능하므로, 여러 변수가 동일한 객체를 안전하게 공유할 수 있음


* **메모리 효율성**
* **가변 객체**: 크기가 큰 데이터를 효율적으로 수정할 수 있음
* **불변 객체**: 동일한 값을 가진 여러 변수가 같은 객체를 참조할 수 있어 메모리 사용을 최소화할 수 있음


---

## 8. 얕은 복사 (Shallow Copy)

### 개념

* 객체의 최상위 요소만 새로운 메모리에 복사하는 방법
* 내부에 **중첩된 객체**가 있다면 그 객체의 참조만 복사됨

> **💡 TIP: 얕은 복사의 함정, '가변 객체'**
> * 얕은 복사 후 중첩된 리스트나 딕셔너리 같은 가변 객체를 수정하면, **원본 객체와 복사본 객체가 함께 변경**됩니다.
> * 이는 복사본의 중첩 객체가 여전히 원본 객체의 중첩 객체를 참조하고 있기 때문입니다.
> 
> 

### 얕은 복사 구현 방법 3가지

1. **리스트 슬라이싱** (`[:]`)
2. **`copy()` 메서드**
3. **`list()` 함수**

#### 1. 리스트 슬라이싱

* 1차원 리스트에서의 얕은 복사
* 리스트 슬라이싱 `[:]`은 원본 리스트와 동일한 내용의 **새로운 리스트**를 만듭니다.
* 이때 새로운 리스트에 복사되는 것은 요소 자체의 값이 아니라 해당 요소들이 참조하는 주소입니다.

```python
a = [1, 2, 3]
b = a[:]

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

print(a is b)  # False (최상위 리스트 자체는 서로 다른 객체)

```

#### 2. `copy()` 메서드

* `list.copy()`는 원본 리스트와 동일한 내용을 가진 **새로운 리스트 객체**를 반환합니다.
* 슬라이싱과 마찬가지로 복사된 새 리스트의 요소들은 원본 리스트의 요소들과 **동일한 객체들을 참조**합니다.

```python
a = [1, 2, 3]
b = a.copy()

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

print(a is b)  # False

```

#### 3. `list()` 함수

* `list()` 형변환 함수를 통해서도 얕은 복사본을 만들 수 있습니다.

```python
a = [1, 2, 3]
b = list(a)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

print(a is b)  # False

```

### 얕은 복사의 한계 (다차원 리스트)

* 2차원 리스트와 같이 **변경 가능한 객체 안에 변경 가능한 객체가 있는 경우**, `a`와 `b`의 주소는 다르지만 **내부 객체의 주소는 같기 때문에 함께 변경**됩니다.

```python
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]] -> 1차원 요소 변경은 영향을 주지 않음
print(b)  # [999, 2, [3, 4, 5]]

# 중첩된 내부 리스트의 요소를 변경하는 경우
b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]] -> 원본도 함께 변경됨!
print(b)  # [999, 2, [3, 100, 5]]

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True

```

#### 1차원 vs 다차원 리스트 차이점

* **1차원 리스트**: 얕은 복사만으로도 충분히 독립적인 복사본을 만들 수 있음
* **다차원 리스트**: 최상위 리스트만 복사되고, **내부 리스트는 여전히 원본과 같은 객체를 참조**함

---

## 9. 깊은 복사 (Deep Copy)

### 개념

* 객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법
* 중첩된 객체까지 모두 새로운 객체로 생성됨

> **💡 TIP: 완전한 독립성 보장**
> * 깊은 복사는 원본 객체와 복사본이 **완전한 독립적**임을 보장합니다.
> * 복사본의 어떤 수준에 있는 중첩 내용을 변경하더라도 원본 객체에는 절대 영향을 주지 않습니다.
> 
> 

### 깊은 복사 방법

* 파이썬 내장 `copy` 모듈에서 제공하는 `deepcopy()` 함수를 사용

```python
import copy

new_object = copy.deepcopy(original_object)

```

### 깊은 복사 예시

#### 예시 1) 다차원 리스트에서의 깊은 복사

```python
import copy

a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100

print(a)  # [1, 2, [3, 4, 5]]   -> 원본 변경 안 됨
print(b)  # [1, 2, [3, 100, 5]] -> 복사본만 변경됨

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False

```

#### 예시 2) 중첩된 딕셔너리 및 복합 객체에서의 깊은 복사

```python
import copy

original = {
    'a': [1, 2, 3],
    'b': {'c': 4, 'd': [5, 6]}
}

copied = copy.deepcopy(original)

# 내부 중첩 요소 수정
copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')
# 원본: {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}

print(f'복사본: {copied}')
# 복사본: {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}

print(f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}")
# False

```


---

## 10. List Comprehension (리스트 컴프리헨션)

### 개념

* 간결하고 효율적인 리스트 생성 방법
* 파이썬 개발자들이 선호하는 스타일로, 코드를 더 **"Pythonic(파이썬답게)"** 작성하는 대표적인 방식

### 기본 구조 및 조건문

```python
# 기본 형태
[expression for 변수 in iterable]

# 조건문 포함 형태 (if 조건문은 필터링 역할 / 선택 사항)
[expression for 변수 in iterable if 조건식]

```

#### 각 구성 요소의 역할

* **expression (표현식)**: 결과 리스트에 추가될 값
* **변수**: 순회 중인 현재 요소
* **iterable (순회 가능한 객체)**: 반복할 데이터
* **if 조건식**: 필터링 조건 (명시하지 않으면 모든 요소에 대해 표현식 적용)

### 사용 전/후 비교

* **사용 전 (for loop)**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)  # [1, 4, 9, 16, 25]

```

* **사용 후 (List Comprehension)**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)  # [1, 4, 9, 16, 25]

```

### 활용 예시 (2차원 배열 생성 / 인접 행렬)

```python
# 방법 1
data1 = [[0] * 5 for _ in range(5)]

# 방법 2
data2 = [[0 for _ in range(5)] for _ in range(5)]

# 결과:
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]

```

> **⚠️ 주의사항: Comprehension을 남용하지 말자**
> * *"Simple is better than complex"*
> * *"Keep it simple, stupid"*
> * 코드가 지나치게 복잡해지면 가독성을 위해 일반적인 `for` 문을 사용하는 것이 좋습니다.
> 
> 

---

## 11. 리스트 생성 방식 및 성능 비교

### 리스트를 생성하는 3가지 방법

```python
# 1. loop (for 문)
result1 = []
for i in range(10):
    result1.append(i)

# 2. list comprehension
result2 = [i for i in range(10)]

# 3. map
result3 = list(map(lambda i: i, range(10)))

```

### 성능 비교 및 특징

1. **`list comprehension`**
* 가장 'Pythonic'하며 대부분의 경우 **우수한 성능**을 보임


2. **`map`**
* 특정 상황(`int`, `str` 등 내장 함수와 함께 사용할 때)에서 가장 빠름
* 사용자 정의 함수나 `lambda`와 함께 사용될 때는 list comprehension과 성능이 비슷하거나 약간 느릴 수 있음


3. **`for loop`**
* 일반적으로 가장 느리다고 알려져 있으나, 파이썬 버전이 올라가면서 성능 차이가 많이 줄어듦
* 여러 줄에 걸친 **복잡한 조건문이나 예외 처리가 필요할 때는 유일한 선택지**이자 매우 유용함



> **💡 TIP**
> 성능 차이는 대부분의 경우 마이크로초 단위로 미미하므로, **코드의 가독성과 유지보수성을 최우선**으로 고려하여 상황에 맞는 명확한 방법을 선택하는 것을 권장합니다.

---

## 12. 메서드 체이닝 (Method Chaining)

### 개념

* 여러 메서드를 연속해서 호출하는 방식

### 문자열에서의 메서드 체이닝 예시

```python
text = 'heLLo, woRld!'

# 1. 단계별 실행
step1 = text.swapcase()                   # 'HEllO, WOrLD!' (대소문자 반전)
step2 = step1.replace('l', 'z')          # 'HEzzO, WOrLD!' ('l'을 'z'로 교체)

# 2. 한 줄로 실행 (메서드 체이닝)
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!

```

### 리스트에서의 흔한 실수와 올바른 해결책

#### ❌ 흔한 실수

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 실수 1: sort()는 None을 반환하므로 result에 None이 저장됨
result = numbers.copy().sort()
print(result)  # None

# 실수 2: append()가 반환한 None 뒤에는 메서드를 이을 수 없음
numbers.append(7).extend([8, 9])  # AttributeError: 'NoneType' object has no attribute 'extend'

```

#### ⭕ 올바른 해결책

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 해결 1: 새로운 리스트를 반환하는 내장 함수 sorted() 사용
sorted_numbers = sorted(numbers)

# 해결 2: 메서드를 단계별로 나누어 작성
copied_list = numbers.copy()
copied_list.sort()

```

### ⚠️ 메서드 체이닝 주의사항

* **모든 메서드가 체이닝을 지원하는 것은 아닙니다.**
* **메서드가 객체를 반환할 때만** 체이닝이 가능합니다.
* `None`을 반환하는 메서드(예: 리스트의 `append()`, `sort()`)는 메서드 체이닝이 불가능합니다.
* 메서드 체이닝을 사용할 때는 각 메서드의 **반환값**을 정확히 이해하고 있어야 합니다.

---

## 13. 문자 유형 판별 메서드

문자열에 포함된 문자들의 유형을 판별하는 대표적인 메서드 3가지의 포함 관계는 다음과 같습니다.


$$\text{isdecimal()} \subseteq \text{isdigit()} \subseteq \text{isnumeric()}$$

### 1. `isdecimal()`

* 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 `True`

### 2. `isdigit()`

* `isdecimal()`과 비슷하지만, **유니코드 숫자**(예: `①`, `³`)도 숫자로 인식하여 `True`

### 3. `isnumeric()`

* `isdigit()`보다 더 광범위하게 **분수, 지수, 한자 숫자, 로마 숫자 등** 다양한 유니코드 숫자 기호를 숫자로 인식하여 `True`

### 비교표

| 메서드 | `isdecimal()` | `isdigit()` | `isnumeric()` | 예시 문자열 |
| --- | --- | --- | --- | --- |
| **일반 숫자** | **True** | **True** | **True** | `"038"`, `"0 3 8"` |
| **지수 / 특수 숫자** | False | **True** | **True** | `"⁰³⁸"`, `"⓪③⑧"` |
| **분수 / 한자 숫자** | False | False | **True** | `"½"`, `"壹貳參"` |
| **문자 / 음수 / 실수** | False | False | False | `"abc"`, `"38.0"`, `"-38"` |

새로 첨부해주신 **파이썬 문법 규격(BNF, EBNF)** 슬라이드 내용을 가독성 있게 정리했습니다.

---

## 14. 파이썬 문법 규격 (BNF / EBNF)

### BNF & EBNF 개념

#### 1. BNF (Backus-Naur Form)

* 프로그래밍 언어의 문법을 공식적으로 표현하기 위한 표기법

#### 2. EBNF (Extended Backus-Naur Form)

* BNF를 **확장한 표기법**
* 메타 기호를 추가하여 더 간결하고 표현력이 강해진 형태

### 대표적인 EBNF 메타 기호

| 메타 기호 | 의미 |
| --- | --- |
| `[]` | **선택적 요소** (Optional) |
| `{}` | **0번 이상 반복** (Repetition) |
| `()` | **그룹화** (Grouping) |

### EBNF 메타 기호 `[]` 사용 예시

* **딕셔너리의 `pop` 메서드 공식 문서 규격**

$$\text{pop}(key[, \text{default}])$$



> **공식 문서 설명:**
> If $key$ is in the dictionary, remove it and return its value, else return $default$.
> If $default$ is not given and $key$ is not in the dictionary, a `KeyError` is raised.

### BNF와 같은 표기법을 사용하는 이유

* 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 **통일하여 정의**하기 위함

> **💡 TIP: EBNF 메타 기호의 실용적 활용**
> * `[]`와 같은 EBNF 기호는 파이썬 공식 문서에서 **함수나 메서드의 파라미터**를 설명할 때 널리 사용됩니다.
> * 예시의 `pop(key[, default])`처럼, **대괄호(`[]`) 안에 있는 파라미터는 선택 사항(생략 가능)**임을 의미합니다.
> * 이 기호를 알고 있으면 공식 문서만 보고도 어떤 파라미터가 **필수**이고, 어떤 파라미터를 **생략**할 수 있는지 한눈에 파악할 수 있습니다.
> 
>