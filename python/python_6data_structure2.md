
# 비시퀀스 데이터 구조

## 1. 시퀀스 vs 비시퀀스 (Sequence vs Non-sequence)

### 비교 요약

| 구분 | 시퀀스 (Sequence) | 비시퀀스 (Non-sequence) |
| --- | --- | --- |
| **자료형** | `str`, `list`, `tuple`, `range` | `dict`, `set` |
| **찾는 기준** | 위치(인덱스) | 키 또는 값 자체 |
| **접근 예시** | `books[0]` | `phonebook['민수']` / `'민수' in phonebook` |
| **슬라이싱** | **가능** | **불가** |
| **중복** | **허용** | **불가** (`dict`의 키, `set`의 요소) |

> **💡 TIP: 인덱스가 사라지면 무엇이 좋아지나요?**
> * **시퀀스:** '민수'의 번호를 찾으려면 처음부터 하나씩 대조해야 합니다.
> * **비시퀀스:** 이름표를 곧바로 위치로 바꿔 한 번에 찾아냅니다.
> * 데이터가 10개일 때는 큰 차이가 없지만, **10만 개 이상이 되면 결정적인 성능 차이**가 발생합니다.
> 
> 

---

## 2. 딕셔너리 (Dictionary)

### 개념

* 키(Key)와 값(Value)을 짝지어 저장하는 자료구조

### 특징 및 구조

* 내부적으로 해시 테이블(Hash Table)을 사용하여 키-값 쌍을 관리합니다.
* 키를 통한 값의 **삽입, 삭제, 검색이 데이터의 크기와 관계없이 매우 빠릅니다.**
* **키(Key):** `hashable`한 **고유 값**이어야 합니다 (중복 불가).
* **값(Value):** 중복이 가능하며 어떤 자료형도 저장할 수 있습니다.

---

## 3. 딕셔너리 주요 메서드

| 메서드 | 설명 |
| --- | --- |
| `D.get(k)` | 키 `k`에 연결된 값을 반환 (키가 없으면 `None` 반환) |
| `D.get(k, v)` | 키 `k`에 연결된 값을 반환하거나, 키가 없으면 기본값 `v`를 반환 |
| `D.keys()` | 딕셔너리 `D`의 키를 모은 객체를 반환 |
| `D.values()` | 딕셔너리 `D`의 값을 모은 객체를 반환 |
| `D.items()` | 딕셔너리 `D`의 키/값 쌍을 모은 객체를 반환 |
| `D.setdefault(k)` | 딕셔너리 `D`에서 키 `k`와 연결된 값을 반환 |
| `D.setdefault(k, v)` | 키 `k`가 있으면 연결된 값을 반환, 없으면 `k: v` 쌍을 추가하고 `v`를 반환 |
| `D.update(other)` | `other`의 키/값 쌍으로 `D`를 갱신 (기존 키는 덮어씀, 없는 키는 추가) |
| `D.pop(k)` | 키 `k`를 제거하고 연결된 값을 반환 (없으면 에러) |
| `D.pop(k, v)` | 키 `k`를 제거하고 연결된 값을 반환 (없으면 `v`를 반환) |
| `D.clear()` | 딕셔너리 `D`의 모든 키/값 쌍을 제거 |

---

## 4. 딕셔너리 메서드 상세 및 사용 예시

### 1) `.get(key[, default])`

* 키에 연결된 값을 안전하게 조회합니다.
* 키가 없을 경우 `KeyError` 발생 대신 `None` 또는 지정한 `default` 값을 반환합니다.

```python
person = {'name': 'Alice', 'age': 25}

print(person.get('name'))              # Alice
print(person.get('country'))           # None
print(person.get('country', 'Unknown'))# Unknown

# print(person['country'])             # KeyError 발생

```

### 2) `.keys()`, `.values()`, `.items()`

* **`.keys()`**: 딕셔너리의 모든 키를 모은 객체(`dict_keys`) 반환
* **`.values()`**: 딕셔너리의 모든 값을 모은 객체(`dict_values`) 반환
* **`.items()`**: 딕셔너리의 모든 키-값 튜플 쌍을 모은 객체(`dict_items`) 반환

```python
person = {'name': 'Alice', 'age': 25}

# .keys()
print(person.keys())  # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)       # name, age 순차 출력

# .values()
print(person.values())# dict_values(['Alice', 25])

# .items()
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value) # name Alice / age 25

```

### 3) `.setdefault(key[, default])`

* 키에 연결된 값을 반환하되, **키가 없다면 `default`와 연결한 키를 딕셔너리에 자동으로 추가**하고 `default`를 반환합니다.

```python
person = {'name': 'Alice', 'age': 25}

print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

```

### 4) `.update([other])`

* `other`가 제공하는 키/값 쌍으로 기존 딕셔너리를 갱신합니다. (기존 키는 값을 덮어쓰고, 없는 키는 새로 추가)

```python
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

# 1. 딕셔너리 객체로 업데이트
person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

# 2. 키워드 인자로 업데이트
person.update(age=100, address='SEOUL')
print(person) # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}

```

### 5) `.pop(key[, default])`

* 지정한 키를 제거하고 연결되었던 값을 반환합니다.
* 키가 없을 경우 에러가 발생하지만, `default`를 지정해두면 `default` 값을 반환합니다.

```python
person = {'name': 'Alice', 'age': 25}

print(person.pop('age'))            # 25
print(person)                       # {'name': 'Alice'}
print(person.pop('country', None))  # None (에러 없음)
# print(person.pop('country'))      # KeyError 발생

```

### 6) `.clear()`

* 딕셔너리의 모든 키/값 쌍을 제거하여 빈 딕셔너리로 만듭니다.

```python
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}

```

---

## 5. 딕셔너리의 확장: `defaultdict`

### 개념

* 파이썬 내장 모듈인 `collections`에서 제공하는 딕셔너리의 확장판
* **존재하지 않는 키를 조회하거나 수정할 때, 자동으로 '기본값'을 생성**해주는 자료구조
* `KeyError` 걱정 없이 값을 수정하거나 추가할 때 매우 유용함

> **📦 collections 모듈이란?**
> 파이썬의 범용 내장 컨테이너(`list`, `dict`, `set`, `tuple`)를 보완하기 위해 더 효율적이고 특수한 기능을 갖춘 고성능 데이터 타입을 제공하는 표준 라이브러리입니다.

---

## 6. 기본 딕셔너리 vs `defaultdict` 비교

### 상황: 문자열에서 각 문자의 등장 횟수 세기 (`'banana'`)

* **기본 딕셔너리 활용**
```python
text = 'banana'
counts = {}

for char in text:
    # 키가 존재하는지 매번 확인해야 함
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

print(counts)  # {'b': 1, 'a': 3, 'n': 2}

```


* **`defaultdict` 활용 (개선)**
```python
from collections import defaultdict

text = 'banana'
counts = defaultdict(int)  # 기본값을 정수(0)로 설정

for char in text:
    # 키 존재 확인 불필요! 없으면 0으로 자동 생성 후 +1
    counts[char] += 1

print(counts)  # defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})

```



---

## 7. `defaultdict` 구문 및 활용 예시

### 기본 구문

```python
defaultdict(자료형)

```

### 자주 쓰는 패턴

1. **숫자 세기 (카운팅):** `defaultdict(int)` $\rightarrow$ 키가 없으면 `0`으로 초기화
2. **그룹핑 / 리스트 모으기:** `defaultdict(list)` $\rightarrow$ 키가 없으면 빈 리스트 `[]`로 초기화

### 활용 예시: 색상별 과일 분류하기

```python
from collections import defaultdict

fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
fruit_by_color = defaultdict(list)

for color, fruit in fruits:
    # color 키가 없으면 빈 리스트 [] 생성 -> append 바로 가능
    fruit_by_color[color].append(fruit)

print(fruit_by_color)
# defaultdict(<class 'list'>, {'red': ['apple', 'cherry'], 'yellow': ['banana']})

```

---

## 8. `defaultdict` 주의사항 및 핵심 요약

### ⚠️ 주의사항: 단순 조회 시에도 키 생성

* `defaultdict`는 **조회(접근)만 해도 키가 자동으로 생성**됩니다.
* 예: `print(my_dict['missing_key'])` 실행 시 `0`(또는 지정된 기본값)이 출력되면서 해당 키가 딕셔너리에 추가됩니다.
* 따라서 "단순히 키가 존재하는지 확인할 때"는 주의해서 사용해야 합니다.

> **💡 TIP: 언제 쓰면 좋을까요?**
> * **일반 `dict`:** 데이터의 단순 조회가 주 목적이거나, 키의 존재 여부가 로직에서 중요할 때
> * **`defaultdict`:** 데이터를 집계하거나 그룹핑할 때, 초기화 코드를 줄이고 로직의 핵심에 집중하고 싶을 때
> 
> 

> **💡 TIP: `.setdefault()`와의 차이점**
> * `.setdefault()`는 메서드를 **호출할 때마다 기본값을 인자로 전달**해 주어야 합니다.
> * `defaultdict`는 **객체를 생성할 때 한 번만 설정**해 두면 되므로, 반복문 안에서 코드가 훨씬 깔끔해집니다.
> 
>

---

# 비시퀀스 데이터 구조 (이어서)

## 9. 세트 (Set)

### 개념

* **고유한 항목들의 정렬되지 않은 컬렉션** (중복 없는 데이터의 집합)

### 특징 및 구조

* 내부적으로 해시 테이블(Hash Table)을 사용하여 데이터를 저장합니다.
* 항목의 고유성(중복 제거)을 효율적으로 보장합니다.
* 데이터 크기와 관계없이 항목의 추가, 삭제, 존재 여부 확인 (`in` 연산)이 매우 빠릅니다.
* 합집합, 교집합, 차집합 등 **수학적인 집합 연산**을 간편하게 수행할 수 있는 것이 가장 큰 특징입니다.

---

## 10. 세트 주요 메서드

| 메서드 | 설명 |
| --- | --- |
| `s.add(x)` | 세트 `s`에 항목 `x`를 추가 (이미 `x`가 있다면 변화 없음) |
| `s.update(iterable)` | 세트 `s`에 다른 `iterable`의 요소들을 추가 |
| `s.clear()` | 세트 `s`의 모든 항목을 제거 |
| `s.remove(x)` | 세트 `s`에서 항목 `x`를 제거 (**항목 `x`가 없을 경우 `KeyError` 발생**) |
| `s.pop()` | 세트 `s`에서 **임의의 항목을 반환하고 제거** |
| `s.discard(x)` | 세트 `s`에서 항목 `x`를 제거 (**항목이 없어도 에러 없음**) |

---

## 11. 세트 기본 메서드 상세 및 사용 예시

### 1) `.add(x)`

* 세트에 단일 요소 `x`를 추가합니다. 이미 존재한다면 중복을 허용하지 않으므로 변화가 없습니다.

```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add('d')
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a'}

my_set.add('d')  # 이미 존재하므로 변화 없음
print(my_set)  # {1, 'b', 3, 2, 'c', 'd', 'a'}

```

### 2) `.update(iterable)`

* 여러 요소가 담긴 `iterable`(리스트, 튜플 등)을 전달받아 세트에 한 번에 추가합니다.

```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}

```

### 3) `.clear()`

* 세트의 모든 항목을 제거하여 빈 세트(`set()`)로 만듭니다.

```python
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set)  # set()

```

### 4) `.remove(x)` vs `.discard(x)`

* 두 메서드 모두 항목 `x`를 제거하지만, **존재하지 않는 값을 제거하려 할 때의 동작 방식**에 차이가 있습니다.

```python
my_set = {'a', 'b', 'c', 1, 2, 3}

# .remove(x) : 없는 항목 제거 시 KeyError 발생
my_set.remove(2)
print(my_set)  # {'b', 1, 3, 'c', 'a'}
# my_set.remove(10)  # KeyError: 10 발생!

# .discard(x) : 없는 항목을 제거해도 에러가 발생하지 않음
my_set.discard(2)
print(my_set)  # {1, 3, 'a', 'c', 'b'}
my_set.discard(10)  # 에러 없이 안전하게 넘어가짐

```

### 5) `.pop()`

* 세트에서 **임의의 요소를 제거하고 그 값을 반환**합니다. (순서가 없는 컬렉션이므로 특정 위치 지정 불가)

```python
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()
print(element)  # 1 (임의의 요소 반환)
print(my_set)   # {2, 3, 'b', 'a', 'c'}

```

---

## 12. 세트의 집합 연산 메서드 & 연산자

| 메서드 | 연산자 | 설명 |
| --- | --- | --- |
| `set1.difference(set2)` | `set1 - set2` | **차집합:** `set1`에는 있지만 `set2`에는 없는 항목으로 세트 생성 |
| `set1.intersection(set2)` | `set1 & set2` | **교집합:** `set1`과 `set2` 모두에 들어있는 항목으로 세트 생성 |
| `set1.issubset(set2)` | `set1 <= set2` | **부분집합 여부:** `set1`의 항목이 모두 `set2`에 들어있으면 `True` |
| `set1.issuperset(set2)` | `set1 >= set2` | **상위집합 여부:** `set1`이 `set2`의 모든 항목을 포함하면 `True` |
| `set1.union(set2)` | `(set1 I set2 )`| **합집합:** `set1` 또는 `set2`에 들어있는 항목으로 세트 생성 |

### 사용 예시

```python
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

# 차집합
print(set1.difference(set2))   # {0, 2, 4}

# 교집합
print(set1.intersection(set2)) # {1, 3}

# 부분집합 확인
print(set1.issubset(set2))     # False
print(set3.issubset(set1))     # True

# 상위집합 확인
print(set1.issuperset(set2))   # False

# 합집합
print(set1.union(set2))        # {0, 1, 2, 3, 4, 5, 7, 9}

```

---

# 비시퀀스 데이터 구조 (이어서)

## 13. 해시 테이블 (Hash Table)

### 개념

* 키(Key)와 값(Value)을 짝지어 저장하는 자료구조입니다.
* **도서관 비유:** 수백 권의 책 중에서 책 제목(키)을 색인(해시 함수)에 입력하여 몇 번째 책장(인덱스)에 있는지 알아내면, 해당 책장(배열)으로 바로 가서 책(값)을 꺼내는 방식입니다. (전체를 일일이 뒤지는 것보다 훨씬 빠름)

### 작동 원리

1. 키(Key)를 **해시 함수**를 통해 해시 값(Hash Value)으로 변환합니다.
2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾습니다.
3. 이를 통해 **검색, 삽입, 삭제를 매우 빠르게($O(1)$) 수행**할 수 있습니다.

---

## 14. 해시 함수 (Hash Function) & 해시 난수화

### 해시 함수란?

* **임의의 길이를 가진 데이터**를 입력받아 고정된 길이의 정수(해시 값)로 변환해 주는 함수입니다.
* 생성된 해시 값은 해당 데이터를 식별하는 '지문' 역할을 수행합니다.

### 타입별 해시 특징 (정수 vs 문자열)

* **정수 (Integer):**
* 같은 정수는 항상 같은 해시 값을 가집니다 (예: `hash(1)`은 항상 동일).


* **문자열 (String):**
* 보안상의 이유로 해시 난수화(Hash Randomization)가 적용되어, 파이썬 프로세스가 실행될 때마다 난수 시드(seed) 값이 달라집니다.
* 따라서 동일한 문자열이라도 **실행할 때마다 해시 값이 달라질 수 있습니다.**



---

## 15. 해시 테이블과 `set`, `dict`의 관계

### `set`에서의 작동 방식

* 각 요소를 해시 함수로 변환하여 나온 해시 값에 맞춰 해시 테이블 내부 버킷(bucket)에 위치시킵니다.
* 따라서 요소의 위치는 "버킷 위치(인덱스)"가 결정하므로 **순서를 보장하지 않습니다.**
* **`set.pop()`의 특성:**
* "무작위(random)" 요소를 제거하는 것이 아니라, 해시 테이블 내부 버킷 순서에 따라 **"임의의(arbitrary)" 요소**를 반환하고 제거합니다.
* 문자열의 경우 실행 시마다 해시 난수화로 인해 `pop()` 되는 순서가 달라질 수 있습니다.



### `dict`에서의 작동 방식

* `Key → 해시 함수 → 해시 값 → 해시 테이블 저장` 순으로 동작합니다.
* 내부 구현은 해시 테이블 기반이지만, **Python 3.7+ 이상에서는 삽입 순서가 보장**되도록 언어 사양이 변경되었습니다.

---

## 16. 해시 가능성 (Hashable)

### 개념

* `hash()` 함수에 전달하여 고유한 해시 값을 얻을 수 있는 객체를 **Hashable**하다고 합니다.
* **해시 테이블 기반 자료구조(`set`의 요소, `dict`의 Key)에는 Hashable한 객체만 사용할 수 있습니다.**

### 불변성(Immutability)과의 관계

* **불변 타입 (Hashable 가능):** `int`, `float`, `str`, `tuple` (내부 요소가 모두 불변일 때)
* **가변 타입 (Hashable 불가능):** `list`, `dict`, `set`

```python
# Hashable 객체 예시
print(hash(1))         # 정상 출력
print(hash('a'))       # 정상 출력
print(hash((1, 2, 3))) # 정상 출력

# Unhashable 예시 (TypeError 발생)
# print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3]}    # TypeError: unhashable type: 'list'
# my_dict = {{3, 2}: 'a'} # TypeError: unhashable type: 'set'

```

> **💡 가변 객체가 Hashable하지 않은 이유**
> * 가변 객체는 값이 변경될 수 있습니다. 만약 값이 변경되면 **해시 값도 함께 변하게 됩니다.**
> * 해시 테이블은 **"동일 키 $\rightarrow$ 동일 위치"**라는 전제로 빠른 검색을 수행하는데, 값이 바뀌면 데이터가 저장된 위치를 찾을 수 없게 되어 **무결성이 깨집니다.**
> * 따라서 파이썬은 무결성을 보장하기 위해 가변 객체의 해시 값 계산을 금지합니다.
> 
> 

---

## 17. 해시 테이블 핵심 요약

* **빠른 연산:** 해시 값을 인덱스로 사용하여 데이터 저장 및 검색 속도가 매우 빠릅니다.
* **순서와 무작위성:** `set`은 순서가 없고 `pop()` 시 반환되는 요소의 순서를 예측할 수 없으며, 문자열은 해시 난수화의 영향을 받습니다.
* **키의 조건:** 불변(Immutable) 객체만 `set`의 요소나 `dict`의 Key(`Hashable`)로 사용할 수 있습니다.