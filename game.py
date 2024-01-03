import random

x = random.randint(1, 50)
print(x)

for i in range(15):
    y = int(input("猜數字0-50"))
    if y == x:
        print("正確")
        break
    else:
        if y > x:
            print("猜低一點")
        else:
            print("猜高一點")

        print("錯")
