string = input()
size = len(string)
string_changed=string
line1=""
line2=0
line3=""
letters_1=['a','e','i','o','u','y']
letters_2=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
for i in range(5,-1,-1):
    for y in range(0,size):
        if string[y]==letters_1[i]:
            line1+=(letters_1[i])
            line2+=1

for i1 in range(len(letters_2)-1,-1,-1):
    for y1 in range(0,size):
        if string[y1]==letters_2[i1]:
            line3+=(letters_2[i1])


print("("+line1+ ", " +str(line2)+ ", "+line3+")")
