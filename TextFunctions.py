motherset = {
"symbols":['(',')','+','-','*','/','=','<=','>='],
"alphabet":['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
}

def popup():
    file = open("popup.txt")
    for line in file:
        print(line,end="")

def draw(matrix, counter_r, counter_c):
    for i in range(counter_r):
        print("  |",end="")
        for j in range(counter_c):
            if matrix[i][j] <= 9 and matrix[i][j] >= 0:
                print("",matrix[i][j],end="| ")
            else:
                print(matrix[i][j],end="| ")
        print("")

# -------------------------------- loading -------------------------------------

def load():
    # counter_constraints = 0
    counter_r = 0 # row
    counter_c = 1 # column (1 for R.H.D (result(s))) o_O
    index_dict = dict() # keeper
    file = open("TextSamples.txt")

    # processing the file
    for line in file:
        counter_r += 1
        index_dict[counter_r] = list() # a list for each row
        for seg in line.split():
            if seg not in motherset["symbols"] and seg not in motherset["alphabet"]:
                # print(seg,end=" ")
                index_dict[counter_r].append(seg) # filling the semi-matrix
            elif seg in motherset["alphabet"] and counter_r == 1:
                counter_c += 1

    # filling the matrix
    matrix = [[0 for x in range(counter_c)] for y in range(counter_r)]
    for i in range(counter_r):
        for j in range(counter_c):
            matrix[i][j] = int(index_dict[i+1][j])

    return matrix,counter_r,counter_c

# --------------------------------- simplex ------------------------------------

def simplex(matrix,counter_r,counter_c):
    ne=0 # all negative elements
    for i in range(counter_c):
        if matrix[0][i] < 0:
            ne+=1

    for i in range(ne):
        matrix=sim1(matrix,counter_r,counter_c)
    return matrix

def sim1(matrix, counter_r, counter_c):
    pivot_c = 0
    pivot_r = 0
    pivot_number = 0

    # finding the minimum number of first row to find the privot column
    min=matrix[0][0]
    for i in range(counter_c):
        if matrix[0][i] < min:
            min = matrix[0][i]
            pivot_c = i
    print("  min is", min)
    print("  pivot column", pivot_c+1)

    # finding pivot row and pivot number
    pivot_r = matrix[1][counter_c-1]
    for i in range(counter_r-1):
        if matrix[i+1][counter_c-1]/matrix[i+1][pivot_c] < pivot_r:
            pivot_r = i+1
            pivot_number = matrix[i+1][pivot_c]
    print("  pivot row is", pivot_r+1)
    print("  pivot number", pivot_number)

    # dividing all elements of pivot row by pivot number
    for i in range(counter_c):
        matrix[pivot_r][i] /= pivot_number
    draw(matrix,counter_r,counter_c)
    print("")

    # zero-ing the pivot column
    for i in range(counter_r-1):
        invs = matrix[i][pivot_c] * (-1)
        for j in range(counter_c):
            matrix[i][j] += invs * matrix[pivot_r][j]
    draw(matrix,counter_r,counter_c)
    return matrix
