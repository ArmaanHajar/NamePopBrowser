from Database import Database

class Name:
    def __init__(self, NameCount, Name, Year, Gender):
        self.__Name = Name
        self.__Year = Year
        self.__Gender = Gender
        self.__NameCount= NameCount

    def get_name(self):
        return self.__Name

    def get_year(self):
        return self.__Year

    def get_gender(self):
        return self.__Gender

    def get_min_names(self):
        return self.__NameCount

    @staticmethod
    def fetch_names(gender, year, min_names):
        return Database.fetch_names(gender, year, min_names)

class Gender:
    BOTH_GENDERS = '-- M + F --'
    def __init__(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    @staticmethod
    def fetch_genders():
        return Database.fetch_genders()

class Year:
    ALL_YEARS = "-- All Years --"
    def __init__(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    @staticmethod
    def fetch_years():
        return Database.fetch_years()