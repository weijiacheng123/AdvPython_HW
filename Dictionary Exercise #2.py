codes = {'A':'%','a':'9','B':'@','b':'#','C':'!','c':'3','D':'$','d':'4','E':'1','e':'5','F':'^','f':'6','G':'&','g':'7','H':'*','h':'8','I':'(','i':'9',

         'J':')','j':'z','K':'-','k':'x','L':'_','l':'c','M':'+','m':'v','N':'=','n':'b','O':'`','o':'n','P':'~','p':'m','Q':'{','q':'s','R':'[','r':'d',

         'S':'}','s':'f','T':']','t':'g','U':':','u':'h','V':';','v':'j','W':'"','w':'k','X':'<','x':'l','Y':'>','y':'q','Z':'0','z':'a'}

 

info_security = open('info_security.txt','r')
file_read = info_security.read()

new = ""

for i in file_read:
    if i not in codes.keys():
        new += i
    else:
        x = codes[i]
        #print(i,x)
        new += x

encrypted_file = open('encrypted.txt','w')
encrypted_file.write(new)
encrypted_file.close()

print(new)