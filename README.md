# Post Calculator
### **TODO list**
**Google style Docstring, PEP8 권장**
- [ ] token class 상세히 만들기
- [ ] CFG 에 따라서 Tree class 만들기
- [ ] CFG에 따라서 Parse Tree 그리기

## 연산자 (+, -, *, /)를 지원하는 후위 연산계산기


- Input specification
<!-- input spec이나 test case를 상세히 촘촘하게 만들기
이렇게는 안하겠지? No 다 만들어서 예외처리 -->

    - 숫자와 연산자를 입력받는다. 
    - 숫자는 정수와 소수점 실수를 지원한다.
    - 연산자는 +, -, *, /를 지원한다.
    - 연산자는 맨 앞이나 뒤에 올 수 없다.
    - 연산자는 연속해서 올 수 없다.
    - 괄호는 피연산자와 연속해서 올 수 없다.