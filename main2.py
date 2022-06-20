#!/usr/bin/python3
import tkinter as tk
import json
import pathlib
import tkinter.messagebox as mbox


def a_app_data():
    global app_data
    app_data["app"] = {"act_lang": language}
    app_data["app"] = {"app_state": app_state}
    w_data(app_data)


def a_rec_data(key1):
    global rec_data
    rec_data[key1] = {"name": rec_name,
                      "port": rec_port,
                      "time": rec_time,
                      "reg": rec_reg,
                      "cat": rec_cat,
                      "ingr": rec_ingr,
                      "prep": rec_prep}
    w_data("rec")


def r_app_data():
    filename = 'config/app_data.json'

    filepath = pa_app + '/Cookbook/' + filename
    with open(filepath, 'r') as app_data_file:
        app_data_dict = json.load(app_data_file)
    return app_data_dict


def r_rec_data():
    filename = 'config/rec_data.json'
    filepath = pa_app + '/Cookbook/' + filename
    with open(filepath, 'r') as rec_data_file:
        rec_data_dict = json.load(rec_data_file)

    return rec_data_dict


def set_app_state(state):
    global app_data
    app_data['app']['app_state'] = state
    print("appdata", app_data)


def set_colors(b_app, b_fra, f_app):
    global bg_app, bg_act, bg_fra, fg_app, fg_act
    bg_app = app_data["color"][b_app]
    bg_act = app_data["color"][f_app]
    bg_fra = app_data["color"][b_fra]
    fg_app = app_data["color"][f_app]
    fg_act = app_data["color"][b_app]


def w_data(file):
    if file == "rec":
        with open('config/rec_data.json', 'w') as file:
            json.dump(rec_data, file)
    else:
        with open("config/app_data.json", "w") as file:
            print(app_data)
            json.dump(app_data, file)


class CB:
    def __init__(self):
        self.la_reg = None
        self.la_ingr, self.tf_ingr, self.tf_prep, self.la_prep = (None,) * 4
        self.la_name, self.la_port, self.la_time, self.la_cate = (None,) * 4
        self.en_name, self.en_port, self.en_time, self.en_cate, self.en_reg = (None,) * 5
        self.fr_preparation, self.fr_pict, self.fr_ingredients, self.fr_info = (None,) * 4
        self.fr_choose, self.la_choos, self.lb_choose_rec = (None,) * 3
        self.la_titel = None
        self.menubar, self.filemenu, self.helpmenu, self.language_menu = (None,) * 4

        self.root = tk.Tk()
        self.root.title(app_data[language]["cookbook"])
        self.root.config(width=1200, height=600, bg=fg_app)
        self.root.resizable(width=False, height=False)

        self.pi_rec_a = tk.PhotoImage(file=pa_startpic)
        self.logo_pic = tk.PhotoImage(file=pa_logo)
        self.spoon_pic = tk.PhotoImage(file=pa_spoonpic)

        # create all frames
        self.fr_bottom = tk.Frame(width=1200, height=40, bg=bg_app)
        self.fr_bottom.place(x=0, y=560)
        self.fr_top = tk.Frame(width=1200, height=55, bg=bg_app)
        self.fr_top.place(x=0, y=0)

        # create all Labels
        self.la_logo = tk.Label(self.fr_bottom, image=self.logo_pic, bg=bg_app)
        self.la_logo.place(x=5, y=5)
        self.la_titel = tk.Label(self.fr_top, text=app_data[language]["la_titel"], font=font24,
                                 bg=bg_app, fg=fg_app)
        self.la_titel.place(x=5, y=5)
        self.la_spoon = tk.Label(self.fr_top, image=self.spoon_pic, bg=bg_app)
        self.la_spoon.place(x=990, y=5)

        # create buttons
        self.bu_left = tk.Button(self.fr_bottom, text=app_data[language]['new_rec'], bg=bg_app, fg=fg_app,
                                 width=25, activebackground=bg_act, activeforeground=fg_act,
                                 command=self.but_l_func)
        self.bu_left.place(x=700, y=5)
        self.bu_right = tk.Button(self.fr_bottom, text=app_data[language]['edit_rec'], bg=bg_app, fg=fg_app,
                                  width=25, activebackground=bg_act, activeforeground=fg_act,
                                  command=self.but_r_func)
        self.bu_right.place(x=950, y=5)

        self.cr_menubar()
        self.cr_fr_info()
        self.cr_fr_picture()
        self.fr_choose_rec()
        self.cr_fr_ingredients()
        self.cr_fr_preparation()
        self.set_but_state()
        self.root.mainloop()

    def ask_not_save(self):
        res = mbox.askquestion(app_data[language]["attention"]), app_data[language]["warning"]
        if res == 'yes':
            self.save_new_rec()
            self.site_my_rec()
        elif res == 'no':
            self.site_my_rec()

    def but_l_func(self):
        self.set_but_text()
        if app_state <= 1:
            self.set_but_state()
            self.site_new_rec()
        elif app_state == 2:
            self.set_but_state()
            self.save_new_rec()
        if app_state == 4:
            self.save_edi_rec()
            self.site_my_rec()

    def but_r_func(self):
        if app_data["app"]["app_state"] == 1:
            self.site_edit_rec()
        elif app_state == 2 or app_state == 4:
            self.ask_not_save()
        elif app_state == 3 or app_state == 5:
            self.site_my_rec()

    def clear_all_fields(self):
        for item in [self.en_name, self.en_port, self.en_time, self.en_reg, self.en_cate, self.tf_ingr, self.tf_prep]:
            item.delete('0.1', 'end')

    def cr_menubar(self):
        menufont = font8
        self.menubar = tk.Menu(self.root, font=menufont, bg=bg_app, fg=fg_app,
                               activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu.add_command(label=app_data[language]["new_rec"], command=self.site_new_rec)
        self.filemenu.add_command(label=app_data[language]["edit_rec"], command=self.site_edit_rec)
        self.filemenu.add_command(label=app_data[language]["quit"], command=self.quit_app)
        self.menubar.add_cascade(label=app_data[language]["file"], menu=self.filemenu)

        self.language_menu = tk.Menu(self.menubar, tearoff=1, font=menufont, bg=bg_app, fg=fg_app,
                                     activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.language_menu.add_command(label=app_data[language]["german"], command=lambda: self.set_language('de'))
        self.language_menu.add_command(label=app_data[language]["english"], command=lambda: self.set_language('en'))
        self.language_menu.add_command(label=app_data[language]["french"], command=lambda: self.set_language('fr'))
        self.menubar.add_cascade(label=app_data[language]["language"], menu=self.language_menu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.helpmenu.add_command(label=app_data[language]['about'])
        self.helpmenu.add_command(label=app_data[language]['help'])
        self.menubar.add_cascade(label=app_data[language]['help'], menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def fr_choose_rec(self):
        self.fr_choose = tk.Frame(width=900, height=100, bg=bg_app)
        self.fr_choose.place(x=335, y=58)
        self.la_choos = tk.Label(self.fr_choose, text=app_data[language]['la_choos'],
                                 font=font10, bg=bg_app, fg=fg_app)
        self.la_choos.place(x=5, y=0)
        self.lb_choose_rec = tk.Listbox(self.fr_choose, font=font8,
                                        width=30, height=5, bg=bg_app, fg=fg_app, selectbackground=bg_act,
                                        selectforeground=fg_act, border=0)
        self.lb_choose_rec.place(x=5, y=20)
        self.insert_lbox_rec()
        self.lb_choose_rec.bind('<<ListboxSelect>>', self.rec_sel)

    def rec_sel(self, evt):
        global rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep
        if app_state == 0:
            set_app_state(1)
        self.set_but_state()
        rec_name = (str((self.lb_choose_rec.get(self.lb_choose_rec.curselection()))))
        rec_port = rec_data[rec_name]['port']
        rec_time = rec_data[rec_name]['time']
        rec_reg = rec_data[rec_name]['reg']
        rec_cat = rec_data[rec_name]['cat']
        rec_ingr = rec_data[rec_name]['ingr']
        rec_prep = rec_data[rec_name]['prep']
        self.set_act_rec_pic()
        self.fill_all_fields()
        print(evt)

    def fill_all_fields(self):
        en_list = [self.en_name, self.en_port, self.en_time, self.en_cate, self.en_reg, self.tf_ingr, self.tf_prep]
        keylist = ['name', 'port', 'time', 'cat', 'reg', 'ingr', 'prep']
        self.field_state(1)
        self.clear_all_fields()
        for i in range(len(en_list)):
            en_list[i].insert('0.1', rec_data[rec_name][keylist[i]])
        self.field_state(0)

    def cr_en_info(self):
        self.en_name = tk.Text(self.fr_info, font=font10, height=1, width=25,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_port = tk.Text(self.fr_info, font=font10, height=1, width=25,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_time = tk.Text(self.fr_info, font=font10, height=1, width=25,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_cate = tk.Text(self.fr_info, font=font10, height=1, width=25,
                               bg=bg_app, fg=fg_app, relief='flat')
        self.en_reg = tk.Text(self.fr_info, font=font10, height=1, width=25,
                              bg=bg_app, fg=fg_app, relief='flat')
        y_var = 10
        for i in [self.en_name, self.en_port, self.en_time, self.en_cate, self.en_reg]:
            i.place(x=100, y=y_var)
            y_var += 28

    def cr_fr_info(self):
        self.fr_info = tk.Frame(width=333, height=150, bg=bg_app)
        self.fr_info.place(x=0, y=58)
        self.cr_la_info()
        self.cr_en_info()

    def cr_fr_ingredients(self):
        self.fr_ingredients = tk.Frame(width=333, height=397, bg=bg_app)
        self.fr_ingredients.place(x=335, y=160)
        self.la_ingr = tk.Label(self.fr_ingredients, text=app_data[language]["la_ingr"],
                                font=font14, bg=bg_app, fg=fg_app)
        self.la_ingr.place(x=5, y=5)
        self.tf_ingr = tk.Text(self.fr_ingredients, font=font10,
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
        self.la_prep = tk.Label(self.fr_preparation, text=app_data[language]["preparation"],
                                font=font14, bg=bg_app, fg=fg_app)
        self.la_prep.place(x=5, y=5)
        self.tf_prep = tk.Text(self.fr_preparation, font=font10, height=20, width=60, bg=bg_app, fg=fg_app)
        self.tf_prep.place(x=5, y=40)

    def cr_la_info(self):
        self.la_name = tk.Label(self.fr_info, text=app_data[language]["name"], font=font10,
                                bg=bg_app, fg=fg_app)
        self.la_port = tk.Label(self.fr_info, text=app_data[language]["portions"], font=font10,
                                bg=bg_app, fg=fg_app)
        self.la_time = tk.Label(self.fr_info, text=app_data[language]["time"], font=font10,
                                bg=bg_app, fg=fg_app)
        self.la_cate = tk.Label(self.fr_info, text=app_data[language]["category"], font=font10,
                                bg=bg_app, fg=fg_app)
        self.la_reg = tk.Label(self.fr_info, text=app_data[language]["region"], font=font10,
                               bg=bg_app, fg=fg_app)

        y_var = 10
        for i in [self.la_name, self.la_port, self.la_time, self.la_cate, self.la_reg]:
            i.place(x=5, y=y_var)
            y_var += 28

    def insert_lbox_rec(self):
        rec_list = list(rec_data.keys())
        rec_list.sort()
        for index in range(len(rec_list)):
            self.lb_choose_rec.insert(index, rec_list[index])

    def save_edi_rec(self):
        self.site_my_rec()
        print("Recipe saved")

    def save_new_rec(self):
        self.site_my_rec()
        print("Recipe saved")

    def site_my_rec(self):
        self.la_titel['text'] = app_data[language]["la_titel"]

        self.field_state(1)
        self.fill_all_fields()
        self.field_state(0)

        set_app_state(1)
        self.set_but_state()
        self.set_but_text()

        print('...end of site_my_rec function...')

    def site_new_rec(self):
        self.la_titel['text'] = app_data[language]["new_rec"]

        self.field_state(1)
        self.clear_all_fields()
        set_app_state(2)
        self.set_but_text()
        self.set_but_state()

        print('...end of site_new_rec function...')

    def site_edit_rec(self):
        self.la_titel['text'] = app_data[language]["edit_rec"]
        self.field_state(1)
        set_app_state(4)
        self.set_but_text()
        self.set_but_state()
        print('...end of site_edit_rec function...')

    def set_but_state(self):
        if app_data["app"]["app_state"] == 0:
            self.bu_right['state'] = 'disabled'
        else:
            self.bu_right['state'] = 'normal'

    def set_but_text(self):
        if app_state <= 1:
            self.bu_left['text'] = app_data[language]["new_rec"]
            self.bu_right['text'] = app_data[language]["edit_rec"]
        else:
            self.bu_left['text'] = app_data[language]["save"]
            self.bu_right['text'] = app_data[language]["chancel"]

    def set_label_text(self):
        self.root.title(app_data[language]["cookbook"])
        self.la_titel['text'] = app_data[language]["la_titel"]
        self.la_choos['text'] = app_data[language]["la_choos"]
        self.la_ingr['text'] = app_data[language]["la_ingr"]
        self.la_prep['text'] = app_data[language]["preparation"]

    def set_language(self, lang):
        global language
        app_data['app']['act_lang'] = lang
        language = app_data["app"]["act_lang"]
        self.cr_menubar()
        self.set_but_text()
        self.set_label_text()

    def set_act_rec_pic(self):
        self.pi_rec_a['file'] = pa_app + '/Cookbook/Bilder/' + rec_name + '.png'

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
    app_data = r_app_data()
    app_state = app_data["app"]["app_state"]
    rec_data = r_rec_data()

    pa_startpic = pa_app + app_data['paths']['startpic']
    pa_spoonpic = pa_app + app_data['paths']['spoonpic']
    pa_logo = pa_app + app_data['paths']['logo']

    # define the variables
    bg_app, bg_act, bg_fra, fg_app, fg_act = ('',) * 5  # colors
    language = app_data['app']['act_lang']
    rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep = ('',) * 7

    font24 = ("Calibri", 24)
    font18 = ("Calibri", 18)
    font14 = ("Calibri", 14)
    font10 = ("Calibri", 10)
    font8 = ("Calibri", 8)

    # config the App
    set_colors('anthracite', 'black', 'lightgreen')

    # Start the App
    app = CB()
    app.quit_app()
