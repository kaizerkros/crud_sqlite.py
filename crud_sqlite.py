import sqlite3 # crea conexion con sqlite3 
def conectar_db(): # funcion para conectar base de datos
    return sqlite3.connect('clientes.db')

print("bienvenido al menu de seleccion a continuacion seleccion la opcion deseada")
print("--------------------------------------------------------------------------")
def menu_Seleccion(): # menu de seleccion de usuarios crud con todas las opciones
    print("\n----MENU DE CLIENTES----")
    print("1. listar clientes")
    print("2. agregar clientes")
    print("3. buscar cliente")
    print("4. actualizar imformacion de cliente")
    print("5. eliminar cliente ")
    print("6. salir")

def listar_usuario(): #funcion de listar usuarios conectada a una base de datos "clientes.db"
    try : 
        print ("bienvenido a la lista de clientes")    
        conexion = conectar_db() # conecta con base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall() #selecciona varias lineas de tabla dentro de la base de datos
        if clientes:
            print("Listado de clientes \n") # imprime la lista de clientes
            for clientes in clientes :
             print(f"ID: {clientes[0]}     |       Nombre:  {clientes[1]}    |       Email:  {clientes[2]}  |       telefono:  {clientes[3]}   direccion:  {clientes[4]}  | ciudad:  {clientes[5]}  |")
        else:
            print("No se pudo obtener los datos")
    except sqlite3.Error as e : # escepcion frente a errores
        print (f'Error al acceder a la base de datos: {e}')
    finally: # termina coneccion de la funcion listar uusarios
        if conexion:
            conexion.close()


def agregar_clientes(): # funcion para agregar clientes
    try :
        print("ingrese los datos del nuevo cliente ")
        conexion = conectar_db() # coneccion con base de datos
        cursor = conexion.cursor()
        nombre = input("Ingrese nombre: ").strip()
        email = input("Ingrese email: ").strip()
        telefono = input ("Ingrese telefono: ").strip()
        direccion = input ("Ingrese direccion: ").strip()
        ciudad = input ("Ingrese ciudad: ").strip()
        cursor.execute("INSERT INTO clientes (nombre,email,telefono,direccion,ciudad) VALUES (?,?,?,?,?)",(nombre,email,telefono,direccion,ciudad))
        conexion.commit() # se ingresan los valores de input en la base de datos 
        print("cliente agregado con éxito")
    except Exception as error:
        print(f"Ocurrió un error: {error}")
    finally:
        if conexion:
            conexion.close()


def buscar_clientes() : # funcion buscar clientes
        try :
            print("ingrese nombre del cliente ")
            conexion = conectar_db() # coneccion  base de datos
            cursor = conexion.cursor()
            while True : # bucle de condicion para verificar caracteres invalidos 
                texto_a_buscar = input("Ingrese texto a buscar o escriba SALIR: ").strip()
                if texto_a_buscar == "SALIR" :
                    print("bienvenido de nuevo al menu")
                    break
                if any(caracter.isdigit() for caracter in texto_a_buscar):
                    print("no se permiten numeros")
                    continue
                if not texto_a_buscar:
                    print("no puede estar vacio")
                    continue  
                else : # no se cumplio ninguna condicion anterior por lo tanto "PRINT cliente no enc..."
                    print("cliente no encontrado asegurese de que el cliente que ingresa exista")
                filtro = f"%{texto_a_buscar}%" # filtro para buscar similitudes de caracteres
                query_buscar = """SELECT * FROM clientes WHERE nombre LIKE ? """
                cursor.execute(query_buscar,(filtro,)) #busqueda en la base de datos
                clientes = cursor.fetchall()     
                if clientes :
                    print("Listado de clientes encontrados con la informacion que proporcionaste \n")
                    print("si desea salir escriba SALIR en mayusculas ")
                for clientes in clientes : # listado de clientes encontrados
                    print(f"ID: {clientes[0]}     |       Nombre:  {clientes[1]}    |       Email:  {clientes[2]}  |       Telefono:  {clientes[3]} |       direccion:  {clientes[4]}  |     ciudad:  {clientes[5]}  | ")
        except Exception as error:
            print(f"Ocurrió un error: {error}")
        finally : 
            if conexion :
                conexion.close()


def actualizar_imformacion(): #funcion actualizar informacion del cliente
    try :
        print("ingrese el id de cliente que desea atualizar ")    
        conexion = conectar_db() # coneccion a la base de datos
        cursor = conexion.cursor()
        id = input("Ingrese el id del usuario a actualizar: ")
        cursor.execute("SELECT * FROM clientes WHERE id = ?",(int(id),)) # busca la informacion que se indico en la base de datos
        cliente = cursor.fetchone() # seleciona una linea de tabla de la base de datos 
        if cliente: # muestra los datos actuales de los clientes y da la opcion de mantenerlos
            print("deje el campo en blanco para mantener los valores actuales") 
            nombre = input(f"Nombre actual {cliente[1]} ...Ingrese el nuevo nombre: ").strip() or cliente [1]
            email = input(f"Email actual {cliente[2]} ...Ingrese el nuevo email: ").strip() or cliente [2]
            telefono = input (f"telefono actual {cliente[3]} ...Ingrese el nueva telefono: ").strip() or cliente [3]
            direccion = input (f"direccion actual {cliente[4]} ...Ingrese la nueva direccion: ").strip() or cliente [4]
            ciudad = input (f"ciudad actual {cliente[5]} ...Ingrese la nueva ciudad: ").strip() or cliente [5]
            cursor.execute("UPDATE clientes SET nombre = ?, email = ?, telefono = ?,direccion = ?, ciudad = ? WHERE id = ?",( nombre, email, telefono, direccion, ciudad, (int(id))))
            conexion.commit() # actualiza la imformacion de la base de datos 
            print("cliente actualizado con éxito")
        else:
            print("cliente no encontrado")
    except sqlite3.Error as error: 
        print (" error al actualizar base de datos")
    finally :
        if conexion :
            conexion.close()
        
def eliminar_clientes ():  
    try :
        print("ingrese los datos ")
        while True : # bucle de condicion verdadera 
            conexion = conectar_db()
            cursor = conexion.cursor()
            id = input("Ingrese el id del cliente a eliminar: ").strip()
            cursor.execute("SELECT * FROM clientes WHERE id = ?",(int(id),)) # selecciona clientes en la base de datos segun el id
            clientes = cursor.fetchone()   
            if clientes : # imprime tabla con el cliente encontrado
                print(f"ID: {clientes[0]}     |       Nombre:  {clientes[1]}    |       Email:  {clientes[2]}  |       Telefono:  {clientes[3]} |       direccion:  {clientes[4]}  |     ciudad:  {clientes[5]}  | ")
                confirmacion = input("estas seguro de que deseas eliminar este cliente SI/NO").upper()
                if confirmacion == "SI" :
                    cursor.execute("DELETE FROM clientes WHERE id = ?",(int(id),))
                    conexion.commit() # lo elimina de la base de datos y cierra coneccion
                    print("cliente ELIMINADO con éxito")
                    break 
                elif confirmacion == "NO" :
                    print ("eliminacion cancelada el cliente no fue eliminado")
                    break
                else :
                    print("opcion no valida por favor confirme con SI/NO")
            else :
                print("no se encontrado ningun usuario con el ID que ingresaste")
                break
    except sqlite3.Error as error :
        print("error al eliminar cliente ")
    finally :
        if conexion :
            conexion.close()    

opcion = 0 
while opcion != 6: # bucle de condicion con valor de 6 para terminar el bucle
    menu_Seleccion()
    try :
        opcion = int(input("ingrese su opcion "))
        if opcion == 1 :
            listar_usuario()
        elif opcion == 2 : 
            agregar_clientes()
        elif opcion == 3: 
            buscar_clientes()
        elif opcion == 4:
            actualizar_imformacion()
        elif opcion == 5 : 
            eliminar_clientes()
        elif opcion == 6 :
            print(" muchas gracias por su visita profe.....")
    except ValueError :
        ("caracter invalido debes ingresar un numero ")                   
