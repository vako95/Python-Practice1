# def  decotarator(feeee):
#     def wrapper(*args, **kwargs):
#         print("до")
#         result = feeee(*args, **kwargs)
#         print("после")
#         return result
#     return wrapper

# @decotarator
# def myFunc():
#     print("my Funcc","raxdelite",sep="-")

# myFunc()
# exit()



# def overr(*args):
#     if len(args) == 1:
#         return args[0]
#     elif len(args) == 2:
#         return args[0] + " " + args[1]
#     else:
#         return "Invalid number of arguments"

# print(overr("Vako"))  # Выведет: Vako
# print(overr("Vako", "Huseynov"))  # Выведет: Vako Huseynov
# print(overr("Vako", "Huseynov", "extra"))  # Выведет: Invalid number