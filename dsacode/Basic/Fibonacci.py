prev=0
next=1
print(prev)
print(next)
for i in range(5):
    printnumber= prev + next
    print(printnumber)
    prev= next
    next =printnumber