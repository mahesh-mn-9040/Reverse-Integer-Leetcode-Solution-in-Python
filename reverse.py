
        x=int(input())
        rev_num = 0
        if (x < 0):
            x = -(x)
            while(x > 0):
                rev_num = rev_num*10+ x % 10
                x = int(x / 10)
            rev_num = -(rev_num)
        else:
            while(x > 0):
                rev_num = rev_num*10+ x % 10
                x = int(x / 10)    
        return rev_num if -2**31 <= rev_num <= 2**31 else 0
