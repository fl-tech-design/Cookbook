#!/usr/bin/python3
import tkinter as tk
import ast
import pathlib

bg_app, bg_act, bg_fra, fg_app, fg_act = ('',) * 5
pa_app = str(pathlib.Path().absolute())


def check_app_state():
    app_state = r_data('app', 'app_state')
    return app_state


def r_data(key_1, key_2):
    data_file = open(pa_app + '/Cookbook/config/app_data.txt', 'r')
    data_from_file = data_file.read()
    data_file.close()
    readed_dict = ast.literal_eval(data_from_file)
    data_dict = readed_dict[key_1]
    data_val = data_dict[key_2]
    return data_val


def r_da_dict():
    data_file = open(pa_app + '/Cookbook/config/app_data.txt', 'r')
    data_from_file = data_file.read()
    data_file.close()
    readed_dict = ast.literal_eval(data_from_file)
    return readed_dict


def w_data_dict(data_dict):
    data_file = open(pa_app + '/Cookbook/config/app_data.txt', 'w')
    data_file.write(data_dict)
    data_file.close()


def set_colors(b_app, b_fra, f_app):
    global bg_app, bg_act, bg_fra, fg_app, fg_act
    bg_app = r_data('color', b_app)
    bg_act = r_data('color', f_app)
    bg_fra = r_data('color', b_fra)
    fg_app = r_data('color', f_app)
    fg_act = r_data('color', b_app)


class CB:
    def __init__(self):
        self.fr_top, self.la_titel = (None,) * 2
        self.new_rec_data_dict = {}
        self.data_dict = r_da_dict()
        self.app_stat = self.data_dict['app']['app_state']
        print(self.app_stat)
        self.menubar, self.filemenu, self.helpmenu, self.language_menu = (None,) * 4
        self.fr_botom, self.bu_bottom_l, self.bu_bottom_r = (None,) * 3
        self.language = r_data('app', 'act_lang')
        set_colors('anthracite', 'black', 'lightgreen')
        self.root = tk.Tk()
        self.root.title(r_data(self.language, 'cookbook'))
        self.root.config(width=1200, height=600, bg=fg_app)
        self.root.resizable(width=False, height=False)

        self.act_name_var = tk.StringVar(value='')
        self.act_port_var = tk.StringVar(value='')

        self.cr_menubar()
        self.cr_fr_top()
        self.cr_fr_info()
        self.cr_fr_picture()
        self.cr_fr_bottom()
        self.root.mainloop()

    def cr_menubar(self):
        menufont = r_data('fonts', 'Cal8')
        self.menubar = tk.Menu(self.root, font=menufont, bg=bg_app, fg=fg_app,
                               activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.filemenu.add_command(label=r_data(self.language, 'new_rec'), command=self.site_new_rec)
        self.filemenu.add_command(label=r_data(self.language, 'edit_rec'), command=self.site_edit_rec)
        self.filemenu.add_command(label=r_data(self.language, 'quit'), command=self.quit_app)
        self.menubar.add_cascade(label=r_data(self.language, 'file'), menu=self.filemenu)

        self.language_menu = tk.Menu(self.menubar, tearoff=1, font=menufont, bg=bg_app, fg=fg_app,
                                     activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.language_menu.add_command(label=r_data(self.language, 'german'), command=lambda: self.set_language('de'))
        self.language_menu.add_command(label=r_data(self.language, 'english'), command=lambda: self.set_language('en'))
        self.language_menu.add_command(label=r_data(self.language, 'french'), command=lambda: self.set_language('fr'))
        self.menubar.add_cascade(label=r_data(self.language, 'language'), menu=self.language_menu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0, font=menufont, bg=bg_app, fg=fg_app,
                                activebackground=bg_act, activeforeground=fg_act, relief='flat')
        self.helpmenu.add_command(label=r_data(self.language, 'about'))
        self.helpmenu.add_command(label=r_data(self.language, 'help'))
        self.menubar.add_cascade(label=r_data(self.language, 'help'), menu=self.helpmenu)

        self.root.config(menu=self.menubar)

    def cr_fr_bottom(self):
        a_state = r_data('app', 'app_state')
        self.fr_botom = tk.Frame(width=1200, height=40, bg=bg_app)
        self.fr_botom.place(x=0, y=560)
        self.bu_bottom_l = tk.Button(self.fr_botom, text=r_data(self.language, 'new_rec'), bg=bg_app, fg=fg_app,
                                     width=25, activebackground=bg_act, activeforeground=fg_act,
                                     command=self.site_new_rec)
        self.bu_bottom_l.place(x=600, y=5)
        self.bu_bottom_r = tk.Button(self.fr_botom, text=r_data(self.language, 'edit_rec'), bg=bg_app, fg=fg_app,
                                     width=25, activebackground=bg_act, activeforeground=fg_act,
                                     command=self.site_edit_rec)
        if a_state == 0:
            self.bu_bottom_r['state'] = 'disabled'
        else:
            self.bu_bottom_r['state'] = 'normal'
        self.bu_bottom_r.place(x=850, y=5)

    def cr_fr_info(self):
        self.fr_info = tk.Frame(width=333, height=150, bg=bg_app)
        self.fr_info.place(x=0, y=72)

    def cr_fr_picture(self):
        self.fr_pict = tk.Frame(width=333, height=333, bg=bg_app)
        self.fr_pict.place(x=0, y=224)

    def cr_fr_top(self):
        self.fr_top = tk.Frame(width=1200, height=69, bg=bg_app)
        self.fr_top.place(x=0, y=0)
        self.la_titel = tk.Label(self.fr_top, text=r_data(self.language, 'my_recipe'), font=r_data('fonts', 'Cal24'),
                                 bg=bg_app, fg=fg_app)
        self.la_titel.place(x=5, y=5)



    def site_new_rec(self):
        self.data_dict['app']['app_state'] = 1
        w_data_dict(str(self.data_dict))
        self.cr_fr_bottom()
        self.set_but_text()
        print('...end of site_new_rec function...')

    def site_edit_rec(self):
        self.set_but_text()
        print('...end of site_edit_rec function...')

    def set_but_text(self):
        if self.bu_bottom_l['text'] == r_data(self.language, 'new_rec'):
            self.bu_bottom_l['text'] = r_data(self.language, 'save')
            self.bu_bottom_r['text'] = r_data(self.language, 'chancel')
        else:
            self.bu_bottom_l['text'] = r_data(self.language, 'new_rec')
            self.bu_bottom_r['text'] = r_data(self.language, 'edit_rec')

    def set_language(self, language):
        self.data_dict['app']['act_lang'] = language
        self.language = self.data_dict['app']['act_lang']

        self.cr_menubar()
        self.set_but_text()
        self.cr_fr_top()
        w_data_dict(str(self.data_dict))

    def quit_app(self):
        self.data_dict['app']['app_state'] = 0
        w_data_dict(str(self.data_dict))
        self.root.quit()

if __name__ == '__main__':
    app = CB()
    app.quit_app()

