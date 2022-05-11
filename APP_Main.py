#!/usr/bin/python3
import tkinter as tk
import pathlib
import time
import ast


def cr_but_page(self, master, t, fon, b, f, targetsite, r, c, w=15, px=0, py=0, rs=1, cs=1, st=''):
    tk.Button(self, text=t, font=fon, bg=b, fg=f, width=w, activebackground=bg_act, activeforeground=fg_act,
              command=lambda: master.switch_frame(targetsite),
              relief='groove').grid(row=r, column=c,
                                    padx=px, pady=py,
                                    rowspan=rs, columnspan=cs,
                                    sticky=st)


def cr_but_back(self, master):
    tk.Button(self, text=r_di_val(pa_lan, 'back'), font=fo_sma, bg=bg_app, fg=fg_app,
              width=10, activebackground=bg_act, activeforeground=fg_act,
              command=lambda: master.switch_frame(PageStart),
              relief='groove').grid(row=51, column=10, rowspan=2, columnspan=6, sticky='s')


def cr_fra(self, widt, heig, r, c, px=0, py=0, b='', rs=1, cs=1, st=''):
    tk.Frame(self, width=widt, height=heig, bg=b).grid(row=r, column=c,
                                                       padx=px, pady=py,
                                                       rowspan=rs, columnspan=cs,
                                                       sticky=st)


def cr_fr_ma(win, master, ts1, ts2, r, c):
    fr_main = tk.Frame(win, bg=bg_app, width=400, height=200)
    fr_main.grid(row=r, column=c, rowspan=4, columnspan=17)
    cr_lab(fr_main, r_di_val(pa_lan, 'inst_main'), fo_mid, bg_app, fg_app, 0, 0, 0, 0, 1, 2)
    cr_but_page(fr_main, master, r_di_val(pa_lan, 'new_rec'), fo_mid, bg_app, fg_app, ts1, 1, 0, 20, 0, 0, 1, 1)
    cr_but_page(fr_main, master, r_di_val(pa_lan, 'edit_rec'), fo_mid, bg_app, fg_app, ts2, 1, 1, 20, 2, 0, 1, 1)


def cr_line(self, widt, heig, r, c, rs=1, cs=1, st=''):
    tk.Frame(self, width=widt, height=heig, bg=fg_app).grid(row=r, column=c,
                                                            rowspan=rs, columnspan=cs,
                                                            sticky=st)


def cr_lab(win, t, fo, b, f, r, c, px=0, py=0, rs=1, cs=1, s=''):
    tk.Label(win, text=t, font=fo,
             bg=b, fg=f).grid(row=r, column=c,
                              padx=px, pady=py,
                              rowspan=rs, columnspan=cs,
                              sticky=s)


def cr_pic(win, img, r, c, b='green', px=0, py=0, rs=1, cs=1, st=''):
    tk.Label(win, image=img, bg=b).grid(row=r, column=c, padx=px, pady=py,
                                        rowspan=rs, columnspan=cs,
                                        sticky=st)


def cr_rast_page(win, bg='red'):
    # zeropoint x=0, y=0
    cr_fra(win, 4, 4, 0, 0, 2, 2, 'blue')
    # create raster
    for i in range(55):
        cr_fra(win, 20, 2, 0, i + 1, 1, 0, bg)
    for i in range(55):
        cr_fra(win, 2, 15, i + 1, 0, 0, 1, bg)


def cr_lines_ps(win):
    # create Lines
    cr_line(win, 6, 795, 4, 18, 47, 1)
    cr_line(win, 398, 3, 9, 0, 1, 19, 'w')
    cr_line(win, 760, 3, 15, 18, 1, 34, 'e')
    cr_line(win, 398, 3, 30, 0, 1, 19, 'w')


def cr_lines_pn(win):
    # create all lines @ the new_recipe_page
    # cr_line(win, 3, 765, 3, 6, 20, 1, 'n')
    pass


def cr_lines_pe(win):
    # create all lines @ the edit_recipe_page
    # cr_line(win, 3, 765, 3, 4, 20, 1, 'n')
    pass


def cr_view_main(win, act_rec_name_var, r, c):
    fr_main = tk.Frame(win, width=360, height=320, bg=bg_app)
    fr_main.grid(row=r, column=c, rowspan=19, columnspan=20, sticky='w')
    cr_fra(fr_main, 150, 2, 0, 1, 0, 0)
    cr_fra(fr_main, 200, 2, 0, 2, 0, 0, 'green')
    for i in range(5):
        cr_fra(fr_main, 2, 50, i + 1, 0, 0, 0)
    tk.Label(fr_main, text='Name:', font=fo_big, bg=bg_app, fg=fg_app).grid(row=1, column=1, sticky='w')
    tk.Label(fr_main, text=r_di_val(pa_rec_d + act_rec_name_var + '_d.txt', 'name'),
             font=fo_big, bg=bg_app, fg=fg_app).grid(row=1, column=2, sticky='w')
    tk.Label(fr_main, text='Portionen:', font=fo_big, bg=bg_app, fg=fg_app).grid(row=2, column=1, sticky='w')
    tk.Label(fr_main, text=r_di_val(pa_rec_d + act_rec_name_var + '_d.txt', 'port'),
             font=fo_big, bg=bg_app, fg=fg_app).grid(row=2, column=2, sticky='w')
    tk.Label(fr_main, text='Kategorie:', font=fo_big, bg=bg_app, fg=fg_app).grid(row=3, column=1, sticky='w')
    tk.Label(fr_main, text=r_di_val(pa_rec_d + act_rec_name_var + '_d.txt', 'cat'),
             font=fo_big, bg=bg_app, fg=fg_app).grid(row=3, column=2, sticky='w')
    tk.Label(fr_main, text='Region:', font=fo_big, bg=bg_app, fg=fg_app).grid(row=4, column=1, sticky='w')
    tk.Label(fr_main, text=r_di_val(pa_rec_d + act_rec_name_var + '_d.txt', 'reg'),
             font=fo_big, bg=bg_app, fg=fg_app).grid(row=4, column=2, sticky='w')


def cr_view_ingr(win, recipe, stat=0):
    fr_prep = tk.Frame(win, width=400, height=550, bg=bg_app)
    fr_prep.grid(row=15, column=19, rowspan=36, columnspan=10)
    cr_lab(fr_prep, r_di_val(pa_lan, 'ingr'), fo_big, bg_app, fg_app, 0, 0, 0, 0, 1, 1, 'nw')
    tf_ing = tk.Text(fr_prep, width=30, height=31, relief='flat', bg=bg_app, fg=fg_app)
    tf_ing.grid(row=1, column=0)
    tf_ing.delete('0.0', 'end')
    tf_ing.insert('0.0', recipe)
    if stat == 0:
        tf_ing.config(state='disabled')
    else:
        tf_ing.config(state='normal')


def cr_view_prep(self, recipe, stat=0):
    self.fr_prep = tk.Frame(self, width=500, height=550, bg=bg_app)
    self.fr_prep.grid(row=15, column=29, rowspan=36, columnspan=22)
    cr_lab(self.fr_prep, r_di_val(pa_lan, 'titel_prep'), fo_big, bg_app, fg_app, 0, 0, 0, 0, 1, 1, 'nw')
    self.tf_ing = tk.Text(self.fr_prep, width=55, height=31, relief='flat', bg=bg_app, fg=fg_app)
    self.tf_ing.grid(row=1, column=0)
    self.tf_ing.delete('0.0', 'end')
    self.tf_ing.insert('0.0', recipe)
    if stat == 0:
        self.tf_ing.config(state='disabled')
    else:
        self.tf_ing.config(state='normal')


def cr_win_tit(win, text, spoon, logo):
    cr_lab(win, r_di_val(pa_lan, text), fo_tit, bg_app, fg_app, 1, 1, 0, 0, 3, 16, 'w')
    cr_line(win, 1150, 6, 4, 0, 1, 58, 'w')
    cr_line(win, 1150, 6, 50, 0, 1, 58, 'sw')
    cr_pic(win, spoon, 1, 40, bg_app, 0, 0, 3, 10)
    cr_pic(win, logo, 51, 1, bg_app, 0, 0, 3, 5, 'w')


def print_event(event):
    print('----------------------------------------------------')
    print('Value: evt_var... only printed. %s' % event)
    print('----------------------------------------------------')


def r_di_val(filepath, keyword):
    file_dict = open(filepath, 'r')
    data_from_file = file_dict.read()
    file_dict.close()
    readed_dict = ast.literal_eval(data_from_file)
    dict_value = readed_dict[keyword]
    return dict_value


def set_colors(b_app, b_fra, f_app):
    global bg_app, bg_act, bg_fra, fg_app, fg_act
    bg_app = r_di_val(pa_col_f, b_app)
    bg_act = r_di_val(pa_col_f, f_app)
    bg_fra = r_di_val(pa_col_f, b_fra)
    fg_app = r_di_val(pa_col_f, f_app)
    fg_act = r_di_val(pa_col_f, b_app)


def ret_act_rec(act_rec_name):
    pa = pa_rec + act_rec_name + '.txt'
    f = open(pa, 'r')
    fd = f.read()
    f.close()
    return fd


def ret_act_ing(act_rec_name):
    pa = pa_rec_d + act_rec_name + '_i.txt'
    f = open(pa, 'r')
    fd = f.read()
    f.close()
    return fd


class CB(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.f_rec_lists, self.data_f_rec_lists = [None, ] * 2
        self.menubar, self.filemenu, self.helpmenu, self.lbox_menu = (None,) * 4
        self._frame = None
        self.switch_frame(PageStart)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        self.configure(bg=bg_app)

    def cr_menubar(self, fo, bg, fg, bga, fga):
        self.menubar = tk.Menu(self, font=fo, bg=bg, fg=fg, activebackground=bga, activeforeground=fga, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.filemenu.add_command(label=r_di_val(pa_lan, 'new_rec'),
                                  command=lambda: self.master.switch_frame(PageNewRec))
        self.filemenu.add_command(label=r_di_val(pa_lan, 'edit_rec'),
                                  command=lambda: self.master.switch_frame(PageEditRec))
        self.filemenu.add_command(label=r_di_val(pa_lan, 'quit'), command=self.quit)

        self.menubar.add_cascade(label=r_di_val(pa_lan, 'file'), menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=fo, bg=bg, fg=fg, activebackground=bga,
                                activeforeground=fga, relief='flat')
        self.helpmenu.add_command(label=r_di_val(pa_lan, 'about'))
        self.helpmenu.add_command(label=r_di_val(pa_lan, 'help'))
        self.menubar.add_cascade(label=r_di_val(pa_lan, 'help'), menu=self.helpmenu)

        self.master.config(menu=self.menubar)

    def ret_lists_rec(self, listpath):
        self.f_rec_lists = open(listpath, 'r')
        self.data_f_rec_lists = self.f_rec_lists.read().split()
        self.f_rec_lists.close()
        return self.data_f_rec_lists


class PageStart(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.fr_prep, self.tf_prep = (None,) * 2
        self.pa_act_rec_var = tk.StringVar()
        self.pa_act_pic_var = tk.StringVar()
        self.pa_act_ing_var = tk.StringVar()
        self.act_rec_name_var = tk.StringVar(value='')
        self.menubar, self.filemenu, self.helpmenu, self.fr_choo, self.lbox_rec = (None,) * 5
        self.configure(bg=bg_app)
        CB.cr_menubar(self, fo_sma, bg_app, fg_app, fg_app, bg_app)
        self.pi_spo = tk.PhotoImage(file=pa_spo)
        self.pi_log = tk.PhotoImage(file=pa_log)
        self.pi_sta = tk.PhotoImage(file=pa_pi_start)
        self.pi_rec_a = tk.PhotoImage(file=pa_pi_start)
        self.rec_list_var = tk.StringVar(value=CB.ret_lists_rec(self, pa_rec_l))
        self.act_rec_f = ret_act_rec(self.pa_act_rec_var.get())
        # Window configs with a raster, the top and bottom and the separate-lines

        cr_rast_page(self, bg_app)
        cr_win_tit(self, 'main_tite', self.pi_spo, self.pi_log)
        cr_lines_ps(self)
        # create a field for act_pic frame and Label
        cr_lab(self, r_di_val(pa_lan, 'act_rec_pic'), fo_big, bg_app, fg_app, 10, 1, 10, 0, 2, 9, 'w')
        self.fr_act_pic = tk.Frame(self, bg=bg_fra, width=300, height=300)
        self.fr_act_pic.grid(row=12, column=2, rowspan=18, columnspan=15)
        tk.Label(self.fr_act_pic, image=self.pi_rec_a, bg=bg_app, width=290, height=290).grid(row=0, column=0,
                                                                                              padx=5, pady=5,
                                                                                              rowspan=1, columnspan=1)

        cr_fr_ma(self, self.master, PageNewRec, PageEditRec, 5, 1)
        # create a field for choosing a recipe
        self.pr_data()
        self.cr_fr_choose(5, 19)
        cr_view_ingr(self, ret_act_ing(self.act_rec_name_var.get()))
        cr_view_prep(self, ret_act_rec(self.act_rec_name_var.get()))
        cr_view_main(self, self.act_rec_name_var.get(), 31, 1)

    def cr_fr_choose(self, r, c):
        self.fr_choo = tk.Frame(self, bg=bg_app, relief='flat')
        self.fr_choo.grid(row=r, column=c, rowspan=10, columnspan=14)
        cr_lab(self.fr_choo, r_di_val(pa_lan, 'sel_menu'), fo_big, bg_app, fg_app, 0, 0, 0, 0, 1, 1, 'w')
        cr_lab(self.fr_choo, r_di_val(pa_lan, 'inst_choo'), fo_mid, bg_app, fg_app, 1, 0, 0, 0, 1, 1, 'w')
        self.lbox_rec = tk.Listbox(self.fr_choo, listvariable=self.rec_list_var, width=30, height=5,
                                   bg=bg_app, fg=fg_app, selectmode='browse',
                                   selectbackground=bg_act, selectforeground=fg_act, border=5)
        self.lbox_rec.grid(row=2, column=0, padx=0, pady=5, rowspan=1, columnspan=1, sticky='w')
        self.lbox_rec.bind('<<ListboxSelect>>', self.cur_rec_sel)

    def cur_rec_sel(self, evt):
        self.act_rec_name_var.set(str((self.lbox_rec.get(self.lbox_rec.curselection()))))
        self.pa_act_rec_var.set(pa_rec + self.act_rec_name_var.get() + '.txt')
        self.pa_act_pic_var.set(pa_rec + self.act_rec_name_var.get() + '.png')
        self.pa_act_ing_var.set(pa_rec_d + self.act_rec_name_var.get() + '_d.txt')
        self.set_act_rec_pic()
        cr_view_prep(self, ret_act_rec(self.act_rec_name_var.get()))
        cr_view_ingr(self, ret_act_ing(self.act_rec_name_var.get()))
        cr_view_main(self, self.act_rec_name_var.get(), 31, 1)

        self.pr_data()
        print_event(evt)

    def pr_data(self):
        print('------------------------------------\n'
              ' Printfunc in Class Pagestart: %s\n'
              '------------------------------------' % str(time.asctime()))
        print('pa_app:\t\t\t\t\t%s' % pa_app)
        print('pa_pat:\t\t\t\t\t%s' % pa_pat)
        print('pa_lan:\t\t\t\t\t%s' % pa_lan)
        print('pa_rec:\t\t\t\t\t%s' % pa_rec)
        print('pa_spo:\t\t\t\t\t%s' % pa_spo)
        print('self.act_rec_name_var.get(): \t\t%s' % self.act_rec_name_var.get())
        print('pa_act_rec_var:\t\t\t\t%s' % self.pa_act_rec_var.get())
        print('pa_act_pic_var:\t\t\t\t%s' % self.pa_act_pic_var.get())
        print('act_rec_f:\t\t\t\t%s' % self.act_rec_f)
        print('CB.ret_lists_rec(CB, pa_li_rec):\t%s' % CB.ret_lists_rec(CB, pa_rec_l))
        print('pa_rec_d:\t\t\t\t%s' % pa_rec_d)
        print('self.pa_act_dic_var:\t\t\t%s' % self.pa_act_ing_var.get())

        print('\n___________________End of Printfunction___________________\n\n')

    def set_act_rec_pic(self):
        self.pi_rec_a['file'] = pa_pic + '/' + self.act_rec_name_var.get() + '.png'


class PageNewRec(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.menubar, self.filemenu, self.helpmenu = (None,) * 3
        self.configure(bg=bg_app)
        CB.cr_menubar(self, fo_sma, bg_app, fg_app, fg_app, bg_app)
        self.spoon = tk.PhotoImage(file=pa_spo)
        self.logo = tk.PhotoImage(file=pa_log)
        self.rec_list_var = tk.StringVar(value=CB.ret_lists_rec(self, pa_rec_l))
        cr_rast_page(self, bg_app)
        cr_win_tit(self, 'new_rec', self.spoon, self.logo)
        cr_lines_pn(self)
        cr_but_back(self, master)


class PageEditRec(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.act_rec_name_var = tk.StringVar()
        self.menubar, self.filemenu, self.helpmenu, = (None,) * 3
        self.configure(bg=bg_app)
        CB.cr_menubar(self, fo_sma, bg_app, fg_app, fg_app, bg_app)
        self.spoon = tk.PhotoImage(file=pa_spo)
        self.logo = tk.PhotoImage(file=pa_log)

        cr_rast_page(self, 'red')
        cr_win_tit(self, 'edit_rec', self.spoon, self.logo)
        cr_lines_pe(self)
        cr_fr_ma(self, self.master, PageNewRec, PageEditRec, 5, 1)
        cr_but_back(self, master)


if __name__ == "__main__":
    pa_app = str(pathlib.Path().absolute())
    pa_pat = pa_app + '/Cookbook/config/paths.txt'
    pa_lan = pa_app + r_di_val(pa_pat, 'file_language')
    pa_fon = pa_app + r_di_val(pa_pat, 'file_fonts')
    pa_col_f = pa_app + r_di_val(pa_pat, 'file_colors')
    pa_rec_l = pa_app + r_di_val(pa_pat, 'recipelist')
    pa_spo = pa_app + r_di_val(pa_pat, 'spoon')
    pa_log = pa_app + r_di_val(pa_pat, 'logo')
    pa_cat_f = pa_app + r_di_val(pa_pat, 'category')
    pa_pi_start = pa_app + r_di_val(pa_pat, 'startpic')
    pa_rec = pa_app + r_di_val(pa_pat, 'dir_recipe')
    pa_pic = pa_app + r_di_val(pa_pat, 'dir_recipe')
    pa_rec_d = pa_app + r_di_val(pa_pat, 'rec_d')

    fo_tit = r_di_val(pa_fon, 'Calibri24')
    fo_big = r_di_val(pa_fon, 'Calibri14')
    fo_mid = r_di_val(pa_fon, 'Calibri10')
    fo_sma = r_di_val(pa_fon, 'Calibri8')
    bg_app, bg_act, bg_fra, fg_app, fg_act = ('',) * 5

    set_colors('anthracite', 'black', 'orange')
    app = CB()
    app.title('Kochbuch')
    app.geometry('1150x900')
    app.resizable(width=False, height=False)

    app.mainloop()
