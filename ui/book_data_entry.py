

from tkinter import *
from tkinter.messagebox import showerror, showinfo
from typing import Optional
from bl.book_bl import BookBL
from common.book import Book
from common.data_type import FormAction, FormResult, MethodResult, State



class BookDataEntryForm(Toplevel):

    def __init__(self, form_action: FormAction, book_bl: BookBL, instance: Optional[Book] = None) -> None:
        super().__init__()
        self.__book_bl: BookBL() = book_bl # type: ignore
        self.__form_action = form_action
        self.__form_result = FormResult.RUNNING
        self.__selected_instance: Book | None = instance
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

        #region title
        self.__title_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__title_frame.pack(side=TOP, fill=X, pady=(15, 20))
        self.__title_frame.propagate(False)
        # endregion

        #region author
        self.__author_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__author_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__author_frame.propagate(False)
        # endregion

        #region publisher
        self.__publisher_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__publisher_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__publisher_frame.propagate(False)
        # endregion

        #region publication year
        self.__publicationyear_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__publicationyear_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__publicationyear_frame.propagate(False)
        # endregion
        
        #region isbn
        self.__isbn_frame = Frame(
            master=self.__body_frame,
            bg='#EEEDED',
            height=50
            )
        self.__isbn_frame.pack(side=TOP, fill=X, pady=(0, 20))
        self.__isbn_frame.propagate(False)
        # endregion

        # endregion


        #region properties

        # region header
        if self.form_action == FormAction.CREATE:
            form_title = 'Book Data Entry'

        elif self.form_action == FormAction.UPDATE:
            form_title = 'Book Edit Form'

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
        self.__title_var = StringVar()
        self.__author_var = StringVar()
        self.__publisher_var = StringVar()
        self.__publication_year_var = StringVar()
        self.__isbn_var = StringVar()

        if self.form_action == FormAction.UPDATE:
            self.__id_var.set(self.__selected_instance.id)
            self.__title_var.set(self.__selected_instance.title)
            self.__author_var.set(self.__selected_instance.author)
            self.__publisher_var.set(self.__selected_instance.publisher)
            self.__publication_year_var.set(self.__selected_instance.publication_year)
            self.__isbn_var.set(self.__selected_instance.isbn)



        #endregion

        # region title
        self.__title_label = Label(
            master=self.__title_frame,
            width=10,
            anchor=W,
            text='Title',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__title_label.pack(side=TOP, fill=X)

        self.__title_entry = Entry(
            master=self.__title_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__title_var
            )
        self.__title_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region author
        self.__author_label = Label(
            master=self.__author_frame,
            width=10,
            anchor=W,
            text='Author',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__author_label.pack(side=TOP, fill=X)

        self.__author_entry = Entry(
            master=self.__author_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__author_var
            )
        self.__author_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region publisher
        self.__publisher_label = Label(
            master=self.__publisher_frame,
            width=10,
            anchor=W,
            text='Publisher',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__publisher_label.pack(side=TOP, fill=X)

        self.__publisher_entry = Entry(
            master=self.__publisher_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__publisher_var
            )
        self.__publisher_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region publication year
        self.__publicationyear_label = Label(
            master=self.__publicationyear_frame,
            width=10,
            anchor=W,
            text='Publication year',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__publicationyear_label.pack(side=TOP, fill=X)

        self.__publicationyear_entry = Entry(
            master=self.__publicationyear_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__publication_year_var
            )
        self.__publicationyear_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        # region isbn
        self.__isbn_label = Label(
            master=self.__isbn_frame,
            width=10,
            anchor=W,
            text='ISBN',
            bg='#EEEDED',
            font=('arial', 11, 'bold')
            )
        self.__isbn_label.pack(side=TOP, fill=X)

        self.__isbn_entry = Entry(
            master=self.__isbn_frame,
            bd=1,
            bg='#F5F5F5',
            font=('arial', 11, 'normal'),
            textvariable=self.__isbn_var
            )
        self.__isbn_entry.pack(side=BOTTOM, fill=X, expand=True)
        # endregion

        #endregion


    def __save(self):
        try:
            instance = Book(
                title=self.__title_var.get(),
                author=self.__author_var.get(),
                publisher=self.__publisher_var.get(),
                publication_year=self.__publication_year_var.get(),
                isbn=self.__isbn_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__book_bl.create(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'title':
                        self.__title_var.set('')
                    case 'author':
                        self.__author_var.set('')
                    case 'publisher':
                        self.__publisher_var.set('')
                    case 'publication_year':
                        self.__publication_year_var.set('')
                    case 'isbn':
                        self.__isbn_var.set('')
            
            showerror('Error!', message_str)
        else:
            showinfo('Success!', message_str)
            self.__form_result = FormResult.SAVE
            self.destroy()


    def __edit(self):
        try:
            instance = Book(
                title=self.__title_var.get(),
                author=self.__author_var.get(),
                publisher=self.__publisher_var.get(),
                publication_year=self.__publication_year_var.get(),
                isbn=self.__isbn_var.get(),
                id=self.__id_var.get()
            )
        except BaseException as err:
            showerror('error', 'error message')
            return
        
        result: MethodResult = self.__book_bl.update(instance=instance)
        message_list = []

        for message in result.message:
            message_list.append(f'{message.field}! {message.value}')

        message_str = "\n".join(message_list)

        if result.state == State.ERROR:

            for err in result.message:
                match err.field:
                    case 'title':
                        self.__title_var.set('')
                    case 'author':
                        self.__author_var.set('')
                    case 'publisher':
                        self.__publisher_var.set('')
                    case 'publication_year':
                        self.__publication_year_var.set('')
                    case 'isbn':
                        self.__isbn_var.set('')
            
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


    