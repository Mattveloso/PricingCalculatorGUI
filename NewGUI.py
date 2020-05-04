


#M
def cheapPattern():
    Cheap_Canvas = Canvas(Canvas_Frame, width=300, height=300)
    Cheap_Canvas.grid(row=0, column=0, columnspan=5, rowspan=5)

    #creates column coordenates for placement of polygons to create CHEAP PATTERN
    col1=[0,75,150,225]*10 #reoeats every 4
    col2=range(30,301,30) #Creates tuple with numbers from 30 to 300, changes every 4
    col2_altered =[]
    for value in col2: #for loop for creating a list that only changes values every 4
        for repetition in range(0,4):
            col2_altered.append(value)
    col2=col2_altered
    print(col2)
    col3=[75,150,225,300]*10 #repeats every 4
    col4=col2 #they're the same, so let's keep it equal
    col5=[55,130,205,280]*10 #repeats every 4
    col6=range(0,271,30) #changes every 4
    col6_altered =[]
    for value in col6: #for loop for creating a list that only changes values every 4
        for repetition in range(0,4): #Do this 4x before going forward
            col6_altered.append(value)
    col6=col6_altered
    print(col6)
    col7=[20,95,170,245]*10 #repeats every 4
    col8=col6

    for number in range(0,40): #as we need polygons, let's create the polygons with a for loop
        Cheap_Canvas.create_polygon(col1[number],col2[number],col3[number],col4[number],
                                    col5[number],col6[number],col7[number],col8[number],
                                    fill=colourFill.get(),outline="black")
    ColorCReset()
#\M
