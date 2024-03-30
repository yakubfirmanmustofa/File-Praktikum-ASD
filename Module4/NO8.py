from random import randint as r
Answer = r(1,100)
al = list(range(0,100))
i= 1
print(Answer)
front = 0
back = 99
while True:
    x = int(input("Masukkan tebakan dari("+ str(al[front]) + ","+ 
str(al[back]+1) + ") ke-%i:> " %i))
    mid = (front + back) // 2
    if x == Answer:
        print("BENAR SEKALI")
        break
    elif x < Answer:
        front = x + 1
        print("TO THE RIGHT")
    elif x > Answer:
        back = x - 2
        print("TO THE LEFT")
    i+=1
