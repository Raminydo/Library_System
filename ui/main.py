

from tkinter import *
from ui.author_list import AuthorListForm
from ui.book_list import BookListForm
from ui.publisher_list import PublisherListForm
from common.data_type import FormResult


class MainForm(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.__initialize_component()
        self.__form_result = FormResult.RUNNING
        self.protocol(name='WM_DELETE_WINDOW', func=self.__close)

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
        self.__body_frame = Frame(master=self, bg='#EEEDED')
        self.__body_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.__body_frame.propagate(False)
        # endregion

        # region menu
        menubar = Menu(self)
        form_menu = Menu(menubar, tearoff=0)
        form_menu.add_command(label="Book", command=self.__book_menu_onclick)
        form_menu.add_command(label='Author', command=self.__author_menu_onclick)
        form_menu.add_command(label='Publisher', command=self.__publisher_menu_onclick)
        form_menu.add_separator()
        form_menu.add_command(label="Exit", command=self.__close)
        menubar.add_cascade(label="Library", menu=form_menu)

        self.config(menu=menubar)
        # endregion

    def __close(self):
        self.__form_result = FormResult.CLOSE
        self.destroy()

    def __book_menu_onclick(self):
        self.withdraw()

        form = BookListForm()
        self.wait_window(window=form)

        self.deiconify()

    def __author_menu_onclick(self):
        self.withdraw()

        form = AuthorListForm()
        self.wait_window(window=form)

        self.deiconify()

    def __publisher_menu_onclick(self):
        self.withdraw()

        form = PublisherListForm()
        self.wait_window(window=form)

        self.deiconify()


