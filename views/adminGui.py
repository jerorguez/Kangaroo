from models.modules import *
from models.product import Product
from models.user import User
from views.productGui import Product, ProductGUI


class AdminGui(ctk.CTkToplevel):
    # PATH___________________________________
    CONF_PATH = './config/config.json'

    # WD CONFIG______________________________
    WIDTH = 900
    HEIGHT = 400

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

        # ICONS_________________________________
        self.icon_add = ImageTk.PhotoImage(Image.open(self.conf.get('icon_add')).resize((self.conf.get('icon_size'), self.conf.get('icon_size')), Image.ANTIALIAS))
        self.icon_edit = ImageTk.PhotoImage(Image.open(self.conf.get('icon_edit')).resize((self.conf.get('icon_size'), self.conf.get('icon_size')), Image.ANTIALIAS))
        self.icon_logout = ImageTk.PhotoImage(Image.open(self.conf.get('icon_logout')).resize((self.conf.get('icon_size'), self.conf.get('icon_size')), Image.ANTIALIAS))
        self.icon_info = ImageTk.PhotoImage(Image.open(self.conf.get('icon_info')).resize((self.conf.get('icon_size'), self.conf.get('icon_size')), Image.ANTIALIAS))

        # MAIN LAYOUT (2x1)_____________________
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.left_fr = ctk.CTkFrame(self, corner_radius=0)
        self.left_fr.grid(row=0, column=0, sticky='news')

        self.right_fr = ctk.CTkFrame(self)
        self.right_fr.grid(row=0, column=1, sticky='news', padx=20, pady=20)

        # LEFT FRAME LAYOUT (1x8)________________
        self.left_fr.rowconfigure((0, 8), minsize=40)
        self.left_fr.rowconfigure(7, weight=1)

        self.user_info = ctk.CTkLabel(self.left_fr, text='Admin', text_font=('Roboto', 20)).grid(row=0, column=0, padx=10, pady=20)

        self.btn1 = ctk.CTkButton(self.left_fr, text='Add Product', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=180, image=self.icon_add, compound='right', command=lambda:ProductGUI(self, 0)).grid(row=1, column=0, padx=10, pady=5)
        self.btn2 = ctk.CTkButton(self.left_fr, text='Edit Product', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=180, image=self.icon_edit, compound='right', command=lambda:ProductGUI(self, 1)).grid(row=4, column=0, padx=10, pady=5)
        self.btn3 = ctk.CTkButton(self.left_fr, text='Logout', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=120, image=self.icon_logout, compound='right', command=lambda:GUI.go_back(self, self.parent)).grid(row=8, column=0, padx=10, pady=20)

        # RIGHT FRAME_______________________________
        self.right_fr = ctk.CTkFrame(self)
        self.right_fr.grid(row=0, column=1, sticky='news', padx=20, pady=20)

        self.right_fr.columnconfigure((0, 2), weight=1)
        self.right_fr.rowconfigure(1, weight=1)

        self.yscroll_users = tk.Scrollbar(self.right_fr, orient=tk.VERTICAL)
        self.xscroll_users = tk.Scrollbar(self.right_fr, orient=tk.HORIZONTAL)
        self.yscroll_products = tk.Scrollbar(self.right_fr, orient=tk.VERTICAL)
        self.xscroll_products = tk.Scrollbar(self.right_fr, orient=tk.HORIZONTAL)

        self.lab_users = ctk.CTkLabel(self.right_fr, text='Users', text_font=('Roboto', 20)).grid(row=0, column=0, sticky='news', pady=10)
        self.users = tk.Listbox(self.right_fr, bg=self.conf.get('white'), fg=self.conf.get('black'), font=('Roboto', 14), yscrollcommand=self.yscroll_users.set, xscrollcommand=self.xscroll_users.set)
        self.users.grid(row=1, column=0, sticky='news', padx=10, pady=10)

        self.yscroll_users.config(command=self.users.yview)
        self.yscroll_users.grid(row=1, column=1, sticky='ns')
        self.xscroll_users.config(command=self.users.xview)
        self.xscroll_users.grid(row=2, column=0, sticky='ew')

        self.lab_users = ctk.CTkLabel(self.right_fr, text='Products', text_font=('Roboto', 20)).grid(row=0, column=2, sticky='news', pady=10)
        self.products = tk.Listbox(self.right_fr, bg=self.conf.get('white'), fg=self.conf.get('black'), font=('Roboto', 14), yscrollcommand=self.yscroll_products.set, xscrollcommand=self.xscroll_products.set)
        self.products.grid(row=1, column=2, sticky='news', padx=10, pady=10)

        self.yscroll_products.config(command=self.products.yview)
        self.yscroll_products.grid(row=1, column=3, sticky='ns')
        self.xscroll_products.config(command=self.products.xview)
        self.xscroll_products.grid(row=2, column=2, sticky='ew')

        GUI.load_listbox(User, self.users)
        GUI.load_listbox(Product, self.products)