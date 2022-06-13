from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from models.modules import *
from models.product import Product

class ProductGUI(ctk.CTkToplevel):
    # PATH___________________________________
    CONF_PATH = './config/config.json'

    # WD CONFIG______________________________
    WIDTH = 600
    HEIGHT = 200

    def __init__(self, parent, mode):
        super().__init__(parent)
        self.conf = Json.read_json(self.CONF_PATH)

        self.parent = parent
        self.mode = mode

        ctk.set_appearance_mode(self.conf.get('set_mode'))
        ctk.set_default_color_theme(self.conf.get('color_th'))
        self.resizable(False, False)
        GUI.center_wd(self, self.WIDTH, self.HEIGHT)
        
        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2, 3), weight=1)

        # VAR DECLARATIONS___________________
        self.vars = [tk.StringVar() for i in range(5)]

        # MODE SETTIGNS______________________
        if self.mode == 0:
            self.title('Admin | Add Product')
            self.placeholders = ["Name", "Category", "Supplier", "Price"]

        elif self.mode == 1:
            self.title('Admin | Edit Product')
            self.placeholders = ["Name2", "Category2", "Supplier2", "Price2"]
            self.id = ctk.CTkEntry(self, text=self.vars[4], placeholder_text='id', text_font=('Roboto', 14), width=250).grid(row=0, column=0, columnspan=2, sticky='news', padx=20, pady=5)

        # GUI DESIGN__________________________
        self.name = ctk.CTkEntry(self, text=self.vars[0], placeholder_text=self.placeholders[0], text_font=('Roboto', 14), width=250).grid(row=1, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.category = ctk.CTkEntry(self, text=self.vars[1], placeholder_text=self.placeholders[1], text_font=('Roboto', 14), width=250).grid(row=1, column=2, columnspan=2, sticky='news', padx=20, pady=5)
        self.supplier = ctk.CTkEntry(self, text=self.vars[2], placeholder_text=self.placeholders[2], text_font=('Roboto', 14), width=250).grid(row=2, column=0, columnspan=2, sticky='news', padx=20, pady=5)
        self.price = ctk.CTkEntry(self, text=self.vars[3], placeholder_text=self.placeholders[3], text_font=('Roboto', 14), width=250).grid(row=2, column=2, columnspan=2, sticky='news', padx=20, pady=5)

        self.btn1 = ctk.CTkButton(self, text='Back', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=70, command=self.destroy).grid(row=3, column=2, sticky='we', padx=20, pady=5)
        self.btn2 = ctk.CTkButton(self, text='Submit', text_color=self.conf.get('white'), text_font=('Roboto', 14), cursor='hand2', width=70, command=self.submit).grid(row=3, column=3, sticky='we', padx=20, pady=5)


    def __entries(self, i):
        datas = [v.get().title() for v in self.vars]
        return ["" if data in self.placeholders else data for data in datas][i]

    def __not_empty(self):
        return False if "" in [self.__entries(i) for i in range(len(self.vars))] else True

    def valid_price(self, price):
        try:
            float(price)
            return True
        except ValueError:
            return False

    def submit(self):
        if self.mode == 0:
            if not self.__not_empty():
                messagebox.showerror(title='ERROR', message='There cannot be empty fields.')
            elif Product.check_product(self.__entries(0)):
                messagebox.showerror(title='ERROR', message='The product already exists.')
            elif not self.valid_price(self.__entries(3)):
                messagebox.showerror(title='ERROR', message='The price is not valid.')
            else:
                prod = Product(
                    self.__entries(0), #name
                    self.__entries(1), #category
                    self.__entries(2), #supplier
                    '{:.2f}'.format(float(self.__entries(3))) #price
                )

                Product.add_product(self.__entries(0), prod)
                self.destroy()