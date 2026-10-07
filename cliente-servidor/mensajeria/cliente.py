import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

def recibir_mensajes(conexion):
    while True:
        try:
            datos = conexion.recv(1024)
            if not datos:
                print("\nSe perdió la conexión")
                break
            print(f"\n{datos.decode()}")
            print("> ", end="", flush=True)
        except ConnectionResetError:
            print("Conexión terminada")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT,))
    print("Conectado al servidor")

    
    nombre = input("Ingrese su nombre: ")
    cliente.sendall(nombre.encode())

    print("Escribe tu mensaje. Usa 'salir' para terminar la conexión")

    hilo = threading.Thread(target=recibir_mensajes, args=(cliente,), daemon=True)
    hilo.start()

    while True:
        mensaje = input("> ")
        if mensaje.lower() == "salir":
            break
        cliente.sendall(mensaje.encode())