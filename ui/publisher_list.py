

from tkinter import *
from tkinter.messagebox import askyesno, showerror
from tkinter.ttk import Treeview
from bl.publisher_bl import PublisherBL
from common.publisher import Publisher
from common.data_type import FormAction, FormResult, MethodResult, State
from ui.publisher_data_entry import PublisherDataEntryForm




class PublisherListForm(Toplevel):

    def __init__(self) -> None:
        super().__init__()

        try:
            self.__publisher_bl = PublisherBL()
        except:
            showerror('Error', 'Error')
            self.destroy()
            return

        self.__initialize_component()
        self.form_result = FormResult.RUNNING
        self.__refresh_grid()


    def __refresh_grid(self): 
        for row in self.__publisher_grid.get_children():
            self.__publisher_grid.delete(row)

        for publisher in self.__publisher_bl.get_all():
            self.__publisher_grid.insert(
                '',
                'end',
                values=(
                    publisher.id,
                    publisher.name,
                    publisher.phone,
                    publisher.location
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
            text='Publisher List',
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

        # region publisher grid
        self.__publisher_grid = Treeview(
            master=self.__body_frame,
            columns=('id', 'name', 'phone', 'location'),
            displaycolumns=('name', 'phone', 'location'),
            show='headings',
            selectmode='extended'
        )
        

        column_width = self.__publisher_grid.winfo_width()

        self.__publisher_grid.column(column='id', anchor='center', width=column_width)
        self.__publisher_grid.column(column='name', anchor='center', width=column_width)
        self.__publisher_grid.column(column='phone', anchor='center', width=column_width)
        self.__publisher_grid.column(column='location', anchor='center', width=column_width)

        self.__publisher_grid.heading(column='id', anchor='center', text='ID')
        self.__publisher_grid.heading(column='name', anchor='center', text='Name')
        self.__publisher_grid.heading(column='phone', anchor='center', text='Phone')
        self.__publisher_grid.heading(column='location', anchor='center', text='Location')


        self.__publisher_grid.pack(fill=BOTH, expand=True)
        # endregion

        # region config grid and scrollbar
        self.__publisher_grid.configure(yscrollcommand=self.__ver_scrollbar.set)
        self.__ver_scrollbar['command'] = self.__publisher_grid.yview
        # endregion

        # endregion



    def __get_selected_rows(self) -> list[Publisher]:
        selected_publisher: list[Publisher] = []
        selected_rows = self.__publisher_grid.selection()

        for row_id in selected_rows:
            row_data = self.__publisher_grid.item(row_id, 'values')
            selected_publisher.append(
                Publisher(
                    name=row_data[1],
                    phone=row_data[2],
                    location=row_data[3],
                    id=row_data[0]
                )
            )

        return selected_publisher



    def __add_btn_onclick(self):
        self.withdraw()

        form = PublisherDataEntryForm(form_action=FormAction.CREATE, publisher_bl=self.__publisher_bl)
        self.wait_window(window=form)

        if form.form_result == FormResult.SAVE:
            self.__refresh_grid()

        self.deiconify()


    def __edit_btn_onclick(self):
        selected_publisher: list[Publisher] = self.__get_selected_rows()

        if not selected_publisher:
            showerror('Error', 'Error message')
            return
        
        if len(selected_publisher) > 1:
            showerror('Error', 'Error message')
            return
        
        self.withdraw()
        form = PublisherDataEntryForm(
            form_action=FormAction.UPDATE,
            publisher_bl=self.__publisher_bl,
            instance=selected_publisher[0]
        )
        self.wait_window(window=form)

        if form.form_result == FormResult.EDIT:
            self.__refresh_grid()

        self.deiconify()


    def __delete_btn_onclick(self):
        selected_publisher: list[Publisher] = self.__get_selected_rows()
        
        if not selected_publisher:
            showerror('Error', 'Error message')
            return
        
        for publisher in selected_publisher:
            if askyesno('Message', 'Are you sure?'):
                result: MethodResult = self.__publisher_bl.delete(instance=publisher)
                
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

    
    