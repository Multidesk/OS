import time

def pt(arguments):
    print('$> '+str(arguments))

def pt_chrono(M,S):
    M = str(M)
    S = str(S)

    if int(M) < 10:
        M = '0' + M
    if int(S) < 10:
        S = '0' + S

    print('$> '+ M +':'+ S, end="\r")

def pt_err(err):
    print(c_red('/!\ ')+str(err))

def ent():
    return str(input("?> "))

def pt_l(list):
    print("\n")
    for i,j in enumerate(list):
        time.sleep(0.15)
        print(str(i)+'> '+j)
        time.sleep(0.15)

def c_green(string):
    return('\033[92m'+str(string)+'\033[0m')

def c_red(string):
    return('\033[91m'+str(string)+'\033[0m')

def c_lblue(string):
    return('\033[94m'+str(string)+'\033[0m')

def c_blue(string):
    return('\033[34m'+str(string)+'\033[0m')
