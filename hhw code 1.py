#code to callculate percentage of given subject
sub=int(input('no of subjects: '))
a=0

for i in range(sub):
    a+=int(input(f"marks in subject {i+1}= "))
print(a)
avg=a/sub
print("your percentage is: ",avg)
if avg>=90:
    print("your grade is A")
elif avg>=80:
    print("your grade is B")
elif avg>=50:
    print("your grade is C")
elif avg>=33:
    print("your grade is D")
else:
    print("Failed")