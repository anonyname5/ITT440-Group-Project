import socket
import ssl
import threading
import json

HOST = '10.0.191.27'  # Use your server's IP address
PORT = 443
CERT_FILE = 'private.crt'
KEY_FILE = 'private.key'

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    
    conn = context.wrap_socket(conn, server_side=True)
    
    try:
        # Indicate that the SSL connection has been successfully established
        print("SSL connection established successfully")
        
        data = conn.recv(1024)
        if data:
            health_data = json.loads(data.decode())
            print(f"Received health data from {addr}: {health_data}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    finally:
        conn.close()
        print(f"Connection closed by {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server listening on", HOST, "port", PORT)
    
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
