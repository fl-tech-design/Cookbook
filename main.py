#!/usr/bin/python3
import tkinter as tk
import pathlib
import ast


def cr_frame(win, bg, w, h, x, y):
    tk.Frame(win, bg=bg, width=w, height=h).place(x=x, y=y)


def colors(keyword):
    f = open(str(pathlib.Path().absolute()) + r_conf_path('colors'), 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    value_from_keyword = change_list_to_dict[keyword]
    return value_from_keyword


def fonts(keyword):
    f = open(str(pathlib.Path().absolute()) + r_conf_path('fonts'), 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    value_from_keyword = change_list_to_dict[keyword]
    return value_from_keyword


def german(keyword):
    f = open(str(pathlib.Path().absolute()) + '/Cookbook/config/de.txt', 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    value_from_keyword = change_list_to_dict[keyword]
    return value_from_keyword


def r_list_menu():
    comm_list_file = open(str(pathlib.Path().absolute()) + r_conf_path('menulist'), 'r')
    comm_list = comm_list_file.read().split()
    comm_list_file.close()
    return comm_list


def a_list_menu(name):
    comm_list = r_list_menu()
    if name not in comm_list:
        comm_list_file = open(str(pathlib.Path().absolute()) + r_conf_path('menulist'), 'a')
        comm_list_file.write('\n' + name)
        comm_list_file.close()


def r_conf_path(keyword):
    f = open(str(pathlib.Path().absolute()) + '/Cookbook/config/paths.txt', 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    value_from_keyword = change_list_to_dict[keyword]
    return value_from_keyword


def w_new_recipe(filename, keyword, data):
    recipe_path = str(pathlib.Path().absolute()) + r_conf_path('recipe') + filename + '.txt'
    list_recipes = r_list_menu()
    if filename not in list_recipes:
        f = open(recipe_path, 'w')
        f.write("{'Name': '%s'}" % filename)
        f.close()
        a_list_menu(filename)
    f = open(recipe_path, 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    change_list_to_dict[keyword] = data
    f = open(recipe_path, 'w')
    f.write(str(change_list_to_dict))
    f.close()


def r_di_recipe(filename):
    recipe_path = str(pathlib.Path().absolute()) + r_conf_path('recipe') + filename + '.txt'
    f = open(recipe_path, 'r')
    read_dict_as_string = f.read()
    f.close()
    change_list_to_dict = ast.literal_eval(read_dict_as_string)
    if '' in change_list_to_dict:
        del change_list_to_dict['']
    return change_list_to_dict


class CookBook:
    def __init__(self):
        self.path_app = str(pathlib.Path().absolute())
        self.path_pics = self.path_app + r_conf_path('recipe')
        self.recipe_path = self.path_app + r_conf_path('recipe')
        self.text_preparation = self.act_rec_path = self.newmenu = self.val_lbox = self.s_about = None
        self.en_name = self.en_ingr = self.en_quant = self.tf_preparation = self.fr_name = None
        self.di_recipe = self.li_k_recipe = self.fr_ingr = self.menubar = self.filemenu = self.helpmenu = None
        self.bg_app = self.bg_frame = self.fg_app = self.bg_act = self.fg_act = ''

        self.prev_start_y = 250

        self.fo_titel = fonts('Calibri23')
        self.fo_big = fonts('Calibri14')
        self.fo_midd = fonts('Calibri10')
        self.fo_small = fonts('Calibri8')

        self.ingr_dict = {}
        self.list_dict = []

        self.set_colors('anthrazit', 'black', 'orange')

        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title(german('win_titel'))
        self.root.config(bg=self.bg_app)

        self.act_pict_path = self.prev_var = tk.StringVar()
        self.list_menu = r_list_menu()
        self.li_menu_var = tk.StringVar()
        # noinspection PyTypeChecker
        self.li_menu_var.set(self.list_menu)
        self.cr_lab(self.root, german('main_titel'), self.fo_titel, 10, 10)
        self.cr_lab(self.root, german('instruction_main'), self.fo_midd, 10, 60)
        self.cr_lab(self.root, german('select_menu'), self.fo_midd, 430, 160)

        self.cr_but(self.root, german('new_menu_save'), self.fo_small, self.new_recipe_site, 10, 120, 20)
        # create pics
        self.fr_pic = tk.Frame(self.root, bg=self.bg_frame, width=410, height=412)
        self.fr_pic.place(x=10, y=180)
        self.pic_menu_path = tk.PhotoImage(file=self.act_pict_path.get(), width=400, height=400)
        self.pic_spoon_path = tk.PhotoImage(file=self.path_app + r_conf_path('spoon'), width=200, height=100)
        self.cr_pic(self.fr_pic, self.pic_menu_path, 4, 5)
        self.cr_pic(self.root, self.pic_spoon_path, 580, -20)
        # create listbox for choosing the recipe
        self.lbox_rec = tk.Listbox(self.root, listvariable=self.li_menu_var, width=41, height=5, bg=self.bg_frame,
                                   fg=self.fg_app, borderwidth=2, selectmode='browse')
        self.lbox_rec.place(x=430, y=180)
        self.lbox_rec.bind('<<ListboxSelect>>', self.cur_select)
        # Create Lines
        cr_frame(self.root, self.fg_app, 3, 600, 425, 60)
        cr_frame(self.root, self.fg_app, 2000, 3, 0, 60)
        # starting the menubar and the application
        self.menu_bar(self.root, self.fo_small, self.bg_app, self.fg_app, self.bg_act, self.fg_act)
        self.root.mainloop()

    def menu_bar(self, win, fo, bg, fg, bga, fga):
        self.menubar = tk.Menu(win, font=fo, bg=bg, fg=fg, activebackground=bga, activeforeground=fga, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.filemenu.add_command(label=german('new_rec'), command=self.new_recipe_site)
        self.filemenu.add_command(label=german('quit'), command=win.quit)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.helpmenu.add_command(label=german('help'))
        self.helpmenu.add_command(label=german('about'), command=self.site_about)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label=german('help'), menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def new_recipe_site(self):
        self.newmenu = tk.Toplevel(bg=self.bg_app)
        self.newmenu.title('Ein neues Menü speichern')
        self.newmenu.config(width=800, height=600)
        self.cr_lab(self.newmenu, german('new_menu_save'), self.fo_titel, 10, 10)

        # Frame for new ingredients
        self.fr_ingr = tk.Frame(self.newmenu, bg=self.bg_frame, width=321, height=128)
        self.fr_ingr.place(x=442, y=20)
        cr_frame(self.fr_ingr, self.bg_app, 315, 120, 3, 4)
        self.cr_lab(self.fr_ingr, german('instr_ingr'), self.fo_big, 6, 3)
        self.cr_lab(self.fr_ingr, german('label_ingr'), self.fo_midd, 6, 35)
        self.en_ingr = tk.Entry(self.fr_ingr, width=30, bg=self.bg_app, fg=self.fg_app)
        self.en_ingr.place(x=69, y=33)
        self.cr_lab(self.fr_ingr, german('label_quan'), self.fo_midd, 6, 62)
        self.en_quant = tk.Entry(self.fr_ingr, width=30, bg=self.bg_app, fg=self.fg_app)
        self.en_quant.place(x=69, y=60)
        self.cr_but(self.fr_ingr, german('add'), self.fo_small, self.add_ingr, 7, 92, 40)

        # Frame for name entry's etc
        self.fr_name = tk.Frame(self.newmenu, bg=self.bg_frame, width=321, height=128)
        self.fr_name.place(x=10, y=60)
        cr_frame(self.fr_name, self.bg_app, 315, 120, 3, 4)
        self.cr_lab(self.fr_name, german('la_name'), self.fo_midd, 10, 50)
        self.en_name = tk.Entry(self.fr_name, width=30, bg=self.bg_app, fg=self.fg_app)
        self.en_name.place(x=73, y=50)
        self.cr_lab(self.newmenu, german('titel_prep'), self.fo_big, 10, 565)
        self.cr_lab(self.fr_ingr, german('label_ingr'), self.fo_big, 10, 258)
        self.cr_lab(self.newmenu, german('tit_prev'), self.fo_titel, 400, 160)

        self.tf_preparation = tk.Text(self.newmenu, font=self.fo_small, width=43, height=20, relief='flat',
                                      bg=self.bg_app, fg=self.fg_app)
        self.tf_preparation.place(x=11, y=293)
        self.cr_but(self.newmenu, german('add'), self.fo_small, self.add_preparation, 185, 565)
        self.cr_but(self.newmenu, german('menu_save'), self.fo_small, self.save_new_recipe, 328, 565, 42)
        self.cr_but(self.newmenu, german('chancel'), self.fo_small, self.save_new_recipe, 660, 565)

    def site_about(self):
        self.s_about = tk.Toplevel(self.root, bg=self.bg_app)
        self.s_about.title = german('about')
        self.s_about.config(width=300, height=150)

    def cr_lab(self, win, text, font, x, y):
        tk.Label(win, text=text, font=font,
                 bg=self.bg_app, fg=self.fg_app).place(x=x, y=y)

    def cr_but(self, win, text, font, com, x, y, w=15):
        tk.Button(win, text=text, font=font,
                  bg=self.bg_app, fg=self.fg_app, width=w,
                  activebackground=self.bg_act, activeforeground=self.fg_act,
                  command=com).place(x=x, y=y)

    def cr_pic(self, win, img, x, y):
        tk.Label(win, image=img,
                 bg=self.bg_app, fg=self.fg_app).place(x=x, y=y)

    def get_dict_list(self, dictionary):
        for key in dictionary.keys():
            self.list_dict.append(key)
        return self.list_dict

    def cur_select(self, evt):
        self.val_lbox = str((self.lbox_rec.get(self.lbox_rec.curselection())))
        self.set_picture(self.val_lbox)
        print(evt)

    def set_picture(self, image):
        self.pic_menu_path['file'] = self.path_pics + '/' + image + '.png'

    def save_new_recipe(self):
        w_new_recipe(self.en_name.get(), self.en_ingr.get(), self.en_quant.get())
        w_new_recipe(self.en_name.get(), 'Name', self.en_name.get())
        self.newmenu.destroy()

    def chancel_new_recipe(self):
        self.newmenu.destroy()

    def add_preparation(self):
        self.ingr_dict['Name'] = self.en_name.get()
        self.act_rec_path = self.recipe_path + self.ingr_dict['Name'] + '.txt'
        w_new_recipe(self.ingr_dict['Name'], 'zubereitung', self.tf_preparation.get('1.0', 'end'))
        self.tf_preparation.delete('0.1', 'end')

    def add_ingr(self):
        self.ingr_dict['Name'] = self.en_name.get()
        self.act_rec_path = self.recipe_path + self.ingr_dict['Name'] + '.txt'
        w_new_recipe(self.ingr_dict['Name'], self.en_ingr.get(), self.en_quant.get())
        self.en_ingr.delete(0, 'end')
        self.en_quant.delete(0, 'end')
        self.create_preview()

    def create_preview(self):
        self.di_recipe = r_di_recipe(self.en_name.get())
        self.li_k_recipe = self.get_dict_list(self.di_recipe)
        for key in range(len(self.li_k_recipe)):
            self.cr_lab(self.newmenu, self.li_k_recipe[key], self.fo_midd, 400, self.prev_start_y)
            self.cr_lab(self.newmenu, self.di_recipe[self.li_k_recipe[key]],
                        self.fo_midd, 500, self.prev_start_y)
            self.prev_start_y += 18
        self.prev_start_y = 250

    def set_colors(self, b_app, b_frame, f_app):
        self.bg_app = colors(b_app)
        self.bg_frame = colors(b_frame)
        self.fg_app = colors(f_app)
        self.bg_act = colors(f_app)
        self.fg_act = colors(b_app)


if __name__ == '__main__':
    app = CookBook()
