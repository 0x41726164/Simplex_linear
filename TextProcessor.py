from TextFunctions import popup,load,draw,simplex

motherset = {
0:["0","exit","end","quit"],
1:["1","help"],
2:["2","load"],
3:["3","simp"],
4:["4"],
}

popup()
print("")
while(1):
    cmnd = input("> ")
    if cmnd in motherset[0]:
        break
    elif cmnd in motherset[1]:
        popup()
    elif cmnd in motherset[2]:
        temp = load()
        matrix = temp[0]
        counter_r = temp[1]
        counter_c = temp[2]
        draw(matrix,counter_r,counter_c)
    elif cmnd in motherset[3]:
        matrix=simplex(matrix,counter_r,counter_c)
        draw(matrix,counter_r,counter_c)
    elif cmnd in motherset[4]:
        break
