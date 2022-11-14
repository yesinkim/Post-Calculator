```
# CFG Rule
Expr: Term Increments
Increments: Increment Increments | ε
Increment: AddOp Term

Term: Factors Scalings
Scalings: Scaling Scalings | ε
Scaling: MulOp Factors
Factors: Factor | - Factor
Factor: Number | Enclosed
Enclosed: ( Expr )

AddOp: + | -
MulOp: * | /

Number: 정규표현식으로 처리(int or float)
```

-  Input Spec
    - 사용가능한 연산자는 +, -, *, /, (, ) 총 6가지로 정의한다.
    - 사용가능한 피연산자는 정수(int), 소수점(float), 음수(negative number) 를 모두 포함한다.
    - 소수점은 소수점 앞과 뒤의 정수를 넣어 표현하는 것으로 제한한다.
    - 예를들어 .2, 2. 이런 표현식은 제한함
    - 연산자와 피연산자 사이의 공백을 허용한다. 
    - 괄호 앞 - 부호가 붙은 경우 허용


TODO
- [ ] 코드뜯어보면서 질문리스트 만들어올 것.
- [ ] 이것을 기본으로 유니테스트 테스트케이스 만들 것.
- [ ] 주석 달아보기