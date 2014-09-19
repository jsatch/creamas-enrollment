__author__ = 'hernan'

import csv
import psycopg2
from datetime import date


HOST = 'ec2-107-22-234-129.compute-1.amazonaws.com'
DATABASE = 'de5svld1vf8lt4'
USER = 'mpgnghxzhorpdj'
PASSWORD = 'HtZFVvyVLfXh4Qk2wemNHLHvnu'


def cargar_alumnos():

    conn_string = 'host=%s dbname=%s user=%s password=%s' % (HOST, DATABASE, USER, PASSWORD)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    with open('bd_talara.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            fecha = row[8].split(' ')
            #print date(int(fecha[2]), int(fecha[1]), int(fecha[0]))
            sql = """INSERT INTO matricula_alumno ("nombreCompleto", semestre_id, grado_id, seccion_id, nivel_id, colegio_id,
                  "fechaNacimiento", telefono, tutor,"fechaRegistro", "fechaActualizacion",  estado)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, '-', '-' ,now(), now(), 'N')"""
            cursor.execute(sql, (row[0], row[1], row[2], row[3], row[4], row[5],
                                 date(int(fecha[2]), int(fecha[1]), int(fecha[0]))))

            print row[0] + " - " + row[1] + " - " + row[5]

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    cargar_alumnos()
