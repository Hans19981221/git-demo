import random

start = 1
end = 50

x = random.randint(start, end)
print(f"範圍:{start}~{end}")

# print(x)


for i in range(3):
    y = int(input(f"猜數字0-50({start}~{end}):"))
    if y == x:
        print("正確")
        break
    else:
        if y > x:
            print("猜低一點")
            if end > y:
                end = y - 1
        else:
            if start < y:
                print("猜高一點")
            start = y + 1

        print("錯")

if y != x:
    print(f"猜錯了。答案是:{x}")
else:
    print(f"猜對了，共猜{i+1}次")
