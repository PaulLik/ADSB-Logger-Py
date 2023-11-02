import pyodbc

def connectDB():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Sync\Airframes2019.mdb;")
    cursor = conn.cursor()

    sql = "SELECT 'B' as Type, 'B' & BrandID as ID, BrandName AS Name, NULL as Parent, 2 as Child FROM Brands UNION SELECT 'T', 'T' & TypeID, TypeBase & ' (' & TypeCode & ')', 'B' & TypeBrand, 4 FROM Types ORDER BY Type, Name;"
    
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row.Name)


def findAircraft(afHex):

    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Sync\Airframes2019.mdb;")
    cursor = conn.cursor()

    sql = "SELECT Airframes.AfHex, Brands.BrandName, Airframes.AfModel, Types.TypeCode, Airframes.AfTail, Airlines.AlName, Airlines.AlICAO, Airlines.AlIATA, Countries.CountryName, Countries.CountryCode FROM Countries INNER JOIN ((Brands INNER JOIN Types ON Brands.BrandID = Types.TypeBrand) INNER JOIN (Airlines INNER JOIN Airframes ON Airlines.AlID = Airframes.AfAirline) ON Types.TypeID = Airframes.AfType) ON Countries.CountryID = Airlines.AlCountry WHERE Airframes.AfHex = '" + afHex + "';"

    cursor.execute(sql)
    af = cursor.fetchone()
    if af:
        aircraft = af.BrandName + " " + af.AfModel + " (" + af.TypeCode + "), " + af.AlName + ", " + af.CountryName
    else:
        aircraft = "Неизвестный борт"
    
    return aircraft


def loadAirports():

    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\Sync\Airframes2019.mdb;")
    cursor = conn.cursor()

    sql = "SELECT Airports.ApID, Airports.ApIATA, Countries.CountryName, Airports.ApCity, Airports.ApName, Airports.ApICAO FROM Countries INNER JOIN Airports ON Countries.CountryID = Airports.ApCountry;"

    cursor.execute(sql)

    global airports
    airports = cursor.fetchall()


if __name__ == "__main__":
    loadAirports()
