


def insertar():
    deptno = int(input("Inserte el número de departamento : "))
    dnombre = input("Inserte el nombre del departamento")
    loc = input("Inserte la localidad del departamento")

    from datetime import date

    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        # DEPT_NO  DNOMBRE, LOC así se llaman las columnas de la tabla departamento.

        ConsultaAlta = ("INSERT INTO DEPT "
                        "(DEPT_NO, DNOMBRE, LOC) "
                        "VALUES (:P1, :P2, :P3)")

        datosDepartamento = (deptno, dnombre, loc)
        cursor.execute(ConsultaAlta, datosDepartamento)
        connection.commit()

    except connection.Error as error:
        print("Error: ", error)

    connection.close()


#--------------------------------------------------------------


def consultar():
    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        consulta = ("SELECT DEPT_NO, DNOMBRE, LOC FROM DEPT" )
        cursor.execute(consulta)

        resultado = False
        for dep, nom, loc in cursor:
            print("Número Departamento: ", dep)
            print("Nombre Deparamento: ", nom)
            print("Localidad donde se ubica : ", loc)
            resultado = True
        if resultado == False:
            print("Sin resultados")
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

#--------------------------------------------------------------
quiereIntentarlo=True
letra="S"

while quiereIntentarlo :
    while letra== "S" or letra =="s" :
            print("Gracias por participar : ..... ")
            print( "1.- ALTA DEPARTAMENTO ")
            print("2 .- CONSULTA DEPARTAMENTOS ")
            print(" ---------------------------------- ")
            opcion = input("Introduzca la opción requerida :  \n")
            if opcion=="1":
                insertar()
            else:
                consultar()
            print(" ----------------------------------------------")
            intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
            if intento=="S" or intento=="s" :
                quiereIntentarlo=True
            else:
                quiereIntentarlo=False








