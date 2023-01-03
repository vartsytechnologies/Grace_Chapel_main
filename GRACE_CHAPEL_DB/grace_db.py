__author__ = "VARTSY"

import datetime
from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt

import backend_1
import time
from tkinter import PhotoImage,ttk
from tkinter import Frame,Menu
from tkinter.ttk import Notebook,Style
import random
import sqlite3
import tithe_backend
from tkinter import *
import numpy as np
import cv2
import attendance_db
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

#===========================================main class =======================================================
class App():
	def __init__(self,master):
		self.master = master
		self.master.title("Grace Chapel")
		self.master.geometry("1400x750+0+0")
		self.master.resizable(0,0)
#==================================functions===============================================================

		self.id = StringVar()
		self.name = StringVar()
		self.type= StringVar()
		self.place_of_birth = StringVar()
		self.date_of_birth = StringVar()
		self.gender= StringVar()
		self.department = StringVar()
		self.SEARCH = StringVar()
		self.phone = StringVar()
		self.address= StringVar()
		self.email = StringVar()
		self.status = StringVar()
		self.occupation = StringVar()
		self.fax = StringVar()
		self.emloyer = StringVar()
		self.hometown= StringVar()
		self.region= StringVar()
		self.Tithe = StringVar()
		self.health = StringVar()
		self.how = StringVar()
		self.company = StringVar()
		self.pst_address = StringVar()
		self.contact = StringVar()
		self.level= StringVar()
		self.edu_instution = StringVar()
		#================================tithe system variables==========================
		self.mem_id= StringVar()
		self.name1 = StringVar()
		self.month = StringVar()
		self.amount= StringVar()
		self.date = StringVar()
		self.card_ent1 = IntVar()
		self.card_ent2 = IntVar()
		self.card_ent3 = IntVar()

		#========================attendance system variables===============================
		self.sort = StringVar()

		def reset1():
			self.mem_id.set("")
			self.name1.set("")
			self.month.set("")
			self.amount.set("")
			self.date.set("")









		def Reset():
			self.name.set("")
			self.type.set("")
			self.place_of_birth.set("")
			self.date_of_birth.set("")
			self.gender.set("")
			self.department.set("")
			self.phone.set("")
			self.address.set("")
			self.email.set("")
			self.status.set("")
			self.occupation.set("")
			self.fax.set("")
			self.emloyer.set("")
			self.hometown.set("")
			self.region.set("")
			self.Tithe.set("")
			self.health.set("")
			self.how.set("")
			self.company.set("")
			self.pst_address.set("")
			self.contact.set("")
			self.level.set("")
			self.edu_instution.set("")

			self.SEARCH.set("GCI/ZT/")


		def Search_payee():
			self.listbox_tithe.delete(0, END)
			for row in tithe_backend.search(self.mem_id.get(), self.name1.get(), self.month.get(), self.amount.get(), self.date.get()):
				self.listbox_tithe.insert(END, row, str(' '))



		def StudentRec(event):
			try:
				global selected_tuple
				index = self.listbox.curselection()[0]
				selected_tuple = self.listbox.get(index)
				self.entry1.delete(0, END)
				self.entry1.insert(END, selected_tuple[1])
				self.entry2.delete(0, END)
				self.entry2.insert(END, selected_tuple[2])

			except IndexError:
				pass

		def StudentRec2(event):
			try:
				global selected_tuple

				index = self.listbox_tithe.curselection()[0]
				selected_tuple = self.listbox_tithe.get(index)
				self.entry1.delete(0, END)
				self.entry1.insert(END, selected_tuple[1])
				self.entry2.delete(0, END)
				self.entry2.insert(END, selected_tuple[2])
				self.entry3.delete(0, END)
				self.entry3.insert(END, selected_tuple[3])
				self.entry4.delete(0, END)
				self.entry4.insert(END, selected_tuple[4])
				self.entry6.delete(0, END)
				self.entry6.insert(END, selected_tuple[5])

			except IndexError:
				pass

		def graph():
			figure = plt.Figure(figsize=(6, 6), dpi=100)
			figure.add_subplot(111).bar([1, 2, 3, 4], [1, 2, 3, 4])
			chart = FigureCanvasAgg(self.graph_frame, figure)
			chart.get_tk_widget().place(relx=0, rely=0)

			plt.grid()

			axes = plt.axes()
			axes.set_xlim([0, 6.3])
			axes.set_ylim([-3, 3])

		def Display():
			self.listbox.delete(0, END)
			for row in backend_1.view():
				self.listbox.insert(END, row, str(' '))

		def delkey():
			tithe_backend.delete(selected_tuple[0])
			Reset()
			Display1()

		def Update():
			tithe_backend.delete(selected_tuple[0])
			tithe_backend.Insert(self.mem_id.get(), self.name1.get(), self.month.get(), self.amount.get()
								   , self.date.get())
			self.listbox_tithe.delete(0, END)
			self.listbox_tithe.insert(END,(self.mem_id.get(), self.name1.get(), self.month.get(), self.amount.get(), self.date.get()))


		def Display1():
			self.listbox_tithe.delete(0, END)
			for row in tithe_backend.view():
				self.listbox_tithe.insert(END, row, str(' '))

		Reset()

		def SearchRecord():
			# checking search text is empty or not
			if self.SEARCH.get() != "":
				# clearing current display data			# open database
				conn = sqlite3.connect('grace1.db')
				# select query with where clause
				cursor = conn.execute("SELECT * FROM member1 WHERE mem_id LIKE ?",
									  ('%' + str(self.SEARCH.get()) + '%',))
				# fetch all matching records
				fetch = cursor.fetchall()
				# loop for displaying all records into GUI
				for data in fetch:
					self.tree.insert('', 'end', values=(data))
				cursor.close()
				conn.close()
			elif self.SEARCH.get() != DisplayData():
				messagebox.showwarning("Search Error", "Name Is not recognized")

		def Submit():
			if (len(self.name.get()) != 0):
				backend_1.Insert(self.id.get(),self.name.get(),self.type.get(),self.place_of_birth.get(),self.date_of_birth.get(),self.gender.get(),self.department.get(),self.phone.get(),self.address.get(),self.email.get(),self.status.get(),self.occupation.get(),self.fax.get(),self.emloyer.get(),self.hometown.get(),self.region.get(),self.Tithe.get(),self.how.get(),self.health.get(),self.company.get(),self.pst_address.get(),self.contact.get(),self.level.get(),self.edu_instution.get())

			else:
				messagebox.showwarning("Input Error", "Please Fill the form before submission")

		def take_photo():
			cam = cv2.VideoCapture(0)
			cv2.namedWindow("test")
			img_counter = 0
			while True:
				ret, frame = cam.read()
				if not ret:
					print("failed to grab frame")
					break
				cv2.imshow("test", frame)

				k = cv2.waitKey(1)
				if k % 256 == 27:
					# ESC pressed
					print("Escape hit, closing...")
					break
				elif k % 256 == 32:
					# SPACE pressed
					img_name = "opencv_frame_{}.png".format(img_counter)
					cv2.imwrite(img_name, frame)
					print("{} written!".format(img_name))
					img_counter += 1

			cam.release()

		def welcome():
			self.frame_1 = Frame(self.master,width = 1400,height = 750,bg = "white")
			self.frame_1.place(relx = 0,rely =0)
			self.frame_1_1 = Frame(self.master, width=1400, height=400, bg="#9A0033")
			self.frame_1_1.place(relx=0, rely=0.3)
			self.church_logo= Label(self.frame_1_1,bg = "#9A0033")
			self.img_1_1 = PhotoImage(file = "graphics/church.png")
			self.church_logo.config(image = self.img_1_1)
			self.church_logo.place(relx = 0.8,rely = 0.1)
			self.label = "GRACE CHAPEL INTERNATIONAL\n(2022)"
			self.lbl_1 = Label(self.frame_1,text = self.label,bg = "white",fg = "blue",font = ("times new romans",35,"bold"))
			self.lbl_1.place(relx = 0.26,rely=0.08)
			self.label2 = "Powered by VARTSY"
			self.lbl_2 = Label(self.frame_1,text = self.label2,bg = "white",fg = "blue",font = ("times new romans",12,"bold"))
			self.lbl_2.place(relx = 0.47,rely = 0.85)
#=================================================phot logo ======================================================
			self.image_lbl =Label(self.frame_1)
			self.logo = PhotoImage(file = "graphics/lmis.png")
			self.image_lbl.config(image = self.logo, bg = "white")
			self.image_lbl.place(relx = 0.08,rely = 0)

			self.msg = "For God So loved the world that he gave his only begotten son \n that whosoever believes in him should not perish but \n have everlasting life\n (Ephesians 6:1)"
			self.msg_lbl = Label(self.frame_1_1,text = self.msg,font = ("times new romans",20),bg ="#9A0033",fg ="white" )
			self.msg_lbl.place(relx = 0.2,rely = 0.3)
#==================================================get started============================================================
			self.btn = Button(self.frame_1_1,command = get)
			self.img2 = PhotoImage(file ="graphics/get.png")
			self.btn.config(image = self.img2,bg ="#9A0033",bd =0)
			self.btn.place(relx = 0.45,rely = 0.75)
			self.lbl_3 = Label(self.frame_1_1,text = "GET STARTED",font = ("times new romans",12,"bold"),bg = "white",fg = "purple")
			self.lbl_3.place(relx=0.48,rely = 0.82)

		def DisplayData():
			# clear current data
			self.tree.delete(*self.tree.get_children())
			# open databse
			conn = sqlite3.connect('grace1.db')
			# select query
			cursor = conn.execute("SELECT * FROM member1")
			# fetch all data from database
			fetch = cursor.fetchall()
			# loop for displaying all data in GUI
			count = 0
			for data in fetch:
				if count % 2==0:
					self.tree.insert('', 'end', values=(data),tags =('evenrow'))
				else:
					self.tree.insert('', 'end', values=(data), tags=('oddrow'))
				count +=1
			cursor.close()
			conn.close()

			self.SEARCH.set("GCI/ZT/")



		def delete():
			if self.tree.selection():
				result = messagebox.askquestion('Python - Delete Data Row In SQLite',
												'Are you sure you want to delete this record?', icon="warning")
				if result == 'yes':
					curItem =self.tree.focus()
					contents = (self.tree.item(curItem))
					selecteditem = contents['values']
					self.tree.delete(curItem)
					backend_1.delete(selecteditem[0])

				else:
					DisplayData()

#==================================================Signin_Page =========================================================
		def Sign():
			self.frame_2 = Frame(self.master,width = 1400,height = 750,)
			self.frame_2.place(relx = 0,rely =0)

			def Time():
				hour = time.strftime("%I")
				min = time.strftime("%M")
				sec = time.strftime("%S")
				am_pm = time.strftime("%p")

				self.Time.config(text = hour + " : "+min + " : "+sec +" "+ am_pm)
				self.Time.after(1000, Time)

			self.Time= Label(self.frame_2,font = ("times new romans", 20 , "bold"),fg = "blue")
			self.Time.place(relx = 0.8,rely = 0.02)
			Time()


			self.log_frame_1 = Frame(self.frame_2,width = 400,height = 600,bg = "white",bd= 1,relief = RAISED)
			self.log_frame_1.place(relx = 0.16,rely =0.1)



			self.avatar = Label(self.log_frame_1,bg = "white")
			self.avat = PhotoImage(file = "graphics/avatar.png")
			self.avatar.config(image =self.avat)
			self.avatar.place(relx = 0.26,rely = 0.09)
#=================================================credentials ============================================================
			self.user = Label(self.log_frame_1,text = "Username",font = ("aquawax",15),bg = "white",fg = "blue")
			self.user.place(relx=0.18,rely  = 0.4)
			self.entimg1 = Label(self.log_frame_1,bg ="white")
			self.ent_1_image = PhotoImage(file="graphics/entry.png")
			self.entimg1.config(image = self.ent_1_image)
			self.entimg1.place(relx =0.18,rely = 0.6)
			self.entry_2 = Entry(self.log_frame_1,show = "*",width =40,bd = 0)
			self.entry_2.place(relx = 0.2,rely = 0.612)

			self.passw = Label(self.log_frame_1, text="Password",font=("aquawax", 15), bg="white", fg="blue")
			self.passw.place(relx=0.18, rely=0.54)
			self.entimg2= Label(self.log_frame_1, bg="white")
			self.ent_2_image = PhotoImage(file="graphics/entry.png")
			self.entimg2.config(image=self.ent_1_image)
			self.entimg2.place(relx=0.18, rely=0.47)

			self.entry_1 = Entry(self.log_frame_1, width=40, bd=0)
			self.entry_1.place(relx=0.2, rely=0.482)

			self.btn = Button(self.log_frame_1, command=login)
			self.img2 = PhotoImage(file="graphics/loginbtn.png")
			self.btn.config(image=self.img2, bg="white", bd=0)
			self.btn.place(relx=0.3, rely=0.7)

			self.log_frame_2 = Frame(self.frame_2, width=500, height=600, bg="#9A0033", bd=1, relief=RAISED)
			self.log_frame_2.place(relx=0.43, rely=0.1)
			self.txt = "WELCOME BACK\n\nLogin to have full access to this software Now\n"
			self.wel = Label(self.log_frame_2,text = self.txt,font = ("times new romans",15, "bold"),fg ="white",bg ="#9A0033")
			self.wel.place(relx = 0.02,rely = 0.4)


			"""self.bg = Label(self.log_frame_2, )
			self.back = PhotoImage(file="graphics/f2.png")
			self.bg.config(image=self.back)
			self.bg.place(relx=0, rely=0)"""


		def main():
			self.frame_3 = Frame(self.master,width = 1400,height = 750)
			self.frame_3.place(relx = 0,rely =0)
			self.nav_frame_1 = Frame(self.frame_3,width = 1400,height = 40,bg = "#9A0033")
			self.nav_frame_1.place(relx = 0,rely =0)
			self.nav_label =Label(self.nav_frame_1,text = "GRACE CHAPEL INTERNATIONAL DATABASE SYSTEM ",font=("times new romans",15,"bold"),bg ="#9A0033",fg = "white")
			self.nav_label.place(relx = 0.3,rely = 0.3)
			self.menubar = Menu(self.frame_3,background ="red",fg = "white")
			root.config(menu = self.menubar)
			self.file_menu = Menu(self.menubar,tearoff = 0)
			self.file_menu.add_command(label = 'Add Members')
			self.file_menu.add_command(label = 'Open...')
			self.file_menu.add_command(label = 'Close',command =root.destroy)
			self.file_menu.add_command(label = 'Settings')
			self.file_menu.add_separator()

			self.give_menu = Menu(self.menubar,tearoff = 0)
			self.give_menu.add_command(label ='Tithes',command = tithe)
			self.give_menu.add_command(label='Offering',command = tithe)
			self.give_menu.add_command(label='Send Reminders')
			self.file_menu.add_command(label = 'Logout',command =logout)
			self.menubar.add_cascade(label ='Add Members',menu = self.file_menu,font = ("arial",20))
			self.menubar.add_cascade(label='Tithes and Offering', menu=self.give_menu)
			self.menubar.add_cascade(label='Attendance', menu=self.file_menu,command = attendance)
			self.menubar.add_cascade(label='Settings', menu=self.file_menu)

			#======================logo frame===========================
			self.side_frame=Frame(self.frame_3,width = 340,height =660,bg ="white",relief = "raised")
			self.side_frame.place(relx =0,rely =0.0522)

			self.content_frame = LabelFrame(self.frame_3,width = 1030,height =680,)
			self.content_frame.place(relx = 0.232,rely = 0.0522)

			#===================================cards===============================================
			def count():
				self.entry_card.config(state = "disable",disabledbackground = "#9A0033",disabledforeground = "white")
				conn = sqlite3.connect("grace1.db")
				cur = conn.cursor()
				cur.execute("SELECT COUNT(*) FROM member1")
				result = cur.fetchone()[0]
				self.card_ent1.set(result)
			self.card_1 = Frame(self.content_frame, width =200,height = 120,relief =RAISED,bd =2,bg = "#9A0033")
			self.card_1.place(relx = 0.02,rely = 0.1)
			self.entry_card = Entry(self.card_1,bg = "#9A0033",fg= "white",bd = 0,font =("franklin gothic",42,"bold"),textvariable = self.card_ent1,)
			self.entry_card.place(relx=0.25,rely =0.13)
			count()
			self.card_1_label = Label(self.card_1,text  = "Total Members",font = ("franklin gothic", 12,"bold"),bg = "#9A0033",fg = "white")
			self.card_1_label.place(relx = 0.05,rely =0.7)

			self.card_2 = Frame(self.content_frame, width = 200,height = 120,relief =RAISED,bd =2,bg = "#9A0033")
			self.card_2.place(relx = 0.23,rely = 0.1)
			self.entry_card_2= Entry(self.card_2, bg="#9A0033", fg="white", bd=0, font=("franklin gothic", 35, "bold"),
									textvariable=self.card_ent2,state = "disable",disabledbackground = "#9A0033",disabledforeground = "white")
			self.entry_card_2.place(relx=0.25, rely=0.13)


			self.card_2_label = Label(self.card_2, text="Total Present ", font=("franklin gothic", 12, "bold"),
									  bg="#9A0033", fg="white")
			self.card_2_label.place(relx=0.05, rely=0.7)

			self.card_3 = Frame(self.content_frame, width=200, height=120, relief=RAISED, bd=2,bg = "#9A0033")
			self.card_3.place(relx=0.44, rely=0.1)

			self.entry_card_3 = Entry(self.card_3, bg="#9A0033", fg="white", bd=0, font=("franklin gothic", 35, "bold"),
									textvariable=self.card_ent3,state = "disable",disabledbackground = "#9A0033",disabledforeground = "white")
			self.entry_card_3.place(relx=0.25, rely=0.13)

			self.card_3_label = Label(self.card_3, text="New Members ", font=("franklin gothic", 12, "bold"),
									  bg="#9A0033", fg="white")
			self.card_3_label.place(relx=0.05, rely=0.7)



			self.graph_frame = Frame(self.content_frame,width =630,height = 200,bg = "white",relief= RAISED,bd = 2)
			self.graph_frame.place(relx= 0.02,rely = 0.33)

			self.new_frame = Frame(self.content_frame, width=630, height=200, relief=FLAT, bg = "white")
			self.new_frame.place(relx=0.02, rely=0.68)

			self.label_mem= Frame(self.new_frame, width=630, height=40, bg="#9A0033")
			self.label_mem.place(relx=0, rely=0)

			self.event_frame = Frame(self.content_frame,width = 260,height = 300,relief = FLAT,bg= "white")
			self.event_frame.place(relx=0.7,rely = 0.1)
			self.label_event = Frame(self.event_frame,width = 260,height = 40,bg = "#9A0033")
			self.label_event.place(relx = 0,rely =  0)

			self.btn_img_12 = Label(self.content_frame,)
			self.btn_img12 = PhotoImage(file="graphics/graph2.png")
			self.btn_img_12.config(image=self.btn_img12)
			self.btn_img_12.place(relx=0.69, rely=0.575)





			#========================================side_bar ============================

			self.btn_img_1= Label(self.side_frame, bg="white")
			self.btn_img = PhotoImage(file="graphics/lmis.png")
			self.btn_img_1.config(image=self.btn_img)
			self.btn_img_1.place(relx=0.12, rely=0.01)

			separator1= Frame(self.side_frame, width=300, height=2)
			separator1.place(relx=0, rely=0.37)

			#==================================side__bar__buttons============================
			self.btn_1  = Button(self.side_frame,text = "Membership",bd =0 , fg = "blue",bg = "white",font =(" times new romans",14),activeforeground ="red",activebackground = "white",command = member)
			self.btn_1.place(relx = 0.2,rely = 0.4)
			self.btn_2 = Button(self.side_frame,text = "Add New Members",bd =0 , fg = "blue",bg = "white",font =(" times new romans",14),activeforeground ="red",activebackground = "white",command = add_mem)
			self.btn_2.place(relx = 0.2,rely = 0.47)
			self.btn_3 = Button(self.side_frame, text="Tithes and Offering", bd=0, fg="blue", bg="white",command = tithe,
								font=(" times new romans", 14),activeforeground ="red",activebackground = "white")
			self.btn_3.place(relx=0.2, rely=0.54)

			self.btn_4 = Button(self.side_frame, text="Ai Attendance System", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14),activeforeground ="red",activebackground = "white",command = attendance)
			self.btn_4.place(relx=0.2, rely=0.61)

			self.btn_5 = Button(self.side_frame, text="Departments", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14),activeforeground ="red",activebackground = "white")
			self.btn_5.place(relx=0.2, rely=0.68)

			separator = Frame(self.side_frame,width =300,height = 2)
			separator.place(relx =0,rely = 0.75)

			self.btn_6 = Button(self.side_frame, text="Log out", bd=0, fg="blue", bg="white",command = logout,
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_6.place(relx=0.2, rely=0.78)

			self.btn_7= Button(self.side_frame, text="Settings", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_7.place(relx=0.2, rely=0.85)
			self.btn_5 = Button(self.side_frame, text="Developers", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_5.place(relx=0.2, rely=0.92)

	#=============================================icons==================================================
			self.icon_1 = Label(self.side_frame, bg="white")
			self.icon = PhotoImage(file="graphics/membership.png")
			self.icon_1.config(image=self.icon)
			self.icon_1.place(relx=0.05, rely=0.4)

			self.icon_2 = Label(self.side_frame, bg="white")
			self.icon_a = PhotoImage(file="graphics/offer.png")
			self.icon_2.config(image=self.icon_a)
			self.icon_2.place(relx=0.05, rely=0.54)

			self.icon_3 = Label(self.side_frame, bg="white")
			self.icon_b = PhotoImage(file="graphics/ai.png")
			self.icon_3.config(image=self.icon_b)
			self.icon_3.place(relx=0.06, rely=0.61)

			self.icon_4 = Label(self.side_frame, bg="white")
			self.icon_c = PhotoImage(file="graphics/logout.png")
			self.icon_4.config(image=self.icon_c)
			self.icon_4.place(relx=0.065, rely=0.78)

			self.icon_5 = Label(self.side_frame, bg="white")
			self.icon_d = PhotoImage(file="graphics/dev.png")
			self.icon_5.config(image=self.icon_d)
			self.icon_5.place(relx=0.06, rely=0.92)

			self.icon_6 = Label(self.side_frame, bg="white")
			self.icon_e = PhotoImage(file="graphics/set.png")
			self.icon_6.config(image=self.icon_e)
			self.icon_6.place(relx=0.06, rely=0.85)

			self.icon_7 = Label(self.side_frame, bg="white")
			self.icon_f = PhotoImage(file="graphics/de.png")
			self.icon_7.config(image=self.icon_f)
			self.icon_7.place(relx=0.06, rely=0.68)

			self.icon_9= Label(self.side_frame, bg="white")
			self.icon_g = PhotoImage(file="graphics/add.png")
			self.icon_9.config(image=self.icon_g)
			self.icon_9.place(relx=0.06, rely=0.47)

		#===================================================================================================
		def membership():
			self.frame_4 = Frame(self.master, width=1400, height=750)
			self.frame_4.place(relx=0, rely=0)



			self.menubar = Menu(self.frame_4, background="red", fg="white")
			root.config(menu=self.menubar)
			self.file_menu = Menu(self.menubar, tearoff=0)
			self.file_menu.add_command(label='Add Members')
			self.file_menu.add_command(label='Open...')
			self.file_menu.add_command(label='Close', command=root.destroy)
			self.file_menu.add_command(label='Settings')
			self.file_menu.add_separator()

			self.give_menu = Menu(self.menubar, tearoff=0)
			self.give_menu.add_command(label='Tithes')
			self.give_menu.add_command(label='Offering')
			self.give_menu.add_command(label='Pledges')
			self.give_menu.add_command(label='Send Reminders')
			self.file_menu.add_command(label='Dashboard', command=main)
			self.menubar.add_cascade(label='Add Members', menu=self.file_menu, font=("arial", 20),command = add_mem)
			self.menubar.add_cascade(label='Tithes and Offering', menu=self.give_menu)
			self.menubar.add_cascade(label='Attendance', menu=self.file_menu)
			self.menubar.add_cascade(label='Settings', menu=self.file_menu)

			self.nav_frame_4 = Frame(self.master, width=1400, height=60, bg="#9A0033")
			self.nav_frame_4.place(relx=0, rely=0)

			self.display_btn = Button(self.nav_frame_4,text = "DISPLAY",font = ("times new roman",15,"bold"),bg = "#9A0033",fg = "white",bd = 0,command =DisplayData )
			self.display_btn.place(relx = 0.85,rely = 0.28)

			self.search = Entry(self.nav_frame_4,width =35,font = ("times new roman",15),textvariable = self.SEARCH)
			self.search.place(relx = 0.4,rely = 0.28)
			self.search_btn = Button(self.nav_frame_4,text = "SEARCH",font = ("times new roman",10),bg ="blue",fg  ="white",command = SearchRecord)
			self.search_btn.place(relx = 0.65,rely = 0.28)

			self.nav_frame_5 = Frame(self.master, width=1400, height=30, bg="white",relief = RAISED,bd = 1)
			self.nav_frame_5.place(relx=0, rely=0.08)

			self.nav_label_1 = Label(self.nav_frame_5,text ="ACTIONS",font = ("times new roman",12),bg = "white",fg ="black")
			self.nav_label_1.place(relx =0.1,rely =0)

			self.tree_frame= Frame(self.frame_4, width = 1050,height = 640)
			self.tree_frame.place(relx = 0.2,rely = 0.1)

			self.scrollbarx = Scrollbar(self.tree_frame, orient=HORIZONTAL)
			self.scrollbary = Scrollbar(self.tree_frame, orient=VERTICAL)
			self.tree = ttk.Treeview(self.tree_frame, columns=(
				'S/N', "Membership ID", "Name", "Membership Type", "Place Of Birth", "Date Of Birth","Gender","Department","Telephone", "Address", "Email", "Marital Status", "Occupation", "Fax","Employer","HomeTown", "Region", "Pays Tithe?", "Mode Of Visit","Health Status", "Company Name","Post Address","Emerg. Contact", "Education Level","Name Of Institution"),
									 selectmode="extended", height=18, yscrollcommand=self.scrollbary.set,
									 xscrollcommand=self.scrollbarx.set)
			#self.tree.configure(selectmode="extended")
			style = ttk.Style()
			#Pick a theme
			style.theme_use('clam')

			style.configure("Treeview.Heading", font=("times new roman", 15,"bold"), foreground='blue',fieldbackground = "silver")
			style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 15, ),background="silver",foreground ="white"
							,rowheight=40,fieldbackground = "silver")
			style.map('Treeview',background = [('selected','green')])
			self.scrollbary.config(command=self.tree.yview)
			self.scrollbary.place(relx=0.95, rely=0.05, height=500)
			self.scrollbarx.config(command=self.tree.xview)
			self.scrollbarx.place(relx=0.08, rely=0.9, width=900)

			self.tree.heading('S/N', text="S/N", anchor=W)
			self.tree.heading('Membership ID', text="Membership ID", anchor=W)
			self.tree.heading('Name', text="Name", anchor=W)
			self.tree.heading('Membership Type', text="Membership Type", anchor=W)
			self.tree.heading('Place Of Birth', text="Place Of Birth", anchor=W)
			self.tree.heading('Date Of Birth', text="Date Of Birth", anchor=W)
			self.tree.heading('Gender', text="Gender", anchor=W)
			self.tree.heading('Department', text="Department", anchor=W)
			self.tree.heading('Telephone', text="Telephone", anchor=W)
			self.tree.heading('Address', text="Address", anchor=W)
			self.tree.heading('Email', text="Email", anchor=W)
			self.tree.heading('Marital Status', text="Marital Status", anchor=W)
			self.tree.heading('Occupation', text="Occupation", anchor=W)
			self.tree.heading('Fax', text="Fax", anchor=W)
			self.tree.heading('Employer', text="Employer", anchor=W)
			self.tree.heading('HomeTown', text="HomeTown", anchor=W)
			self.tree.heading('Region', text="Region", anchor=W)
			self.tree.heading('Pays Tithe?', text="Pays Tithe?", anchor=W)
			self.tree.heading('Mode Of Visit', text="Mode Of Visit", anchor=W)
			self.tree.heading('Health Status', text="Health Status", anchor=W)
			self.tree.heading('Company Name', text="Company Name", anchor=W)
			self.tree.heading('Post Address', text="Post Address", anchor=W)
			self.tree.heading('Emerg. Contact', text="Emerg. Contact", anchor=W)
			self.tree.heading('Education Level', text="Education Level", anchor=W)
			self.tree.heading('Name Of Institution', text="Name Of Institution", anchor=W)

			self.tree.column('#0', stretch=NO, minwidth=0, width=0)
			self.tree.column('#1', stretch=NO, minwidth=0, width=150)
			self.tree.column('#2', stretch=NO, minwidth=0, width=150)
			self.tree.column('#3', stretch=NO, minwidth=0, width=150)
			self.tree.column('#4', stretch=NO, minwidth=0, width=150)
			self.tree.column('#5', stretch=NO, minwidth=0, width=150)
			self.tree.column('#6', stretch=NO, minwidth=0, width=150)
			self.tree.column('#6', stretch=NO, minwidth=0, width=150)
			self.tree.column('#7', stretch=NO, minwidth=0, width=150)
			self.tree.column('#8', stretch=NO, minwidth=0, width=150)
			self.tree.column('#9', stretch=NO, minwidth=0, width=150)
			self.tree.column('#10', stretch=NO, minwidth=0, width=150)
			self.tree.column('#11', stretch=NO, minwidth=0, width=150)
			self.tree.column('#12', stretch=NO, minwidth=0, width=150)
			self.tree.column('#13', stretch=NO, minwidth=0, width=150)
			self.tree.column('#14', stretch=NO, minwidth=0, width=150)
			self.tree.column('#15', stretch=NO, minwidth=0, width=150)
			self.tree.column('#16', stretch=NO, minwidth=0, width=150)
			self.tree.column('#17', stretch=NO, minwidth=0, width=150)
			self.tree.column('#18', stretch=NO, minwidth=0, width=150)
			self.tree.column('#19', stretch=NO, minwidth=0, width=150)
			self.tree.column('#20', stretch=NO, minwidth=0, width=150)
			self.tree.column('#21', stretch=NO, minwidth=0, width=150)
			self.tree.column('#22', stretch=NO, minwidth=0, width=150)
			self.tree.column('#23', stretch=NO, minwidth=0, width=150)
			self.tree.column('#24', stretch=NO, minwidth=0, width=150)


			self.tree.place(relx=0.08, rely=0.03, width=900, height=550)
			self.tree.tag_configure('oddrow',background = 'lightblue')
			self.tree.tag_configure('evenrow', background='white')
			self.tree.bind("<Double-1>", double_tap)






			self.side_frame1= Frame(self.frame_4,width = 320,height =640,bg ="white",relief = "raised")
			self.side_frame1.place(relx =0,rely= 0.06)

			self.btn_1 = Button(self.side_frame1, text="Add New Members", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white",
								command=add_mem)
			self.btn_1.place(relx=0.2, rely=0.1)
			self.btn_2 = Button(self.side_frame1, text="Edit this Member", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_2.place(relx=0.2, rely=0.15)
			self.btn_3 = Button(self.side_frame1, text="Delete this member", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white",command = delete)
			self.btn_3.place(relx=0.2, rely=0.2)

			self.btn_4 = Button(self.side_frame1, text="send email to this member", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_4.place(relx=0.2, rely=0.25)

			self.btn_5 = Button(self.side_frame1, text="Send mass email to view", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_5.place(relx=0.2, rely=0.3)



			self.btn_6 = Button(self.side_frame1, text="send text/sms to this person", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_6.place(relx=0.2, rely=0.35)

			self.btn_7 = Button(self.side_frame1, text="send mass text/sms to view", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_7.place(relx=0.2, rely=0.4)
			self.btn_5 = Button(self.side_frame1, text="Record Church attendance", bd=0, fg="blue", bg="white",
								font=(" times new romans", 14), activeforeground="red", activebackground="white")
			self.btn_5.place(relx=0.2, rely=0.45)

			self.btn_img_a = Label(self.side_frame1, bg="white")
			self.btn_img = PhotoImage(file="graphics/edit.png")
			self.btn_img_a.config(image=self.btn_img)
			self.btn_img_a.place(relx=0.1, rely=0.154)

			self.btn_img_b = Label(self.side_frame1, bg="white")
			self.btn_img_1 = PhotoImage(file="graphics/del.png")
			self.btn_img_b.config(image=self.btn_img_1)
			self.btn_img_b.place(relx=0.1, rely=0.2)

			self.btn_img_c = Label(self.side_frame1, bg="white")
			self.btn_img_2 = PhotoImage(file="graphics/mail.png")
			self.btn_img_c.config(image=self.btn_img_2)
			self.btn_img_c.place(relx=0.1, rely=0.256)

			self.btn_img_d= Label(self.side_frame1, bg="white")
			self.btn_img_3 = PhotoImage(file="graphics/mail.png")
			self.btn_img_d.config(image=self.btn_img_3)
			self.btn_img_d.place(relx=0.1, rely=0.31)

			self.btn_img_e = Label(self.side_frame1, bg="white")
			self.btn_img_4 = PhotoImage(file="graphics/sms.png")
			self.btn_img_e.config(image=self.btn_img_4)
			self.btn_img_e.place(relx=0.1, rely=0.356)

			self.btn_img_f = Label(self.side_frame1, bg="white")
			self.btn_img_5 = PhotoImage(file="graphics/sms.png")
			self.btn_img_f.config(image=self.btn_img_5)
			self.btn_img_f.place(relx=0.1, rely=0.41)

			self.btn_img_g = Label(self.side_frame1, bg="white")
			self.btn_img_6 = PhotoImage(file="graphics/attend.png")
			self.btn_img_g.config(image=self.btn_img_6)
			self.btn_img_g.place(relx=0.1, rely=0.456)

			self.btn_img_h = Label(self.side_frame1, bg="white")
			self.btn_img_7 = PhotoImage(file="graphics/new.png")
			self.btn_img_h.config(image=self.btn_img_7)
			self.btn_img_h.place(relx=0.1, rely=0.09)

			separator2 = Frame(self.side_frame1, width=300, height=2)
			separator2.place(relx=0, rely=0.55)

			self.picture_frame = Frame(self.side_frame1, width =200, height =200,bd = 1,relief = SUNKEN)
			self.picture_frame.place(relx=0.18,rely=0.58)

			self.id = "GCI/ZT/25614525"
			self.member_id = Label(self.side_frame1, text = "ID: " + " "+self.id,bg="white",fg="blue",font = ("times new roman", 15))
			self.member_id.place(relx=0.2,rely=0.9)

			self.btn_img_id= Label(self.picture_frame, bg="white")
			self.btn_img_8 = PhotoImage(file="graphics/id.png")
			self.btn_img_id.config(image=self.btn_img_8)
			self.btn_img_id.place(relx=0, rely=0)

			DisplayData()
		#==================================================new members registration==============================
		def add_mem():
			self.add_mem = Toplevel()
			self.add_mem.geometry("1300x750+0+10")
			self.add_mem.resizable(0,0)


			self.fm = Frame(self.add_mem, height=720, width=1300)
			self.fm.place(relx=0, rely=0.09)
			self.frame1 = Frame(self.add_mem, height=60, width=1400, bg="#9A0033")
			self.frame1.place(relx=0, rely=0)
			self.sublbl = Label(self.frame1, text="NEW MEMBERS ENTRY FORM", bg="#9A0033", fg="white",
								font=("arial", 18, "bold"))
			self.sublbl.place(relx = 0.3,rely=0.2)



			#==============================functions===================================
			self.id = StringVar()
			self.name = StringVar()

			#=========================================frames ================================================
			self.con_frame_1 = LabelFrame(self.fm,text ="PERSONAL DETAILS",width = 1200,height = 300,bg = "white")
			self.con_frame_1.place(relx = 0.03,rely = 0.02)

			def gen_id():
				self.data_a_1.config(state='disabled',disabledbackground = "#9A0033",disabledforeground = "white")
				self.rand_id = random.randint(10000000, 20000000)
				self.conv_id = ('GCI/ZT/' + str(self.rand_id))
				self.id.set(self.conv_id)

			self.data_a = Label(self.con_frame_1,text = "Member ID",font = ("times new roman", 15),bg = "white", fg = "black")
			self.data_a.place(relx= 0.01,rely = 0.01)
			self.data_a_1 = Entry(self.con_frame_1,width = 30,bg = "white",fg = "blue",font = ("times new roman", 14),textvariable = self.id)
			self.data_a_1.place(relx = 0.2,rely =0.01)

			gen_id()

			self.data_b = Label(self.con_frame_1, text="Member Name", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_b.place(relx=0.01, rely=0.16)
			self.data_b_1 = Entry(self.con_frame_1, width=30, bg="white", fg="blue", font=("times new roman", 14),textvariable = self.name)
			self.data_b_1.place(relx=0.2, rely=0.16)

			self.data_c = Label(self.con_frame_1, text="Membership Type", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_c.place(relx=0.01, rely=0.31)
			self.data_c_1 = ttk.Combobox(self.con_frame_1, width=28,textvariable = self.type,value = ("Pastor","Usher","Deacon/Deaconess","Departmental Head","Instrumentalist","Singer"), font=("times new roman", 14))
			self.data_c_1.place(relx=0.2, rely=0.31)

			self.data_d = Label(self.con_frame_1, text="Place Of Birth", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_d.place(relx=0.01, rely=0.46)
			self.data_d_1 = Entry(self.con_frame_1, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.place_of_birth)
			self.data_d_1.place(relx=0.2, rely=0.46)

			self.data_e = Label(self.con_frame_1, text="Date Of Birth", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_e.place(relx=0.01, rely=0.61)
			self.data_e_1 = Entry(self.con_frame_1, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.date_of_birth)
			self.data_e_1.place(relx=0.2, rely=0.61)

			self.data_f = Label(self.con_frame_1, text="Gender", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_f.place(relx=0.01, rely=0.76)
			self.data_f_1 = ttk.Combobox(self.con_frame_1, width=28, value = ("Male","Female","Others"), font=("times new roman",14),textvariable = self.gender)
			self.data_f_1.place(relx=0.2, rely=0.76)

			self.data_g = Label(self.con_frame_1, text="Department", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_g.place(relx=0.5, rely=0.01)
			self.data_g_1 = ttk.Combobox(self.con_frame_1, width=20, value=(
			"Church Board", "Men", "Youth", "Women", "Children", "Music","Intercessors","Evangelism", "Ushering"),
										 font=("times new roman", 14),textvariable = self.department)
			self.data_g_1.place(relx=0.6, rely=0.01)

			self.data_i = Label(self.con_frame_1, text="Telephone", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_i.place(relx=0.5, rely=0.16)
			self.data_i_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),textvariable = self.phone)
			self.data_i_1.place(relx=0.6, rely=0.16)

			self.data_j = Label(self.con_frame_1, text="Address", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_j.place(relx=0.5, rely=0.31)
			self.data_j_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),textvariable = self.address)
			self.data_j_1.place(relx=0.6, rely=0.31)

			self.data_k = Label(self.con_frame_1, text="Email", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_k.place(relx=0.5, rely=0.46)
			self.data_k_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),textvariable = self.email)
			self.data_k_1.place(relx=0.6, rely=0.46)


			self.data_l = Label(self.con_frame_1, text="Marital Status", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_l.place(relx=0.5, rely=0.61)
			self.data_l_1 = ttk.Combobox(self.con_frame_1, width=20, value=(
			"Married", "Single", "Separated", "Window/Widower", "Others"),
										 font=("times new roman", 14),textvariable = self.status)
			self.data_l_1.place(relx=0.6, rely=0.61)

			self.data_m = Label(self.con_frame_1, text="Occupation", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_m.place(relx=0.5, rely=0.76)
			self.data_m_1 = Entry(self.con_frame_1, width=22, bg="white", fg="black", font=("times new roman", 14),textvariable = self.occupation)
			self.data_m_1.place(relx=0.6, rely=0.76)

			self.upload_btn =Button(self.con_frame_1,text = "Upload Photo",font = ("times new roman ",14),width = 18,bg = "#9A0033",fg="white",command =take_photo)
			self.upload_btn.place(relx = 0.79,rely = 0.76)

			self.picture_frame = Frame(self.fm, width=200, height=200, bd=1, relief=SUNKEN)
			self.picture_frame.place(relx=0.18, rely=0.58)


			self.btn_img_id = Label(self.con_frame_1, bg="white")
			self.btn_img_8_A = PhotoImage(file="graphics/id_1.png")
			self.btn_img_id.config(image=self.btn_img_8_A)
			self.btn_img_id.place(relx=0.8, rely=0)

			self.con_frame_2 = LabelFrame(self.fm, width=1000, height=300, bg="white")
			self.con_frame_2.place(relx=0.03, rely=0.46)

			self.data_1 = Label(self.con_frame_2, text="Fax", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_1.place(relx=0.01, rely=0.01)
			self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),textvariable = self.fax)
			self.data_1_1.place(relx=0.2, rely=0.01)

			self.data_2 = Label(self.con_frame_2, text="Employer", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_2.place(relx=0.01, rely=0.16)
			self.data_2_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),textvariable = self.emloyer)
			self.data_2_1.place(relx=0.2, rely=0.16)

			self.data_1 = Label(self.con_frame_2, text="Hometown", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_1.place(relx=0.01, rely=0.31)
			self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),textvariable = self.hometown)
			self.data_1_1.place(relx=0.2, rely=0.31)

			self.data_l = Label(self.con_frame_2, text="Region", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_l.place(relx=0.01, rely=0.46)
			self.data_l_1 = ttk.Combobox(self.con_frame_2, width=23, value=(
				"Greater Accra", "Oti", "Bono East", "Central", "Eastern","Upper East", "Upper West", "Savana","Volta", "North East", "Bono","Ahafo", "Western North", "Northern", "Ashanti", "Westerm"),
										 font=("times new roman", 14),textvariable = self.region)
			self.data_l_1.place(relx=0.2, rely=0.46)

			self.data_l = Label(self.con_frame_2, text="Tither", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_l.place(relx=0.01, rely=0.61)
			self.data_l_1 = ttk.Combobox(self.con_frame_2, width=23, value=(
				"Yes", "No", ),
										 font=("times new roman", 14),textvariable = self.Tithe)
			self.data_l_1.place(relx=0.2, rely=0.61)

			self.data_1 = Label(self.con_frame_2, text="Heath Status", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_1.place(relx=0.01, rely=0.76)
			self.data_1_1 = Entry(self.con_frame_2, width=25, bg="white", fg="black", font=("times new roman", 14),textvariable = self.health)
			self.data_1_1.place(relx=0.2, rely=0.76)

			self.data_g = Label(self.con_frame_2, text="Department", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_g.place(relx=0.5, rely=0.01)
			self.data_g_1 = ttk.Combobox(self.con_frame_2, width=28, value=(
				"Church Board", "Men", "Youth", "Women", "Children", "Music", "Intercessors", "Evangelism", "Ushering"),
										 font=("times new roman", 14),textvariable = self.how)
			self.data_g_1.place(relx=0.65, rely=0.01)

			self.data_i = Label(self.con_frame_2, text="Company Name", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_i.place(relx=0.5, rely=0.16)
			self.data_i_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.company)
			self.data_i_1.place(relx=0.65, rely=0.16)

			self.data_j = Label(self.con_frame_2, text="Post Address", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_j.place(relx=0.5, rely=0.31)
			self.data_j_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.pst_address)
			self.data_j_1.place(relx=0.65, rely=0.31)

			self.data_k = Label(self.con_frame_2, text="Emerg. Contact", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_k.place(relx=0.5, rely=0.46)
			self.data_k_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.contact)
			self.data_k_1.place(relx=0.65, rely=0.46)

			self.data_l = Label(self.con_frame_2, text="Edu. Level", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_l.place(relx=0.5, rely=0.61)
			self.data_l_1 = ttk.Combobox(self.con_frame_2, width=28, value=(
				"University", "SHS", "JHS", "Training college", "N/A"),
										 font=("times new roman", 14),textvariable = self.level)
			self.data_l_1.place(relx=0.65, rely=0.61)

			self.data_m = Label(self.con_frame_2, text="Year", font=("times new roman", 15), bg="white",
								fg="black")
			self.data_m.place(relx=0.5, rely=0.76)
			self.data_m_1 = Entry(self.con_frame_2, width=30, bg="white", fg="black", font=("times new roman", 14),textvariable = self.edu_instution)
			self.data_m_1.place(relx=0.65, rely=0.76)

			#==================================================commands register buttons ==================================

			self.btn_frame = LabelFrame(self.fm, width=200, height=300, bg="white")
			self.btn_frame.place(relx=0.8, rely=0.46)

			self.upload_btn = Button(self.btn_frame, text="SUBMIT", font=("times new roman ", 14), width=14,command = Submit,bg = "#9A0033",fg="white")
			self.upload_btn.place(relx=0.05, rely=0.01)

			self.upload_btn = Button(self.btn_frame, text="RESET", font=("times new roman ", 14), width=14,command =Reset,bg = "#9A0033",fg="white")
			self.upload_btn.place(relx=0.05, rely=0.21)

			self.upload_btn = Button(self.btn_frame, text="EXIT", font=("times new roman ", 14), width=14,command = self.add_mem.destroy,bg = "#9A0033",fg="white")
			self.upload_btn.place(relx=0.05, rely=0.41)
			self.upload_btn = Button(self.btn_frame, text="UPDATE", font=("times new roman ", 14), width=14,bg = "#9A0033",fg="white")
			self.upload_btn.place(relx=0.05, rely=0.61)
#===============================================tithes and offering=========================================
		def tithe():
			self.tframe = Frame(self.master,width = 1400,height = 720,)
			self.tframe.place(relx = 0,rely =0)
			self.menubar = Menu(self.tframe, background="red", fg="white")
			root.config(menu=self.menubar)
			self.file_menu = Menu(self.menubar, tearoff=0)
			self.file_menu.add_command(label='Add Members')
			self.file_menu.add_command(label='Open...')
			self.file_menu.add_command(label='Close', command=root.destroy)
			self.file_menu.add_command(label='Settings')
			self.file_menu.add_separator()

			self.give_menu = Menu(self.menubar, tearoff=0)
			self.give_menu.add_command(label='Tithes')
			self.give_menu.add_command(label='Offering')
			self.give_menu.add_command(label='Pledges')
			self.give_menu.add_command(label='Send Reminders')
			self.file_menu.add_command(label='Dashboard', command=main)
			self.menubar.add_cascade(label='Add Members', menu=self.file_menu, font=("arial", 20),command = add_mem)
			self.menubar.add_cascade(label='Tithes and Offering', menu=self.give_menu)
			self.menubar.add_cascade(label='Attendance', menu=self.file_menu)
			self.menubar.add_cascade(label='Settings', menu=self.file_menu)
			self.sideframe = Frame(self.tframe,width = 1400,height = 670,bg = "#9A0033",bd =2,)
			self.sideframe.place(relx=0,rely = 0.07)

			self.con_frame = Frame(self.tframe,width =1400,height = 700)
			self.con_frame.place(relx = 0.2,rely =0)
			self.nav_frame =Frame(self.tframe,width = 1400,height = 55,bg = "#9A0033",bd = 2,relief = SUNKEN)
			self.nav_frame.place(relx=0,rely = 0)
			self.tnav_label = Label(self.nav_frame,text = "GRACE CHAPEL TITHE AND OFFERING DATA", font = ("arial",18,"bold"),fg ="white",bg = "#9A0033")
			self.tnav_label.place(relx = 0.3,rely =0.36)



			"""def StudentRec2(event):
				try:
					global selected_tuple

					index = self.listbox_tithe.curselection()[0]
					selected_tuple = self.listbox_tithe.get(index)

					self.mem_id.delete(0, END)
					self.mem_id.insert(END, selected_tuple[1])
					self.name1.delete(0, END)
					self.name1.insert(END, selected_tuple[2])
					self.month.delete(0, END)
					self.month.insert(END, selected_tuple[3])
					self.amount.delete(0, END)
					self.amount.insert(END, selected_tuple[4])
					self.date.delete(0, END)
					self.date.insert(END, selected_tuple[5])

				except IndexError:
					pass"""

			def Send():
				if (len(self.mem_id.get()) != 0):
					tithe_backend.Insert(self.mem_id.get(), self.name1.get(), self.month.get(), self.amount.get(),self.date.get()
									)

				else:
					messagebox.showwarning("Input Error", "Please Fill the form before submission")

			Mysky = "#DCF0F2"
			Myyellow = "#F2C84B"

			style = Style()


			"""style.theme_create("dummy", parent="alt", settings={
				"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
				"TNotebook.Tab": {
					"configure": {"padding": [5, 1], "background": Mysky},
					"map": {"background": [("selected", Myyellow)],
							"expand": [("selected", [1, 1, 1, 0])]}}})"""

			#style.theme_use("dummy")



			self.tabcontrol = ttk.Notebook(self.con_frame,width = 1300,height = 700)
			self.offer = Frame(self.tabcontrol)
			self.tithe = Frame(self.tabcontrol)
			self.pledge = Frame(self.tabcontrol)
			self.t_db = Frame(self.tabcontrol)
			self.tabcontrol.add(self.offer,text = "OFFECTORY")
			self.tabcontrol.add(self.tithe,text= "TITHE")
			self.tabcontrol.add(self.pledge,text = "PLEDGE")
			self.tabcontrol.add(self.t_db, text="TITHE DATABASE")
			self.tabcontrol.place(relx = 0,rely =0.08)
			self.entry_frame = Frame(self.tithe,width = 700,height =250,bd =3,relief = SUNKEN)
			self.entry_frame.place(relx = 0,rely = 0)
			self.btn_frame = Frame(self.tithe, width=200, height=250, bd=3, relief=SUNKEN)
			self.btn_frame.place(relx=.65, rely=0)

			self.bt_1 = Button(self.btn_frame,text = "SAVE DATA",font = ("times new roman",14),width = 15,command =Send)
			self.bt_1.place(relx = 0.04,rely = 0.02)
			self.bt_1 = Button(self.btn_frame, text="UPDATE TITHER", font=("times new roman", 14), width=15,command =  Update)
			self.bt_1.place(relx=0.04, rely=0.25)
			self.bt_1 = Button(self.btn_frame, text="DELETE TITHER", font=("times new roman", 14), width=15,command = delkey)
			self.bt_1.place(relx=0.04, rely=0.48)
			self.bt_1 = Button(self.btn_frame, text="DISPLAY TITHER", font=("times new roman", 14), width=15,command =Display1)
			self.bt_1.place(relx=0.04, rely=0.71)

			self.btn_frame2 = Frame(self.tithe, width=140, height=250, bd=2, relief=SUNKEN,)
			self.btn_frame2.place(relx=0.55, rely=0.0)
			self.bt_1 = Button(self.btn_frame2,text = "IMPORT",font = ("times new roman",14),width = 12,command =Display)
			self.bt_1.place(relx = 0.04,rely = 0.02)
			self.bt_1 = Button(self.btn_frame2, text="ADD", font=("times new roman", 14), width=12,command =add_mem)
			self.bt_1.place(relx=0.04, rely=0.25)
			self.bt_1 = Button(self.btn_frame2, text="RESET", font=("times new roman", 14), width=12,command =reset1)
			self.bt_1.place(relx=0.04, rely=0.48)
			self.bt_1 = Button(self.btn_frame2, text="CLOSE", font=("times new roman", 14), width=12,)
			self.bt_1.place(relx=0.04, rely=0.71)




			self.lbl1=Label(self.entry_frame,text = "Member ID",font = ("times new roman",14))
			self.lbl1.place(relx = 0.05,rely =0.0)
			self.entry1 = Entry(self.entry_frame,font = ("times new roman",14),width=25,textvariable = self.mem_id)
			self.entry1.place(relx=0.25,rely =0.0)
			self.lbl2= Label(self.entry_frame, text="Name", font=("times new roman", 14))
			self.lbl2.place(relx=0.05, rely=0.2)
			self.entry2 = Entry(self.entry_frame, font=("times new roman", 14), width=25,textvariable = self.name1)
			self.entry2.place(relx=0.25, rely=0.2)
			self.lbl3= Label(self.entry_frame, text="Month", font=("times new roman", 14))
			self.lbl3.place(relx=0.05, rely=0.4)
			self.entry3 = ttk.Combobox(self.entry_frame, font=("times new roman", 14), width=25,textvariable = self.month,value =("January","February","March","April","May","June","July","August","September","October","November","December"))
			self.entry3.place(relx=0.25, rely=0.4)
			self.lbl4 = Label(self.entry_frame, text="Amount Paid", font=("times new roman", 14))
			self.lbl4.place(relx=0.05, rely=0.6)
			self.entry4 = Entry(self.entry_frame, font=("times new roman", 14), width=25,textvariable = self.amount)
			self.entry4.place(relx=0.25, rely=0.6)
			self.lbl5 = Label(self.entry_frame, text="Date Paid", font=("times new roman", 14))
			self.lbl5.place(relx=0.05, rely=0.8)

			def gen_date():
				#self.entry6.config()
				self.time_today=datetime.datetime.now()
				self.date.set(f" {self.time_today}")

			self.entry6 = Entry(self.entry_frame, font=("times new roman", 14), width=25,textvariable = self.date)
			self.entry6.place(relx=0.25, rely=0.8)
			gen_date()

			self.picture_frame_1 = Frame(self.entry_frame, width=200, height=200, bd=2, relief=SUNKEN)
			self.picture_frame_1.place(relx=0.7, rely=0.05)
			#======================================Tither Id ===========================================

			self.btn_img_id_1 = Label(self.picture_frame_1, bg="white")
			self.btn_img_tithe= PhotoImage(file="graphics/id.png")
			self.btn_img_id_1.config(image=self.btn_img_tithe)
			self.btn_img_id_1.place(relx=0, rely=0)

			self.listbox_frame = Frame(self.tithe, width=1050, height=300, bd=3, relief=SUNKEN)
			self.listbox_frame.place(relx=0, rely=0.45)
			self.scrollbarx = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
			self.scrollbary = Scrollbar(self.listbox_frame, orient=VERTICAL)

			self.scrollbarx.place(relx=0.08, rely=0.9, width=12000)
			self.listbox= Listbox(self.listbox_frame,width =170,height = 15,bd =3)
			self.listbox.place(relx = 0,rely = 0)
			self.listbox.bind('<<ListboxSelect>>', StudentRec)



			self.scrollbary.config(command=self.listbox.yview)
			self.scrollbary.place(relx=0.98, rely=0, height=270)
			self.scrollbarx.config(command=self.listbox.xview)
			self.scrollbarx.place(relx=0, rely=0.87, width=1022)

			"""self.scrollbarx_tithe = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
			self.scrollbary_tithe = Scrollbar(self.listbox_frame, orient=VERTICAL)
			self.listbox_tithe = Listbox(self.listbox_frame, width=83, height=15, bd=2)
			self.listbox_tithe.place(relx=0.5, rely=0)
			self.listbox_tithe.bind('<<ListboxSelect>>', StudentRec2)
			self.scrollbary_tithe.config(command=self.listbox_tithe.yview)
			self.scrollbary_tithe.place(relx=0.98, rely=0, height=270)
			self.scrollbarx_tithe.config(command=self.listbox_tithe.xview)
			self.scrollbarx_tithe.place(relx=0.5, rely=0.87, width=430)"""

			self.search1 = Entry(self.tithe, width=26, font=("times new roman", 15), textvariable="look")
			self.search1.place(relx=0.02, rely=0.4)
			self.search_btn1 = Button(self.tithe, text="SEARCH", font=("times new roman", 10),
									 bd=2)
			self.search_btn1.place(relx=0.22, rely=0.4)

			"""self.search2 = Entry(self.tithe, width=26, font=("times new roman", 15), textvariable="say")
			self.search2.place(relx=0.45, rely=0.4)
			self.search_btn2 = Button(self.tithe, text="SEARCH", font=("times new roman", 10),command = Search_payee,
									  bd=2)
			self.search_btn2.place(relx=0.65, rely=0.4)"""



			def Reset_tithe():
				self.amount.set("GHC")

			def  search_win():
				self.search_win = Toplevel()
				self.search_win.geometry("400x200+500+300")
				self.search_win.resizable(0,0)
				self.search_win.title("Search Tithers")

				def SearchRecord_tithe():
					# checking search text is empty or not
					if self.SEARCH.get() != "":
						# clearing current display data
						self.tree.delete(*self.tree.get_children())
						# open database
						conn = sqlite3.connect('tithe.db')
						# select query with where clause
						cursor = conn.execute("SELECT * FROM finan WHERE mem_id LIKE ?",
											  ('%' + str(self.SEARCH.get()) + '%',))
						# fetch all matching records
						fetch = cursor.fetchall()
						# loop for displaying all records into GUI
						for data in fetch:
							self.tree.insert('', 'end', values=(data))
						cursor.close()
						conn.close()
					elif self.SEARCH.get() != DisplayData_tithe():
						messagebox.showwarning("Search Error", "Name Is not recognized")

				self.search_L=Label(self.search_win,text = "SEARCH TITHE PAYER",font=("times new roman",12))
				self.search_L.place(relx = 0.08,rely =0.2)

				self.search_entry=Entry(self.search_win,width = 30,font = ("times new roman",15),fg = "purple")
				self.search_entry.place(relx = 0.1,rely =0.34)

				self.search_LBtn = Button(self.search_win,text ="SEARCH",font = ("times new roman",13),width = 23,command =SearchRecord_tithe)
				self.search_LBtn.place(relx =0.2,rely=0.54)


			def delete_tithe():
				if self.tree.selection():
					result = messagebox.askquestion('Python - Delete Data Row In SQLite',
													'Are you sure you want to delete this record?', icon="warning")
					if result == 'yes':
						curItem = self.tree.focus()
						contents = (self.tree.item(curItem))
						selecteditem = contents['values']
						self.tree.delete(curItem)
						tithe_backend.delete(selecteditem[0])

					else:
						DisplayData_tithe()

			def DisplayData_tithe():
				# clear current data
				self.tree.delete(*self.tree.get_children())
				# open databse
				conn = sqlite3.connect('tithe.db')
				# select query
				cursor = conn.execute("SELECT * FROM finan")
				# fetch all data from database
				fetch = cursor.fetchall()
				# loop for displaying all data in GUI
				for data in fetch:
					self.tree.insert('', 'end', values=(data))
				cursor.close()
				conn.close()

				Reset_tithe()

			self.scrollbarx = Scrollbar(self.t_db, orient=HORIZONTAL)
			self.scrollbary = Scrollbar(self.t_db, orient=VERTICAL)
			self.tree = ttk.Treeview(self.t_db, columns=(
				'S/N', "Membership ID", "Name", "Month Of Payment", "Amount Paid", "Date Of Payment"),
									 selectmode="extended", height=13, yscrollcommand=self.scrollbary.set,xscrollcommand=self.scrollbarx.set)
			#self.tree.configure(selectmode="extended")
			style = Style()
			style.configure("Treeview.Heading", font=("times new roman", 15,"bold"), foreground='purple')
			style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 14, ),foreground='purple')
			self.scrollbary.config(command=self.tree.yview)
			self.scrollbary.place(relx=0.94, rely=0.0, height=510)
			self.scrollbarx.config(command=self.tree.xview)
			self.scrollbarx.place(relx=0.02, rely=0.74, width=900)

			self.tree.heading('S/N', text="S/N", anchor=W)
			self.tree.heading('Membership ID', text="Membership ID", anchor=W)
			self.tree.heading('Name', text="Name", anchor=W)
			self.tree.heading('Month Of Payment', text="Month Of Payment", anchor=W)
			self.tree.heading('Amount Paid', text="Amount Paid", anchor=W)
			self.tree.heading('Date Of Payment', text="Date Of Payment", anchor=W)


			self.tree.column('#0', stretch=NO, minwidth=0, width=0)
			self.tree.column('#1', stretch=NO, minwidth=0, width=150)
			self.tree.column('#2', stretch=NO, minwidth=0, width=150)
			self.tree.column('#3', stretch=NO, minwidth=0, width=150)
			self.tree.column('#4', stretch=NO, minwidth=0, width=150)
			self.tree.column('#5', stretch=NO, minwidth=0, width=150)
			self.tree.column('#6', stretch=NO, minwidth=0, width=150)



			self.tree.place(relx=0.02, rely=0.0, width=1040, height=500)

			self.a_btn_Frame = Frame(self.t_db,width = 900 , height = 50,bd = 2,relief = SUNKEN)
			self.a_btn_Frame.place(relx = 0.03,rely = 0.78)
			self.display_btn = Button(self.a_btn_Frame,text = "DISPLAY",font = ("times new roman",14),command = DisplayData_tithe)
			self.display_btn.place(relx = 0.02,rely =0.1)
			self.export_btn = Button(self.a_btn_Frame, text="EXPORT TO EXCEL", font=("times new roman", 14))
			self.export_btn.place(relx=0.15, rely=0.1)
			self.delete_btn = Button(self.a_btn_Frame, text="DELETE RECORD", font=("times new roman", 14),command = delete_tithe)
			self.delete_btn.place(relx=0.4, rely=0.1)
			self.delete_btn = Button(self.a_btn_Frame, text="SEARCH RECORDS", font=("times new roman", 14),
									 command=search_win)

			self.delete_btn.place(relx=0.6, rely=0.1)
			self.delete_btn = Button(self.a_btn_Frame, text="CLEAR DATA", font=("times new roman", 14),
									 command=delete_tithe)
			self.delete_btn.place(relx=0.82, rely=0.1)


		#=============================================attendance system=====================================
		def attendance():

			def view_content():
				self.listbox_at.delete(0, END)
				for row in backend_1.view():
					self.listbox_at.insert(END, f"{row[0]}          {row[1]}          {row[2]}", str(' '))
			self.sort.set("Sort by")
			self.masterframe= Frame(self.master,width =1400,height = 750,bg = "#9A0033")
			self.masterframe.place(relx=0,rely=0)
			self.sideframe = Frame(self.masterframe,width = 250,height = 750,bg= "#9A0033")
			self.sideframe.place(relx=0,rely =0)
			self.naveframe = Frame(self.masterframe,width = 1200,height = 90,bg ="#9A0033")
			self.naveframe.place(relx = 0.1772,rely = 0)
			self.main_con = Frame(self.masterframe,width = 1100,height = 600,bg = 'white')
			self.main_con.place(relx = 0.17,rely = 0.12)
			self.nav_label = Label(self.naveframe,text = "GRACE CHAPEL ATTENDANCE SYSTEM",font =("arial",19,"bold"),bg ="#9A0033",fg = "white")
			self.nav_label.place(relx = 0.2,rely = 0.4)

			#=============================================Manual Attendance================================

			self.manual_Frame = Frame(self.main_con,width = 590,height = 1000,relief = SUNKEN,bd = 4)
			self.manual_Frame.place(relx =0,rely = 0.0 )
			self.listbox_frame = Frame(self.manual_Frame, width=570, height=200, bd=3, relief=SUNKEN)
			self.listbox_frame.place(relx=0, rely=0)
			self.scrollbarx = Scrollbar(self.listbox_frame, orient=HORIZONTAL)
			self.scrollbary = Scrollbar(self.listbox_frame, orient=VERTICAL)

			self.scrollbarx.place(relx=0.08, rely=0.9, width=12000)
			self.listbox_at = Listbox(self.listbox_frame, width=86, height=10, bd=3,font = ("times new roman",13))
			self.listbox_at.place(relx=0.02, rely=0)
			self.listbox_at.bind('<<ListboxSelect>>', "StudentRec")
			self.scrollbary.config(command=self.listbox_at.yview)
			self.scrollbary.place(relx=0.98, rely=0, height=270)
			self.scrollbarx.config(command=self.listbox_at.xview)
			self.scrollbarx.place(relx=0, rely=0.87, width=1022)

			self.name_ent = Entry(self.manual_Frame,bd = 2,font = ("times new roman",14),width = 28)
			self.name_ent.place(relx = 0.0,rely = 0.25)
			self.date_entry = Entry(self.manual_Frame,bd = 2,font = ("times new roman",14),width = 15)
			self.date_entry.place(relx=0.45,rely =0.25)
			self.mark =ttk.Combobox(self.manual_Frame,value = ("Present","Absent"),font = ("times new roman",14),width = 15)
			self.mark.place(relx = 0.7,rely=0.25)

			#===================================================Buttons========================================================
			self.get_member = Button(self.manual_Frame,text = "Get Member",font = ("times new roman",14),command =view_content)
			self.get_member.place(relx = 0.2,rely = 0.3)

			self.submit_att = Button(self.manual_Frame, text="Submit Attendance", font=("times new roman", 14))
			self.submit_att.place(relx=0.4, rely=0.3)

			self.reset = Button(self.manual_Frame, text="Reset", font=("times new roman", 14))
			self.reset.place(relx=0.7, rely=0.3)

			self.attendance_tree= Frame(self.manual_Frame,width =550,height = 200,relief =SUNKEN,bd =4)
			self.attendance_tree.place(relx = 0.01,rely = 0.36)

			self.tree = ttk.Treeview(self.attendance_tree, columns=(
				'S/N', "Member","Date","Attendance Status"),
									 selectmode="extended", height=18, yscrollcommand=self.scrollbary.set,
									 xscrollcommand=self.scrollbarx.set)
			# self.tree.configure(selectmode="extended")
			style = ttk.Style()
			# Pick a theme
			style.theme_use('clam')

			style.configure("Treeview.Heading", font=("times new roman", 15, "bold"), foreground='blue',
							fieldbackground="silver")
			style.configure("Treeview", highlightthickness=4, bd=2, font=('times new roman', 15,), background="silver",
							foreground="white"
							, rowheight=40, fieldbackground="silver")
			style.map('Treeview', background=[('selected', 'green')])
			self.tree.heading('S/N', text="S/N", anchor=W)
			self.tree.heading('Member', text="Member", anchor=W)
			self.tree.heading('Date', text="Date", anchor=W)
			self.tree.heading('Attendance Status', text="Attendance Status", anchor=W)


			self.tree.column('#0', stretch=NO, minwidth=0, width=0)
			self.tree.column('#1', stretch=NO, minwidth=0, width=50)
			self.tree.column('#2', stretch=NO, minwidth=0, width=150)
			self.tree.column('#3', stretch=NO, minwidth=0, width=150)
			self.tree.column('#4', stretch=NO, minwidth=0, width=170)


			self.tree.place(relx=0.02, rely=0.0, width=1040, height=500)

			#============================================Automated Attendance System==========================
			self.automated_Frame = Frame(self.main_con, width=480, height=600, relief=SUNKEN, bd=4)
			self.automated_Frame.place(relx=0.55, rely=0.0)

			self.ai_bg = Label(self.automated_Frame, bg="white")
			self.ai_bg_p = PhotoImage(file="graphics/ai11.png")
			self.ai_bg.config(image=self.ai_bg_p)
			self.ai_bg.place(relx=0, rely=0)
			self.head_label = Label(self.ai_bg,text = "Face Recognition System",font = ("times new roman",23,"bold"),bg = "#010912",fg = "#f1f1f1")
			self.head_label.place(relx = 0.12,rely = 0.1)
			self.lbl = Button(self.ai_bg,text = "Start Automatic Attendance System",font = ("times new roman",14),bg = "#010912",fg = "#f1f1f1")
			self.lbl.place(relx = 0.2,rely = 0.8)
			view_content()

		#===============================================AI System==============================================================================
		def Ai():
			self.window = Toplevel()
			self.window.geometry()

		#===============================================Functions==============================================================================

		def get():
			self.frame_1.destroy()
			Sign()

		def login():
			self.frame_2.destroy()
			main()
			self.card_ent2.set(3)
			self.card_ent3.set(0)
			graph()

		def logout():
			self.frame_3.destroy()
			Sign()

		def member():
			self.frame_3.destroy()
			membership()

		def double_tap(self):
			item = self.tree.identify('item')
			global bill_num
			bill_num = self.tree.item(item)['values'][0]

			global bill
			bill = Toplevel()
			# pg = open_bill(bill)
			# bill.protocol("WM_DELETE_WINDOW", exitt)
			bill.mainloop()

		welcome()

root = Tk()
app = App(root)
root.mainloop()