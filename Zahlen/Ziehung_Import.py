# -*- coding: utf-8 -*-
import sqlite3


def makedb():
    connection = sqlite3.connect("EuroJP_Ziehungen.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute("""DROP TABLE Ziehung""")
    except Exception, e:
        pass
    cursor.execute("""CREATE TABLE Ziehung ( zNummer INTEGER, zDatum TEXT )""")
    try:
        cursor.execute("""DROP TABLE ZZahlen""")
    except Exception, e:
        pass
    cursor.execute("""CREATE TABLE ZZahlen ( zNummer INTEGER, GZ1 INTEGER, \
        GZ2 INTEGER, GZ3 INTEGER, GZ4 INTEGER, GZ5 INTEGER, EZ1 INTEGER, EZ2 INTEGER)""")

    cursor.close()
    connection.close()


def main():
    jahre = ["2012", "2013", "2014", "2015"]
    zaehler = 0
    connection = sqlite3.connect("EuroJP_Ziehungen.sqlite")
    cursor = connection.cursor()

    for jahr in jahre:
        datei = "EJ_ab_" + jahr + ".csv"
        f = open(datei, "r")
        sql1 = "INSERT INTO Ziehung VALUES (?,?)"
        sql2 = "INSERT INTO ZZahlen VALUES (?,?,?,?,?,?,?,?)"
        for line in f.readlines():
            zaehler += 1
            datum = line.split(",")[1] + jahr
            werte = (zaehler, datum)
            cursor.execute(sql1, werte)

            werte = []
            werte.append(zaehler)
            for i in range(3, 10):
                werte.append(int(line.split(",")[i]))
            cursor.execute(sql2, werte)

    f = open("EJ_ab_2016.csv", "r")
    for line in f.readlines():
        zaehler += 1
        datum = line.split(";")[0]
        werte = (zaehler, datum)
        cursor.execute(sql1, werte)

        werte = []
        werte.append(zaehler)
        for i in range(1, 8):
            werte.append(int(line.split(";")[i]))
        cursor.execute(sql2, werte)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    makedb()
    main()
