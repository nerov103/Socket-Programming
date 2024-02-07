from base64 import b64encode, b64decode



#createa a function for read the file in thos function
def read_fun(file_path):
    with open(file_path, "rb")as file:
        return b64encode(file.read())
    
main_input = str(input("enter your file name:"))
main_input = main_input.split()
if main_input[0]=="uplod":
    result = read_fun(main_input[1])
    main_input.append(result)


print(main_input)
print(type(main_input))


