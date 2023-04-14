# fileNotfound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an made up error")


#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abd"
# print(text + 5)


# BMI

height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)