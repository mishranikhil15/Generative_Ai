def reverse_string(str):
    n=len(str)
    # print(n)
    bag=""
    for i in range(n,0,-1):
       bag=bag+str[i-1]
    print(bag)   
str="Python is fun"
reverse_string(str)