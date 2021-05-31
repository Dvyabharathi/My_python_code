# step 1:
Beatles = []
#

# step 2:

Beatles.append("John Lennon")
Beatles.append("Paul")
Beatles.append("George")
#

# step 3:
for members in range(len(Beatles)//2):
    Beatles.append("Stu")
    Beatles.append("Pete")

print(Beatles)

# step 4:
del Beatles[3]
del Beatles[3]

print(Beatles)

# step 5:
Beatles.insert(0,"Ringo")

print(len(Beatles))
print(Beatles)
