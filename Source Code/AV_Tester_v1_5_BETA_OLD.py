import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("AV Tester v1.5[BETA] by Rutuj Runwal")
root.geometry("600x300") 
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))  
messagebox.showinfo("AboutUS", "AV Tester v1.5[BETA] by Rutuj Runwal")

def Initiate():
	root1 = Tk()
	root1.title("AV-Tester by Rutuj Runwal")
	root1.geometry("400x150") 
	root1.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id())) 

	Input= Entry(root1,width=60,borderwidth=3)
	Input.insert(0, "Please REMOVE this text and enter your antivirus name ")
	Input.pack()

	def Begin_test():
		try:
			page = requests.get("http://maliciouswebsitetest.com")
			soup = BeautifulSoup(page.content,'html.parser')
			myLabel = Label(root1,text='Done!')
			myLabel.pack()
		except(ConnectionError, Exception):
			messagebox.showerror("Error", "Network Error Code:RR101\nCheck 'Help' tab for more Information")
			myLabel_error = Label(root1,text='Network Error, Please try again with a stable connection')
			myLabel_error.pack()
	def Begin_test2():
		try:
			page = requests.get("http://secure.eicar.org/eicar_com.zip")
			soup = BeautifulSoup(page.content,'html.parser',from_encoding="iso-8859-1")
			myLabel = Label(root1,text='Done!')
			myLabel.pack()
		except ConnectionError:
			messagebox.showerror("Error", "Network Error Code:RR101\nCheck 'Help' tab for more Information")
			myLabel_error = Label(root1,text='Network Error, Please try again with a stable connection')
			myLabel_error.pack()

	myButton = Button(root1,text='Test1[Malicious Website Test]!',command=Begin_test,bg='#add8e6')
	myButton1 = Button(root1,text='Test2[Eicar File Test]!',command=Begin_test2,bg='#FFB6C1')

	myButton.pack()
	myButton1.pack()

	root1.mainloop()

def Begin_disc():
	global Label_disc
	try:
		Label_About.pack_forget()
		Label_help.pack_forget()
		Label_disc = Label(root,text="This program is designed for Educational use Only")
		Label_disc.pack()
	except NameError:
		Label_disc = Label(root,text="This program is designed for Educational use Only")
		Label_disc.pack()

def Begin_About():
	global Label_About
	try:
		Label_disc.pack_forget()
		Label_help.pack_forget()
		Label_About = Label(root,text="Developed by Rutuj Runwal\nSpecial thanks to IKARUS Security.")
		Label_About.pack()
	except NameError:
		Label_About = Label(root,text="Developed by Rutuj Runwal\nSpecial thanks to IKARUS Security.")
		Label_About.pack()

def Begin_help():
	global Label_help
	try:
		Label_About.pack_forget()
		Label_disc.pack_forget()
		Label_help = Label(root,text="Please Ensure a stable Internet connection for tests to run properly\n----------\n For additional Information Contact: rutujrunwal001@gmail.com")
		Label_help.pack()
	except NameError:
		Label_help = Label(root,text="Please Ensure a stable Internet connection for tests to run properly\n----------\n For additional Information Contact: rutujrunwal001@gmail.com")
		Label_help.pack()


Button_Test = Button(root,text='Test!',command=Initiate)
Button_Discl = Button(root,text='Disclaimer!',command=Begin_disc)
Button_About = Button(root,text='About!',command=Begin_About)
Button_help = Button(root,text='Help!',command=Begin_help)

Button_Test.pack()
Button_Discl.pack()
Button_About.pack()
Button_help.pack()

root.mainloop()
