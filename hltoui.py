import hl7;
from tkinter import *;
#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Hl7 messsage to GUI')
 
message = "MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|20201105102050||ADT^A01|0000000|P|2.5.1\rEVN|A01|20201105102132|20201106102135|1|||\rPID|Pat01|P01|||Erukulla^Sandeep||19990220|M\r\r"
#message+= 'PID|Pat01|P01|||Erukulla^Sandeep||19990220|M\r'
 
h=hl7.parse(message)
print(h)
#username label and text entry box
firstnameLabel = Label(tkWindow, text="First name").grid(row=0, column=0)
firstname = StringVar()
firstname.set(h.segment('PID')[5][0][0])
firstnameEntry = Entry(tkWindow, textvariable=firstname).grid(row=0, column=1)  
#print(h[1][5][0])
lastnameLabel = Label(tkWindow, text="Last name").grid(row=1, column=0)
lastname = StringVar()
lastname.set(h.segment('PID')[5][0][1])
lastnameEntry = Entry(tkWindow, textvariable=lastname).grid(row=1, column=1)
#password label and password entry box
patientIDLabel = Label(tkWindow, text="Patient ID").grid(row=2, column=0)
patientID = StringVar()
patientID.set(h.segment('PID')[1][0])
patientIDEntry = Entry(tkWindow, textvariable=patientID).grid(row=2, column=1)
 
dateOfBirthLabel = Label(tkWindow, text="Date Of Birth").grid(row=3, column=0)
dateOfBirth = StringVar()
dateOfBirth.set(h.segment('PID')[7])
dateOfBirthEntry = Entry(tkWindow, textvariable=dateOfBirth).grid(row=3, column=1)
genderLabel = Label(tkWindow,text="Gender").grid(row=4, column=0)  
gender = StringVar()
gender.set(h.segment('PID')[8])
genderEntry = Entry(tkWindow, textvariable=gender).grid(row=4, column=1)  
 
#validateLogin = partial(validateLogin, username, password)
 
#login button
#loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
 
tkWindow.mainloop()
# message = 'MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|20201105093917||ADT^A01|0000000|P|2.5.1|\r'
# message+= 'PID|Pat01|P01|||Erukulla^Sandeep||19990220|M\r'
 
# h=hl7.parse(message)
# patientID.set(h[1][1][0])
# firstname.set(h[1][5][0])
# lastname.set(h[1][5][1])
#print(patientID.get())
