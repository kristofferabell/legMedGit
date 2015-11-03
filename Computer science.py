
def birthday(n):
    if n == 1:
        return 1
    else:
        s = birthday(n-1)
        return s*(365-(n-1))/365.0



a = birthday(1)

<<<<<<< HEAD
print a

# Mangler kommentar
# kommentarer!!!!!!!
print "Hello, World!"

=======
print "ER I GLAR?!?!?!?"
>>>>>>> 5a5bc4bd018f41a497d4b0c792cf267e118550aa

print "S7-LAN FTW"
