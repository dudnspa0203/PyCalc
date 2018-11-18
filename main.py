import calc

sub_routine = calc.calc_routine()
next(sub_routine)
print("계산기를 시작합니다.")
while True:
    chars = input("숫자를 입력하세요.")
    if chars == "EOF":
        break
    print(sub_routine.send(chars))


print("계산기 종료")
