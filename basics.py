#concatenate data types
a , b , c = 6, 7.8, "dicttion"
print("{}""{}".format("value is ", b))
print(type(b))

#datatypes
#list --> mutable --> change the value --> updation
values = ['a','b',2,43,5.6,"yeah"]
print(values[3])
values.insert(5,"babe")
print(values)

#tuple --> immutable

val = [1,2,3, "adhi"]
val[2]= 'adhi1'
print(val)

#dictionary

dic = {"a": 2, 2: "adf", "ad": "adas"}
print(dic[2])
print(dic["ad"])

dict = {}
dict['firstname'] = "adhithya"
dict['lastname'] = "narendran"
dict['concatenate'+"lastname"] = "yes" + "no"
print(dict)

#loops --> if conditiion

a = 5

if a > 3:
    print("ofcourse")
else:
    print("jerk")

#for loop

obj = [2, 3, 4, 5]

