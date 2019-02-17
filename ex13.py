from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the file name agian:")
file_again = input(">>")

print(file_again.read())

txt.close()

file_again.close()
