

check = "L"

#Button Functions
#-------------------------------------------------------------------------
def Choice():
    global check
    if Course_Score.get() == 1 :
        Literal_Options.grid_forget()
        Percentage_Entry.configure(state = NORMAL)
        check = "P"

    elif Course_Score.get() == 0 :
        Percentage_Entry.delete(0,END)
        Percentage_Entry.configure(state = DISABLED)
        Literal_Options.grid(row = 0 ,column = 1)
        check = "L"

Courses_Number = 0

def Add_Course():
    global Courses_Number ,check ,point
    score = DoubleVar()
    point = DoubleVar()
    if check == "P" :
        try :
            Percentage = float(Percentage_Entry.get())
            if Percentage >= 0.0 and Percentage <= 100.0 :
                if Percentage >= 93.0 and Percentage <= 100.0 :
                    point = 4.0
                elif Percentage >= 89.0 and Percentage < 93.0 :
                    point = 3.7
                elif Percentage >= 84.0 and Percentage < 89.0 :
                    point = 3.3
                elif Percentage >= 80.0 and Percentage < 84.0 :
                    point = 3.0
                elif Percentage >= 76.0 and Percentage < 80.0 :
                    point = 2.7
                elif Percentage >= 73.0 and Percentage < 76.0 :
                    point = 2.3
                elif Percentage >= 70.0 and Percentage < 73.0 :
                    point = 2.0
                elif Percentage >= 67.0 and Percentage < 70.0 :
                    point = 1.7
                elif Percentage >= 64.0 and Percentage < 67.0 :
                    point = 1.3
                elif Percentage >= 60.0 and Percentage < 64.0 :
                    point = 1.0
                elif Percentage < 60.0 :
                    point = 00.0

                Courses_Number += 1
                Courses_Number_Display.configure(text = Courses_Number)
                HoursList.append(hours.get())
                Hours_Number_Display.configure(text = sum(HoursList))
                ScoreList.append(point)
                score = point
                TotalList.append( float(score * hours.get()) )

            else :
                Percentage_Entry.delete(0 ,END)
                tkinter.messagebox.showerror("ERROR !" ,"You must enter a value between 0 and 100")

        except ValueError :
            Percentage_Entry.delete(0 ,END)
            tkinter.messagebox.showerror("ERROR !" ,"You must enter a value between 0 and 100")

    elif check == "L" :
        Courses_Number += 1
        Courses_Number_Display.configure(text = Courses_Number)
        HoursList.append(hours.get())
        Hours_Number_Display.configure(text = sum(HoursList))
        ScoreList.append(Literal_Points.get(letter.get()))
        score = Literal_Points.get(letter.get())
        TotalList.append( float(score * hours.get()) )

def Undo() :
    global Courses_Number
    if len(TotalList) != 0 :
        HoursList.pop()
        ScoreList.pop()
        TotalList.pop()
        Courses_Number -= 1
        if Courses_Number == 0 and sum(HoursList) == 0 :
            Courses_Number_Display.configure(text = "")
            Hours_Number_Display.configure(text = "")
            Letter.configure(text = "")
        else :
            Courses_Number_Display.configure(text = Courses_Number)
            Hours_Number_Display.configure(text = sum(HoursList))

        Percentage_Entry.delete(0 ,END)
        GPA_Display.configure(text = "")
        Grade_Display.configure(text = "")
        Load_Display.configure(text = "")


    else: tkinter.messagebox.showwarning("Warning !" ,"You didn't add any course to undo addition")


def Caculate_GPA() :
    if sum(HoursList) != 0 :
        gpa = float(sum(TotalList)/sum(HoursList))
        print ("Course Points * Hours = ")
        print (sum(TotalList))
        print ("Hours = ")#93
        print (sum(HoursList))
        grade = StringVar()
        load = StringVar()
        f_color = StringVar()
        let = StringVar()
        
        if gpa == 4.0:
            grade = "Excellent"
            f_color = "green"
            let = "A"
            load = "Full Load"
        elif gpa >= 3.7 and gpa <= 4.0 :
            grade = "Excellent"
            f_color = "green"
            let = "A-"
            load = "Full Load"
        elif gpa >= 3.3 and gpa < 3.7 :
            grade = "Excellent"
            f_color = "green"
            let = "B+"
            load = "Full Load"
        elif gpa >= 3.0 and gpa < 3.3 :
            grade = "Very Good"
            f_color = "#000fff000"
            let = "B"
            load = "Full Load"
        elif gpa >= 2.7 and gpa < 3.0 :
            grade = "Very Good"
            f_color = "#000fff000"
            let = "B-"
            load = "Full Load"
        elif gpa >= 2.3 and gpa < 2.7 :
            grade = "Good"
            f_color = "orange"
            let = "C+"
            load = "Full Load"
        elif gpa >= 2.0 and gpa < 2.3 :
            grade = "Good"
            f_color = "orange"
            let = "C"
            load = "Full Load"
        elif gpa >= 1.7 and gpa < 2.0 :
            grade = "Good"
            f_color = "orange"
            let = "C-"
            load = "Half Load"
        elif gpa >= 1.3 and gpa < 1.7 :
            grade = "Pass"
            f_color = "magenta"
            let = "D+"
            load = "Half Load"
        elif gpa >= 1 and gpa < 1.3 :
            grade = "Pass"
            f_color = "magenta"
            let = "D"
            load = "Half Load"
        elif gpa < 1.0 :
            grade = "Weak"
            f_color = "red"
            let = "F"
            load = "Half Load"
        else :
            grade = "asd"
            let = "asd"
            load = "asd"



        GPA_Display.configure(text = round(gpa ,3))
        Grade_Display.configure(text = grade ,fg = f_color)
        Load_Display.configure(text = load, fg = f_color)
        Letter.configure(text = let)

    else :tkinter.messagebox.showwarning("Warning !" ,"You must add a course to be calculated")

def New():
    global check ,Courses_Number
    CheckBtn.deselect()
    Courses_Number = 0
    Percentage_Entry.delete(0,END)
    Percentage_Entry.configure(state = DISABLED)
    Literal_Options.grid(row = 0 ,column = 1)
    check = "L"
    Courses_Number_Display.configure(text = "")
    Hours_Number_Display.configure(text = "")
    GPA_Display.configure(text = "")
    Grade_Display.configure(text = "")
    Load_Display.configure(text = "")
    Letter.configure(text = "")
    
    ScoreList.clear()
    HoursList.clear()
    TotalList.clear()

def About():
    root.maxsize(width = 280 ,height = 400)
    tkinter.messagebox.showinfo("" ,"A GPA Calculator based on the grading system applied in Alexandria University\nSupervised By:\nDr. Hossam Abdelbaki\nMade by: Team 72\nMohamed Yasser and Monica Ihab\nThird Year Communication.")
    root.maxsize(width = 280 ,height = 270)

# ROOT
#-------------------------------------------------------------------------
root = Tk()
root.title("GPA Calculator")

letter = StringVar()
letter.set("A")
hours = IntVar()
Course_Score = IntVar()
ScoreList = []
HoursList = []
TotalList = []
Literal_Points = {'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':00.0}

# TOP FRAME
#-------------------------------------------------------------------------
Top_Frame = Frame(root)
Top_Frame.pack(side = TOP)

Course_Score_Hours = LabelFrame(Top_Frame ,relief = FLAT)
Course_Score_Hours.pack(side = TOP )

#Defining Boxes
Course_Score_LabelFrame = LabelFrame(Course_Score_Hours ,text = "Course Score")
Course_Score_LabelFrame.pack(side = RIGHT ,padx = 5)

Hours_lblFrame = LabelFrame(Course_Score_Hours ,text = "Course Hours")
Hours_lblFrame.pack(side = BOTTOM ,padx = 5)

Subj_lblFrame = LabelFrame(Course_Score_Hours ,text = "Course Name")
Subj_lblFrame.pack(side = TOP ,padx = 5)

#Course Score Box Components
Label(Course_Score_LabelFrame ,text = "Literal Grade").grid(row =0)
CheckBtn = Checkbutton(Course_Score_LabelFrame ,text = "Percentage   " ,variable = Course_Score ,onvalue = 1 ,offvalue = 0 ,command = Choice)#Percentage Check Button
CheckBtn.grid(row = 1)

Percentage_Entry = Entry(Course_Score_LabelFrame ,width = 5 ,state = DISABLED) #Percentage Entry
Percentage_Entry.grid(row = 1 ,column = 1)

Label(Course_Score_LabelFrame ,text = "%").grid(row = 1 ,column = 3)

Literal_Options = OptionMenu(Course_Score_LabelFrame ,letter ,"A","A-" ,"B+" ,"B" ,"B-","C+" ,"C" ,"C-","D+" ,"D" ,"F" )#Grade Options Menu
Literal_Options.grid(row = 0 ,column = 1)

#Course Hours Box Components
Radiobutton(Hours_lblFrame ,text = "1" ,variable = hours ,value = 1).pack(side = LEFT) #For 1 Credit Hour Courses
Radiobutton(Hours_lblFrame ,text = "2" ,variable = hours ,value = 2).pack(side = LEFT)  #For 2 Credit Hours Courses
Hours_RadioBtn = Radiobutton(Hours_lblFrame ,text = "3" ,variable = hours ,value = 3) #For 3 Credit Hours Courses
Hours_RadioBtn.pack(side = RIGHT)
Hours_RadioBtn.select()

#Course Name Box Components
Label(Subj_lblFrame ,text = "Course: ").grid(row =0)
Subject_Entry = Entry(Subj_lblFrame ,width = 10) #Course Name Entry
Subject_Entry.grid(row = 0 ,column = 2)
Label(Subj_lblFrame ,text = " ").grid(row = 0 ,column = 3)

GPA_Grade_Frame = Frame(Top_Frame ,relief = FLAT)
GPA_Grade_Frame.pack(side = BOTTOM ,pady = 5)

Button(GPA_Grade_Frame ,text = "Add Course" ,command = Add_Course ,bg = "#e6e6e6").grid(row = 0 ,pady = 5) #Add Course Button

Button(GPA_Grade_Frame ,text = "Undo" ,command = Undo).grid(row = 1) #Undo Button 

Label(GPA_Grade_Frame ,text = "Total Courses :").grid(row = 0 ,column = 1 ,pady = 2)
Courses_Number_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 2) #Total Courses Display 
Courses_Number_Display.grid(row = 0, column = 2 ,pady = 2)

Label(GPA_Grade_Frame ,text = "Total Hours    :").grid(row = 1 ,column = 1 ,pady = 2)
Hours_Number_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 2) #Total Hours Display 
Hours_Number_Display.grid(row = 1 ,column = 2 ,pady = 2)

Button(GPA_Grade_Frame ,text = "Calculate GPA" ,width = 15 ,command = Caculate_GPA ,bg = "#d2d2d2").grid(row = 2 ,columnspan = 3 ,pady = 5) #Calculate GPA Button

Label(GPA_Grade_Frame ,text = "GPA     :").grid(row = 3)
GPA_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 15) #GPA Display 
GPA_Display.grid(row = 3 ,column = 1)

Label(GPA_Grade_Frame ,text = "Load    :").grid(row = 5)
Load_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 15) #LOAD Display
Load_Display.grid(row = 5 ,column = 1)

Label(GPA_Grade_Frame ,text = "Grade   :").grid(row = 4)
Grade_Display = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 15) #Grade Display
Grade_Display.grid(row = 4 ,column = 1)

Letter = Label(GPA_Grade_Frame ,relief = RIDGE ,width = 3) #Letter Display 
Letter.grid(row = 4,column = 3)

# BOTTOM FRAME
#-------------------------------------------------------------------------
Bottom_Frame = Frame(root)
Bottom_Frame.pack(side = BOTTOM)

Buttons_LabelFrame = LabelFrame(Bottom_Frame ,relief = FLAT)
Buttons_LabelFrame.pack(side = TOP ,pady = 5)

Button(Buttons_LabelFrame ,text = " New  " ,command = New ,bg = "#e6e6e6").pack(side =LEFT ,padx = 15) #New Button 

Button(Buttons_LabelFrame ,text = "About" ,command = About ,bg = "#e6e6e6").pack(side = RIGHT ,padx = 15) #About Button 


root.maxsize(width= 320 ,height = 300)
root.minsize(width= 320 ,height = 300)

root.mainloop()