

from tkinter import *
from tkinter.messagebox import askyesno, showerror
from tkinter.ttk import Treeview
from bl.book_bl import BookBL
from common.book import Book
from common.data_type import FormAction, FormResult, MethodResult, State
from ui.book_data_entry import BookDataEntryForm



class BookListForm(Toplevel):

    def __init__(self) -> None:
        super().__init__()

        try:
            self.__book_bl = BookBL()
        except BaseException as err:
            showerror('Error', 'Error')
            self.destroy()
            return

        self.__initialize_component()
        self.form_result = FormResult.RUNNING
        self.__refresh_grid()


    def __refresh_grid(self): 
        for row in self.__book_grid.get_children():
            self.__book_grid.delete(row)

        for book in self.__book_bl.get_all():
            self.__book_grid.insert(
                '',
                'end',
                values=(
                    book.id,
                    book.title,
                    book.author,
                    book.publisher,
                    book.publication_year,
                    book.isbn
                )
            )

    def __initialize_component(self):

        # region window
        win_width = 600
        win_height = 600
        padd_left = (self.winfo_screenwidth() // 2) - (win_width // 2)
        padd_top = (self.winfo_screenheight() // 2) - (win_height // 2)

        self.geometry(f'{win_width}x{win_height}+{padd_left}+{padd_top}')
        self.resizable(width=False, height=False)
        self.configure(background='#EEEDED')
        self.title('Library Management System')
        # endregion


        # region frame
        self.__header_frame = Frame(
            master=self,
            bg='#EEEDED',
            height=40,
            highlightbackground='#3C486B',
            highlightthickness=1,
        )
        self.__header_frame.pack(side=TOP, fill=X)
        self.__header_frame.propagate(False)

        self.__footer_frame = Frame(
            master=self,
            bg='#EEEDED',
            height=55,
            highlightbackground='#3C486B',
            highlightthickness=1,
        )
        self.__footer_frame.pack(side=BOTTOM, fill=X)
        self.__footer_frame.propagate(False)

        self.__body_frame = Frame(master=self, bg='#EEEDED')
        self.__body_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.__body_frame.propagate(False)
        # endregion

        # region header
        self.__form_title_label = Label(
            master=self.__header_frame,
            anchor=W,
            text='Book List',
            bg='#EEEDED',
            font=('arial', 13, 'bold'),
        )
        self.__form_title_label.pack(side=LEFT, padx=10)
        # endregion

        # region Footer
        self.__add_btn = Button(
            master=self.__footer_frame,
            text='Add',
            padx=10,
            pady=10,
            bg='#1679AB',
            fg='black',
            command=self.__add_btn_onclick,
        )
        self.__add_btn.pack(side=RIGHT, padx=(0, 10), pady=10)

        self.__edit_btn = Button(
            master=self.__footer_frame,
            text='Edit',
            padx=10,
            pady=10,
            bg='#FFDE95',
            fg='black',
            command=self.__edit_btn_onclick,
        )
        self.__edit_btn.pack(side=RIGHT, padx=(0, 10), pady=10)

        self.__delete_btn = Button(
            master=self.__footer_frame,
            text='Delete',
            padx=10,
            pady=10,
            bg='#A23131',
            fg='black',
            command=self.__delete_btn_onclick,
        )
        self.__delete_btn.pack(side=RIGHT, padx=(0, 10), pady=10)

        self.__back_btn = Button(
            master=self.__footer_frame,
            text='Back',
            padx=10,
            pady=10,
            bg='black',
            fg='white',
            command=self.__back_btn_onclick,
        )
        self.__back_btn.pack(side=LEFT, padx=10, pady=10)
        # endregion


        # region body

        # region scrollbar
        self.__ver_scrollbar = Scrollbar(
            master=self.__body_frame, orient='vertical')
        self.__ver_scrollbar.pack(side=RIGHT, fill=Y)
        # endregion

        # region book grid
        self.__book_grid = Treeview(
            master=self.__body_frame,
            columns=('id', 'title', 'author', 'publisher', 'publication_year', 'isbn'),
            displaycolumns=('title', 'author', 'publisher', 'publication_year', 'isbn'),
            show='headings',
            selectmode='extended'
        )
        

        column_width = self.__book_grid.winfo_width()

        self.__book_grid.column(column='id', anchor='center', width=column_width)
        self.__book_grid.column(column='title', anchor='center', width=column_width)
        self.__book_grid.column(column='author', anchor='center', width=column_width)
        self.__book_grid.column(column='publisher', anchor='center', width=column_width)
        self.__book_grid.column(column='publication_year', anchor='center', width=column_width)
        self.__book_grid.column(column='isbn', anchor='center', width=column_width)

        self.__book_grid.heading(column='id', anchor='center', text='ID')
        self.__book_grid.heading(column='title', anchor='center', text='Title')
        self.__book_grid.heading(column='author', anchor='center', text='Author')
        self.__book_grid.heading(column='publisher', anchor='center', text='Publisher')
        self.__book_grid.heading(column='publication_year', anchor='center', text='Publication Year')
        self.__book_grid.heading(column='isbn', anchor='center', text='ISBN')

        self.__book_grid.pack(fill=BOTH, expand=True)
        # endregion

        # region config grid and scrollbar
        self.__book_grid.configure(yscrollcommand=self.__ver_scrollbar.set)
        self.__ver_scrollbar['command'] = self.__book_grid.yview
        # endregion

        # endregion


    def __add_btn_onclick(self):
        self.withdraw()

        form = BookDataEntryForm(form_action=FormAction.CREATE, book_bl=self.__book_bl)
        self.wait_window(window=form)

        if form.form_result == FormResult.SAVE:
            self.__refresh_grid()

        self.deiconify()


    def __edit_btn_onclick(self):
        selected_books: list[Book] = self.__get_selected_rows()

        if not selected_books:
            showerror('Error', 'Error message')
            return
        
        if len(selected_books) > 1:
            showerror('Error', 'Error message')
            return
        
        self.withdraw()
        form = BookDataEntryForm(
            form_action=FormAction.UPDATE,
            book_bl=self.__book_bl,
            instance=selected_books[0]
        )
        self.wait_window(window=form)

        if form.form_result == FormResult.EDIT:
            self.__refresh_grid()

        self.deiconify()


    def __delete_btn_onclick(self):
        selected_book: list[Book] = self.__get_selected_rows()
        
        if not selected_book:
            showerror('Error', 'Error message')
            return
        
        for book in selected_book:
            if askyesno('Message', 'Are you sure?'):
                result: MethodResult = self.__book_bl.delete(instance=book)
                
                message_list = []

                for msg in result.message:
                    message_list.append(f'{msg.field}!, {msg.value}')

                message_str = '\n'.join(message_list)

                if result.state == State.ERROR:
                    showerror('Error!', message_str)
                else:
                    self.__refresh_grid()

                
    def __back_btn_onclick(self):
        self.form_result = FormResult.BACK
        self.destroy()

    
    def __get_selected_rows(self) -> list[Book]:
        selected_book: list[Book] = []
        selected_rows = self.__book_grid.selection()

        for row_id in selected_rows:
            row_data = self.__book_grid.item(item=row_id, option='values')
            selected_book.append(
                Book(
                    title=row_data[1],
                    author=row_data[2],
                    publisher=row_data[3],
                    publication_year=row_data[4],
                    isbn=row_data[5],
                    id=row_data[0]
                )
            )

        return selected_book




