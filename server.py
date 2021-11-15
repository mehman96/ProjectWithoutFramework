from tkinter import *

def save():
 firstname_info=firstname.get()
 lastname_info=lastname.get()
 print(firstname_info,lastname_info)

# file=open("user.txt" )
# file.write (firstname_info)
# file.write(lastname_info) 
# file.close()
# print("User", firstname_info ,"has been register sucessfully")


screen =Tk()
screen.geometry('500x500')
screen.title('Register Form')
heading = Label(text='Form' ,bg="black",fg='red',height='3',width='500')
heading.pack()

firstname_text = Label(text='Firstname *')
lastname_text =Label(text='Lastame *')
firstname_text.place(x= 15, y=70)
lastname_text.place(x=15,y=140)

firstname =StringVar()
lastname =StringVar()

firstname_entry = Entry(textvariable=firstname,width='30')
lastname_entry = Entry(textvariable=lastname,width='30')

firstname_entry.place(x=15,y=100)
lastname_entry.place(x= 15,y=180)

register =Button(screen,text="Register",width='30',height='2',command=save)
register.place(x=15 ,y=290)
