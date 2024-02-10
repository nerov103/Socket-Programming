import os

# def change_directory():
#     '''function use to change the corrty directory'''
#     pta = input('enter your folder path and name:')
#     if pta.startswith("cd"):
#         new_dir = os.getcwd()
#         new_path = pta[3:]
#         create_path = os.path.join(new_dir, new_path)
#         return os.chdir(create_path)


# return_valu = change_directory()
# print(return_valu)

# h = "cd vic"

# print(h.encode())
# print(h.decode(h))
# print(h[3:])


#read a file
# with open("red.txt", 'r') as f:
#     re_txt = f.read()
#     print(re_txt)

print(os.getcwd())

def change_dir(peta):
    '''This Function is used to change the current directory'''
    str_pt = peta[3:]
    get_dir = os.getcwd()
    create_pat = os.path.join(get_dir, str_pt)
    os.chdir(create_pat)
    return os.getcwd()

x = change_dir('cd vic')
print(x)



