from tkinter import *

root = Tk()
root.geometry("1300x600")
root.bg = "green"
root.title("PRESENT WRAPPING AND GIFT CARDS")
global colourFill
colourFill = StringVar()
Top_Frame = Frame(root, width=1350, height=100, bd=12, relief="raise", bg="Green")
Top_Frame.grid(row=0)
MainTitle = Label(Top_Frame, font=("arial", 30, "bold"), text="WELCOME TO BIBS PRESENT WRAPPING & GIFT CARDS")
MainTitle.grid(row=0, column=0)

BottomMainFrame = Frame(root, width=1350, height=650, bd=4, relief="raise")
BottomMainFrame.grid(row=1)

Paper_Type_Main_Frame = Frame(BottomMainFrame, width=300, height=650, bd=4, relief="raise")
Paper_Type_Main_Frame.grid(row=0, column=0)
Paper_Type_Tops_Frame = Frame(Paper_Type_Main_Frame, width=300, height=300, bd=4, relief="raise")
Paper_Type_Tops_Frame.grid(row=1, column=0)
Present_Type_Frame = Frame(Paper_Type_Main_Frame, width=300, height=300, bd=4, relief="raise")
Present_Type_Frame.grid(row=2)
Canvas_Frame = Frame(Paper_Type_Main_Frame, width=300, height=300, bd=4, relief="raise")
Canvas_Frame.grid(row=1, column=1)
Colour_Frame_Button = Frame(Paper_Type_Main_Frame, width=300, height=300, bd=4, relief="raise")
Colour_Frame_Button.grid(row=2, column=1)

varCheapPattern = IntVar()
varCheapPattern.set(0)
varExpensivePattern = IntVar()
varExpensivePattern.set(0)
var_Cube = IntVar()
var_Cube.set(0)
var_Cuboid = IntVar()
var_Cuboid.set(0)
var_Cylinder = IntVar()
var_Cylinder.set(0)
varCheapPaper = StringVar()
varCheapPaper.set('0')
varExpensivePaper = StringVar()
varExpensivePaper.set('0')
varBow = StringVar()
varBow.set('0')
varGiftCardFlatRate = StringVar()
varGiftCardFlatRate.set("0")
varGiftCardPerCharacterRate = StringVar()
varGiftCardPerCharacterRate.set(' ')

Present = Label(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), text="PAPER TYPE, BOW & CARDS")
Present.grid(row=0, column=0)
CheapPaper = Checkbutton(Paper_Type_Tops_Frame, text="Cheap Paper\t\t\t\t£0.04p per cm2", variable=varCheapPaper,
                         onvalue=1, offvalue=0, font=("arial", 18, "bold")).grid(row=1, column=0, sticky=W)
Entry(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), textvariable=varCheapPaper, width=6, state=NORMAL).grid(row=1,
                                                                                                                 column=1)
ExpensivePaper = Checkbutton(Paper_Type_Tops_Frame, text="Expensive Paper\t\t\t\t£0.75p per cm2",
                             variable=varExpensivePaper, onvalue=1, offvalue=0, font=("arial", 18, "bold")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
Entry(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), textvariable=varExpensivePaper, width=6,
      state=NORMAL).grid(row=2, column=1)
Bow = Checkbutton(Paper_Type_Tops_Frame, text="Bow\t\t\t\t\t£1.50p", variable=varBow, onvalue=1, offvalue=0,
                  font=("arial", 18, "bold")).grid(row=3, column=0, sticky=W)
Entry(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), textvariable=varBow, width=6, state=NORMAL).grid(row=3,
                                                                                                          column=1)
GiftCardFlatRate = Checkbutton(Paper_Type_Tops_Frame, text="Gift Card (Flat Rate\t\t\t£0.50p)",
                               variable=varGiftCardFlatRate, onvalue=1, offvalue=0, font=("arial", 18, "bold")).grid(
    row=4,
    column=0, sticky=W)
Entry(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), textvariable=varGiftCardFlatRate, width=6, state=NORMAL).grid(
    row=4, column=1)
GiftCardPerCharacterRate = Checkbutton(Paper_Type_Tops_Frame, text="Gift Card (Per Character Rate £0.02p)",
                                       variable=varGiftCardPerCharacterRate, font=("arial", 18, "bold")).grid(row=5,
                                                                                                              column=0,
                                                                                                              sticky=W)

Entry(Paper_Type_Tops_Frame, font=("arial", 16, "bold"), textvariable=varGiftCardPerCharacterRate, width=10,
      state=NORMAL).grid(row=5, column=1)

#M: I can probably make this better also
Presents = Label(Present_Type_Frame, font=("arial", 18, "bold"), text="Present Types Shapes\t\t")
Presents.grid(row=0, column=1)
Checkbutton(Present_Type_Frame, text='Cube Shape Sizes\t\t\t', variable=var_Cube).grid(row=1, column=0, sticky=W)
Label(Present_Type_Frame, text='Length', justify='right').grid(row=3, column=0)
Entry(Present_Type_Frame, width=6, textvariable=var_Cube).grid(row=3, column=0, sticky=W)
Checkbutton(Present_Type_Frame, text='Cuboid Shape Sizes', variable=var_Cuboid).grid(row=1, column=1, sticky=W)
Entry(Present_Type_Frame, width=6, textvariable=var_Cuboid).grid(row=2, column=1, sticky=W)
Label(Present_Type_Frame, text='Length', justify='right').grid(row=2, column=1)
Entry(Present_Type_Frame, width=6, textvariable=var_Cuboid).grid(row=3, column=1, sticky=W)
Label(Present_Type_Frame, text='Height', justify='right').grid(row=3, column=1)
Entry(Present_Type_Frame, width=6, textvariable=var_Cuboid).grid(row=4, column=1, sticky=W)
Label(Present_Type_Frame, text='Width', justify='right').grid(row=4, column=1)
Checkbutton(Present_Type_Frame, text='Cylinder Shape Sizes', variable=var_Cylinder).grid(row=1, column=2, sticky=W)
Entry(Present_Type_Frame, width=6, textvariable=var_Cylinder).grid(row=2, column=2, sticky=W)
Label(Present_Type_Frame, text='Height', justify='right').grid(row=3, column=0)
Entry(Present_Type_Frame, width=6, textvariable=var_Cylinder).grid(row=3, column=2, sticky=W)
Label(Present_Type_Frame, text='Radius', justify='right').grid(row=3, column=0)


def Reset_Button():
    var_Cube.set(0)
    var_Cuboid.set(0)
    var_Cylinder.set(0)
    varGiftCardPerCharacterRate.set(' ')
    varGiftCardFlatRate.set('0')
    varCheapPaper.set('0')
    varExpensivePaper.set('0')
    varBow.set('0')
    var_Cube.get()
    cheapPattern()
    ColorEReset()
    ColorCReset()
    expensivePattern()
    varCheapPattern.set(0)
    varExpensivePattern.set(0)


def cheapPattern_1():
    if varCheapPattern.get() == 1:
        Check_Cheap.configure(state=NORMAL)
    elif varCheapPattern.get() == 0:
        Check_Cheap.configure(state=DISABLED)


def expensivePattern_1():
    if varExpensivePattern.get() == 1:
        Check_Expensive.configure(state=NORMAL)
    elif varExpensivePattern.get() == 0:
        Check_Expensive.configure(state=DISABLED)


def ColorCReset():
    varCheapPaper.set(0)


def ColorEReset():
    varCheapPaper.set(0)
    return


def Purple():
    colourFill.set("purple")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()


def DarkSlateGray():
    colourFill.set("DarkSlateGray4")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()


def DeepSkyBlue():
    colourFill.set("DeepSkyBlue")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()


def LightSeaGreen():
    colourFill.set("LightSeaGreen")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()


def VioletRed():
    colourFill.set("VioletRed")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()


def Gold():
    colourFill.set("Gold")
    if varExpensivePaper.get() == 1:
        expensivePattern()
    elif varCheapPaper.get() == 1:
        cheapPattern()

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

#Below I've hidden the code from the first attempt
# def cheapPattern(): #M: This is something that you should avoid at all cost. Substitute for loops or use numpy
#     Cheap_Canvas = Canvas(Canvas_Frame, width=300, height=300)
#     Cheap_Canvas.grid(row=0, column=0, columnspan=5, rowspan=5)
#     Cheap_Canvas.create_polygon(0, 30, 75, 30, 55, 0, 20, 0, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 30, 150, 30, 130, 0, 95, 0, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 30, 225, 30, 205, 0, 170, 0, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 30, 300, 30, 280, 0, 245, 0, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 60, 75, 60, 55, 30, 20, 30, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 60, 150, 60, 130, 30, 95, 30, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 60, 225, 60, 205, 30, 170, 30, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 60, 300, 60, 280, 30, 245, 30, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 90, 75, 90, 55, 60, 20, 60, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 90, 150, 90, 130, 60, 95, 60, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 90, 225, 90, 205, 60, 170, 60, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 90, 300, 90, 280, 60, 245, 60, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 120, 75, 120, 55, 90, 20, 90, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 120, 150, 120, 130, 90, 95, 90, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 120, 225, 120, 205, 90, 170, 90, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 120, 300, 120, 280, 90, 245, 90, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 150, 75, 150, 55, 120, 20, 120, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 150, 150, 150, 130, 120, 95, 120, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 150, 225, 150, 205, 120, 170, 120, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 150, 300, 150, 280, 120, 245, 120, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 180, 75, 180, 55, 150, 20, 150, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 180, 150, 180, 130, 150, 95, 150, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 180, 225, 180, 205, 150, 170, 150, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 180, 300, 180, 280, 150, 245, 150, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 210, 75, 210, 55, 180, 20, 180, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 210, 150, 210, 130, 180, 95, 180, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 210, 225, 210, 205, 180, 170, 180, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 210, 300, 210, 280, 180, 245, 180, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 240, 75, 240, 55, 210, 20, 210, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 240, 150, 240, 130, 210, 95, 210, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 240, 225, 240, 205, 210, 170, 210, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 240, 300, 240, 280, 210, 245, 210, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 270, 75, 270, 55, 240, 20, 240, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 270, 150, 270, 130, 240, 95, 240, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 270, 225, 270, 205, 240, 170, 240, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 270, 300, 270, 280, 240, 245, 240, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(0, 300, 75, 300, 55, 270, 20, 270, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(75, 300, 150, 300, 130, 270, 95, 270, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(150, 300, 225, 300, 205, 270, 170, 270, fill=colourFill.get(), outline="black")
#     Cheap_Canvas.create_polygon(225, 300, 300, 300, 280, 270, 245, 270, fill=colourFill.get(), outline="black")
#     ColorCReset()


def expensivePattern(): #M: Also avoid
    Expensive_Canvas = Canvas(Canvas_Frame, width=300, height=300)
    Expensive_Canvas.grid(row=0, column=0, columnspan=5, rowspan=5)
    Expensive_Canvas.create_rectangle(0, 0, 150, 150, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(150, 150, 300, 300, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(180, 120, 300, 0, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(210, 90, 300, 0, fill='white', outline='black')
    Expensive_Canvas.create_rectangle(240, 60, 300, 0, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(0, 180, 120, 300, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(0, 210, 90, 300, fill='white', outline='black')
    Expensive_Canvas.create_rectangle(0, 240, 60, 300, fill=colourFill.get(), outline='black')
    Expensive_Canvas.create_rectangle(0, 270, 30, 300, fill='white', outline='black')
    Expensive_Canvas.create_rectangle(270, 30, 300, 0, fill='white', outline='black')
    ColorEReset()


Check_Cheap = Checkbutton(Colour_Frame_Button, text='cheap pattern', variable=varCheapPattern, command=cheapPattern)
Check_Cheap.grid(row=0, column=0, sticky=NSEW)
Check_Expensive = Checkbutton(Colour_Frame_Button, text='expensive pattern', variable=varExpensivePattern,
                              command=expensivePattern)
Check_Expensive.grid(row=0, column=3, sticky=NSEW)

#M: I think he could probably optimize this (show him)
buttonPurple = Button(Colour_Frame_Button, text="Purple", bg="Purple", command=Purple)
buttonPurple.grid(row=2, column=0, sticky=NSEW)
buttonDarkSlateGray = Button(Colour_Frame_Button, text="Dark Slate Gray", bg="DarkSlateGray4", command=DarkSlateGray)
buttonDarkSlateGray.grid(row=2, column=1, sticky=NSEW)
buttonDeepSkyBlue = Button(Colour_Frame_Button, text="Deep Sky Blue", bg="Deep Sky Blue", command=DeepSkyBlue)
buttonDeepSkyBlue.grid(row=2, column=2, sticky=NSEW)

buttonLightSeaGreen = Button(Colour_Frame_Button, text="Light Sea Green", bg="Light Sea Green", command=LightSeaGreen)
buttonLightSeaGreen.grid(row=3, column=0, sticky=NSEW)
buttonVioletRed = Button(Colour_Frame_Button, text="VioletRed", bg="VioletRed2", command=VioletRed)
buttonVioletRed.grid(row=3, column=1, sticky=NSEW)
buttonGold = Button(Colour_Frame_Button, text="Gold", bg="Gold", command=Gold)
buttonGold.grid(row=3, column=2, sticky=NSEW)
Reset_Button = Button(Paper_Type_Main_Frame, text='Reset', width=10, command=Reset_Button)
Reset_Button.grid(row=3, column=0, sticky=W)

root.mainloop()
