

from tkinter import *
from tkinter.messagebox import askyesno, showerror
from tkinter.ttk import Treeview
from bl.author_bl import AuthorBL
from common.author import Author
from common.data_type import FormAction, FormResult, MethodResult, State
from ui.author_data_entry import AuthorDataEntryForm



class AuthorListForm(Toplevel):

    def __init__(self) -> None:
        super().__init__()

        try:
            self.__author_bl = AuthorBL()
        except BaseException as err:
            showerror('Error', 'Error')
            self.destroy()
            return

        self.__initialize_component()
        self.form_result = FormResult.RUNNING
        self.__refresh_grid()


    def __refresh_grid(self): 
        for row in self.__author_grid.get_children():
            self.__author_grid.delete(row)

        for author in self.__author_bl.get_all():
            self.__author_grid.insert(
                '',
                'end',
                values=(
                    author.id,
                    author.firstname,
                    author.lastname,
                    author.nationalcode,
                    author.phone
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
            text='Author List',
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

        # region author grid
        self.__author_grid = Treeview(
            master=self.__body_frame,
            columns=('id', 'firstname', 'lastname', 'nationalcode', 'phone'),
            displaycolumns=('firstname', 'lastname', 'nationalcode', 'phone'),
            show='headings',
            selectmode='extended'
        )
        

        column_width = self.__author_grid.winfo_width()

        self.__author_grid.column(column='id', anchor='center', width=column_width)
        self.__author_grid.column(column='firstname', anchor='center', width=column_width)
        self.__author_grid.column(column='lastname', anchor='center', width=column_width)
        self.__author_grid.column(column='nationalcode', anchor='center', width=column_width)
        self.__author_grid.column(column='phone', anchor='center', width=column_width)

        self.__author_grid.heading(column='id', anchor='center', text='ID')
        self.__author_grid.heading(column='firstname', anchor='center', text='Firstname')
        self.__author_grid.heading(column='lastname', anchor='center', text='Lastname')
        self.__author_grid.heading(column='nationalcode', anchor='center', text='National Code')
        self.__author_grid.heading(column='phone', anchor='center', text='Phone')

        self.__author_grid.pack(fill=BOTH, expand=True)
        # endregion

        # region config grid and scrollbar
        self.__author_grid.configure(yscrollcommand=self.__ver_scrollbar.set)
        self.__ver_scrollbar['command'] = self.__author_grid.yview
        # endregion

        # endregion



    def __get_selected_rows(self) -> list[Author]:
        selected_author: list[Author] = []
        selected_rows = self.__author_grid.selection()

        for row_id in selected_rows:
            row_data = self.__author_grid.item(row_id, 'values')
            selected_author.append(
                Author(
                    firstname=row_data[1],
                    lastname=row_data[2],
                    nationalcode=row_data[3],
                    phone=row_data[4],
                    id=row_data[0]
                )
            )

        return selected_author



    def __add_btn_onclick(self):
        self.withdraw()

        form = AuthorDataEntryForm(form_action=FormAction.CREATE, author_bl=self.__author_bl)
        self.wait_window(window=form)

        if form.form_result == FormResult.SAVE:
            self.__refresh_grid()

        self.deiconify()


    def __edit_btn_onclick(self):
        selected_authors: list[Author] = self.__get_selected_rows()

        if not selected_authors:
            showerror('Error', 'Error message')
            return
        
        if len(selected_authors) > 1:
            showerror('Error', 'Error message')
            return
        
        self.withdraw()
        form = AuthorDataEntryForm(
            form_action=FormAction.UPDATE,
            author_bl=self.__author_bl,
            instance=selected_authors[0]
        )
        self.wait_window(window=form)

        if form.form_result == FormResult.EDIT:
            self.__refresh_grid()

        self.deiconify()


    def __delete_btn_onclick(self):
        selected_authors: list[Author] = self.__get_selected_rows()
        
        if not selected_authors:
            showerror('Error', 'Error message')
            return
        
        for author in selected_authors:
            if askyesno('Message', 'Are you sure?'):
                result: MethodResult = self.__author_bl.delete(instance=author)
                
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

