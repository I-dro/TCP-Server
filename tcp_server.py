import socket
import struct
import threading
import time


def perform_operation(operation, operand1, operand2):
    #Provide a dictionary for that maps operation codes represented as bytes

    print(f"precheck first: {operand1} second: {operand2}")
    operations = {
        b'+': lambda x, y: x + y,
        b'-': lambda x, y: x - y,
        b"*": lambda x, y: y * x,
        b"/": lambda x, y: x / y if y !=0 else 0,
    }

    if operation in operations:
        return operations[operation](operand1, operand2)
    else:
        raise ValueError("This operaton is not accounted for: " % operation)
    
def manage_client(conn, addr):
    print(f"Connection from {addr}")

    data = conn.recv(1024)
    if len(data) < 9:
        print("Incomplete data recieved")
        conn.close()
        return 
    
    if operation == b'shutdown':
        print("Shutting down the server...")
        conn.sendall(struct.pack('>ff', 1, 0.0))
        conn.close()
        return
    
    
    operation = data[0:1]
    operand1 = struct.unpack('>f', data[1:5])[0]
    operand2 = struct.unpack('>f', data[5:9])[0]

    try: 
        result = perform_operation(operation,operand1, operand2)
        if isinstance(result, int):
            result_data = struct.pack('>fi', 0, result)
        else:
            result_data = struct.pack('>ff', 1, result)
        conn.sendall(result_data)
    except Exception as e:
        print(f"Error performing operation: {e}")
        conn.sendall(struct.pack('>ff', 1, 0.0))

    conn.close()
    
def main():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=manage_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()