# 3
# 2
# 5
# 1

# min=-1.00
# max=4.00
# sum=5.00
# avg=1.67

num = int(input())
lst = []
for _ in range(num):
    current_num = float(input())
    lst.append(current_num)


print(f'min={min(lst):.2f}')
print(f'max={max(lst):.2f}')
print(f'sum={sum(lst):.2f}')
print(f'avg={sum(lst) / len(lst):.2f}')


