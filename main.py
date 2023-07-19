from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Student.db")
root = Tk()
root.title("Student Management System")
root.geometry("1330x700+0+0")
root.config(bg="#23394c")
root.state("zoomed")

enroll_id = StringVar()
student_name = StringVar()
course_name = StringVar()
email = StringVar()
course = StringVar()
college_name = StringVar()
complaint = StringVar()


# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Chaudhary Ranbir Singh University, Jind", font=("Verdana", 18, "bold"), bg="#23394c",
              fg="#fff")
title.grid(row=0, columnspan=2, padx=10, pady=28)

lblEnroll_ID = Label(entries_frame, text="Enroll_ID", font=("Calibri", 16), bg="#535c68", fg="white")
lblEnroll_ID.grid(row=1, column=0, padx=15, pady=15, sticky="w")
txtEnroll_ID = Entry(entries_frame, textvariable=enroll_id, font=("Calibri", 16), width=38)
txtEnroll_ID.grid(row=1, column=1, padx=15, pady=15, sticky="w")

lblStudent_Name = Label(entries_frame, text="Student_Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblStudent_Name.grid(row=1, column=2, padx=15, pady=15, sticky="w")
txtStudent_Name = Entry(entries_frame, textvariable=student_name, font=("Calibri", 16), width=38)
txtStudent_Name.grid(row=1, column=3, padx=15, pady=15, sticky="w")

lblCourse_Name = Label(entries_frame, text="Course_Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblCourse_Name.grid(row=2, column=0, padx=15, pady=15, sticky="w")
txtCourse_Name = Entry(entries_frame, textvariable=course_name, font=("Calibri", 16), width=38)
txtCourse_Name.grid(row=2, column=1, padx=15, pady=15, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=15, pady=15, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=38)
txtEmail.grid(row=2, column=3, padx=15, pady=15, sticky="w")

lblCourse = Label(entries_frame, text="Course", font=("Calibri", 16), bg="#535c68", fg="white")
lblCourse.grid(row=3, column=0, padx=15, pady=15, sticky="w")
comboCourse = ttk.Combobox(entries_frame, font=("Calibri", 16), width=37, textvariable=course, state="readonly")
comboCourse['values'] = ("UG", "PG")
comboCourse.grid(row=3, column=1, padx=15, pady=15, sticky="w")

lblCollege_Name = Label(entries_frame, text="College_Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblCollege_Name.grid(row=3, column=2, padx=15, pady=15, sticky="w")
txtCollege_Name = Entry(entries_frame, textvariable=college_name, font=("Calibri", 16), width=38)
txtCollege_Name.grid(row=3, column=3, padx=15, pady=15, sticky="w")

lblComplaint = Label(entries_frame, text="Complaint", font=("Calibri", 16), bg="#535c68", fg="white")
lblComplaint.grid(row=4, column=0, padx=15, pady=15, sticky="w")
txtComplaint = Text(entries_frame, width=90, height=5, font=("Calibri", 16))
txtComplaint.grid(row=5, column=0, columnspan=4, padx=15, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    enroll_id.set(row[1])
    student_name.set(row[2])
    course_name.set(row[3])
    email.set(row[4])
    course.set(row[5])
    college_name.set(row[6])
    txtComplaint.delete(1.0, END)
    txtComplaint.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_student():
    if txtEnroll_ID.get() == "" or txtStudent_Name.get() == "" or txtCourse_Name.get() == "" or txtEmail.get() == "" or comboCourse.get() == "" or txtCollege_Name.get() == "" or txtComplaint.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All The Details")
        return
    db.insert(txtEnroll_ID.get(), txtStudent_Name.get(), txtCourse_Name.get(), txtEmail.get(), comboCourse.get(),txtCollege_Name.get(), txtComplaint.get(
        1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()


def update_student():
    if txtEnroll_ID.get() == "" or txtStudent_Name.get() == "" or txtCourse_Name.get() == "" or txtEmail.get() == "" or comboCourse.get() == "" or txtCollege_Name.get() == "" or txtComplaint.get(
            1.0, END) == "":
      messagebox.showerror("Erorr in Input", "Please Fill All The Details")
      return
    db.update(row[0], txtEnroll_ID.get(), txtStudent_Name.get(), txtCourse_Name.get(), txtEmail.get(), comboCourse.get(), txtCollege_Name.get(), txtComplaint.get(
        1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    dispalyAll()

def delete_student():
    db.remove(row[0])
    clearAll()
    dispalyAll()

def clearAll():
    enroll_id.set("")
    student_name.set("")
    course_name.set("")
    email.set("")
    course.set("")
    college_name.set("")
    txtComplaint.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=15, pady=15, sticky="w")
btnAdd = Button(btn_frame, command=add_student, text="Add Details", width=15, font=("Calibri", 18, "bold"), fg="#16a085",
              bg="white",bd=1).grid(row=0, column=0)

btnEdit = Button(btn_frame, command=update_student, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                  fg="#2980b9", bg="white",
                  bd=1).grid(row=0, column=1, padx=10)

btnDelete = Button(btn_frame, command=delete_student, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                  fg="#c0392b", bg="white",
                  bd=1).grid(row=0, column=2, padx=10)

btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                  fg="#f39c12", bg="white",
                  bd=1).grid(row=0, column=3, padx=10)
# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1445, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the Headings

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Enroll_ID")
tv.column("2", width=30)
tv.heading("3", text="Student_Name")
tv.heading("4", text="Course_Name")
tv.heading("5", text="Email")
tv.heading("6", text="Course")
tv.column("6", width=20)
tv.heading("7", text="College_Name")
tv.heading("8", text="Complaint")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()