from random import *

def get_final_sign(a, b):
    if a == b:
        return '+'
    else:
        return '-'

score = 0

for i in range(10):
    x = randint(0, 20)
    y = randint(0, 20)
    z = choice(['+', '-'])
    w = choice(['+', '-'])
    q = choice(['+', '-'])
    v = choice(['+', '-'])

    # 부호 적용
    real_x = x if get_final_sign(z, q) == '+' else -x
    real_y = y if get_final_sign(w, v) == '+' else -y

    answer = int(input('{}({}{}) {}({}{}) = '.format(z, q, abs(real_x), w, v, abs(real_y))))
    correct_answer = real_x + real_y


    if answer == correct_answer:
        print("정답!")
        score += 1
    else:
        print(f"땡! 정답은 {correct_answer}였어.")

print("너의 점수는 {}이야".format(score))