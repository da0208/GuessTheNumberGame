import random

def guess_the_number():
    n = int(input("最小値を入力してください: "))
    m = int(input("最大値を入力してください: "))

    while n > m:
        print("最小値は最大値以下である必要があります。")
        n = int(input("最小値を再度入力してください: "))
        m = int(input("最大値を再度入力してください: "))

    random_number = random.randint(n,m)

    for i in range(5):
        guess = int(input(f"{n} から {m} の間の数値を推測してください: "))
        if guess == random_number:
            print("おめでとうございます、正解です！")
            return
        elif guess < random_number:
            print("もっと大きい数です。")
        else:
            print("もっと小さい数です。")

    print("試行回数が上限に達しました。正解は {} でした。".format(random_number))

guess_the_number()
