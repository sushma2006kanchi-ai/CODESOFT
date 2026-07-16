import random
import string

print("=" * 55)
print("           PASSWORD GENERATOR")
print("=" * 55)

while True:

    print("\nPassword Options")
    print("-" * 30)

    try:
        length = int(input("Enter Password Length: "))

        if length < 4:
            print("Password length should be at least 4 characters.")
            continue

    except ValueError:
        print("Invalid Input! Please enter a valid number.")
        continue

    print("\nSelect Character Types")

    uppercase = input("Include Uppercase Letters? (Y/N): ").upper()
    lowercase = input("Include Lowercase Letters? (Y/N): ").upper()
    numbers = input("Include Numbers? (Y/N): ").upper()
    symbols = input("Include Special Characters? (Y/N): ").upper()

    characters = ""

    if uppercase == "Y":
        characters += string.ascii_uppercase

    if lowercase == "Y":
        characters += string.ascii_lowercase

    if numbers == "Y":
        characters += string.digits

    if symbols == "Y":
        characters += string.punctuation

    if characters == "":
        print("\nError: Please select at least one character type.")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n" + "=" * 45)
    print("Generated Password")
    print("=" * 45)
    print(password)
    print("=" * 45)

    again = input("\nGenerate Another Password? (Y/N): ").upper()

    if again != "Y":
        print("\nThank you for using Password Generator.")
        print("Program Closed Successfully!")
        break