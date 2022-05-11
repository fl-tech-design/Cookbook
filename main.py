#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox as mbox
import pathlib
import ast
import time


class CookBook:
    def __init__(self):
        self.f_recipelist = None
        self.recipelist = None
        self.data_f_rec_lists = None
        self.f_rec_lists = None
        self.path_act_recipe_dict = None
        self.file_config, self.data_file_config, self.dict_config, self.dict_config_val = (None,) * 4
        self.file_paths, self.data_file_paths, self.dict_paths, self.dict_paths_val = (None,) * 4
        self.fo_tit, self.fo_big, self.fo_mid, self.fo_sma = (None,) * 4

        # define paths
        self.path_app = str(pathlib.Path().absolute())
        self.path_paths = self.path_app + '/Cookbook/config/paths.txt'
        self.path_color = self.path_app + self.r_conf_file(self.path_paths, 'file_colors')
        self.path_dicts = self.path_app + self.r_conf_file(self.path_paths, 'dicts_recipe')
        self.path_fonts = self.path_app + self.r_conf_file(self.path_paths, 'file_fonts')
        self.path_langu = self.path_app + self.r_conf_file(self.path_paths, 'file_language')
        self.path_pics = self.path_app + self.r_conf_file(self.path_paths, 'dir_recipe')
        self.path_qr = self.path_app + self.r_conf_file(self.path_paths, 'qr_code')
        self.path_recipelist = self.path_app + self.r_conf_file(self.path_paths, 'recipelist')
        self.path_recipelist_d = self.path_app + self.r_conf_file(self.path_paths, 'recipelist_d')
        self.path_recipes = self.path_app + self.r_conf_file(self.path_paths, 'dir_recipe')

        # create variables
        self.site_n_rec, self.val_lb_rec, self.ef_name, self.ef_ingr, \
        self.ef_quant, self.tf_preparation, self.fr_name, self.fr_ingr, self.menubar, \
        self.filemenu, self.helpmenu, self.file, self.site_e_rec, self.siteabout = (None,) * 14
        self.bg_app, self.bg_fra, self.fg_app, self.bg_act, self.fg_act, self.dictdata_as_string = ('',) * 6
        self.list_dict = []
        self.dictfile = None
        self.file_new_recipe, self.file_new_recipe_d, self.recipelist_file, self.recipelist_d_file, \
            = (None,) * 4

        # Set configs
        self.set_colors('anthracite', 'black', 'orange')
        self.set_fonts()
        # Create Mainwindow
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title(self.r_conf_file(self.path_langu, 'win_titel'))
        self.root.config(bg=self.bg_app)

        self.act_pict_path_var = tk.StringVar()
        self.act_rec_name_var = tk.StringVar()
        self.act_rec_path_var = tk.StringVar()

        self.recipelist_d_var = tk.StringVar(value=self.ret_lists_rec(self.path_recipelist_d))
        self.recipelist_var = tk.StringVar(value=self.ret_lists_rec(self.path_recipelist))
        self.li_for_lbox_rec_var = tk.StringVar()
        self.prev_var = tk.StringVar()

        self.new_rec_name_var = tk.StringVar()
        self.ef_port = tk.StringVar()
        self.ef_time = tk.StringVar()

        self.cr_lab(self.root, self.r_conf_file(self.path_langu, 'main_tite'), self.fo_tit, 10, 10)
        self.cr_lab(self.root, self.r_conf_file(self.path_langu, 'inst_main'), self.fo_mid, 12, 85)
        self.cr_lab(self.root, self.r_conf_file(self.path_langu, 'sel_menu'), self.fo_big, 433, 75)

        self.cr_but(self.root, self.r_conf_file(self.path_langu, 'new_men_save'), self.fo_sma, self.site_recipe_new, 12,
                    137, 24)
        self.cr_but(self.root, self.r_conf_file(self.path_langu, 'edit_rec'), self.fo_sma, self.site_recipe_edit, 220,
                    137, 24)

        # create frame for at_recipe_pic
        self.fr_pic = tk.Frame(self.root, bg=self.bg_fra, width=410, height=412)
        self.fr_pic.place(x=10, y=180)
        # Indicate
        self.pi_act_rec = tk.PhotoImage(file=self.act_pict_path_var.get(), width=400, height=400)
        self.spoon = tk.PhotoImage(file=self.path_app + self.r_conf_file(self.path_paths, 'spoon'), width=200,
                                            height=100)
        self.pic_qr_path = tk.PhotoImage(file=self.path_app + self.r_conf_file(self.path_paths, 'qr_code'))

        self.cr_pic(self.fr_pic, self.pi_act_rec, self.bg_app, 4, 5)
        self.cr_pic(self.root, self.spoon, self.bg_app, 580, -20)
        # Create Lines
        self.cr_frame(self.root, self.fg_app, 3, 2000, 425, 69)
        self.cr_frame(self.root, self.fg_app, 2000, 3, 0, 69)
        self.cr_frame(self.root, self.fg_app, 1500, 3, 425, 206)
        self.cr_frame(self.root, self.fg_app, 426, 3, 0, 172)

        # create listbox for choosing the recipe
        self.lbox_recipe = tk.Listbox(self.root, listvariable=self.recipelist_var, width=44, height=5, bg=self.bg_fra,
                                      fg=self.fg_app, borderwidth=2, selectmode='browse')
        self.lbox_recipe.place(x=433, y=105)
        self.lbox_recipe.bind('<<ListboxSelect>>', self.cur_rec_sel)
        self.cr_but(self.root, 'print', self.fo_big, self.print_data, 420, 420)

        # starting the menubar and the application
        self.cr_menubar(self.root, self.fo_sma, self.bg_app, self.fg_app, self.bg_act, self.fg_act)
        self.root.mainloop()

    def cr_menubar(self, win, fo, bg, fg, bga, fga):
        self.menubar = tk.Menu(win, font=fo, bg=bg, fg=fg, activebackground=bga, activeforeground=fga, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.filemenu.add_command(label=self.r_conf_file(self.path_langu, 'new_rec'), command=self.site_recipe_new)
        self.filemenu.add_command(label=self.r_conf_file(self.path_langu, 'edit_rec'), command=self.site_recipe_edit)
        self.filemenu.add_command(label=self.r_conf_file(self.path_langu, 'quit'), command=win.quit)
        self.menubar.add_cascade(label=self.r_conf_file(self.path_langu, 'file'), menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.helpmenu.add_command(label=self.r_conf_file(self.path_langu, 'help'))
        self.helpmenu.add_command(label=self.r_conf_file(self.path_langu, 'about'), command=self.site_about)
        self.menubar.add_cascade(label=self.r_conf_file(self.path_langu, 'help'), menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def site_recipe_new(self):
        # Create a new site for creating a new recipe.
        self.site_n_rec = tk.Toplevel(bg=self.bg_app)
        self.site_n_rec.title(self.r_conf_file(self.path_langu, 'new_men_save'))
        self.site_n_rec.config(width=800, height=628)
        self.cr_lab(self.site_n_rec, self.r_conf_file(self.path_langu, 'new_men_save'), self.fo_tit, 10, 10)

        # Frame for name entry's etc
        self.fr_name = tk.Frame(self.site_n_rec, bg=self.bg_fra, width=326, height=156)
        self.fr_name.place(x=6, y=60)
        self.cr_frame(self.fr_name, self.bg_app, 320, 148, 3, 4)
        self.cr_lab(self.fr_name, self.r_conf_file(self.path_langu, 'la_reci'), self.fo_big, 10, 5)
        self.cr_lab(self.fr_name, self.r_conf_file(self.path_langu, 'la_name'), self.fo_mid, 10, 36)
        self.ef_name = tk.Entry(self.fr_name, width=27, bg=self.bg_app, fg=self.fg_app)
        self.ef_name.place(x=98, y=36)
        self.cr_lab(self.fr_name, self.r_conf_file(self.path_langu, 'la_port'), self.fo_mid, 10, 63)
        self.ef_port = tk.Entry(self.fr_name, width=27, bg=self.bg_app, fg=self.fg_app)
        self.ef_port.place(x=98, y=63)
        self.cr_lab(self.fr_name, self.r_conf_file(self.path_langu, 'la_time'), self.fo_mid, 10, 90)
        self.ef_time = tk.Entry(self.fr_name, width=27, bg=self.bg_app, fg=self.fg_app)
        self.ef_time.place(x=98, y=90)
        self.cr_but(self.fr_name, self.r_conf_file(self.path_langu, 'la_crea'), self.fo_sma,
                    self.but_add_name_func, 5, 122, 41)

        # Frame for new ingredients
        self.fr_ingr = tk.Frame(self.site_n_rec, bg=self.bg_fra, width=450, height=128)
        self.fr_ingr.place(x=345, y=60)
        self.cr_frame(self.fr_ingr, self.bg_app, 444, 120, 3, 4)
        self.cr_lab(self.fr_ingr, self.r_conf_file(self.path_langu, 'instr_ingr'), self.fo_big, 6, 3)
        self.cr_lab(self.fr_ingr, self.r_conf_file(self.path_langu, 'la_ingr'), self.fo_mid, 6, 35)
        self.ef_ingr = tk.Entry(self.fr_ingr, width=46, bg=self.bg_app, fg=self.fg_app)
        self.ef_ingr.place(x=68, y=33)
        self.cr_lab(self.fr_ingr, self.r_conf_file(self.path_langu, 'la_quan'), self.fo_mid, 6, 62)
        self.ef_quant = tk.Entry(self.fr_ingr, width=46, bg=self.bg_app, fg=self.fg_app)
        self.ef_quant.place(x=68, y=60)
        self.cr_but(self.fr_ingr, self.r_conf_file(self.path_langu, 'add'), self.fo_sma, self.add_ingr2dict, 8, 92, 58)

        self.cr_lab(self.site_n_rec, self.r_conf_file(self.path_langu, 'titel_prep'), self.fo_big, 10, 230)
        self.cr_lab(self.fr_ingr, self.r_conf_file(self.path_langu, 'la_ingr'), self.fo_big, 10, 258)
        self.cr_lab(self.site_n_rec, self.r_conf_file(self.path_langu, 'la_prev'), self.fo_tit, 350, 203)

        self.tf_preparation = tk.Text(self.site_n_rec, font=self.fo_sma,
                                      width=45, height=24, relief='flat',
                                      bg=self.bg_app, fg=self.fg_app)
        self.tf_preparation.place(x=8, y=258)
        self.cr_but(self.site_n_rec, self.r_conf_file(self.path_langu, 'save'), self.fo_sma, self.save_new_recipe, 345,
                    595, 60)
        self.cr_but(self.site_n_rec, self.r_conf_file(self.path_langu, 'chancel'), self.fo_sma,
                    lambda: self.close_win(self.site_n_rec), 4, 595,
                    43)
        # Create Lines
        self.cr_frame(self.site_n_rec, self.fg_app, 2000, 3, 0, 50)
        self.cr_frame(self.site_n_rec, self.fg_app, 3, 535, 338, 50)
        self.cr_frame(self.site_n_rec, self.fg_app, 1500, 3, 340, 195)
        self.cr_frame(self.site_n_rec, self.fg_app, 339, 3, 0, 225)
        self.cr_frame(self.site_n_rec, self.fg_app, 2000, 3, 0, 585)

    def site_recipe_edit(self):
        if self.act_rec_name_var.get() == '':
            mbox.showwarning('Achtung', self.r_conf_file(self.path_langu, 'warning'))
        else:
            self.site_e_rec = tk.Toplevel(bg=self.bg_app)
            self.site_e_rec.title(self.r_conf_file(self.path_langu, 'edit_rec'))
            self.site_e_rec.config(width=800, height=628)
            self.cr_lab(self.site_e_rec, self.path_qr, self.fo_tit, 10, 10)

            self.cr_but(self.site_e_rec, self.r_conf_file(self.path_langu, 'chancel'), self.fo_mid,
                        lambda: self.close_win(self.site_e_rec), 200,
                        400)
            self.cr_but(self.site_e_rec, self.r_conf_file(self.path_langu, 'save'), self.fo_mid, self.site_about, 400,
                        400)

    def site_about(self):
        self.siteabout = tk.Toplevel(bg=self.bg_app)
        self.siteabout.title(self.r_conf_file(self.path_langu, 'about'))
        self.siteabout.config(width=400, height=420)
        self.siteabout.resizable(width=False, height=False)
        self.cr_frame(self.siteabout, self.bg_fra, 390, 390, 6, 6)
        self.cr_pic(self.siteabout, self.pic_qr_path, 'grey', 15, 15)
        self.cr_lab(self.siteabout, self.r_conf_file(self.path_langu, 'la_cr_by'), self.fo_mid, 10, 397)

    def add_new_name2recipelist(self):
        self.f_recipelist = open(self.path_recipelist, 'a')
        self.f_recipelist.write('\n' + self.new_rec_name_var.get())
        self.f_recipelist.close()

    def add_new_name2recipelist_d(self):
        self.f_recipelist = open(self.path_recipelist_d, 'a')
        self.f_recipelist.write('\n' + self.new_rec_name_var.get() + '_d')
        self.f_recipelist.close()

    def add_ingr2dict(self):
        pass

    def but_add_name_func(self):
        self.new_rec_name_var.set(self.ef_name.get())
        self.cr_new_recipefiles()

    def cr_lab(self, win, text, font, x, y):
        tk.Label(win, text=text, font=font,
                 bg=self.bg_app, fg=self.fg_app).place(x=x, y=y)

    def cr_but(self, win, text, font, com, x, y, w=15):
        tk.Button(win, text=text, font=font,
                  bg=self.bg_app, fg=self.fg_app, width=w,
                  activebackground=self.bg_act, activeforeground=self.fg_act,
                  command=com).place(x=x, y=y)

    def cr_pic(self, win, img, bg, x, y):
        tk.Label(win, image=img,
                 bg=bg, fg=self.fg_app).place(x=x, y=y)

    def check_recipelist(self):
        if self.new_rec_name_var.get() in self.recipelist_var.get():
            return True
        else:
            return False


    def cr_new_recipefiles(self):
        self.new_rec_name_var.set(self.ef_name.get())
        if not self.check_recipelist():
            self.file_new_recipe_d = open(self.path_dicts + self.new_rec_name_var.get() + '_d.txt', 'w')
            self.file_new_recipe_d.write('')
            self.file_new_recipe_d.close()
            self.file_new_recipe = open(self.path_recipes + self.new_rec_name_var.get() + '.txt', 'w')
            self.file_new_recipe.write('')
            self.file_new_recipe.close()
            self.add_new_name2recipelist()
            self.add_new_name2recipelist_d()
        else:
            mbox.showwarning('Achtung', 'Name ist schon vergeben.')
            self.close_win(self.site_n_rec)
        self.print_data()

    def cur_rec_sel(self, evt):
        self.val_lb_rec = str((self.lbox_recipe.get(self.lbox_recipe.curselection())))
        self.act_rec_name_var.set(self.val_lb_rec)
        self.act_rec_path_var.set(self.path_recipes + self.val_lb_rec + '.txt')
        self.set_act_rec_pic(self.val_lb_rec)
        self.print_data()
        self.print_event(evt)


    def print_data(self):
        print('------------------------------------\n'
              ' Start of Printfunction: %s\n'
              '------------------------------------' % str(time.asctime()))
        print('*********     Paths     *********')
        print('self.path_app:\t\t\t\t%s' % self.path_app)
        print('self.path_paths:\t\t\t%s' % self.path_paths)
        print('self.path_color:\t\t\t%s' % self.path_color)
        print('self.path_dicts:\t\t\t%s' % self.path_dicts)
        print('self.path_fonts:\t\t\t%s' % self.path_fonts)
        print('self.path_langu:\t\t\t%s' % self.path_langu)
        print('self.path_pics:\t\t\t\t%s' % self.path_pics)
        print('self.path_qr:\t\t\t\t%s' % self.path_qr)
        print('self.path_recipelist:\t\t\t%s' % self.path_recipelist)
        print('self.path_recipelist_d:\t\t\t%s' % self.path_recipelist_d)

        print('\n*********     Dicts     *********')

        print('\n*********     Lists     *********')

        print('\n*********   Variabels   *********')
        print('self.act_rec_name_var.get():\t\t%s' % self.act_rec_name_var.get())
        print('self.act_rec_path_var.get():\t\t%s' % self.act_rec_path_var.get())
        print('self.new_rec_name_var.get():\t\t%s' % self.new_rec_name_var.get())
        print('self.recipelist_var.get():\t\t%s' % self.recipelist_var.get())
        print('self.recipelist_d_var.get():\t\t%s' % self.recipelist_d_var.get())
        print('self.val_lb_rec:\t\t\t\t%s' % self.val_lb_rec)

        print('\n*********   Functions   *********')
        print('check_recipelist(self):\t\t\t%s' % self.check_recipelist())

        print('----------------------------------\n'
              '       End of Printfunction       \n'
              '------------------------------------')

    def ret_lists_rec(self, listpath):
        self.f_rec_lists = open(listpath, 'r')
        self.data_f_rec_lists = self.f_rec_lists.read().split()
        self.f_rec_lists.close()
        return self.data_f_rec_lists

    def r_conf_file(self, filepath, keyword):
        self.file_config = open(filepath, 'r')
        self.data_file_config = self.file_config.read()
        self.file_config.close()
        self.dict_config = ast.literal_eval(self.data_file_config)
        self.dict_config_val = self.dict_config[keyword]
        return self.dict_config_val

    def save_new_recipe(self):
        self.close_win(self.site_n_rec)

    def set_colors(self, b_app, bg_fra, f_app):
        self.bg_app = self.r_conf_file(self.path_color, b_app)
        self.bg_fra = self.r_conf_file(self.path_color, bg_fra)
        self.fg_app = self.r_conf_file(self.path_color, f_app)
        self.bg_act = self.r_conf_file(self.path_color, f_app)
        self.fg_act = self.r_conf_file(self.path_color, b_app)

    def set_fonts(self):
        self.fo_tit = self.r_conf_file(self.path_fonts, 'Calibri24')
        self.fo_big = self.r_conf_file(self.path_fonts, 'Calibri14')
        self.fo_mid = self.r_conf_file(self.path_fonts, 'Calibri10')
        self.fo_sma = self.r_conf_file(self.path_fonts, 'Calibri8')

    def set_act_rec_pic(self, image):
        self.pi_act_rec['file'] = self.path_pics + '/' + image + '.png'

    @staticmethod
    def clear_entry(entryfield):
        entryfield.delete(0, 'end')

    @staticmethod
    def close_win(window):
        window.destroy()

    @staticmethod
    def cr_frame(win, bg, w, h, x, y):
        tk.Frame(win, bg=bg, width=w, height=h).place(x=x, y=y)

    @staticmethod
    def print_event(event):
        print('----------------------------------------------------')
        print('Value: evt_var... only printed. %s' % event)
        print('----------------------------------------------------')


if __name__ == '__main__':
    app = CookBook()
