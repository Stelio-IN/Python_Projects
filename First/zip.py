#zip(*iterables)

usernames = ["SIN","INVO","SAM"]
passwords = ["p@ssword","abc123","involution"]

users = zip(usernames, passwords)
print(type(users))
for i in users:
    print(i)

print("<><<><><><><><><><><><><><><><><><><>")
users_list = list(zip(usernames, passwords))

print(type(users_list))
for i in users_list:
    print(i)

print("<><<><><><><><><><><><><><><><><><><>")
user_dic = dict(zip(usernames, passwords))

print(type(user_dic))

for key,value in user_dic.items():
    print(key +" : "+value)