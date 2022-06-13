from models.modules import *
from models.user import User
from views.adminGui import AdminGui
from views.registerGui import RegisterGUI


class App(ctk.CTk):
    
    # PATH_________________________________
    CONF_PATH = './config/config.json'

    # WD CONFIG____________________________
    WIDTH = 400
    HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.conf = Json.read_json(self.CONF_PATH)

        ctk.set_appearance_mode(self.conf.get('set_mode'))
        ctk.set_default_color_theme(self.conf.get('color_th'))
        self.title(self.conf.get('title_main'))
        self.resizable(False, False)
        GUI.center_wd(self, self.WIDTH, self.HEIGHT)

        # VAR DECLARATION____________________
        self.vars = [tk.StringVar() for i in range(2)]
        self.placeholders = ["Username", "Password"]

        # IMAGES_____________________________
        self.logo_img = tk.PhotoImage(file=self.conf.get('logo'))

        # GUI DESIGN_________________________
        self.lab_logo = ctk.CTkLabel(self, image=self.logo_img).pack()

        self.ent_username = ctk.CTkEntry(self, text=self.vars[0], placeholder_text=self.placeholders[0], text_font=('Roboto', 14), width=250).pack(pady=5)
        self.ent_username = ctk.CTkEntry(self, text=self.vars[1], placeholder_text=self.placeholders[1], show='*', text_font=('Roboto', 14), width=250).pack(pady=5)

        self.btn1 = ctk.CTkButton(self, text='Sign In', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', command=self.signin).pack(pady=20)

        self.lab_signup = tk.Label(self, text="Don't have an account? Register now!", bg=self.conf.get('bg'), font=('Roboto, 14'), fg=self.conf.get('blue'), cursor='hand2')
        self.lab_signup.pack(pady=20)
        self.lab_signup.bind('<Button-1>', lambda e:RegisterGUI(self))

        self.lab_footer = tk.Label(self, text="@Xio28 | @Jerorguez\nSee the project on Github", bg=self.conf.get('bg'), fg=self.conf.get('blue'), font=('Roboto', 12), cursor='hand2')
        self.lab_footer.pack()
        self.lab_footer.bind('<Button-1>', lambda e: Modules.open_browser(self.conf.get('url_repo')))

        self.admin = tk.Label(self, text="Admin", bg=self.conf.get('bg'), fg=self.conf.get('blue'), font=('Roboto', 12), cursor='hand2')
        self.admin.pack()
        self.admin.bind('<Button-1>', lambda e: AdminGui(self))

    def __entries(self, i):
        datas = [v.get() for v in self.vars]
        return ["" if data in self.placeholders else data for data in datas][i]

    def signin(self):
        if self.__entries(0) == "":
            messagebox.showerror(title='ERROR', message="The username field cannot be empty.")
        elif self.__entries(0).lower() == 'admin':
            if self.__entries(1) != "1234":
                messagebox.showinfo(title='INFO', message='Admin password: 1234')
            else:
                AdminGui(self)
        elif not User.check_user(self.__entries(0)):
            messagebox.showerror(title='ERROR', message=f'The user "{self.__entries(0)}" does not exist. Please register.')
        else:
            if User.check_credentials(self.__entries(0), self.__entries(1)):
                messagebox.showinfo(message='Ok')
            else:
                messagebox.showinfo(message='The password is incorrect.')

if __name__ == '__main__':
    app = App()
    app.mainloop()