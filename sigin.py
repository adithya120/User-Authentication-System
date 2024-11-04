from importlib.metadata import files
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


#Functionality Part
# def forget_pass():
    # window = Toplevel()
    # window.title("Change Password")
    #
    # bgPic =ImageTk.PhotoImage(file='background.jpg')
    # bglabel = Label(window, image=bgPic)
    # bglabel.grid()
    #
    # heading_label = Label(window, text="RESET PASSWORD",font=("Arial", 18,'bold'),bg='white',fg='magenta2')
    # heading_label.place(x=480,y=60)
    #
    # userLabel = Label(window, text='Username', font=('arial' , 12, 'bold'), bg='white', fg='orchid1')
    # userLabel.place(x=470,y=130)
    #
    # user_entry = Entry(window, width=25, font=('arial', 11, 'bold'), fg='magenta2', bd=0)
    # user_entry.grid(x=470,y=160)
    #
    # Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    # passLabel = Label(window, text='New Password', font=('arial', 18, 'bold'), bg='white', fg='orchid1')
    # passLabel.place(x=470, y=210)
    #
    # newpass_Entry = Entry(window, width=25, font=('arial', 11, 'bold'), fg='magenta2', bd=0)
    # newpass_Entry.place(x=470, y=240)
    #
    # Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)
    # window.mainloop()

def forget_pass():
        window = Toplevel()
        window.title("Change Password")

        bgPic = ImageTk.PhotoImage(file='background.jpg')
        bglabel = Label(window, image=bgPic)
        bglabel.grid()

        heading_label = Label(window, text="RESET PASSWORD", font=("Arial", 18, 'bold'), bg='white', fg='magenta2')
        heading_label.place(x=480, y=60)

        userLabel = Label(window, text='Username', font=('Arial', 12, 'bold'), bg='white', fg='orchid1')
        userLabel.place(x=470, y=130)

        user_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), fg='magenta2', bd=0)
        user_entry.place(x=470, y=160)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

        new_pass_label = Label(window, text='New Password', font=('Arial', 12, 'bold'), bg='white', fg='orchid1')
        new_pass_label.place(x=470, y=210)

        new_pass_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), fg='magenta2', bd=0, show='*')
        new_pass_entry.place(x=470, y=240)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

        confirm_pass_label = Label(window, text='Confirm Password', font=('Arial', 12, 'bold'), bg='white',
                                   fg='orchid1')
        confirm_pass_label.place(x=470, y=290)

        confirm_pass_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), fg='magenta2', bd=0, show='*')
        confirm_pass_entry.place(x=470, y=320)

        Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

        def update_password():
            username = user_entry.get()
            new_password = new_pass_entry.get()
            confirm_password = confirm_pass_entry.get()

            if new_password == '' or confirm_password == '':
                messagebox.showinfo("Error", "All fields are required.")
                return

            if new_password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            # Database code to update the password
            try:
                con = pymysql.connect(host="localhost", user='root', password='123456', database='userdata')
                mycursor = con.cursor()
                query = 'UPDATE data SET password=%s WHERE username=%s'
                mycursor.execute(query, (new_password, username))
                con.commit()
                if mycursor.rowcount > 0:
                    messagebox.showinfo("Success", "Password updated successfully!")
                    window.destroy()  # Close the reset password window
                else:
                    messagebox.showerror("Error", "Username not found.")
            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Connection error: {e}")
            finally:
                if con:
                    con.close()

        submit_button = Button(window, text='Reset Password', font=('Arial', 12, 'bold'), bg='orchid1',
                               command=update_password)
        submit_button.place(x=470, y=380)

        window.mainloop()

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showinfo("Error", "All fields are required.")
    else:
        try:
           con=pymysql.connect(host="localhost",user='root',password='123456')
           mycursor=con.cursor()
        except:
            messagebox.showerror("Error", "Connection is not established try again")
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get() ,passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
             messagebox.showerror("Error", "Invalid username or Password ")
        else:
            messagebox.showinfo("Welcome", "User has been registered successfully")


def signup_page():
    login_window.destroy()
    import Signup



def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if usernameEntry.get() =='Username':
        usernameEntry.delete(0,END)
def password_enter(event):
    if passwordEntry.get() =='Password':
        passwordEntry.delete(0,END)


def delete_user():
    window = Toplevel()
    window.title("Delete User")

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text="DELETE USER", font=("Arial", 18, 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('Arial', 12, 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), fg='magenta2', bd=0)
    user_entry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    def confirm_delete():
        username = user_entry.get()

        if not username:
            messagebox.showinfo("Error", "Username is required.")
            return

        # Function to delete user from the database
        def delete_from_db(username):
            try:
                con = pymysql.connect(host="localhost", user='root', password='123456', database='userdata')
                with con.cursor() as mycursor:
                    query = 'DELETE FROM data WHERE username=%s'
                    mycursor.execute(query, (username,))
                    con.commit()
                    return mycursor.rowcount > 0
            except pymysql.MySQLError as e:
                messagebox.showerror("Database Error", f"Connection error: {e}")
                return False
            finally:
                if con:
                    con.close()

        if delete_from_db(username):
            messagebox.showinfo("Success", "User deleted successfully!")
            window.destroy()  # Close the delete user window
        else:
            messagebox.showerror("Error", "Username not found.")

    submit_button = Button(window, text='Delete User', font=('Arial', 12, 'bold'), bg='orchid1', command=confirm_delete)
    submit_button.place(x=470, y=220)

    window.mainloop()


#GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(False, False)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 20, 'bold'), bg='white', fg='firebrick')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)
frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text ='Forgot Password?',bd=0,bg='white'
                    ,activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light', 9, 'bold')
                    ,fg='firebrick',activeforeground='firebrick',command=forget_pass)
forgetButton.place(x=715,y=295)
DeleteButton=Button(login_window,text ='Delete Button',bd=0,bg='white'
                    ,activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light', 9, 'bold')
                    ,fg='firebrick',activeforeground='firebrick',command=delete_user)
DeleteButton.place(x=600,y=295)

loginButton=Button(login_window,text='login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick'
                   ,activeforeground='white',activebackground='firebrick',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

orLabel=Label(login_window,text='---------------OR---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fblabel=Label(login_window,image=facebook_logo,bg='white')
fblabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
goole_label=Label(login_window,image=google_logo,bg='white')
goole_label.place(x=690,y=440)

twitter_logo=PhotoImage(file='facebook.png')
twitterLabel=Label(login_window,image=facebook_logo,bg='white')
twitterLabel.place(x=740,y=440)

signLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),bg='white')
signLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white'
    ,activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)



login_window.mainloop()