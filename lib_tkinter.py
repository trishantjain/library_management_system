from ast import main
from tkinter import *
import lib_database

# **** ____DONATE FUNCTION____ ****
def trisant():
    print(user_name.cget("text"))

def donate():

    # Function to add book to database
    def donate_submit():
        book_name = book_entry.get()
        no = no_entry.get()
        lib_database.insert_into_database(book_name, no)
        book_entry.delete(0, END)
        no_entry.delete(0, END)

    # Function to exit donate book window
    def exit_donate():
        donate_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')
    donate_window = Tk()
    donate_window.configure(bg="#66ccff")
    donate_window.geometry('700x300')

    # ** Frame 1 of Donate Window
    frame_1 = Frame(donate_window, bg='#66ccff')

    Label(frame_1, text='Book Name: ', bg='#66ccff',
          font=('courier', 18, 'bold')).pack(side=LEFT)

    book_entry = Entry(frame_1, font=('arial', 15))
    book_entry.pack(pady=4)

    frame_1.pack(pady=5)

    # ** Frame 2 of Donate Window
    frame_2 = Frame(donate_window, bg='#66ccff')

    Label(frame_2, text='No of Books: ', bg='#66ccff',
          font=('courier', 18, 'bold')).pack(side=LEFT)

    no_entry = Entry(frame_2, font=('arial', 15))
    no_entry.pack()

    frame_2.pack(pady=10)

    # **** SUBMIT BUTTON ****
    Button(donate_window, text='Submit',
           font=('courier', 16, 'bold'), command=donate_submit).pack()

    # **** EXIT BUTTON ****
    Button(donate_window, text='Exit', bg='red', fg='white',
           font=('courier', 15, 'bold'), command=exit_donate).pack(pady=15)

    donate_window.mainloop()


# **** ____RETURN FUNCTION____ ****

def rtrn():

    def rtrn_submit():
        pass

    def exit_return():
        return_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')
    return_window = Tk()
    return_window.geometry('700x300')

    # **** SUBMIT BUTTON ****
    Button(return_window, text='Exit', bg='red',
           font=('arial', 18, 'bold'), command=rtrn_submit).pack()

    # **** EXIT BUTTON ****
    Button(return_window, text='Exit', bg='red',
           font=('arial', 18, 'bold'), command=exit_return).pack()

    return_entry = Entry(return_window)
    return_entry.pack()

    nort_entry = Entry(return_window)
    nort_entry.pack()

    return_window.mainloop()


# **** ____BORROW FUNCTION____ ****


def borrow():

    def add_book():
        lib_book_list = lib_database.get_book_list()

        for i, j in lib_book_list:
            if i == get_entry.get():
                book_name = get_entry.get()
                print(user_name)
                print(pas_name)
                lib_database.add_book_cred(book_name, user_name, pas_name)
                main_window.destroy()
                main_window.geometry('600x700')
                break

        else:
            Label(borrow_window,
                  text="Sorry! Currently this book is not available").pack()

    def exit_borrow():
        borrow_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')
    borrow_window = Tk()
    borrow_window.geometry('700x300')

    global get_entry
    get_entry = Entry(borrow_window, font=('arial', 15))
    get_entry.pack()

    # lib_database.add_book_cred(no_entry, pas_ck)

    Button(borrow_window, text='Add', bg='red',
           font=('arial', 18, 'bold'), command=add_book).pack()

    Button(borrow_window, text='Exit', bg='red',
           font=('arial', 18, 'bold'), command=exit_borrow).pack()

    borrow_window.mainloop()

# **** ____BOOK LIST FUNCTION____ ****``````


def bookList():

    # Function to destroy list window
    def exit_list():
        list_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')
    list_window = Tk()
    list_window.geometry('700x300')

    k = lib_database.get_book_list()

    for i, j in k:
        Label(list_window, text=i).pack()

    Button(list_window, text='Exit', bg='red',
           font=('arial', 18, 'bold'), command=exit_list).pack()

    list_window.mainloop()


# **** ____LOGIN FUNCTION____ ****``````


def login():

    def logined():
        login_window.destroy()
        main_window.geometry('600x700')
        Button(main_window, text='My List').pack()

    # ---> Submit button function

    def login_cred():
        user_ck = user_entry.get()
        global user_name
        user_name = Label(main_window, text=user_ck)
        user_name.pack()
        trisant()

        pas_ck = pass_entry.get()
        global pas_name
        pas_name = Label(main_window, text=pas_ck)
        pas_name.pack()

        cred = lib_database.check_credentials(user_ck, pas_ck)

        if cred == 1:
            logined()

        else:
            Label(login_window, text='Credentials are wrong!',
                  fg='red').pack()

    # ---> Exit button function
    def exit_logfunc():
        login_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')

    login_window = Tk()
    login_window.geometry('590x300')
    login_window.resizable(False, False)

    # --> Frame 1
    f1 = Frame(login_window, padx=20)
    Label(f1, font=20,  text='Username').pack(side=LEFT)
    user_entry = Entry(f1,  font=('courier', 18))
    user_entry.pack(padx=20, anchor='e')
    f1.pack(anchor='w', padx=30, pady=20)

    # --> Frame 2
    f2 = Frame(login_window, padx=20)
    Label(f2, font=20,  text='Password').pack(side=LEFT)
    pass_entry = Entry(f2,  font=('courier', 18), show="*")
    pass_entry.pack(padx=20, anchor='e')
    f2.pack(anchor='w', padx=30, pady=20)

    # **** SUBMIT BUTTON ****
    submit_login = Button(login_window, text='Submit',
                          font=('courier', 15), command=login_cred)
    submit_login.pack()

    # **** EXIT BUTTON ****
    exit_login = Button(login_window, text='Exit',
                        font=('courier', 15), bg='#c00', command=exit_logfunc)
    exit_login.pack(pady=20)

    login_window.mainloop()


# **** ____SIGN UP FUNCTION____ ****``````


def signup():

    def submit_cred():
        user = user_entry.get()
        pas = pass_entry.get()
        mail = email_entry.get()
        mobile = mobile_entry.get()

        # ----> Entering Credentials Into Database
        lib_database.insert_credentials(user, pas, mail, mobile)

        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        mobile_entry.delete(0, END)
        email_entry.delete(0, END)

    def exit_signfunc():
        signup_window.destroy()
        main_window.geometry('600x700')

    main_window.geometry('0x0')

    signup_window = Tk()
    signup_window.geometry('590x400')
    signup_window.resizable(False, False)

    f4 = Frame(signup_window, padx=20)
    Label(f4, font=20,  text='Username').pack(side=LEFT)
    user_entry = Entry(f4,  font=('courier', 15))
    user_entry.pack(padx=20, anchor='e')
    f4.pack(anchor='w', padx=30, pady=20)

    f5 = Frame(signup_window, padx=20)
    Label(f5, font=20,  text='Password').pack(side=LEFT)
    pass_entry = Entry(f5,  font=('courier', 15), show="*")
    pass_entry.pack(padx=20, anchor='e')
    f5.pack(anchor='w', padx=30, pady=20)

    f6 = Frame(signup_window)
    Label(f6, font=20, text='Email').pack(side=LEFT)
    email_entry = Entry(f6,  font=('courier', 15))
    email_entry.pack(padx=60, anchor='e')
    f6.pack(anchor='w', padx=50, pady=20)

    f7 = Frame(signup_window, padx=20)
    Label(f7, font=20, text='Mobile No').pack(side=LEFT)
    mobile_entry = Entry(f7,  font=('courier', 15))
    mobile_entry.pack(padx=20, anchor='e')
    f7.pack(anchor='w', padx=30, pady=20)

    # ----> SUBMIT BUTTON IN SIGN WINDOW
    submit_sign = Button(signup_window, text='Submit',
                         font=('courier', 15), command=submit_cred)
    submit_sign.pack()

    # ----> EXIT BUTTON IN SIGN WINDOW
    exit_sign = Button(signup_window, text='Exit', bg='#c00', fg='white',
                       font=('courier', 15), command=exit_signfunc)
    exit_sign.pack(pady=20)

    signup_window.mainloop()


if __name__ == '__main__':
    main_window = Tk()
    main_window.geometry('600x700')
    main_window.resizable(False, False)
    main_window.configure(bg='bisque')

    Label(text='Welcome to Arihant Library', bg='bisque',
          font=('courier', 21, 'bold', 'underline', 'italic')).pack(pady=20)

    Label(text='We have: -', bg='bisque',
          font=('arial ', 13, 'bold')).pack(anchor='w', padx=12)

    # ****** ----> Frame No. 1
    f1 = Frame(main_window, bg='bisque')

    Label(f1, text='Competition Books', bg='bisque',
          font=('arial', 13, 'bold')).pack(anchor='w')

    Label(f1, text='Comedy Books', bg='bisque',
          font=('arial', 13, 'bold')).pack(anchor='w')

    Label(f1, text='School Books', bg='bisque',
          font=('arial', 13, 'bold')).pack(anchor='w')
    f1.pack()

    # ****** ----> Frame No. 2
    f2 = Frame(main_window, bg='bisque')

    # --> Donate Button
    Button(f2, text='Donate', bg='#cc9999',
           font=('simsun', 15, 'bold'), command=donate).pack(side=LEFT, padx=10)

    # --> Borrow Button
    Button(f2, text='Borrow', bg='#cc9999',
           font=('simsun', 15, 'bold'), command=borrow).pack(side=LEFT, padx=10)

    # --> Return Button
    Button(f2, text='Return', bg='#cc9999',
           font=('simsun', 15, 'bold'), command=rtrn).pack(side=LEFT, padx=10)

    # --> List Button
    Button(f2, text='Book List', bg='#cc9999',
           font=('simsun', 15, 'bold'), command=bookList).pack(side=LEFT, padx=10)

    f2.pack(pady=40)

    # ****** ----> Frame No. 3
    f3 = Frame(main_window, bg='bisque')

    # --> Login Button
    Button(f3, text='LOGIN', font=('consolas', 17),
           bg='#cc9999', command=login).pack(side=LEFT, padx=29)

    # --> Signup Button
    Button(f3, text='SIGN UP', font=('consolas', 17),
           bg='#cc9999', command=signup).pack(side=LEFT, padx=29)
    f3.pack(pady=100)

    Button(text='EXIT', font=('courier', 17, 'bold'),
           bg='#cc9999', command=main_window.destroy).pack()

    main_window.mainloop()
