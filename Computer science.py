
def birthday(n):
    if n == 1:
        return 1
    else:
        s = birthday(n-1)
        return s*(365-(n-1))/365.0


a = birthday(366)
print a



