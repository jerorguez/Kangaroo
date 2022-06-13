import json
import os
import tkinter as tk
import webbrowser
from os.path import exists
from tkinter import messagebox

import customtkinter as ctk
from inflection import pluralize
from PIL import Image, ImageTk


class Modules:
    @staticmethod
    def open_browser(url):
        webbrowser.open_new_tab(url)

    # Assigns an automatic id
    @staticmethod
    def auto_key(ref):
        datas = Json.json2list(ref)
        return datas[-1].get('id') +1 if len(datas) != 0 else 1

    # Verify that the params match
    @staticmethod
    def are_equals(*params):
        return all(param == params[0] for param in params)

class Json:
    @classmethod
    def path(cls, ref):
        return './databases/{}.txt'.format(pluralize(ref.__name__).lower())

    @classmethod
    def read_json(cls, path):
        with open(path) as f:
            return json.load(f)

    @classmethod
    def json2list(cls, ref):
        cls.create_json(ref)
        with open(cls.path(ref)) as f:
            return [json.loads(data) for data in f.readlines()]

    @classmethod
    def create_json(cls, ref):
        path = cls.path(ref)
        if not exists(path):
            return open(path, 'x')

    @classmethod
    def write_json(cls, ref, obj):
        with open(cls.path(ref), 'a') as f:
            f.write(json.dumps(obj.__dict__) + '\n')

    @classmethod
    def overwrite(cls, ref, datas):
        with open('./databases/auxiliar.txt', 'w') as f:
            for i in range(len(datas)):
                if i == len(datas) -1:
                    f.write(json.dumps(datas[i]))
                else:
                    f.write(json.dumps(datas[i]) + '\n')
        
        os.remove(Json.path(ref))
        os.rename('./databases/auxiliar.txt', Json.path(ref))

class GUI:
    # Center tkinter wd
    @classmethod
    def center_wd(cls, wd, width, height):
        sc_width = wd.winfo_screenwidth()
        sc_height = wd.winfo_screenheight()
        x = (sc_width/2) - (width/2)
        y = (sc_height/2) - (height/2)
        wd.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    @classmethod
    def on_closing(cls, wd, parent):
        wd.destroy()
        parent.destroy()

    @classmethod
    def go_back(cls, wd, parent):
        wd.destroy()
        parent.deiconify()

    @classmethod
    def load_listbox(cls, path, listbox):
        listbox.delete(0, tk.END)
        for data in Json.json2list(path):
            listbox.insert(tk.END, data)