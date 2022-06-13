from models.modules import *
from models.user import User

class RegisterGUI(ctk.CTkToplevel):
    
    # PATH_________________________________
    CONF_PATH = './config/config.json'

    # WD CONFIG____________________________
    WIDTH = 600
    HEIGHT = 280

    def __init__(self, parent):
        super().__init__(parent)
        self.conf = Json.read_json(self.CONF_PATH)

        self.parent = parent
        self.parent.withdraw()

        ctk.set_appearance_mode(self.conf.get('set_mode'))
        ctk.set_default_color_theme(self.conf.get('color_th'))
        self.title(self.conf.get('title_admin'))
        self.resizable(False, False)
        GUI.center_wd(self, self.WIDTH, self.HEIGHT)

        self.protocol('WM_DELETE_WINDOW', lambda:GUI.on_closing(self, self.parent))

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # VAR DECLARATIONS___________________
        self.vars = [tk.StringVar() for i in range(9)]
        self.placeholders = ["Username", "DNI", "Name", "Last Name", "Email", "Contact", "Address", "Password", "Confirm Password"]

        # GUI DESIGN_________________________

        self.title = ctk.CTkLabel(self, text='Kangaroo | Sign Up Form', bg_color=self.conf.get('blue'), text_color=self.conf.get('white'), text_font=('Roboto', 16)).grid(row=0, column=0, columnspan=4, sticky='news')
        self.separator = ctk.CTkLabel(self, text='').grid(row=1, column=0, pady=3)

        self.username = ctk.CTkEntry(self, text=self.vars[0], placeholder_text=self.placeholders[0], text_font=('Roboto', 14), width=250).grid(row=2, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.dni = ctk.CTkEntry(self, text=self.vars[1], placeholder_text=self.placeholders[1], text_font=('Roboto', 14), width=250).grid(row=2, column=2, columnspan=2, sticky='news', padx=20, pady=5)
        self.name = ctk.CTkEntry(self, text=self.vars[2], placeholder_text=self.placeholders[2], text_font=('Roboto', 14), width=250).grid(row=3, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.l_name = ctk.CTkEntry(self, text=self.vars[3], placeholder_text=self.placeholders[3], text_font=('Roboto', 14), width=250).grid(row=3, column=2, columnspan=2, sticky='news', padx=20, pady=5)
        self.email = ctk.CTkEntry(self, text=self.vars[4], placeholder_text=self.placeholders[4], text_font=('Roboto', 14), width=250).grid(row=4, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.contact = ctk.CTkEntry(self, text=self.vars[5], placeholder_text=self.placeholders[5], text_font=('Roboto', 14), width=250).grid(row=4, column=2, columnspan=2, sticky='news', padx=20, pady=5)
        self.address = ctk.CTkEntry(self, text=self.vars[6], placeholder_text=self.placeholders[6], text_font=('Roboto', 14), width=250).grid(row=5, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.pass1 = ctk.CTkEntry(self, text=self.vars[7], placeholder_text=self.placeholders[7], show='*', text_font=('Roboto', 14), width=250).grid(row=5, column=2, columnspan=2, sticky='news', padx=20, pady=5)
        self.pass2 = ctk.CTkEntry(self, text=self.vars[8], placeholder_text=self.placeholders[8], show='*', text_font=('Roboto', 14), width=250).grid(row=6, column=0, columnspan=2, sticky='news', padx=20, pady=5)

        self.btn1 = ctk.CTkButton(self, text='Back', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=70, command=lambda:GUI.go_back(self, self.parent)).grid(row=6, column=2, sticky='we', padx=20, pady=5)
        self.btn2 = ctk.CTkButton(self, text='Submit', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=70, command=self.submit).grid(row=6, column=3, sticky='we', padx=20, pady=5)

    
    def __entries(self, i):
        datas = [v.get() for v in self.vars]
        return ["" if data in self.placeholders else data for data in datas][i]

    def __not_empty(self):
        return False if "" in [self.__entries(i) for i in range(len(self.vars))] else True

    def submit(self):
        if not self.__not_empty():
            messagebox.showerror(title='ERROR', message='There cannot be empty fields')
        elif User.check_user(self.__entries(0)):
            messagebox.showerror(title='ERROR', message='The username already exists.')
        elif not Modules.are_equals(self.__entries(7), self.__entries(8)):
            messagebox.showerror(title='ERROR', message='Passwords do not match')
        else:
            user = User(
                self.__entries(0), #username
                self.__entries(7), #password
                self.__entries(4), #email
                self.__entries(2), #name
                self.__entries(3), #last_name
                self.__entries(1), #dni
                self.__entries(6), #address
                self.__entries(5), #contact
            )

            User.add_user(self.__entries(0), user)
            GUI.go_back(self, self.parent)