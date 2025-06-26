

from tkinter import *
from tkinter.messagebox import showerror, showinfo
from typing import Optional
from bl.author_bl import AuthorBL
from common.author import Author
from common.data_type import FormAction, FormResult, MethodResult, State


class AuthorDataEntryForm(Toplevel):

    def __init__(self, form_action: FormAction, author_bl: AuthorBL, instance: Optional[Author] = None) -> None:
        super().__init__()
        self.__author_bl: AuthorBL() = author_bl # type: ignore
        self.__form_action = form_action
        self.__form_result = FormResult.RUNNING
        self.__selected_instance: Author | None = instance
        self.__initialize_component()
        self.protocol(name='WM_DELETE_WINDOW', func=self.__close)

    def __initialize_component(self):

        # region window
        win_width = 500
        win_height = 500
        padd_left = (self.winfo_screenwidth()//2) - (win_width//2)
        padd_top = (self.winfo_screenheight()//2) - (win_height//2)

        self.geometry(f'{win_width}x{win_height}+{padd_left}+{padd_top}')
        self.resizable(width=False, height=False)
        self.configure(background='#EEEDED')
        self.title('Library Management System')
        # endregion


        # region frame

        # region header
        self.__header_frame = Frame(
            master=self,
            bg='#EEEDED',
            height=40,
            highlightbackground='#3C486B',
            highlightthickness=1
            )
        self.__header_frame.pack(side=TOP, fill=X)
        self.__header_frame.propagate(False)
        # endregion

        # region footer
        self.__footer_frame = Frame(
            master=self,
            bg='#EEEDED',
            height=55,
            highlightbackground='#3C486B',
            highlightthickness=1
            )
        self.__footer_frame.pack(side=BOTTOM, fill=X)
        self.__footer_frame.propagate(False)
        # endregion

        # region body
        self.__body_frame = Frame(
            master=self,
            bg='#EEEDED'
            )
        self.__body_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.__body_frame.propagate(False)
        # endregion

        #region firstname
        self.__firstname_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__firstname_frame.pack(side=TOP, fill=X, pady=(15, 20))
        self.__firstname_frame.propagate(False)
        # endregion

        #region lastname
        self.__lastname_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__lastname_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__lastname_frame.propagate(False)
        # endregion

        #region national code
        self.__nationalcode_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__nationalcode_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__nationalcode_frame.propagate(False)
        # endregion

        #region phone
        self.__phone_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__phone_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__phone_frame.propagate(False)
        # endregion

        # endregion


        #region properties

        # region header
        if self.form_action == FormAction.CREATE:
            form_title = 'Author Data Entry'

        elif self.form_action == FormAction.UPDATE:
            form_title = 'Author Edit Form'

        self.__form_title_label = Label(
            master=self.__header_frame,
            anchor=W,
            text=form_title,
            bg='#EEEDED',
            font=('arial', 13, 'bold')
            )
        self.__form_title_label.pack(side=LEFT, padx=10)
        # endregion

        # region Footer
        if self.form_action == FormAction.CREATE:
            self.__save_btn = Button(
                master=self.__footer_frame,
                text='Save',
                padx=10,
                pady=5,
                bg='#1F6650',
                fg='white',
                command=self.__save
                )
            self.__save_btn.pack(side=RIGHT, padx=5, pady=5)

        elif self.form_action == FormAction.UPDATE:
            self.__save_btn = Button(
                master=self.__footer_frame,
                text='Save',
                padx=10,
                pady=5,
                bg='#1F6650',
                fg='white',
                command=self.__edit
                )
            self.__save_btn.pack(side=RIGHT, padx=5, pady=5)

        self.__back_btn = Button(
            master=self.__footer_frame,
            text='Back',
            padx=10,
            pady=5,
            bg='#A23131',
            fg='white',
            command=self.__back
            )
        self.__back_btn.pack(side=LEFT, padx=5, pady=5)
        # endregion

        # region variables
        self.__id_var = StringVar()
        self.__firstname_var = StringVar()
        self.__lastname_var = StringVar()
        self.__nationalcode_var = StringVar()
        self.__phone_var = StringVar()

        if self.form_action == FormAction.UPDATE:
            self.__id_var.set(self.__selected_instance.id)
            self.__firstname_var.set(self.__selected_instance.firstname)
            self.__lastname_var.set(self.__selected_instance.lastname)
            self.__nationalcode_var.set(self.__selected_instance.nationalcode)
            self.__phone_var.set(self.__selected_instance.phone)

        #endregion

        # region firstname
        self.__firstname_label = Label(
            master=self.__firstname_frame,
            width=10,
            anchor=W,
            text='Firstname',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__firstname_label.pack(side=TOP, fill=X)

        self.__firstname_entry = Entry(
            master=self.__firstname_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__firstname_var
            )
        self.__firstname_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region lastname
        self.__lastname_label = Label(
            master=self.__lastname_frame,
            width=10,
            anchor=W,
            text='Lastname',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__lastname_label.pack(side=TOP, fill=X)

        self.__lastname_entry = Entry(
            master=self.__lastname_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__lastname_var
            )
        self.__lastname_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region national code
        self.__nationalcode_label = Label(
            master=self.__nationalcode_frame,
            width=10,
            anchor=W,
            text='National Code',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__nationalcode_label.pack(side=TOP, fill=X)

        self.__nationalcode_entry = Entry(
            master=self.__nationalcode_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__nationalcode_var
            )
        self.__nationalcode_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region phone
        self.__phone_label = Label(
            master=self.__phone_frame,
            width=10,
            anchor=W,
            text='Phone',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__phone_label.pack(side=TOP, fill=X)

        self.__phone_entry = Entry(
            master=self.__phone_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__phone_var
            )
        self.__phone_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        #endregion


    def __save(self):
        try:
            instance = Author(
                firstname=self.__firstname_var.get(),
                lastname=self.__lastname_var.get(),
                nationalcode=self.__nationalcode_var.get(),
                phone=self.__phone_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__author_bl.create(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'firstname':
                        self.__firstname_var.set('')
                    case 'lastname':
                        self.__lastname_var.set('')
                    case 'nationalcode':
                        self.__nationalcode_var.set('')
                    case 'phone':
                        self.__phone_var.set('')
            
            showerror('Error!', message_str)
        else:
            showinfo('Success!', message_str)
            self.__form_result = FormResult.SAVE
            self.destroy()

    def __edit(self):
        try:
            instance = Author(
                firstname=self.__firstname_var.get(),
                lastname=self.__lastname_var.get(),
                nationalcode=self.__nationalcode_var.get(),
                phone=self.__phone_var.get(),
                id=self.__id_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__author_bl.update(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'firstname':
                        self.__firstname_var.set('')
                    case 'lastname':
                        self.__lastname_var.set('')
                    case 'nationalcode':
                        self.__nationalcode_var.set('')
                    case 'phone':
                        self.__phone_var.set('')
            
            showerror('Error!', message_str)
        else:
            showinfo('Success!', message_str)
            self.__form_result = FormResult.EDIT
            self.destroy()

    def __back(self):
        self.__form_result = FormResult.BACK
        self.destroy()

    def __close(self):
        self.__form_result = FormResult.CLOSE
        self.destroy()


    # region form action
    @property
    def form_action(self) -> FormAction:
        return self.__form_action
    # endregion

    # region form result
    @property
    def form_result(self) -> FormResult:
        return self.__form_result
    # endregion


    