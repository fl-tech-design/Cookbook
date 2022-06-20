#!/usr/bin/python3
import tkinter as tk
import json
import pathlib
import tkinter.messagebox as mbox


def r_data(data):
    if data == 0:
        filepath = pa_app_data
    else:
        filepath = pa_rec_data
    with open(filepath, "r") as app_data_file:
        app_data_dict = json.load(app_data_file)
    return app_data_dict


def set_app_state(state):
    global app_data
    app_data["app"]["app_state"] = state
    print("appstate", app_data["app"]["app_state"])
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
        self.pi_rec_a = tk.PhotoImage(file=pa_startpic)
        self.logo_pic = tk.PhotoImage(file=pa_logo)
        self.spoon_pic = tk.PhotoImage(file=pa_spoonpic)
        # create frames
        self.fr_bott = tk.Frame(self.root, width=1200, height=40, bg=bg_app)
        self.fr_choo = tk.Frame(self.root, width=900, height=100, bg=bg_app)
        self.fr_ingr = tk.Frame(self.root, width=333, height=397, bg=bg_app)
        self.fr_info = tk.Frame(self.root, width=333, height=150, bg=bg_app)
        self.fr_pic = tk.Frame(self.root, width=333, height=333, bg=bg_app)
        self.fr_prep = tk.Frame(self.root, width=600, height=397, bg=bg_app)
        self.fr_top = tk.Frame(self.root, width=1200, height=55, bg=bg_app)
        # place frames
        fr_list = [self.fr_bott, self.fr_choo, self.fr_ingr, self.fr_info, self.fr_prep, self.fr_top, self.fr_pic]
        fr_x = [0, 335, 335, 0, 670, 0, 0]
        fr_y = [560, 58, 160, 58, 160, 0, 220]
        for index in range(len(fr_list)):
            fr_list[index].place(x=fr_x[index], y=fr_y[index])
        tk.Frame(self.fr_pic, width=323, height=323, bg=bg_fra).place(x=5, y=12)

        # create Labels
        self.la_time = tk.Label(self.fr_info, text=app_data[language]["time"], font=font10, bg=bg_app, fg=fg_app)
        self.la_cate = tk.Label(self.fr_info, text=app_data[language]["category"], font=font10, bg=bg_app, fg=fg_app)
        self.la_choos = tk.Label(self.fr_choo, text=app_data[language]["la_choos"], font=font10, bg=bg_app, fg=fg_app)
        self.la_reg = tk.Label(self.fr_info, text=app_data[language]["region"], font=font10, bg=bg_app, fg=fg_app)
        self.la_ingr = tk.Label(self.fr_ingr, text=app_data[language]["la_ingr"], font=font14, bg=bg_app, fg=fg_app)
        self.la_logo = tk.Label(self.fr_bott, image=self.logo_pic, bg=bg_app)
        self.la_name = tk.Label(self.fr_info, text=app_data[language]["name"], font=font10, bg=bg_app, fg=fg_app)
        self.la_pic = tk.Label(self.fr_pic, image=self.pi_rec_a, width=300, height=300)
        self.la_port = tk.Label(self.fr_info, text=app_data[language]["portions"], font=font10, bg=bg_app, fg=fg_app)
        self.la_prep = tk.Label(self.fr_prep, text=app_data[language]["preparation"], font=font14, bg=bg_app, fg=fg_app)
        self.la_titel = tk.Label(self.fr_top, text=app_data[language]["la_titel"], font=font24, bg=bg_app, fg=fg_app)
        self.la_spoon = tk.Label(self.fr_top, image=self.spoon_pic, bg=bg_app)
        # place labels
        la_list = [self.la_choos, self.la_logo, self.la_ingr, self.la_prep, self.la_titel, self.la_pic, self.la_spoon]
        la_x = [5, 5, 5, 5, 5, 15, 990]
        la_y = [0, 5, 5, 5, 5, 23, 5]
        for i in range(len(la_list)):
            la_list[i].place(x=la_x[i], y=la_y[i])
        y_la_info = 10
        for la_info in [self.la_name, self.la_port, self.la_time, self.la_cate, self.la_reg]:
            la_info.place(x=5, y=y_la_info)
            y_la_info += 28
        # create textfields
        self.tf_cat = tk.Text(self.fr_info, font=font10, height=1, width=25, bg=bg_app, fg=fg_app, relief="flat")
        self.tf_ingr = tk.Text(self.fr_ingr, font=font10, height=20, width=40, bg=bg_app, fg=fg_app)
        self.tf_name = tk.Text(self.fr_info, font=font10, height=1, width=25, bg=bg_app, fg=fg_app, relief="flat")
        self.tf_time = tk.Text(self.fr_info, font=font10, height=1, width=25, bg=bg_app, fg=fg_app, relief="flat")
        self.tf_port = tk.Text(self.fr_info, font=font10, height=1, width=25, bg=bg_app, fg=fg_app, relief="flat")
        self.tf_prep = tk.Text(self.fr_prep, font=font10, height=20, width=60, bg=bg_app, fg=fg_app)
        self.tf_reg = tk.Text(self.fr_info, font=font10, height=1, width=25, bg=bg_app, fg=fg_app, relief="flat")
        # place textfields
        self.tf_ingr.place(x=5, y=40)
        self.tf_prep.place(x=5, y=40)
        y_tf_info = 10
        for tf_info in [self.tf_name, self.tf_port, self.tf_time, self.tf_cat, self.tf_reg]:
            tf_info.place(x=100, y=y_tf_info)
            y_tf_info += 28
        # create buttons
        self.bu_left = tk.Button(self.fr_bott, text=app_data[language]["new_rec"], bg=bg_app, fg=fg_app,
                                 width=25, activebackground=bg_act, activeforeground=fg_act,
                                 command=self.but_l_func)
        self.bu_right = tk.Button(self.fr_bott, text=app_data[language]["edit_rec"], bg=bg_app, fg=fg_app,
                                  width=25, activebackground=bg_act, activeforeground=fg_act,
                                  command=self.but_r_func, state="disabled")
        # place buttons
        self.bu_left.place(x=700, y=5)
        self.bu_right.place(x=950, y=5)
        # create listboxes
        self.lb_choose_rec = tk.Listbox(self.fr_choo, font=font8,
                                        width=30, height=5, bg=bg_app, fg=fg_app, selectbackground=bg_act,
                                        selectforeground=fg_act, border=0)
        self.lb_choose_rec.place(x=5, y=20)
        self.insert_lbox_rec()
        self.lb_choose_rec.bind('<<ListboxSelect>>', self.rec_sel)

        self.cr_menubar()
        self.root.mainloop()

    def ask_not_save(self):
        res = mbox.askokcancel(app_data[language]["attention"]), app_data[language]["warning"]
        print(res)
        if res:
            self.save_rec()
            self.site_my_rec()
        else:
            self.site_my_rec()

    def but_l_func(self):
        print("appstate from leftbutton ", app_data["app"]["app_state"])
        if app_data["app"]["app_state"] <= 1:
            self.site_new_rec()
        elif app_data["app"]["app_state"] == 2:
            self.save_rec()
        elif app_data["app"]["app_state"] == 3:
            self.save_rec()
            self.site_my_rec()

    def but_r_func(self):
        if app_data["app"]["app_state"] == 1:
            self.site_edit_rec()
        elif app_data["app"]["app_state"] == 2:
            self.ask_not_save()
        elif app_data["app"]["app_state"] == 3:
            self.site_my_rec()

    def clear_all_fields(self):
        for item in [self.tf_name, self.tf_port, self.tf_time, self.tf_reg, self.tf_cat, self.tf_ingr, self.tf_prep]:
            item.delete("0.1", "end")

    def cr_menubar(self):
        menufont = font8
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

    def rec_sel(self, evt):
        global rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep
        if app_data["app"]["app_state"] == 0:
            set_app_state(1)
            self.set_but_state(1)
        rec_name = (str((self.lb_choose_rec.get(self.lb_choose_rec.curselection()))))
        rec_port = rec_data[rec_name]["port"]
        rec_time = rec_data[rec_name]["time"]
        rec_reg = rec_data[rec_name]["reg"]
        rec_cat = rec_data[rec_name]["cat"]
        rec_ingr = rec_data[rec_name]["ingr"]
        rec_prep = rec_data[rec_name]["prep"]
        self.show_rec_pic()
        self.fill_all_fields()
        print(evt)

    def fill_all_fields(self):
        en_list = [self.tf_name, self.tf_port, self.tf_time, self.tf_cat, self.tf_reg, self.tf_ingr, self.tf_prep]
        keylist = ["name", "port", "time", "cat", "reg", "ingr", "prep"]
        self.field_state(1)
        self.clear_all_fields()
        for i in range(len(en_list)):
            en_list[i].insert("0.1", rec_data[rec_name][keylist[i]])
        self.field_state(0)

    def insert_lbox_rec(self):
        rec_list = list(rec_data.keys())
        rec_list.sort()
        for index in range(len(rec_list)):
            self.lb_choose_rec.insert(index, rec_list[index])

    def save_rec(self):
        rec_data[self.tf_name.get("0.1", "end-1c")] = {"name": self.tf_name.get("0.1", "end-1c")}
        rec_data[self.tf_name.get("0.1", "end-1c")]["port"] = self.tf_port.get("0.1", "end-1c")
        rec_data[self.tf_name.get("0.1", "end-1c")]["time"] = self.tf_time.get("0.1", "end-1c")
        rec_data[self.tf_name.get("0.1", "end-1c")]["cat"] = self.tf_cat.get("0.1", "end-1c")
        rec_data[self.tf_name.get("0.1", "end-1c")]["reg"] = self.tf_reg.get("0.1", "end-1c")
        rec_data[self.tf_name.get("0.1", "end-1c")]["ingr"] = self.tf_ingr.get("0.1", "end-1c")
        rec_data[self.tf_name.get("0.1", "end-1c")]["prep"] = self.tf_prep.get("0.1", "end-1c")
        w_data("rec")
        self.insert_lbox_rec()
        self.site_my_rec()
        print("Recipe saved")

    def site_my_rec(self):
        self.set_but_text()
        self.la_titel["text"] = app_data[language]["la_titel"]
        if app_data["app"]["app_state"] > 0:
            self.field_state(1)
            # self.fill_all_fields()
            self.field_state(0)
        self.set_but_text()
        print("...end of site_my_rec function...")

    def site_new_rec(self):
        set_app_state(2)
        self.la_titel["text"] = app_data[language]["new_rec"]
        self.field_state(1)
        self.clear_all_fields()
        self.set_but_text()
        print("...end of site_new_rec function...")

    def site_edit_rec(self):
        set_app_state(3)

        self.la_titel["text"] = app_data[language]["edit_rec"]
        self.field_state(1)
        self.set_but_text()
        print("...end of site_edit_rec function...")

    def set_but_state(self, state):
        if state == 0:
            self.bu_right["state"] = "disabled"
        else:
            self.bu_right["state"] = "normal"

    def set_but_text(self):
        if app_data["app"]["app_state"] <= 1:
            self.bu_left["text"] = app_data[language]["new_rec"]
            self.bu_right["text"] = app_data[language]["edit_rec"]
        else:
            self.bu_left["text"] = app_data[language]["save"]
            self.bu_right["text"] = app_data[language]["chancel"]

    def set_label_text(self):
        self.root.title(app_data[language]["cookbook"])
        self.la_titel["text"] = app_data[language]["la_titel"]
        self.la_choos["text"] = app_data[language]["la_choos"]
        self.la_ingr["text"] = app_data[language]["la_ingr"]
        self.la_prep["text"] = app_data[language]["preparation"]

    def set_language(self, lang):
        global language
        app_data["app"]["act_lang"] = lang
        language = app_data["app"]["act_lang"]
        self.cr_menubar()
        self.set_but_text()
        self.set_label_text()

    def check_picture(self):
        path = pathlib.Path(pa_pic + self.tf_name.get("0.1", "end-1c") + ".png")
        return path

    def show_rec_pic(self):
        self.pi_rec_a['file'] = pa_app + '/Cookbook/Bilder/' + rec_name + '.png'

    def field_state(self, s):
        for item in [self.tf_name, self.tf_port, self.tf_time, self.tf_cat, self.tf_ingr, self.tf_prep]:
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
    pa_pic = pa_app + "/Cookbook/Bilder/"
    pa_app_data = pa_app + "/Cookbook/config/app_data.json"
    pa_rec_data = pa_app + "/Cookbook/config/rec_data.json"
    # load files and set language
    app_data = r_data(0)
    rec_data = r_data(1)
    language = app_data["app"]["act_lang"]
    # define picture paths
    pa_startpic = pa_app + app_data["paths"]["startpic"]
    pa_spoonpic = pa_app + app_data["paths"]["spoonpic"]
    pa_logo = pa_app + app_data['paths']['logo']
    # define the global variables
    bg_app, bg_act, bg_fra, fg_app, fg_act = ('',) * 5  # colors
    rec_name, rec_port, rec_time, rec_reg, rec_cat, rec_ingr, rec_prep = ('',) * 7
    # define fonts
    font24 = ("Calibri", 24)
    font18 = ("Calibri", 18)
    font14 = ("Calibri", 14)
    font10 = ("Calibri", 10)
    font8 = ("Calibri", 8)
    # config the App
    set_colors("anthracite", "black", "lightgreen")
    # Start the App
    app = CB()
    app.quit_app()
