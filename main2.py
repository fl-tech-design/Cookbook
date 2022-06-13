#!/usr/bin/python3
import tkinter as tk
import ast
import pathlib
import tkinter.messagebox as mbox


def check_app_state():
    app_state = r_data('app', 'app_state')
    print("def check_app_state():")
    return app_state


def r_data_dict():
    data_file = open(pa_app + pa_config, 'r')
    data_from_file = data_file.read()
    data_file.close()
    readed_dict = ast.literal_eval(data_from_file)
    return readed_dict


def r_data(key_1, key_2):
    readed_dict = r_data_dict()
    dict2 = readed_dict[key_1]
    data_val = dict2[key_2]
    return data_val


def r_rec_list():
    f_rec_list = open(pa_app + r_data('paths', 'rec_list'), 'r')
    rec_list = f_rec_list.read().split()
    f_rec_list.close()
    return rec_list


def ret_app_state():
    app_state = r_data('app', 'app_state')
    return app_state


def ret_act_path(stat):
    if stat == 0:
        stat_0 = pa_rec_d + act_name + '_d.txt'
        return stat_0
    if stat == 1:
        stat_1 = pa_rec_d + act_name + '_i.txt'
        return stat_1
    if stat == 2:
        stat_2 = pa_rec + act_name + '.txt'
        return stat_2
    if stat == 3:
        stat_3 = pa_rec + act_name + '.png'
        return stat_3


def ret_act_rec_data(key):
    f_info = open(ret_act_path(0), 'r')
    data_from_file = f_info.read()
    f_info.close()
    readed_dict = ast.literal_eval(data_from_file)
    return readed_dict[key]


def ret_act_ingr():
    f_ingr = open(ret_act_path(1), 'r')
    ingr_data = f_ingr.read()
    f_ingr.close()
    return ingr_data


def ret_act_prep():
    f_ingr = open(ret_act_path(2), 'r')
    ingr_data = f_ingr.read()
    f_ingr.close()
    return ingr_data


def set_app_state(app_state):
    data_dict['app']['app_state'] = app_state
    w_data_dict(str(data_dict))


def set_colors(b_app, b_fra, f_app):
    global bg_app, bg_act, bg_fra, fg_app, fg_act
    bg_app = r_data('color', b_app)
    bg_act = r_data('color', f_app)
    bg_fra = r_data('color', b_fra)
    fg_app = r_data('color', f_app)
    fg_act = r_data('color', b_app)


def w_data_dict(dict_name):
    data_file = open(pa_app + pa_config, 'w')
    data_file.write(dict_name)
    data_file.close()


class CB:
    def __init__(self):
        self.la_ingr, self.tf_ingr, self.tf_prep, self.la_prep = (None,) * 4
        self.la_name, self.la_port, self.la_time, self.la_cate = (None,) * 4
        self.en_name, self.en_port, self.en_time, self.en_cate = (None,) * 4
        self.fr_preparation, self.fr_pict, self.fr_ingredients, self.fr_info = (None,) * 4
        self.fr_choose, self.la_choos, self.lb_choose_rec = (None,) * 3
        self.fr_top, self.la_titel = (None,) * 2
        self.new_rec_data_dict = {}
        self.app_stat = data_dict['app']['app_state']
        self.menubar, self.filemenu, self.helpmenu, self.language_menu = (None,) * 4
        self.fr_bottom, self.bu_bottom_l, self.bu_bottom_r = (None,) * 3

        self.root = tk.Tk()
        self.root.title(r_data(lang, 'cookbook'))
        self.root.config(width=1200, height=600, bg=fg_app)
        self.root.resizable(width=False, height=False)

        self.act_name_var = tk.StringVar(value='')
        self.act_port_var = tk.StringVar(value='')
        self.pa_act_rec_var = tk.StringVar()
        self.pa_act_pic_var = tk.StringVar()
        self.pa_act_ing_var = tk.StringVar()

        self.pi_rec_a = tk.PhotoImage(file=pa_startpic)

        self.ent_list = [self.en_name, self.en_port, self.en_time, self.en_cate]

        # noinspection PyTypeChecker
        self.rec_list_var = tk.StringVar(value=r_rec_list())

        self.act_rec = {}

        self.cr_menubar()
        self.cr_fr_top()
        self.cr_fr_info()
        self.cr_fr_picture()
        self.fr_choose_rec()
        self.cr_fr_ingredients()
        self.cr_fr_preparation()
        self.cr_fr_bottom()
        self.set_but_state()
        self.root.mainloop()

    def ask_not_save(self):
        res = mbox.askquestion(r_data(lang, 'attention'), r_data(lang, 'warning'))
        if res == 'yes':
            self.save_new_rec()
            self.site_my_rec()
        elif res == 'no':
            self.site_my_rec()
            print("recipe not saved")

    def but_l_func(self):
        self.set_but_text()
        if ret_app_state() <= 1:
            self.set_but_state()
            self.site_new_rec()
        elif ret_app_state() == 2:
            self.set_but_state()
            self.save_new_rec()
        if ret_app_state() == 4:
            self.save_edi_rec()
            self.site_my_rec()

    def but_r_func(self):
        if ret_app_state() == 1:
            self.site_edit_rec()
        elif ret_app_state() == 2 or ret_app_state() == 4:
            self.ask_not_save()
        elif ret_app_state() == 3 or ret_app_state() == 5:
            self.site_my_rec()

    def clear_all_fields(self):
        for item in [self.en_name, self.en_port, self.en_time, self.en_cate, self.tf_ingr, self.tf_prep]:
            item.delete(0.1, 'end')

    def cr_menubar(self):
        menufont = r_data('fonts', 'Cal8')
        self.menubar = tk.Menu(self.root, font=menufont, bg=bg_app, fg=fg_app,
                               activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu.add_command(label=r_data(lang, 'new_rec'), command=self.site_new_rec)
        self.filemenu.add_command(label=r_data(lang, 'edit_rec'), command=self.site_edit_rec)
        self.filemenu.add_command(label=r_data(lang, 'quit'), command=self.quit_app)
        self.menubar.add_cascade(label=r_data(lang, 'file'), menu=self.filemenu)

        self.language_menu = tk.Menu(self.menubar, tearoff=1, font=menufont, bg=bg_app, fg=fg_app,
                                     activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.language_menu.add_command(label=r_data(lang, 'german'), command=lambda: self.set_language('de'))
        self.language_menu.add_command(label=r_data(lang, 'english'), command=lambda: self.set_language('en'))
        self.language_menu.add_command(label=r_data(lang, 'french'), command=lambda: self.set_language('fr'))
        self.menubar.add_cascade(label=r_data(lang, 'language'), menu=self.language_menu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.helpmenu.add_command(label=r_data(lang, 'about'))
        self.helpmenu.add_command(label=r_data(lang, 'help'))
        self.menubar.add_cascade(label=r_data(lang, 'help'), menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def cr_fr_bottom(self):
        self.logo_pic = tk.PhotoImage(file=pa_logo)
        self.fr_bottom = tk.Frame(width=1200, height=40, bg=bg_app)
        self.fr_bottom.place(x=0, y=560)
        self.la_logo = tk.Label(self.fr_bottom, image=self.logo_pic, bg=bg_app)
        self.la_logo.place(x=5, y=5)
        self.bu_bottom_l = tk.Button(self.fr_bottom, text=r_data(lang, 'new_rec'), bg=bg_app, fg=fg_app,
                                     width=25, activebackground=bg_act, activeforeground=fg_act,
                                     command=self.but_l_func)
        self.bu_bottom_l.place(x=700, y=5)
        self.bu_bottom_r = tk.Button(self.fr_bottom, text=r_data(lang, 'edit_rec'), bg=bg_app, fg=fg_app,
                                     width=25, activebackground=bg_act, activeforeground=fg_act,
                                     command=self.but_r_func)
        self.bu_bottom_r.place(x=950, y=5)

    def fr_choose_rec(self):
        self.fr_choose = tk.Frame(width=900, height=100, bg=bg_app)
        self.fr_choose.place(x=335, y=58)
        self.la_choos = tk.Label(self.fr_choose, text=r_data(lang, 'la_choos'),
                                 font=r_data('fonts', 'Cal10'),
                                 bg=bg_app, fg=fg_app)
        self.la_choos.place(x=5, y=0)
        self.lb_choose_rec = tk.Listbox(self.fr_choose, listvariable=self.rec_list_var, font=r_data('fonts', 'Cal8'),
                                        width=30, height=5, bg=bg_app, fg=fg_app, selectbackground=bg_act,
                                        selectforeground=fg_act, border=0)
        self.lb_choose_rec.place(x=5, y=20)
        self.lb_choose_rec.bind('<<ListboxSelect>>', self.rec_sel)

    def rec_sel(self, evt):
        global act_name, pa_act_info, pa_act_ingr, pa_act_reci, pa_act_pict
        if ret_app_state() == 0:
            set_app_state(1)
        self.set_but_state()
        act_name = (str((self.lb_choose_rec.get(self.lb_choose_rec.curselection()))))
        pa_act_info = ret_act_path(0)
        pa_act_ingr = ret_act_path(1)
        pa_act_reci = ret_act_path(2)
        pa_act_pict = ret_act_path(3)
        self.set_act_rec_pic()
        self.site_my_rec()

        print(evt)

    def fill_entry_fields(self):
        en_list = [self.en_name, self.en_port, self.en_time, self.en_cate]
        keylist = ['name', 'port', 'time', 'cat']
        for i in range(len(en_list)):
            en_list[i]['state'] = 'normal'
            en_list[i].delete(0.1, 'end')
            en_list[i].insert(0.1, ret_act_rec_data(keylist[i]))
            if ret_app_state() % 2 == 1:
                en_list[i]['state'] = 'disabled'
            else:
                en_list[i]['state'] = 'normal'

    def fill_tf_ingr(self):
        self.tf_ingr['state'] = 'normal'
        self.tf_ingr.delete(0.1, 'end')
        self.tf_ingr.insert(0.1, ret_act_ingr())
        self.tf_ingr['state'] = 'disabled'

    def fill_tf_prep(self):
        self.tf_prep['state'] = 'normal'
        self.tf_prep.delete(0.1, 'end')
        self.tf_prep.insert(0.1, ret_act_prep())
        self.tf_ingr['state'] = 'disabled'
        print('End of fill_tf_prep')

    def cr_en_info(self):
        self.en_name = tk.Text(self.fr_info, font=r_data('fonts', 'Cal12'), height=1, width=25,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_port = tk.Text(self.fr_info, font=r_data('fonts', 'Cal12'), height=1, width=30,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_time = tk.Text(self.fr_info, font=r_data('fonts', 'Cal12'), height=1, width=30,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_cate = tk.Text(self.fr_info, font=r_data('fonts', 'Cal12'), height=1, width=30,
                               bg=bg_app, fg=fg_app, relief='flat')
        y_var = 10
        for i in [self.en_name, self.en_port, self.en_time, self.en_cate]:
            i.place(x=100, y=y_var)
            y_var += 35

    def cr_fr_info(self):
        self.fr_info = tk.Frame(width=333, height=150, bg=bg_app)
        self.fr_info.place(x=0, y=58)
        self.cr_la_info()
        self.cr_en_info()

    def cr_fr_ingredients(self):
        self.fr_ingredients = tk.Frame(width=333, height=397, bg=bg_app)
        self.fr_ingredients.place(x=335, y=160)
        self.la_ingr = tk.Label(self.fr_ingredients, text=r_data(lang, 'la_ingr'),
                                font=r_data('fonts', 'Cal14'), bg=bg_app, fg=fg_app)
        self.la_ingr.place(x=5, y=5)
        self.tf_ingr = tk.Text(self.fr_ingredients, font=r_data('fonts', 'Cal10'),
                               height=20, width=40, bg=bg_app, fg=fg_app)
        self.tf_ingr.place(x=5, y=40)

    def cr_fr_picture(self):
        self.fr_pict = tk.Frame(width=333, height=347, bg=bg_app)
        self.fr_pict.place(x=0, y=210)
        tk.Frame(self.fr_pict, width=323, height=323, bg=bg_fra).place(x=5, y=12)
        act_pic = tk.Label(self.fr_pict, image=self.pi_rec_a, width=300, height=300)
        act_pic.place(x=15, y=23)

    def cr_fr_preparation(self):
        self.fr_preparation = tk.Frame(width=600, height=397, bg=bg_app)
        self.fr_preparation.place(x=670, y=160)
        self.la_prep = tk.Label(self.fr_preparation, text=r_data(lang, 'preparation'),
                                font=r_data('fonts', 'Cal14'), bg=bg_app, fg=fg_app)
        self.la_prep.place(x=5, y=5)
        self.tf_prep = tk.Text(self.fr_preparation, font=r_data('fonts', 'Cal10'),
                               height=20, width=60, bg=bg_app, fg=fg_app)
        self.tf_prep.place(x=5, y=40)

    def cr_fr_top(self):
        self.spoon_pic = tk.PhotoImage(file=pa_spoonpic)
        self.fr_top = tk.Frame(width=1200, height=55, bg=bg_app)
        self.fr_top.place(x=0, y=0)
        self.la_titel = tk.Label(self.fr_top, text=r_data(lang, 'la_titel'), font=r_data('fonts', 'Cal24'),
                                 bg=bg_app, fg=fg_app)
        self.la_titel.place(x=5, y=5)
        self.la_spoon = tk.Label(self.fr_top, image=self.spoon_pic, bg=bg_app)
        self.la_spoon.place(x=990, y=5)

    def cr_la_info(self):
        self.la_name = tk.Label(self.fr_info, text=r_data(lang, 'name'), font=r_data('fonts', 'Cal12'),
                                bg=bg_app, fg=fg_app)
        self.la_port = tk.Label(self.fr_info, text=r_data(lang, 'portions'), font=r_data('fonts', 'Cal12'),
                                bg=bg_app, fg=fg_app)
        self.la_time = tk.Label(self.fr_info, text=r_data(lang, 'time'), font=r_data('fonts', 'Cal12'),
                                bg=bg_app, fg=fg_app)
        self.la_cate = tk.Label(self.fr_info, text=r_data(lang, 'category'), font=r_data('fonts', 'Cal12'),
                                bg=bg_app, fg=fg_app)
        y_var = 10
        for i in [self.la_name, self.la_port, self.la_time, self.la_cate]:
            i.place(x=5, y=y_var)
            y_var += 35

    def save_edi_rec(self):
        f = open(pa_act_ingr, 'w')
        f.write(self.tf_ingr.get(0.1, 'end'))
        f.close()
        f = open(pa_act_reci, 'w')
        f.write(self.tf_prep.get(0.1, 'end'))
        f.close()
        dic = {'preparation': self.tf_prep.get(0.1, 'end')}
        print(dic['preparation'])

    def save_new_rec(self):
        set_app_state(3)
        self.site_my_rec()
        print("Recipe saved")

    def site_my_rec(self):
        self.la_titel['text'] = r_data(lang, 'la_titel')

        self.field_state(1)
        self.fill_entry_fields()
        self.fill_tf_ingr()
        self.fill_tf_prep()
        self.field_state(0)

        set_app_state(1)
        self.set_but_state()
        self.set_but_text()

        print('...end of site_my_rec function...')

    def site_new_rec(self):
        self.la_titel['text'] = r_data(lang, 'new_rec')

        self.field_state(1)
        self.clear_all_fields()
        set_app_state(2)
        self.set_but_text()
        self.set_but_state()

        print('...end of site_new_rec function...')

    def site_edit_rec(self):
        self.la_titel['text'] = r_data(lang, 'edit_rec')
        self.field_state(1)
        set_app_state(4)
        self.set_but_text()
        self.set_but_state()
        print('...end of site_edit_rec function...')

    def set_but_state(self):
        if ret_app_state() == 0:
            self.bu_bottom_r['state'] = 'disabled'
        else:
            self.bu_bottom_r['state'] = 'normal'

    def set_but_text(self):
        app_state = r_data('app', 'app_state')
        if app_state <= 1:
            self.bu_bottom_l['text'] = r_data(lang, 'new_rec')
            self.bu_bottom_r['text'] = r_data(lang, 'edit_rec')
        else:
            self.bu_bottom_l['text'] = r_data(lang, 'save')
            self.bu_bottom_r['text'] = r_data(lang, 'chancel')

    def set_label_text(self):
        self.root.title(r_data(lang, 'cookbook'))
        self.la_titel['text'] = r_data(lang, 'la_titel')
        self.la_choos['text'] = r_data(lang, 'la_choos')
        self.la_ingr['text'] = r_data(lang, 'la_ingr')
        self.la_prep['text'] = r_data(lang, 'preparation')

    def set_language(self, language):
        global lang, yes_var, no_var
        data_dict['app']['act_lang'] = language
        w_data_dict(str(data_dict))
        lang = r_data('app', 'act_lang')
        yes_var = r_data(lang, 'la_yes')
        no_var = r_data(lang, 'la_no')
        self.cr_menubar()
        self.set_but_text()
        self.set_label_text()

    def set_act_rec_pic(self):
        self.pi_rec_a['file'] = pa_rec + '/' + act_name + '.png'

    def field_state(self, s):
        for item in [self.en_name, self.en_port, self.en_time, self.en_cate, self.tf_ingr, self.tf_prep]:
            if s == 0:
                item['state'] = 'disabled'
            else:
                item['state'] = 'normal'

    def quit_app(self):
        set_app_state(0)
        self.root.quit()


if __name__ == '__main__':
    # define paths
    pa_app = str(pathlib.Path().absolute())
    pa_config = '/Cookbook/config/app_data.txt'
    pa_recipe = pa_app + r_data('paths', 'recipes')
    pa_rec = pa_app + r_data('paths', 'dir_recipe')
    pa_rec_d = pa_app + r_data('paths', 'rec_d')
    pa_startpic = pa_app + r_data('paths', 'startpic')
    pa_spoonpic = pa_app + r_data('paths', 'spoonpic')
    pa_logo = pa_app + r_data('paths', 'logo')

    # define the variables
    bg_app, bg_act, bg_fra, fg_app, fg_act = ('',) * 5  # colors
    lang = r_data('app', 'act_lang')
    data_dict = r_data_dict()
    act_name = ''
    yes_var = r_data(lang, 'la_yes')
    no_var = r_data(lang, 'la_no')

    pa_act_info = ret_act_path(0)
    pa_act_ingr = ret_act_path(1)
    pa_act_reci = ret_act_path(2)
    pa_act_pict = ret_act_path(3)
    # config the App
    set_colors('anthracite', 'black', 'lightgreen')

    # Start the App
    app = CB()
    app.quit_app()
