import socket
import struct


# Change: Implement socket timeouts to avoid hanging indefinitely on network operations

# I used struct to package data, also to ensure correct interpretation of 32-bit 


def send_request(operation, operand1, operand2):
    host = 'localhost'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    request = struct.pack('>c2f', operation.encode(), operand1, operand2)
    client_socket.sendall(request)

    response = client_socket.recv(1024)
    result_type, result = struct.unpack('>ff', response)

    client_socket.close()

    if result_type == 0:
        return int(result)
    else:
        return result
    
if __name__ == "__main__":
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.")
            continue

        operand1 = float(input("Enter first operand: ").strip())
        operand2 = float(input("Enter second operand: ").strip())

        result = send_request(operation, operand1, operand2)
        print(f"Result of {operand1} {operation} {operand2} is {result}")
