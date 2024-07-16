import socket
import struct


# Change: Implement socket timeouts to avoid hanging indefinitely on network operations

# I used struct to package data, also to ensure correct interpretation of 32-bit 


# Encapsulating the client request logic in the send_request function allows 
# me to separate functionality cleanly
# with a few more minutes i would section this function even more.

def send_request(operation, operand1, operand2):

    """
    Sends a request to the server to perform a specified operation on two operands.

    Args:
        operation (str): The operation to perform ('+', '-', '*', '/').
        operand1 (float): The first operand.
        operand2 (float): The second operand.

    Returns:
        int or float: The result of the operation.
    """
    
    # I would allow the user to specify hort and port using argparse
    # Server details
    host = 'localhost'
    port = 12345

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     # Connect the socket to the server's address and port
    client_socket.connect((host, port))

    # Pack the operation and operands into a binary format
    request = struct.pack('>c2f', operation.encode(), operand1, operand2)

    # send packed request to server
    client_socket.sendall(request)
    
    # recieve response from server
    response = client_socket.recv(1024)

    # Unpack the response to get the result type and the result
    result_type, result = struct.unpack('>ff', response)

    # close the socket connection
    client_socket.close()

    # Return result based on the type
    if result_type == 0:
        return int(result)
    else:
        return result
    
# I would change it is that there is a message when the client connects to the server
if __name__ == "__main__":
    # True loop allows the client to continuously accept user inputs for operations 
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.")
            continue

        #Recieve operand from user and convert to float
        operand1 = float(input("Enter first operand: ").strip())
        operand2 = float(input("Enter second operand: ").strip())

    # Send requesst to server and get the result
        result = send_request(operation, operand1, operand2)
        print(f"Result of {operand1} {operation} {operand2} is {result}")
