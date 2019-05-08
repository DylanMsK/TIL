# JavaScript Tutorial



## Introduction to JavaScript

### 1. What is JavaScript?

**[자바스크립트]([https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8](https://ko.wikipedia.org/wiki/자바스크립트))**(JavaScript)는 [객체 기반](https://ko.wikipedia.org/wiki/프로토타입_기반_프로그래밍)의 [스크립트 프로그래밍 언어](https://ko.wikipedia.org/wiki/스크립트_언어)이다. 이 언어는 [웹 브라우저](https://ko.wikipedia.org/wiki/웹_브라우저) 내에서 주로 사용하며, 다른 응용 프로그램의 내장 객체에도 접근할 수 있는 기능을 가지고 있다. 또한 [Node.js](https://ko.wikipedia.org/wiki/Node.js)와 같은 런타임 환경과 같이 서버 사이드 네트워크 프로그래밍에도 사용되고 있다. 자바스크립트는 본래 [넷스케이프 커뮤니케이션즈 코퍼레이션](https://ko.wikipedia.org/wiki/넷스케이프_커뮤니케이션즈_코퍼레이션)의 [브렌던 아이크](https://ko.wikipedia.org/wiki/브렌던_아이크)(Brendan Eich)가 처음에는 *모카*(Mocha)라는 이름으로, 나중에는 *라이브스크립트*(LiveScript)라는 이름으로 개발하였으며, 최종적으로 자바스크립트가 되었다. 자바스크립트가 [썬 마이크로시스템즈](https://ko.wikipedia.org/wiki/썬_마이크로시스템즈)의 [자바](https://ko.wikipedia.org/wiki/자바_(프로그래밍_언어))와 [구문](https://ko.wikipedia.org/wiki/구문_(프로그래밍_언어))(syntax)이 유사한 점도 있지만, 이는 사실 두 언어 모두 C 언어의 기본 구문에 바탕을 뒀기 때문이고, 자바와 자바스크립트는 직접적인 관련성이 없다. 이름과 구문 외에는 자바보다 [셀프](https://ko.wikipedia.org/w/index.php?title=셀프_프로그래밍_언어&action=edit&redlink=1)와 유사성이 많다.

2013년 1월 기준으로, 가장 최근 버전은 자바스크립트 1.8.5이고, [파이어폭스](https://ko.wikipedia.org/wiki/모질라_파이어폭스) 3에서 지원된다. 표준 ECMA-262 3판에 대응하는 자바스크립트 버전은 1.5이다. [ECMA스크립트](https://ko.wikipedia.org/wiki/ECMA스크립트)는 쉽게 말해 자바스크립트의 표준화된 버전이다. [모질라](https://ko.wikipedia.org/wiki/모질라_애플리케이션_스위트) 1.8 베타 1이 나오면서 [XML](https://ko.wikipedia.org/wiki/XML)에 대응하는 확장 언어인 [E4X](https://ko.wikipedia.org/w/index.php?title=E4X&action=edit&redlink=1)(ECMA-357)를 부분 지원하게 되었다. 자바스크립트는 브라우저마다 지원되는 버전이 다르다.

**간단히 말해 정적인 HTML의 한계를 벗어나 동적으로 사용자와 상호작용하기위해 생겨남!**



### 2. Console

로그를 확인하고 스크립트 명령어를 입력하는 패널입니다. 중단점을 건 시점의 변수를 확인할 수 있고 값을 평가하거나 수정할 수 있습니다.

- 크롬 개발자 도구 열기

  1. 크롬 브라우저 메뉴에서 `More Tools（도구 더보기）` > `Developer Tools（개발자 도구）` 선택

  2. 페이지 빈공간에 오른쪽 버튼 누르고 `Inspect(검사)` 선택

  3. MacOS - `⌘`+`⌥`+`I` 또는 Windows - `Ctrl`+`Shift`+`I`

  4. MacOS - `⌘`+`⌥`+`J` 또는 Windows - `Ctrl`+`Shift`+`J` (Console 패널)

  5. MacOS - `⌘`+`⌥`+`C` 또는 Windows - `Ctrl`+`Shift`+`C` (Elements 패널)

     

#### *Console Methods*

기타 다른 method는 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/API/Console) 을 참조

1. `console.log()`

   일반적인 로그를 출력한다. [문자열 치환](https://developer.mozilla.org/en-US/docs/Web/API/console#Using_string_substitutions)(string substitution)과 추가 인자를 사용 할 수 있다.

2. `console.info()`

   정보성 로그를 출력한다. [문자열 치환](https://developer.mozilla.org/en-US/docs/Web/API/console#Using_string_substitutions)(string substitution)과 추가 인자를 사용 할 수 있다.

3. `console.warn()`

   경고 메시지를 출력한다. [문자열 치환](https://developer.mozilla.org/en-US/docs/Web/API/console#Using_string_substitutions)(string substitution)과 추가 인자를 사용할 수 있다.

4. `console.error()`

   에러 메시지를 출력한다. [문자열 치환](https://developer.mozilla.org/en-US/docs/Web/API/console#Using_string_substitutions)(string substitution)과 추가 인자를 사용할 수 있다.

![](/Users/dylan/Desktop/github/TIL/javascript/images/console.png)

5. `console.dir()`

   객체의 사용가능한 javascript method의 리스트를 출력한다.

6. `console.count()`

   라벨이 호출된 횟수를 기록한다.

7. `console.time()`

   지정된 이름으로 [timer](https://developer.mozilla.org/en-US/docs/Web/API/console#Timers)를 시작한다. 한 페이지에서 동시에 10,000개의 타이머까지 실행이 가능하다.

8. `console.timeEnd()`

   지정된 [timer](https://developer.mozilla.org/en-US/docs/Web/API/console#Timers)를 중지하고, 타이머 시작으로 부터 경과된 시간을 출력한다.

```javascript
console.time('timer1');
for (var i = 0; i < 100000; i++);
console.timeEnd('timer1');	// timer: 0.298095603123ms
```



### 3. Comments

한 줄 주석은 `//` , 여러 줄 주석은 `/*  */`

#### *Single line comment*

```javascript
// Prints 5 to the console
console.log(5);

console.log(5);  // Prints 5 
```



#### *Multi-line comment*

```javascript
/*
This is all commented 
console.log(10);
None of this is going to run!
console.log(99);
*/

console.log(/*IGNORED!*/ 5);  // Still just prints 5 
```



### 4. Data Types

자세한 내용은 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript/Data_structures) 참조

#### *기본 타입 (Primitive Values)*

자바스크립에서는 오브젝트를 제외한 모든 값은 변경 불가능한 값 (immutable value) 이다. 예를 들자면, 특히 C 언어와는 다르게도, 문자열은 불변값 (immutable) 이다. 이런 값을 "[primitive values](Null 타입은 딱 한 가지 값, `null` 을 가질 수 있다. 더 알아보려면 [`null`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/null) 와 [Null](https://developer.mozilla.org/en-US/docs/Glossary/Null) 을 보라.)" 라고 일컫는다.

- `Boolean`

  Boolean 은 논리적인 요소를 나타내고, `true` 와 `false` 의 두 가지 값을 가질 수 있다.

- `Null`

  Null 타입은 딱 한 가지 값, `null` 을 가질 수 있다. 더 알아보려면 [`null`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/null) 와 [Null](https://developer.mozilla.org/en-US/docs/Glossary/Null) 을 보라.

- `undefined`

  값을 할당하지 않은 변수는 `undefined` 값을 가진다. 더 알아보려면 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined) 와 [Undefined](https://developer.mozilla.org/en-US/docs/Glossary/Undefined) 을 보라.

위 세 가지 타입은 상수이므로, 이것들로 다른 오브젝트를 표현할 수 없다.

- `Number`

  ECMAScript 표준에 따르면, 숫자의 자료형은 [배정밀도 64비트 형식 IEEE 754 값](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) (-(253 -1) 와 253 -1 사이의 숫자값) 단 하나만 존재한다. **정수만을 표현하기 위한 특별한 자료형은 없다.** 부동 소수점을 표현할 수 있는 것 말고도, Number 타입은 세 가지 의미있는 몇가지 상징적인 값들도 표현할 수 있다. 이 값에는 `+무한대`, `-무한대`, and `NaN` (숫자가 아님)이 있다.

  `+/-Infinity` 보다 크거나 작은지 확인하는 용도로 상수값인 [`Number.MAX_VALUE`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE) 나 [`Number.MIN_VALUE`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE) 을 사용할 수 있다. 또한, ECMAScript 6 부터는 숫자가 배정밀도 부동소수점 숫자인지 확인하는 용도로 [`Number.isSafeInteger()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger) 과 [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER), [`Number.MIN_SAFE_INTEGER`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER) 을 사용할 수 있다. 이 범위를 넘어서면, 자바스크립트의 숫자는 더 이상 안전하지 않다.

  Number 타입의 값 중에는 두 가지 방식으로 표현할 수 있는 유일한 값이 있는데, 0 이다. 0 은 -0 이나 +0 으로 표시할 수 있다. ("0" 은 물론 +0 이다.) 실제로는 이러한 사실은 거의 효력이 없다. 그 예로, `+0 === -0` 은 `true` 이다. 하지만 0으로 나누는 경우 그 차이가 눈에 띌 것이다.

  ```javascript
  > 42 / +0
  Infinity
  > 42 / -0
  -Infinity
  ```

- `String`

  자바스크립트의 [`String`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String) 타입은 텍스트 데이터를 나타내는데 사용한다. 이는 16비트 부호없는 정수 값 요소들의 집합이다. String의 각 요소는 String의 위치를 차지한다. 첫 번째 요소는 0번 인덱스에 있고, 다음 요소는 1번, 그 다음 요소는 2번... 같은 방식이다. String 의 길이는 String이 가지고있는 요소의 갯수이다.

  C 같은 언어와는 다르게, 자바스크립트의 문자열은 변경 불가능 (immutable) 하다. 이것은 한 번 문자열이 생성되면, 그 문자열을 수정할 수 없다는걸 의미한다. 그러나 원래 문자열에서 일부가 수정된 다른 문자열을 만드는건 가능하다. 예를 들자면 이렇다.

  - 원래 문자열에서 각각의 글자를 추출하거나 `String.substr()`을 사용해서 만든 부분 문자열
  - 접합 연산자 (`+`) 나 `String.concat()` 으로 두 문자열을 합친 문자열

- `Symbol`

  Symbol 은 ECMAScript 6 에서 추가되었다. Symbol은 **유일**하고 **변경 불가능한** (immutable) 기본값 (primitive value) 이다. 또한, 객체 속성의 key 값으로도 사용될 수 있다. 몇몇 프로그래밍 언어에서는 Symbol을 atom 이라고 부른다. 또, C 언어의 이름있는 열거형 (enum) 과도 비슷하다. 좀 더 자세히 알아보려면, 자바스크립트의  [Symbol](https://developer.mozilla.org/en-US/docs/Glossary/Symbol) 와 [`Symbol`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Symbol) 객체 래퍼 (wrapper) 를 보라.



#### *객체 (Objects)*

- `Properties`

  자바스크립트에서, 객체는 속성들을 담고있는 가방 (collection) 으로 볼 수 있다. [객체 리터럴 문법 (object literal syntax)](https://developer.mozilla.org/en/JavaScript/Guide/Values,_variables,_and_literals#Object_literals) 으로 제한적으로 몇 가지 속성을 초기화할 수 있고, 그러고 나서 속성들을 추가하거나 제거할 수도 있다. 속성 값은 객체를 포함해 어떠한 자료형도 될 수 있고, 그 덕분에  복잡한 데이터 구조를 형성하는게 가능해진다. 속성은 키 (key) 값으로 식별된다. 키 값은 String 이거나 Symbol 값이다.

  두 종류의 객체 속성이 있는데, 이들은 종류에 따라 특성값들을 가질 수 있다. 데이터 (data) 속성과 접근자 (accessor) 속성이 그것이다.

  - **Data Property**

    키에 값을 연결하고, 아래와 같은 특성들 (attribute) 이 있다.

    | 특성 (Attribute) | 자료형                          | 설명                                                         | 기본값    |
    | ---------------- | ------------------------------- | ------------------------------------------------------------ | --------- |
    | [[Value]]        | JavaScript 타입 <br />모두 가능 | 이 속성에 대한 get 접근으로 반환되는 값                      | undefined |
    | [[Writable]]     | Boolean                         | `false` 라면, 이 속성의 [[Value]]을 바꿀 수 없다             | false     |
    | [[Enumerable]]   | Boolean                         | `true` 라면, 이 속성은 for…in 루프에서 열거될 수 있다        | false     |
    | [[Configurable]] | Boolean                         | `flase` 라면, 이 속성은 제거될 수 없고, [[Value]]와 [[Writable]] 외에는 수정될 수 없다 | false     |

  - **Accessor Property**

    값을 가져오거나 값을 저장하기 위해 키에 하나 혹은 두 개의 접근자 함수 (get, set) 연결짓는다. 아래와 같은 특성이 있다.

    | 특성 (Attribute) | 자료형                       | 설명                                                         | 기본값    |
    | ---------------- | ---------------------------- | ------------------------------------------------------------ | --------- |
    | [[Get]]          | Function 객체 혹은 undefined | 이 속성의 값에 접근할 때마다, 인자 목록 없이 함수가 호출되고, 함수의 반환된 값으로 속성값을 가져온다. [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/get) 을 볼 것 | undefined |
    | [[Set]]          | Function 객체 혹은 undefined | 이 속성의 값이 바뀌려고 할 때마다, 할당된 값을 인자로 함수가 호출된다. [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/set) 을 볼 것 | undefined |
    | [[Enumerable]]   | Boolean                      | `true` 라면, 이 속성은 [for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) 루프에서 열거될 수 있다. | false     |
    | [[Configurable]] | Boolean                      | `false` 라면, 이 속성은 제거될 수 없고, 데이터 속성을 수정할 수 없다. | false     |

    

- `Array`

  [배열(Arrays](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array)) 는 정수키를 가지는 일련의 값들을 표현하기 위한 오브젝트이다. 배열 오브젝트에는 길이를 나타내는 'length'란 속성도 있다. 배열은 Array.prototype을 상속받으므로 배열을 다룰 때 편한 [indexOf](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array/indexOf)(배열에서 값 검색)와 [push](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Array/push) (새로운 값 추가) 같은 함수를 사용할 수 있다. 배열은 리스트나 집합을 표현하는데 적합하다.



### 5. Arithmetic Operators

- [대입 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#대입_연산자)
- [비교 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#비교_연산자)
- [산술 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#산술_연산자)
- [비트단위 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#비트단위_연산자)
- [논리 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#논리_연산자)
- [문자열 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#문자열_연산자)
- [조건 (삼항) 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#조건_(삼항)_연산자)
- [콤마 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#콤마_연산자)
- [단항 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#단항_연산자)
- [관계 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#관계_연산자)



### 6. String Concatenation

