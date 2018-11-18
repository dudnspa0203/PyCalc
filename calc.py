def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x + y

def div(x, y):
    return x + y

def calc_routine():
    calcstr = ""
    hasOp = False
    while True:
        x = (yield calcstr)


        if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
            calcstr += x
            hasOp = False

        elif x == ".":
            calcstr += x
            hasOp = False

        elif x == "c":
            calcstr == ""
            hasOp = False

        elif x == "<-":
            calcstr[-1] = ""
            calcstr.rstrip()
            hasOp = False

        elif x == '+' or x == '-' or x == '*' or '/':
            if hasOp:
                print("이미 연산자가 입력 되어 있습니다.")
            else:
                calcstr += x
                hasOp = True



            '''
            어떻게 하면 분기 수를 줄일 수 있을까
            계산기를 시작합니다.
            숫자를 입력하세요.1
            1
            숫자를 입력하세요.0
            10
            숫자를 입력하세요.+
            10+
            숫자를 입력하세요.+
            이미 연산자가 입력 되어 있습니다.
            
            숫자를 입력하세요.3
            10++
            숫자를 입력하세요.
            
            문자열을 통한 계산 처리
            문자열 스플릿 또는 스택 이용
            '''

