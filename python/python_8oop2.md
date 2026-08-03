# 1. 상속(Inheritance)

### 정의

* **상속(Inheritance):** 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것을 의미합니다.
* 부모 클래스와 자식 클래스 간의 상하 관계가 형성되어, 부모 클래스가 가진 속성과 메서드를 자식 클래스에게 넘겨주는 과정을 **상속 과정**이라고 합니다.

---

## 2. 상속이 필요한 이유

1. **코드 재사용 (Code Reuse)**
* 기존 클래스의 속성과 메서드를 재사용하여 중복 코드를 줄일 수 있습니다.
* 기존 클래스를 직접 수정하지 않고도 새로운 기능을 확장할 수 있습니다.


2. **계층 구조 형성 (Hierarchy Structure)**
* 클래스 간의 관계를 명확히 표현할 수 있습니다.
* 공통 특성을 가진 부모 클래스를 기반으로 더 구체적이고 전문화된 자식 클래스를 만들 수 있습니다.


3. **유지보수의 용이성 (Maintainability)**
* 공통 로직의 수정이 필요할 때 부모 클래스만 수정하면 되므로 유지보수가 매우 용이해집니다.
* 코드의 일관성을 유지하고 modification 범위를 최소화합니다.



---

## 3. 상속 사용 유무 비교 예시

### (1) 상속 없이 구현하는 경우

* 교수(`Professor`)와 학생(`Student`) 클래스를 각각 구현하면 `name`, `age` 속성 및 `talk()` 메서드가 중복으로 정의됩니다.

```python
# 상속 미사용: 코드 중복 발생
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

```

### (2) 상속을 적용한 계층 구조 변경

* 공통 속성(`name`, `age`)과 메서드(`talk`)를 부모 클래스인 `Person`에 정의하여 재사용합니다.

```python
# 부모 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

# 자식 클래스 1 (부모 클래스 이름 명시)
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

# 자식 클래스 2
class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

# 사용 예시
p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 클래스(Person)의 talk() 메서드 재사용
p1.talk()  # 출력: 반갑습니다. 박교수입니다.
s1.talk()  # 출력: 반갑습니다. 김학생입니다.

```

> 💡 **참고:** 자식 클래스를 정의할 때는 클래스 이름 뒤 괄호 안에 **상속받을 부모 클래스 이름**을 반드시 선언해야 합니다.
> 예: `class Dog(Animal):`

---

## 4. 메서드 오버라이딩 (Method Overriding)

### 개념

* 부모 클래스로부터 물려받은 메서드를 자식 클래스에서 **같은 이름, 같은 파라미터 구조로 재정의**하는 것을 말합니다.
* 자식 클래스에서 메서드를 재정의하면, 부모의 메서드 대신 **자식 클래스의 메서드가 호출**됩니다.
* 부모의 기본 기능을 유지하면서 특정 동작만 맞춤형으로 변경하고자 할 때 사용합니다.

### 예시

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 부모 클래스의 eat 메서드를 오버라이딩(재정의)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()
my_dog.eat()  # 출력: Dog가 먹는 중

```

---

## 5. [참고] 오버로딩 (Overloading)과 파이썬에서의 특징

### 오버로딩의 개념

* 같은 이름의 메서드가 **매개변수의 개수나 타입에 따라 서로 다르게 동작**하도록 여러 개 정의하는 기법입니다. (C++, Java 등에서 지원)

### 파이썬에서의 오버로딩 미지원

* **파이썬은 공식적으로 메서드 오버로딩을 지원하지 않습니다.**
* 파이썬에서는 동일한 이름의 메서드가 정의되면 **마지막으로 선언된 메서드가 이전 정의를 덮어씁니다.**

```python
class Example:
    def do_something(self, x):
        print('첫 번째 do_something:', x)

    # 파이썬에서는 이름이 같으면 앞선 정의를 덮어씀
    def do_something(self, x, y):
        print('두 번째 do_something:', x, y)

example = Example()

# 인자를 1개만 전달하면 TypeError 발생
# TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)

```

---

## 1. 다중 상속 (Multiple Inheritance)

### 개념

* **다중 상속:** 둘 이상의 상위(부모) 클래스로부터 속성이나 메서드를 동시에 상속받는 기능입니다.
* 자식 클래스는 상속받은 모든 부모 클래스의 요소를 활용할 수 있습니다.
* **충돌 해결:** 부모 클래스 간에 중복된 속성이나 메서드가 존재할 경우, 클래스 정의 시 작성한 상속 순서(왼쪽 부모 우선)에 따라 호출 결정이 이루어집니다.

### 예시

```python
class Person:
    def __init__(self, name):
        self.name = name

class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'

# Dad를 Mom보다 먼저 상속받음
class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())   # 출력: 첫째가 응애 (자식 클래스 자신)
print(baby1.swim())  # 출력: 첫째가 수영 (오버라이딩된 자식 메서드)
print(baby1.walk())  # 출력: 아빠가 걷기 (Dad에서 상속)
print(baby1.gene)    # 출력: XY (FirstChild(Dad, Mom) 순서상 Dad가 우선)

```

---

## 2. MRO (Method Resolution Order, 메서드 결정 순서)

### MRO란?

* 파이썬이 다중 상속 환경에서 **어떤 부모 클래스의 메서드를 먼저 탐색하고 실행할지 정해놓은 순서 규칙**입니다.
* MRO가 존재하기 때문에 다중 상속 구조에서도 메서드 호출 순서를 예측 가능하게 유지할 수 있습니다.

### C3 Linearization (선형화) 알고리즘 3대 원칙

파이썬은 MRO를 결정할 때 **C3 Linearization** 알고리즘을 사용합니다.

1. **자식 클래스 우선:** 부모 클래스보다 자식 클래스를 먼저 탐색합니다.
2. **왼쪽 부모 우선:** 다중 상속 선언 시, 괄호 안에 나열된 순서(왼쪽 $\rightarrow$ 오른쪽)대로 탐색합니다.
3. **중복 방문 방지 (공통 부모 나중):** 공통 부모 클래스는 모든 자식 클래스의 탐색이 끝난 뒤 **단 한 번만** 탐색합니다.

> 💡 **핵심 요약:** *"자식은 부모보다 먼저, 겹치는 공통 부모는 가장 나중에!"*

---

## 3. 다이아몬드 상속 구조에서의 MRO 탐색 흐름

클래스 $D$가 $B$와 $C$를 상속받고, $B$와 $C$가 공통 부모 $A$를 상속받는 **다이아몬드 구조** 예시입니다.

```text
    A
   / \
  B   C
   \ /
    D

```

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

```

* **MRO 탐색 순서:** $D \rightarrow B \rightarrow C \rightarrow A \rightarrow \text{object}$

1. **D (자신):** 가장 먼저 확인
2. **B (첫 번째 부모):** 왼쪽 부모 우선 적용
3. **C (두 번째 부모):** $B$의 부모인 $A$로 바로 올라가지 않고, 공통 부모 방문을 미루며 형제 클래스 $C$를 먼저 탐색
4. **A (공통 부모):** $B$와 $C$를 모두 확인한 후 마지막에 단 한 번 탐색

---

## 4. `super()` 함수

### 개념 및 역할

* MRO 순서에 따라 **현재 클래스의 상위(부모) 클래스 메서드나 속성에 접근**할 수 있게 해주는 파이썬 내장 함수입니다.
* 부모 클래스의 이름을 직접 하드코딩하지 않고 호출할 수 있어, 클래스명이 변경되거나 상속 구조가 수정되어도 코드의 **유지보수성**이 높아집니다.

### 1) 단일 상속에서의 `super()`

부모 클래스의 생성자(`__init__`)를 호출해 공통 속성을 초기화하고, 자식 클래스 고유의 속성을 추가할 때 주로 사용합니다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 호출하여 공통 속성 초기화
        super().__init__(name, age, number, email)
        self.student_id = student_id  # Student 고유 속성

```

### 2) 다중 상속에서의 `super()`

다중 상속에서 `super()`를 사용하면 단순 직계 부모가 아니더라도 MRO 체인을 따라 다음 순서의 부모 클래스 메서드를 순차적으로 안전하게 호출합니다.

```python
class ParentA:
    def __init__(self):
        super().__init__()  # MRO상 다음 순서인 ParentB의 __init__을 호출
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # MRO에 따라 ParentA의 __init__ 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # MRO 순서상 첫 부모인 ParentA의 show_value() 호출
        print(f'Value from Child: {self.value_c}')

```

---

## 5. MRO 확인 방법 및 MRO가 필요한 이유

### MRO 확인 방법

클래스의 `.mro()` 메서드나 `.__mro__` 속성을 통해 해당 클래스의 메서드 탐색 순서를 리스트나 튜플 형태로 확인할 수 있습니다.

```python
# MRO 확인 방법
print(D.mro())
# 출력: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

print(D.__mro__)

```

### MRO가 필요한 이유

* **중복 호출 방지:** 공통 부모 클래스가 여러 번 실행/액세스되는 것을 방지합니다.
* **순서 보존:** 클래스 정의 시 지정된 (왼쪽 $\rightarrow$ 오른쪽) 상속 순서를 일정하게 보존합니다.
* **예측 가능성 향상:** 복잡한 상속 관계에서도 메서드 호출 순서가 명확하게 유지되어 코드의 **신뢰성, 재사용성, 확장성**이 대폭 향상됩니다.

---

## 1. 버그(Bug)와 디버깅(Debugging)

### (1) 버그 (Bug)

* **정의:** 소프트웨어에서 발생하는 오류 또는 결함입니다.
* **특징:** 프로그램의 **예상된 동작**과 **실제 동작** 사이의 불일치를 뜻합니다.

### (2) 디버깅 (Debugging)

* **정의:** 소프트웨어에서 발생하는 버그를 찾아내고 수정하여 오작동 원인을 식별·수정하는 작업입니다.
* **주요 디버깅 방법:**
1. **`print()` 함수 활용:** 특정 함수 결과나 조건/반복 결과를 나눠 확인하거나 코드를 이분법(bisection)으로 나눠 검증합니다.
2. **IDE/개발 환경 기능 활용:** Breakpoint(중단점)를 설정하고 실행 중 변수 값을 추적합니다.
3. **Python Tutor 활용:** 코드가 실행되는 흐름과 메모리 상태를 시각적으로 직접 확인합니다.
4. **뇌 컴파일 및 눈 디버깅:** 머릿속으로 로직을 돌려보며 정밀하게 코드를 검토합니다.



---

## 2. 파이썬의 에러 유형 (문법 에러 vs 예외)

프로그램 실행 중 예상치 못한 문제가 발생하면 에러(Error)가 생기며, 이를 처리하지 않으면 프로그램이 중단됩니다.

| 구분 | 문법 에러 (Syntax Error) | 예외 (Exception) |
| --- | --- | --- |
| **발생 시점** | **코드 실행 전** (문법 검사 단계) | **코드 실행 중** (런타임 단계) |
| **원인** | 오타, 괄호/콜론 누락 등 문법적 오류 | 존재하지 않는 파일 읽기, 0으로 나누기, 부적절한 값 참조 등 |
| **대표 예시** | `SyntaxError`, `IndentationError` | `ZeroDivisionError`, `ValueError`, `TypeError` 등 |

### 문법 에러 예시

* `SyntaxError: invalid syntax`: `while` 키워드만 적고 뒤에 조건식을 누락한 경우 등
* `SyntaxError: cannot assign to literal`: `5 = 3`과 같이 변수가 아닌 리터럴 상수에 값을 할당하려 한 경우
* `SyntaxError: unterminated string literal`: 문자열 닫는 따옴표(`'`)를 누락한 경우
* `IndentationError`: `for`문이나 `if`문 아래에 들여쓰기(Indentation)를 하지 않은 경우

---

## 3. 파이썬의 주요 내장 예외 (Built-in Exceptions)

파이썬에는 자주 발생하는 예외 상황들이 미리 클래스로 정의되어 있습니다.

* **`ZeroDivisionError`:** 어떤 수를 0으로 나누거나 모듈로 연산(`%`)할 때 발생 (예: `10 / 0`)
* **`NameError`:** 정의되지 않은 지역/전역 변수 이름을 참조하려 할 때 발생 (예: `print(name1)`)
* **`TypeError`:**
* 타입 불일치 (예: `'2' + 2`)
* 인자 개수 초과/누락 (예: `sum()`에 인자를 안 주거나 너무 많이 전달한 경우)
* 인자 타입 불일치 (예: `random.sample(1, 2)`)


* **`ValueError`:** 타입은 맞지만 연산/함수에 부적절한 값을 전달받았을 때 발생 (예: `int('1.5')`, `range(3).index(6)`)
* **`IndexError`:** 시퀀스(리스트, 튜플 등)의 범위를 벗어난 인덱스를 참조할 때 발생 (예: `empty_list[2]`)
* **`KeyError`:** 딕셔너리에 존재하지 않는 키(Key)를 조회할 때 발생 (예: `person['age']`)
* **`ModuleNotFoundError` / `ImportError`:** 존재하지 않는 모듈을 `import` 하거나 모듈 내에 없는 이름을 불러올 때 발생
* **`KeyboardInterrupt`:** 사용자가 실행 중인 프로그램을 강제 종료(`Control-C` 등)할 때 발생

---

## 4. 예외 처리 (Exception Handling)

### 예외 처리란?

예외가 발생했을 때 프로그램이 비정상적으로 튕기거나 종료되지 않고, **안전하게 오류를 처리하며 흐름을 이어가도록 하는 기법**입니다.

### `try - except - else - finally` 구조

```python
try:
    # 1. 예외가 발생할 가능성이 있는 코드 작성
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x

except ZeroDivisionError:
    # 2. 특정 예외(0으로 나누기)가 발생했을 때 실행할 코드
    print('0으로 나눌 수 없습니다.')

except ValueError:
    # 2. 특정 예외(잘못된 문자 입력 등)가 발생했을 때 실행할 코드
    print('유효한 숫자가 아닙니다.')

else:
    # 3. 예외가 전혀 발생하지 않았을 때만 실행할 코드
    print(f'결과: {y}')

finally:
    # 4. 예외 발생 여부와 상관없이 '항상' 마지막에 실행할 코드
    print('프로그램이 종료되었습니다.')

```

---


### (1) 예외 처리의 개념 및 기본 구조

* **개념:** 예외 발생 시 프로그램의 비정상 종료를 막고 안전하게 흐름을 이어가기 위해 사용합니다.
* **`try-except` 구조:**
* `try` 블록: 예외가 발생할 가능성이 있는 코드를 작성합니다.
* `except` 블록: 예외가 발생했을 때 이를 감지하여 대응/처리할 코드를 작성합니다.



---

### (2) 복수 예외 처리 (Multiple Exceptions)

하나의 `try` 블록에서 발생할 수 있는 여러 오류 유형을 구별하여 처리할 수 있습니다.

* **튜플로 여러 예외 묶기:**
발생 가능한 예외들을 `(ValueError, ZeroDivisionError)` 형태의 튜플로 묶어 공통 메시지로 처리합니다.
* **개별 `except` 블록 사용:**
오류 유형별로 별도의 `except` 블록을 구성해 세부적인 대응 메시지를 출력합니다.
* **범용 예외 처리 (`except:`):**
특정하지 않은 모든 예외를 일괄적으로 처리할 때 사용합니다.

---

### (3) `else` 및 `finally` 구문

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    # 예외가 발생하지 않았을 때만 실행되는 블록
    print(f'결과: {y}')
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 블록
    print('프로그램이 종료되었습니다.')

```

* **`else` 블록:** `try` 블록에서 **예외가 발생하지 않았을 때만** 추가 작업을 진행합니다.
* **`finally` 블록:** 예외 발생 여부와 상관없이 **항상 실행**할 코드를 작성합니다.

---

### (4) 예외 처리 시 주의사항 (상속 계층구조)

내장 예외 클래스는 부모-자식 간의 **상속 계층구조**를 가지고 있으므로 `except` 절 작성 시 순서에 유의해야 합니다.

* **상위 클래스 가로채기 문제:**
부모 클래스인 `Exception`을 하위 클래스(예: `ZeroDivisionError`)보다 위에 배치하면, 모든 예외를 상위 클래스가 먼저 가로채게 되어 아래의 세부 예외 처리 블록에 도달하지 못합니다.
* **올바른 작성 순서:**
반드시 **구체적인 하위 예외 클래스**를 먼저 작성하고, 광범위한 상위 예외 클래스(`Exception`)는 맨 마지막에 배치해야 합니다.

새로 첨부해주신 자료(예외 객체 활용, `try-except`와 `if-else` 조합, 접근 방식 비교: EAFP vs LBYL)를 반영하여 **4. 예외 처리**의 서브 항목들을 추가하고, **5. 예외 처리 접근 방식 비교** 섹션을 이어서 깔끔하게 정리했습니다.
-----


### (5) 예외 객체 다루기 (`as` 키워드)

* **예외 객체:** 예외 발생 시 해당 예외에 대한 시스템 메타데이터 및 에러 메시지를 담고 있는 인스턴스입니다.
* **`as` 키워드 활용:** `except 예외클래스 as 변수명:` 형태로 사용하여 예외 객체를 변수에 할당받아 상세한 오류 시스템 메시지를 활용할 수 있습니다.

```python
my_list = []
try:
    number = my_list[1]
except IndexError as error:
    # error 변수에 담긴 구체적인 예외 메시지('list index out of range')를 출력
    print(f'{error}가 발생했습니다.')

```

---

### (6) `try-except`와 `if-else`의 혼용

* 예외 처리 구문(`try-except`) 내부에서 조건문(`if-else`)을 함께 조합하여 더 정교한 로직 제어가 가능합니다.
* 입력 값의 타입/포맷 오류는 `try-except`로 포착하고, 값의 범주(양수/음수 등)는 `if-else`로 검사하는 방식으로 사용합니다.

```python
try:
    x = int(input('숫자를 입력하세요: '))
    if x < 0:
        print('음수는 허용되지 않습니다.')
    else:
        print('입력한 숫자:', x)
except ValueError:
    # 정수로 변환 불가능한 값 입력 시 포착
    print('오류 발생')

```

---

## 5. 예외 처리 접근 방식 비교 (EAFP vs LBYL)

파이썬 프로그래밍에서 예외를 다루는 대표적인 스타일은 **EAFP**와 **LBYL** 두 가지로 나뉩니다.

### (1) 코드 비교 예시

* **EAFP 방식:**
```python
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

```


* **LBYL 방식:**
```python
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')

```



---

### (2) EAFP와 LBYL 특성 비교

| 비교 항목 | EAFP (Easier to Ask for Forgiveness than Permission) | LBYL (Look Before You Leap) |
| --- | --- | --- |
| **핵심 철학** | **"일단 실행하고 예외를 처리"** | **"실행하기 전에 조건을 검사"** |
| **동작 방식** | 일단 코드를 실행한 뒤, 예외가 발생하면 `except` 블록에서 처리함 | 실행 전에 `if` 조건문 등으로 사전 검사하여 예외 상황을 피함 |
| **장단점** | 예외 발생 가능성을 미리 예측하여 대비하지 않아도 되나, 후처리가 필요함 | 예측 가능한 안전한 동작을 하나, 조건문이 누적되면 코드가 길고 복잡해짐 |
| **유용한 상황** | **예외 상황을 사전 예측하기 어렵거나 복잡할 때** (파이썬 권장 스타일) | **예외 상황을 사전에 완벽히 방지하고 싶을 때** |