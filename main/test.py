from cProfile import label
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import psycopg2




#connection

connection = psycopg2.connect(user = "postgres",
                                password = "password",
                                host= "localhost",
                                port = "5432",
                                database = "testing")

cursor = connection.cursor()

clockNum = 1
root = Tk()
root.title('CommScope SKILL CARD')
#root.iconbitmap("/home/varad/Documents/PythonProjects/SkillCard-CS/csico.jpg")
root.geometry("320x680")
root.maxsize(348, 720)
root.minsize(348, 720)

global name , spinning_date, spinning_level, packing_level, feed_level, painting_level, painting_date, packing_date

cursor.execute(''' select scd."clockNumber" ,scd ."name" ,scd.spinning  , scd.painting, scd.packing , scd.feed ,
            sd.spinning ,sd.painting ,sd.packing  from skill_card_db scd 
            inner join skill_date sd on scd."clockNumber"  = sd."clockNumber"
            where scd."clockNumber" = \'{0}\'''' .format(clockNum))
row = cursor.fetchone()
clockNum = row[0]
name = row[1]
spinning_level = row[2]
painting_level = row[3]
packing_level = row[4]
feed_level = row[5]
spinning_date = row[6]
painting_date = row[7]
packing_date = row[8]

    #Photo 
OpImg = Image.open("/home/varad/Documents/PythonProjects/SkillCard-CS/cs.jpg")
resized_image = OpImg.resize((330,320), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)
op_label = Label(root, image=img, highlightthickness=1,highlightbackground="#FF0000")
op_label.grid(row = 0, column = 0, padx=1,pady=5)

# Tabs for Skill and Deviation

Tabs = ttk.Notebook(root)
Tabs.grid(row=1, column=0, padx = 10, pady= 10)

#Style layout and to remove dashed
style = ttk.Style()

style.layout("Tab", [('Notebook.tab', {'sticky': 'nswe', 'children':
    [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
        [('Notebook.label', {'side': 'top', 'sticky': ''})],
    })],
})]
)

style.configure("Tab", focuscolor=style.configure(".")["background"])



#Skills and Dev

skill_frame = Frame(Tabs, width=320, height=380)
deviation_frame = Frame(Tabs, width=320, height=380)

skill_frame.pack(fill = BOTH, expand = 1)
deviation_frame.pack(fill= BOTH,expand= 1)

Tabs.add(skill_frame, text = "Skills")
Tabs.add(deviation_frame, text= "Deviation")

#Content for SKills

Overallframe2 = Frame(deviation_frame, highlightthickness=1,highlightbackground="#FF0000")
Overallframe2.grid(column=1, row= 1, padx=8, pady=10, ipadx= 10)

Overallframe = Frame(skill_frame, width= 300, height= 280 ,highlightthickness=1,highlightbackground="#FF0000")
Overallframe.grid(column=1, row= 1, padx=8, pady=10)

area = Label(Overallframe, text="Area", font=('Helvetica', 10, 'bold'), width = 10, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
skill_level =  Label(Overallframe, text="Skill Level", font=('Helvetica', 10, 'bold'), width = 10, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
doc = Label(Overallframe, text= "DOC", font=('Helvetica', 10, 'bold'), width = 14, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")

#area.pack(side=LEFT,padx=6,pady=8)
#skill_level.pack(side=LEFT,pady=8)
#doc.pack(side=LEFT,padx=6,pady=8)

area.grid(column=1, row=1, padx= 8, pady= 5)
skill_level.grid(column=2, row=1,pady= 5)
doc.grid(column=3, row=1, padx= 8, pady= 5)

# Data for 4 rows

Spinning = Label(Overallframe, text="Spinning", font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
skill_level =  Label(Overallframe, text= spinning_level, font=('Helvetica', 10, 'bold'), fg= "#006400", width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
doc = Label(Overallframe, text= spinning_date, font=('Helvetica', 10, 'bold'),fg = "#006400", width = 12, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")

Spinning.grid(column=1, row=2, padx= 8, pady= 5)
skill_level.grid(column=2, row=2,pady= 5)
doc.grid(column=3, row=2, padx= 8, pady= 5)

#2

Painting = Label(Overallframe, text="Painting", font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
skill_level =  Label(Overallframe, text= painting_level, font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
doc = Label(Overallframe, text= painting_date, font=('Helvetica', 10, 'bold'), width = 12, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")

Painting.grid(column=1, row=3, padx= 8, pady= 5)
skill_level.grid(column=2, row=3,pady= 5)
doc.grid(column=3, row=3, padx= 8, pady= 5)

#3

Packing = Label(Overallframe, text="Packing", font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
skill_level =  Label(Overallframe, text= packing_level, font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
doc = Label(Overallframe, text= packing_date, font=('Helvetica', 10, 'bold'), width = 12, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")

Packing.grid(column=1, row=4, padx= 8, pady= 5)
skill_level.grid(column=2, row=4,pady= 5)
doc.grid(column=3, row=4, padx= 8, pady= 5)

#4

Feed = Label(Overallframe, text="Feed", font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
skill_level =  Label(Overallframe, text= feed_level, font=('Helvetica', 10, 'bold'), width = 9, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")
#doc = Label(Overallframe, text= feed_date, font=('Helvetica', 10, 'bold'), width = 12, height= 2,highlightthickness=2,highlightbackground="#C1C1C1")

Feed.grid(column=1, row=5, padx= 8, pady= 5)
skill_level.grid(column=2, row=5,pady= 5)
#doc.grid(column=3, row=5, padx= 8, pady= 5)


# Last box

Bottomframe = Frame(skill_frame, width= 320, height= 50 ,highlightthickness=1,highlightbackground="#FF0000")
Bottomframe.grid(column=1, row= 6, padx=6, pady=5)

ClockNum = Label(Bottomframe, text= "Clock No:", width= 9, height= 2,anchor=W)
Name = Label(Bottomframe, text="Name", width= 9, height= 2,anchor=W)

ClockNum.grid(row= 10, column= 1, padx= 2)
Name.grid(row=11, column=1, padx= 2)

ClockBox = Label(Bottomframe, text= clockNum, bg ="white" , font=('Helvetica', 10, 'bold'), width = 25, height= 1,highlightthickness=1,highlightbackground="#000000")
NameBox = Label(Bottomframe, text=name,font=('Helvetica', 10, 'bold'), width = 25, height= 1,highlightthickness=1,highlightbackground="#000000")

ClockBox.grid(row=10, column=2, padx= 10, pady=6)
NameBox.grid(row=11,column=2, padx= 10, pady=6)

# ClockNumText = Entry(Bottomframe,width=22)
# ClockNumText.grid(row=10, column=2, padx= 10, pady=6)


#Deviation stuff

AreaDev = Label(Overallframe2, text= "Area", width= 9, height= 2,anchor=W)
reason = Label(Overallframe2, text="Reason", width= 9, height= 2,anchor=W)
auditor = Label(Overallframe2, text="Auditor", width= 9, height= 2,anchor=W)

AreaDev.grid(row= 1, column= 1, padx= 2)
reason.grid(row=2, column=1, padx= 2)
auditor.grid(row= 3, column= 1, padx=2)

AreaDevText = Entry(Overallframe2,width=25)
AreaDevText.grid(row=1, column=2)

reasonText = Entry(Overallframe2,width=25)
reasonText.grid(row=2, column=2)

auditorText = Entry(Overallframe2,width=25)
auditorText.grid(row=3, column=2)

sButton = Button(deviation_frame, text="Submit", width=10,bg="black",fg='white')
sButton.place(relx= 0.5, rely= .45, anchor= CENTER)
root.mainloop()