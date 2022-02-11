a = ['53:14', '245435:543645']
for i in a:
    ind = i.index(':')
    score1 = i[0:ind]
    score2 = i[ind+1:len(i)]
    print('score1 :', score1)
    print('score2 :', score2)
