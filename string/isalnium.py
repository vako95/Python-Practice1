# text = "123456"


# if text.isalnum():
#     for x in text:
#         if int(x) % 2 == 0 :
#             print("четное число", x)
#         elif int(x) % 2 != 0:
#             print("нечетные чмсла",x)
# else:
#                 print("not found")
            
text = "12345"

cetnoye = []
necotnoye = []

if text.isalnum():
    for x in text:
        if int(x) % 2 == 0:
            cetnoye.append(x)
            # print("четные числа",x)
        # else:
            # print("нечетное",x)

print("четные", ",".join(cetnoye))
print("нечетные", ",".join(necotnoye))