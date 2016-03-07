try:
    # Python2
    from Tkinter import *
except ImportError:
    # Python3
    from tkinter import *
import tkMessageBox

l1=[]
cr = 0

def persub(name,r,c):
	#subject name
	sub1 = StringVar()
	label = Label(root,text=name,font=2,fg="#000000")
	label.grid(row=r,column=c)

def setValue(content1,content2):
	global cr
	if content1 =="A+":
		l1.append(4*float(content2))
		cr+=float(content2)
	elif content1=="A":
		l1.append(3.75*float(content2))
		cr+=float(content2)
	elif content1=="A-":
		l1.append(3.50*float(content2))
		cr+=float(content2)
	elif content1=="B+":
		l1.append(3.25*float(content2))
		cr+=float(content2)
	elif content1=="B":
		l1.append(3.00*float(content2))
		cr+=float(content2)
	elif content1=="B-":
		l1.append(2.75*float(content2))
		cr+=float(content2)
	elif content1=="C+":
		l1.append(2.50*float(content2))
		cr+=float(content2)
	elif content1=="C":
		l1.append(2.25*float(content2))
		cr+=float(content2)
	elif content1=="D":
		l1.append(2.00*float(content2))	
		cr+=float(content2)
						
def clear():
     exit()

def pressCalculate():
	sum = 0.0
	global cr
		
	setValue(s1.cget("text"),c1.cget("text"))
	setValue(s2.cget("text"),c2.cget("text"))
	setValue(s3.cget("text"),c3.cget("text"))
	setValue(s4.cget("text"),c4.cget("text"))
	setValue(s5.cget("text"),c5.cget("text"))
	setValue(s6.cget("text"),c6.cget("text"))
	setValue(s7.cget("text"),c7.cget("text"))
	setValue(s8.cget("text"),c8.cget("text"))
	for i in l1:
		sum+=float(i)
	lastCgpa = sum/float(cr)	
	s = tkMessageBox.showinfo("CGPA","Total Credit Hour = "+str(cr)+"\nGrade Point Average(GPA) = " + str(lastCgpa))	
	del l1[:]
	cr=0

if __name__=="__main__":
	root = Tk()
	root.resizable(0,0)
	root.title("Shaonty's GPA Calculator")

	#for sub 1
	#subject name
	persub("Subject 1",2,0)
	
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	
	s1 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s1.grid(padx=5,pady=10,row=2,column=1)
	#credit pe hour
	var2 = StringVar(root)
	
	credit = [0,1,2,3,4,5,6]
	c1 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c1.grid(padx=10,pady=10,row=2,column=2)	
	#for sub 2
	#subject name
	persub("Subject 2",3,0)
	
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	
	s2 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s2.grid(padx=5,pady=10,row=3,column=1)
	var1.set(defaltgrd)
	#credit pe hour
	var2 = StringVar(root)
	
	credit = [0,1,2,3,4,5,6]
	c2 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c2.grid(padx=10,pady=10,row=3,column=2)	
	#for sub 3
	#subject name
	persub("Subject 3",4,0)
	
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	s3 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s3.grid(padx=5,pady=10,row=4,column=1)
	#credit pe hour
	var2 = StringVar(root)
	
	credit = [0,1,2,3,4,5,6]
	c3 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c3.grid(padx=10,pady=10,row=4,column=2)	
	#for sub 4
	#subject name
	persub("Subject 4",5,0)
	
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	s4 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s4.grid(padx=5,pady=10,row=5,column=1)
	#credit pe hour
	var2 = StringVar(root)
	credit = [0,1,2,3,4,5,6]
	c4 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c4.grid(padx=10,pady=10,row=5,column=2)	

	#for sub 5
	#subject name
	persub("Subject 5",6,0)
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	s5 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s5.grid(padx=5,pady=10,row=6,column=1)
	#credit pe hour
	var2 = StringVar(root)
	credit = [0,1,2,3,4,5,6]
	c5 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c5.grid(padx=10,pady=10,row=6,column=2)	

	#for sub 6
	#subject name
	persub("Subject 6",7,0)
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	s6 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s6.grid(padx=5,pady=10,row=7,column=1)
	#credit pe hour
	var2 = StringVar(root)
	credit = [0,1,2,3,4,5,6]
	c6 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c6.grid(padx=10,pady=10,row=7,column=2)	

	#for sub 7
	#subject name
	persub("Subject 7",8,0)
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	s7 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s7.grid(padx=5,pady=10,row=8,column=1)
	#credit pe hour
	var2 = StringVar(root)
	credit = [0,1,2,3,4,5,6]
	c7 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c7.grid(padx=10,pady=10,row=8,column=2)	

	#for sub 8
	#subject name
	persub("Subject 8",9,0)
	#drop down menu of grade point
	defaltgrd="Grade" 
	var1 = StringVar(root)
	grade = ("A+","A","A-","B+","B","B-","C+","C","D","None")
	
	s8 = apply(OptionMenu,(root,var1)+grade)
	var1.set(defaltgrd)
	s8.grid(padx=5,pady=10,row=9,column=1)
	#credit pe hour
	var2 = StringVar(root)
	credit = [0,1,2,3,4,5,6]
	c8 = OptionMenu(root,var2,*credit)
	var2.set("Credit Hour")
	c8.grid(padx=10,pady=10,row=9,column=2)	


	button = Button(root,text="Calculate",bg="green",font=8,width=18,command=pressCalculate)
	button.grid(row=10,column=0,columnspan=2)
	button = Button(root,text="Exit",bg="#cc3300",font=8,width=10,command=clear)
	button.grid(row=10,column=2)
	

	root.mainloop()