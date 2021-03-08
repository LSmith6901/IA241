"""
lec 7 for loop
"""

i = 5
while i >= 0:
    
    try:
        print(1/(i-3))
    except:
        pass
    i = i -1
    
    # if i ==3:
    #     continue
    
    # print(i)

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('zero division error')
    
# except:
#     print('other errors')