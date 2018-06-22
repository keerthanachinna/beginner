def main():
print("enter the staring time")
hr1=int(input("enter the hr1"))
print(hr1)
min1=int(input("enter the min1"))
print(min1)
print("enter the current time")
hr2=int(input("enter the hr2:"))
print(hr2)
min2=int(input("enter the min2:"))
print(min2)
min=min2-min1
hr=hr2-hr1
print("the abs value:%d,%d",hr,min)
