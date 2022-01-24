import pyodbc

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    @classmethod
    def fetch_genders(cls):
        from Name import Gender

        sql = """
        SELECT DISTINCT Gender
        FROM all_data 
        """

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql)
        genders = []
        gender = cursor.fetchone()
        while gender:
            genders.append(Gender(gender[0]))
            gender = cursor.fetchone()
        return genders

    @classmethod
    def fetch_years(cls):
        from Name import Year

        sql = """
        SELECT DISTINCT Year
        FROM all_data 
        """

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql)
        years = []
        year = cursor.fetchone()
        while year:
            years.append(Year(year[0]))
            year = cursor.fetchone()
        return years

    @classmethod
    def fetch_names(cls, gender, year, min_names):
        from Name import Name

        sql = """
        SELECT NameCount, Name, Year, Gender
        FROM all_data
        WHERE Year = ?
        AND Gender = ?
        AND NameCount >= ?
        ORDER BY NameCount DESC;
        """

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql, year, gender, min_names)
        names = []
        name = cursor.fetchone()
        while name:
            names.append(Name(name[0], name[1], name[2], name[3]))
            name = cursor.fetchone()
        return names