# Банкомат выдает сумму максимально возможными купюрами

summ=int(input("Введите требуемую сумму:\n"))
a=[10, 20, 50, 100, 200, 500, 1000]
n=1

if summ%10==0:
    while n<=7 and summ>0:
        b=summ//a[len(a)-n]
        summ=summ%a[len(a)-n]
        if b>0:
            print(str(b)+"*"+str(a[len(a)-n]), end= "   ")
        n += 1
else:
    print("Нет доступных банкнот")


