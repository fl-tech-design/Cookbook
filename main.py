#!/usr/bin/python3
import tkinter as tk
import json
import pathlib
import os
import tkinter.messagebox as mbox


def check_picture():
    act_pic_file = pa_pic + rec_name + ".png"
    return os.path.isfile(act_pic_file)


def clear_lbox(lbox):
    lbox.delete("0", "end")


def r_data(data):
    if data == 0:
        filepath = pa_app_data
    else:
        filepath = pa_rec_data
    with open(filepath, "r") as app_data_file:
        app_data_dict = json.load(app_data_file)
    return app_data_dict


def ret_act_pic_path():
    act_pic_path = pa_app + "/Cookbook/Bilder/" + rec_name + ".png"
    return act_pic_path


def load_rec_data():
    global rec_data
    rec_data = r_data(1)


def load_rec_list():
    global rec_list
    rec_list = list(rec_data.keys())
    rec_list.sort()


def set_app_state(state):
    global app_data
    app_data["app"]["app_state"] = state
    w_data("app")


def set_save_state(state):
    global app_data
    app_data["app"]["save_state"] = state
    w_data("app")


def set_colors(b_app, b_fra, f_app):
    global bg_app, bg_act, bg_fra, fg_app, fg_act
    bg_app = app_data["color"][b_app]
    bg_act = app_data["color"][f_app]
    bg_fra = app_data["color"][b_fra]
    fg_app = app_data["color"][f_app]
    fg_act = app_data["color"][b_app]


def w_data(file):
    if file == "rec":
        with open(pa_rec_data, "w") as file:
            json.dump(rec_data, file)
    else:
        with open(pa_app_data, "w") as file:
            json.dump(app_data, file)


class CB:
    def __init__(self):
        self.menubar, self.filemenu, self.helpmenu, self.language_menu = (None,) * 4
        # create mainwindow
        self.root = tk.Tk()
        self.root.title(app_data[language]["cookbook"])
        self.root.config(width=1200, height=600, bg=fg_app)
        self.root.resizable(width=False, height=False)
        # define pictures
        self.act_rec_pic = tk.PhotoImage(file=pa_startpic)
        self.logo_pic = tk.PhotoImage(file=pa_logo)
        self.spoon_pic = tk.PhotoImage(file=pa_spoonpic)
        # create frames
        self.fr_bott = tk.Frame(self.root, width=1200, height=40, bg=bg_app)
        self.fr_choo = tk.Frame(self.root, width=900, height=100, bg=bg_app)
        self.fr_ingr = tk.Frame(self.root, width=329, height=397, bg=bg_app)
        self.fr_info = tk.Frame(self.root, width=333, height=150, bg=bg_app)
        self.fr_pic = tk.Frame(self.root, width=333, height=347, bg=bg_app)
        self.fr_prep = tk.Frame(self.root, width=600, height=397, bg=bg_app)
        self.fr_top = tk.Frame(self.root, width=1200, height=55, bg=bg_app)
        # place frames
        fr_list = [self.fr_bott, self.fr_choo, self.fr_ingr, self.fr_info, self.fr_prep, self.fr_top, self.fr_pic]
        fr_x = [0, 335, 335, 0, 666, 0, 0]
        fr_y = [560, 58, 160, 58, 160, 0, 210]
        for index in range(len(fr_list)):
            fr_list[index].place(x=fr_x[index], y=fr_y[index])
        tk.Frame(self.fr_pic, width=323, height=323, bg=bg_fra).place(x=5, y=12)
        # create Labels
        self.la_time = tk.Label(self.fr_info, text=app_data[language]["time"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_cate = tk.Label(self.fr_info, text=app_data[language]["category"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_choos = tk.Label(self.fr_choo, text=app_data[language]["la_choos"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_reg = tk.Label(self.fr_info, text=app_data[language]["region"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_ingr = tk.Label(self.fr_ingr, text=app_data[language]["la_ingr"], font=fonts[1], bg=bg_app, fg=fg_app)
        self.la_logo = tk.Label(self.fr_bott, image=self.logo_pic, bg=bg_app)
        self.la_name = tk.Label(self.fr_info, text=app_data[language]["name"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_pic = tk.Label(self.fr_pic, image=self.act_rec_pic, text=app_data[language]["la_choos"], bg=bg_app,
                               fg=fg_app, compound="center", width=300, height=300)
        self.la_port = tk.Label(self.fr_info, text=app_data[language]["portions"], font=fonts[2], bg=bg_app, fg=fg_app)
        self.la_prep = tk.Label(self.fr_prep, text=app_data[language]["preparation"], font=fonts[1], bg=bg_app,
                                fg=fg_app)
        self.la_titel = tk.Label(self.fr_top, text=app_data[language]["la_titel"], font=fonts[0], bg=bg_app, fg=fg_app)
        self.la_spoon = tk.Label(self.fr_top, image=self.spoon_pic, bg=bg_app)
        # place labels
        self.la_list = [self.la_choos, self.la_ingr, self.la_prep, self.la_titel, self.la_name, self.la_port,
                        self.la_time, self.la_cate, self.la_reg, self.la_logo, self.la_pic, self.la_spoon]
        la_x = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 990]
        la_y = [0, 5, 5, 5, 10, 38, 66, 94, 122, 5, 22, 5]
        for i in range(len(self.la_list)):
            self.la_list[i].place(x=la_x[i], y=la_y[i])

        # create textfields
        self.tf_name = tk.Text(self.fr_info, font=fonts[2], height=1, width=25, bg=bg_app, fg=fg_app,
                               insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                               inactiveselectbackground=fg_app)
        self.tf_port = tk.Text(self.fr_info, font=fonts[2], height=1, width=25, bg=bg_app, fg=fg_app,
                               insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                               inactiveselectbackground=fg_app)
        self.tf_time = tk.Text(self.fr_info, font=fonts[2], height=1, width=25, bg=bg_app, fg=fg_app,
                               insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                               inactiveselectbackground=fg_app)
        self.tf_cat = tk.Text(self.fr_info, font=fonts[2], height=1, width=25, bg=bg_app, fg=fg_app,
                              insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                              inactiveselectbackground=fg_app)
        self.tf_reg = tk.Text(self.fr_info, font=fonts[2], height=1, width=25, bg=bg_app, fg=fg_app,
                              insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                              inactiveselectbackground=fg_app)
        self.tf_ingr = tk.Text(self.fr_ingr, font=fonts[2], height=20, width=39, bg=bg_app, fg=fg_app,
                               insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                               inactiveselectbackground=fg_app)
        self.tf_prep = tk.Text(self.fr_prep, font=fonts[2], height=20, width=65, bg=bg_app, fg=fg_app,
                               insertbackground=fg_app, highlightthickness=0, borderwidth=0,
                               inactiveselectbackground=fg_app)

        # place textfields
        self.tf_list = [self.tf_port, self.tf_time, self.tf_cat, self.tf_reg, self.tf_ingr, self.tf_prep, self.tf_name]
        self.tf_keys = ["port", "time", "cat", "reg", "ingr", "prep", "name"]

        tf_x = [100, 100, 100, 100, 5, 5, 100]
        tf_y = [38, 66, 94, 122, 40, 40, 10]
        for i in range(len(self.tf_list)):
            self.tf_list[i].place(x=tf_x[i], y=tf_y[i])
        # create buttons
        self.bu_del = tk.Button(self.fr_bott, text=app_data[language]["del_rec"], bg=bg_app, fg=fg_app, font=fonts[2],
                                width=13, activebackground=bg_act, activeforeground=fg_act, relief="sunken",
                                command=lambda: self.delete_rec(rec_name), state="disabled", highlightthickness=0,
                                borderwidth=0)
        self.bu_left = tk.Button(self.fr_bott, text=app_data[language]["new_rec"], bg=bg_app, fg=fg_app, font=fonts[2],
                                 width=13, activebackground=bg_act, activeforeground=fg_act, relief="sunken",
                                 command=self.but_l_func, highlightthickness=0, borderwidth=0)
        self.bu_right = tk.Button(self.fr_bott, text=app_data[language]["edit_rec"], bg=bg_app, fg=fg_app,
                                  font=fonts[2],
                                  width=13, activebackground=bg_act, activeforeground=fg_act, relief="sunken",
                                  command=self.but_r_func, state="disabled", highlightthickness=0, borderwidth=0)
        # place buttons
        but_x = 750
        for button in [self.bu_left, self.bu_right, self.bu_del]:
            button.place(x=but_x, y=5)
            but_x += 150
        # create listboxes
        self.lb_choose_rec = tk.Listbox(self.fr_choo, font=fonts[3],
                                        width=30, height=5, bg=bg_app, fg=fg_app, selectbackground=bg_act,
                                        selectforeground=fg_act, highlightthickness=0)
        self.lb_choose_rec.place(x=5, y=22)
        self.insert_lbox_rec()
        self.lb_choose_rec.bind("<<ListboxSelect>>", self.sel_rec)

        self.set_but_state(0)
        self.cr_menubar()
        self.root.mainloop()

    def ask_ok_or(self):
        ans = mbox.askokcancel("warning", "Sie haben noch nicht gespeichert")
        if ans:
            self.save_rec()
            self.site_my_rec()
        else:
            self.site_my_rec()

    def but_l_func(self):
        if app_data["app"]["app_state"] <= 1:
            self.site_new_rec()
        elif app_data["app"]["app_state"] >= 2:
            self.save_rec()
            self.site_my_rec()

    def but_r_func(self):
        if app_data["app"]["app_state"] == 1:
            self.site_edit_rec()
        elif app_data["app"]["app_state"] >= 2:
            if app_data["app"]["save_state"] == 1:
                self.ask_ok_or()
            else:
                self.site_my_rec()

    def clear_all_fields(self):
        self.tf_state(1)
        for item in self.tf_list:
            item.delete("0.1", "end")
        self.tf_state(0)

    def cr_menubar(self):
        menufont = fonts[3]
        self.menubar = tk.Menu(self.root, font=menufont, bg=bg_app, fg=fg_app,
                               activebackground=bg_act, activeforeground=fg_act, relief="flat")
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief="flat")
        self.filemenu.add_command(label=app_data[language]["new_rec"], command=self.site_new_rec)
        self.filemenu.add_command(label=app_data[language]["edit_rec"], command=self.site_edit_rec)
        self.filemenu.add_command(label=app_data[language]["quit"], command=self.quit_app)
        self.menubar.add_cascade(label=app_data[language]["file"], menu=self.filemenu)

        self.language_menu = tk.Menu(self.menubar, tearoff=1, font=menufont, bg=bg_app, fg=fg_app,
                                     activebackground=bg_act, activeforeground=fg_act, relief="flat")
        self.language_menu.add_command(label=app_data[language]["german"], command=lambda: self.set_language("de"))
        self.language_menu.add_command(label=app_data[language]["english"], command=lambda: self.set_language("en"))
        self.language_menu.add_command(label=app_data[language]["french"], command=lambda: self.set_language("fr"))
        self.menubar.add_cascade(label=app_data[language]["language"], menu=self.language_menu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief="flat")
        self.helpmenu.add_command(label=app_data[language]["about"])
        self.helpmenu.add_command(label=app_data[language]["help"])
        self.menubar.add_cascade(label=app_data[language]["help"], menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def delete_rec(self, recipename):
        global rec_data
        del rec_data[recipename]
        w_data("rec")
        rec_data = r_data(1)
        self.insert_lbox_rec()
        self.clear_all_fields()

    def fill_all_fields(self):
        global rec_name
        self.clear_all_fields()
        self.tf_state(1)
        if rec_name == "":
            rec_name = rec_list[0]
            for i in range(len(self.tf_list)):
                self.tf_list[i].insert("0.1", rec_data[rec_name][self.tf_keys[i]])
        else:
            for i in range(len(self.tf_list)):
                self.tf_list[i].insert("0.1", rec_data[rec_name][self.tf_keys[i]])
        self.tf_state(0)

    def insert_lbox_rec(self):
        load_rec_list()
        clear_lbox(self.lb_choose_rec)
        for index in range(len(rec_list)):
            self.lb_choose_rec.insert(index, rec_list[index])

    def save_rec(self):
        global rec_data
        rec_data[self.tf_list[6].get("0.1", "end-1c")] = {"name": self.tf_name.get("0.1", "end-1c")}
        for i in range(len(self.tf_list) - 1):
            rec_data[self.tf_list[6].get("0.1", "end-1c")][self.tf_keys[i]] = self.tf_list[i].get("0.1", "end-1c")
        w_data("rec")
        self.insert_lbox_rec()
        set_save_state(0)
        self.site_my_rec()

    def sel_rec(self, evt):
        set_app_state(1)
        self.set_but_state(3)
        self.la_pic["text"] = ""
        self.set_rec_data()
        self.show_rec_pic()
        self.fill_all_fields()
        self.site_my_rec()
        print(evt)

    def set_but_state(self, int_state):
        if int_state == 0:
            self.bu_right["state"] = "disabled"
            self.bu_del["state"] = "disabled"
        elif int_state == 1:
            self.bu_right["state"] = "normal"
            self.bu_del["state"] = "disabled"
        elif int_state == 2:
            self.bu_right["state"] = "disabled"
            self.bu_del["state"] = "normal"
        elif int_state == 3:
            self.bu_right["state"] = "normal"
            self.bu_del["state"] = "normal"

    def set_but_text(self):
        self.bu_del["text"] = app_data[language]["del_rec"]
        if app_data["app"]["app_state"] <= 1:
            self.bu_left["text"] = app_data[language]["new_rec"]
            self.bu_right["text"] = app_data[language]["edit_rec"]
        else:
            self.bu_left["text"] = app_data[language]["save"]
            self.bu_right["text"] = app_data[language]["chancel"]

    def set_label_text(self):
        labelnames = ["la_choos", "la_ingr", "preparation", "la_titel", "name", "portions", "time", "category",
                      "region"]
        self.root.title(app_data[language]["cookbook"])
        for i in range(len(self.la_list) - 3):
            self.la_list[i]["text"] = app_data[language][labelnames[i]]
        if app_data["app"]["app_state"] == 0:
            self.la_pic["text"] = app_data[language]["pls_choose"]
        elif app_data["app"]["app_state"] >= 1:
            self.la_pic["text"] = app_data[language]["photo_ins"]

    def set_language(self, lang):
        global language
        app_data["app"]["act_lang"] = lang
        language = app_data["app"]["act_lang"]
        self.cr_menubar()
        self.set_but_text()
        self.set_label_text()

    def set_rec_data(self):
        global rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep
        rec_name = (str((self.lb_choose_rec.get(self.lb_choose_rec.curselection()))))
        rec_port = rec_data[rec_name]["port"]
        rec_time = rec_data[rec_name]["time"]
        rec_reg = rec_data[rec_name]["reg"]
        rec_cat = rec_data[rec_name]["cat"]
        rec_ingr = rec_data[rec_name]["ingr"]
        rec_prep = rec_data[rec_name]["prep"]

    def site_my_rec(self):
        set_app_state(1)
        self.la_titel["text"] = app_data[language]["la_titel"]
        if app_data["app"]["app_state"] > 0:
            self.fill_all_fields()
            self.set_but_state(3)
        self.set_but_text()

    def site_new_rec(self):
        set_app_state(2)
        set_save_state(1)
        self.set_but_state(1)
        self.la_titel["text"] = app_data[language]["new_rec"]
        self.show_info_pic()
        self.clear_all_fields()
        self.tf_state(1)
        self.set_but_text()

    def site_edit_rec(self):
        set_app_state(3)
        self.set_but_state(3)
        self.la_titel["text"] = app_data[language]["edit_rec"]
        self.set_but_text()
        self.tf_state(1)


    def show_rec_pic(self):
        if check_picture():
            self.act_rec_pic["file"] = ret_act_pic_path()
        else:
            self.show_info_pic()

    def show_info_pic(self):
        self.act_rec_pic["file"] = pa_startpic
        self.la_pic["text"] = app_data[language]["photo_ins"]

    def tf_state(self, s):
        for i in range(len(self.tf_list)):
            if s == 0:
                self.tf_list[i]["state"] = "disabled"
                self.tf_list[i]["borderwidth"] = 0
            else:
                self.tf_list[i]["state"] = "normal"
                self.tf_list[i]["borderwidth"] = 1

    def quit_app(self):
        set_app_state(0)
        self.root.quit()


if __name__ == "__main__":
    # define paths
    pa_app = str(pathlib.Path().absolute())
    pa_pic = pa_app + "/Cookbook/Bilder/"
    pa_app_data = pa_app + "/Cookbook/config/app_data.json"
    pa_rec_data = pa_app + "/Cookbook/config/rec_data.json"
    # load files and set language
    app_data = r_data(0)
    rec_data = {}
    load_rec_data()
    rec_list = []
    load_rec_list()
    language = app_data["app"]["act_lang"]
    # define picture paths
    pa_startpic = pa_app + app_data["paths"]["startpic"]
    pa_spoonpic = pa_app + app_data["paths"]["spoonpic"]
    pa_logo = pa_app + app_data["paths"]["logo"]
    # define the global variables
    bg_app, bg_act, bg_fra, fg_app, fg_act = ("",) * 5  # colors
    rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep = ("",) * 7
    # define fonts
    fonts = [("Calibri", 24), ("Calibri", 14), ("Calibri", 10), ("Calibri", 8)]
    # config the App
    set_colors("anthracite", "black", "lightgreen")
    # Start the App
    app = CB()
    app.quit_app()
