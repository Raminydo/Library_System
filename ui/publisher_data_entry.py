

from tkinter import *
from tkinter.messagebox import showerror, showinfo
from typing import Optional
from bl.publisher_bl import PublisherBL
from common.publisher import Publisher
from common.data_type import FormAction, FormResult, MethodResult, State




class PublisherDataEntryForm(Toplevel):

    def __init__(self, form_action: FormAction, publisher_bl: PublisherBL, instance: Optional[Publisher] = None) -> None:
        super().__init__()
        self.__publisher_bl: PublisherBL() = publisher_bl # type: ignore
        self.__form_action = form_action
        self.__form_result = FormResult.RUNNING
        self.__selected_instance: Publisher | None = instance
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

        #region name
        self.__name_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__name_frame.pack(side=TOP, fill=X, pady=(15, 20))
        self.__name_frame.propagate(False)
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

        #region location
        self.__location_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__location_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__location_frame.propagate(False)
        # endregion

        # endregion


        #region properties

        # region header
        if self.form_action == FormAction.CREATE:
            form_title = 'Publisher Data Entry'

        elif self.form_action == FormAction.UPDATE:
            form_title = 'Publisher Edit Form'

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
        self.__name_var = StringVar()
        self.__phone_var = StringVar()
        self.__location_var = StringVar()

        if self.form_action == FormAction.UPDATE:
            self.__id_var.set(self.__selected_instance.id)
            self.__name_var.set(self.__selected_instance.name)
            self.__phone_var.set(self.__selected_instance.phone)
            self.__location_var.set(self.__selected_instance.location)



        #endregion

        # region name
        self.__name_label = Label(
            master=self.__name_frame,
            width=10,
            anchor=W,
            text='Name',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__name_label.pack(side=TOP, fill=X)

        self.__name_entry = Entry(
            master=self.__name_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__name_var
            )
        self.__name_entry.pack(side=BOTTOM, fill=X, expand=True)
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

        # region location
        self.__location_label = Label(
            master=self.__location_frame,
            width=10,
            anchor=W,
            text='Location',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__location_label.pack(side=TOP, fill=X)

        self.__location_entry = Entry(
            master=self.__location_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__location_var
            )
        self.__location_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        #endregion


    def __save(self):
        try:
            instance = Publisher(
                name=self.__name_var.get(),
                phone=self.__phone_var.get(),
                location=self.__location_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__publisher_bl.create(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'name':
                        self.__name_var.set('')
                    case 'phone':
                        self.__phone_var.set('')
                    case 'location':
                        self.__location_var.set('')
            
            showerror('Error!', message_str)
        else:
            showinfo('Success!', message_str)
            self.__form_result = FormResult.SAVE
            self.destroy()

    def __edit(self):
        try:
            instance = Publisher(
                name=self.__name_var.get(),
                phone=self.__phone_var.get(),
                location=self.__location_var.get(),
                id=self.__id_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__publisher_bl.update(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'name':
                        self.__name_var.set('')
                    case 'phone':
                        self.__phone_var.set('')
                    case 'location':
                        self.__location_var.set('')
            
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


    