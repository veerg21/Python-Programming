# # print("hellowjq")
# a=2
# b=3
# a, b = b, a
# print(a, b)
# word="end"
# if "n" not in word:
#     print("true")
# else:
#     print("false")
# message="flyby"
# index=0
# for i in message:
#     print(index, i)
#     index=index+1
d2={"abc":"cake", "veer":"chips", "somone":"fries", "xyz":{1:"v"}}
print(d2["xyz"])
print(d2.items())
for i, j in d2.items():
    print(i, "loves to eat", j)