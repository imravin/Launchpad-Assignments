d={}
print("No. of students")
n=int(input())
# d=dict(input().split() for i in range(n))
for i in range(n):
    print("Enter your usn: ")
    usn=input()
    print("Enter your name: ")
    name=input()
    d[usn]=name
print(d)