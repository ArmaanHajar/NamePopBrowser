import os
import tkinter as tk
import pygubu
from Name import Gender, Year, Name

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "browser.ui")

class BrowserApp:
    def __init__(self, parent):
        self.init_ui(parent)
        self.setup_tree()
        self.setup_gender_combo()
        self.setup_year_combo()

    def init_ui(self, parent):
        builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', parent)
        builder.connect_callbacks(self)

        self.__builder = builder
        self.__gender_combo = builder.get_object('gender_combo', parent)
        self.__year_combo = builder.get_object('year_combo', parent)
        self.__min_names_entry = builder.get_object('min_names_entry', parent)
        self.__tree = builder.get_object('name_tree', parent)

    def setup_tree(self):
        tree = self.__tree

        tree.configure(columns = (1, 2, 3, 4), displaycolumns = (1, 2, 3, 4))

        tree.heading(1, text = "Name", anchor=tk.W)
        tree.heading(2, text = "Year")
        tree.heading(3, text = "Gender")
        tree.heading(4, text = "Name Count")

        tree.column(1, width=175, anchor=tk.CENTER)
        tree.column(2, width=175, anchor=tk.CENTER)
        tree.column(3, width=175, anchor=tk.CENTER)
        tree.column(4, width=175, anchor=tk.CENTER)


    def setup_gender_combo(self):
        genders = Gender.fetch_genders()
        self.__gender_combo['values'] = [Gender.BOTH_GENDERS] + [gender.get_gender() for gender in genders]
        self.__gender_combo.current(0)

    def setup_year_combo(self):
        years = Year.fetch_years()
        self.__year_combo['values'] = [Year.ALL_YEARS] + [year.get_year() for year in years]
        self.__year_combo.current(0)

    def gender_selected(self, event):
        print("Gender Changed:", self.__gender_combo.get())
        self.fetch_names()

    def year_selected(self, event):
        print("Year Changed:", self.__year_combo.get())
        self.fetch_names()

    def min_names_changed(self, event):
        print("Min Names Changed:", self.__min_names_entry.get())
        self.fetch_names()

    @staticmethod
    def show_to_tuple(name):
        return (
            name.get_name(),
            name.get_year(),
            name.get_gender(),
            name.get_min_names()
        )

    def fetch_names(self):
        try:
            min_names = int(self.__min_names_entry.get())
        except:
            min_names = 100
        if min_names < 100:
            min_names = 100

        try:
            year = int(self.__year_combo.get())
        except:
            return

        names = Name.fetch_names(self.__gender_combo.get(), year, min_names)
        for i in self.__tree.get_children():
            self.__tree.delete(i)

        for i in range(len(names)):
            self.__tree.insert('', 'end', values=BrowserApp.show_to_tuple(names[i]))

    def show_names(self):
        pass

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Name Popularity Browser")
    app = BrowserApp(root)
    app.run()

