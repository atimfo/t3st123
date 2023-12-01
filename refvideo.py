# комментарий
# НОВЫЙ комментарий
n = 0
a = int(input())
while a != 0:
    if a <= 1000 and a % 7 == 0:
        n = n + 1
    a = int(input())
    
print('количество:', n)
