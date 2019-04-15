
def fullname(full_name):
    n = ''
    t = full_name.split(' ')
    for i in t:
        n = n + (i[0])
      
    return n.upper()   

def main():
    full_name = input("What is your full name?")
    print(fullname(full_name))
if __name__ == "__main__":
    main() 



