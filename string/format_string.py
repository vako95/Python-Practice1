# text = "hello"

# say = f"{text} world"

# print(say)

# text = "Книга '{title}' была написана автором {author} и издана в {year} году.".format(
#  title="New",
#     author="vako", 
#     year=95
# )
# print(text)

text = "Hello world,  hello Python!"

x = text.lower().count("hello")

if x > 0:
    print("yes",x)