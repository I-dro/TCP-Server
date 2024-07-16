import socket
import struct
import threading
import time


# I used struct to package data, also to ensure correct interpretation of 32-bit 

# I used threading so that the server can handle multiple client connections simultaneously

# I chose threading over processes because of the simplicity of the operation.
# I wanted to reduce the latency, and as the task is more I/O- bound it just seemed more efficient

# I wanted to implement time for better logging. 

def perform_operation(operation, operand1, operand2):
    # Provide a dictionary  that maps operation codes represented as bytes

    # Change: add more options such as % and !

    print(f"precheck first: {operand1} second: {operand2}")
    operations = {
        b'+': lambda x, y: x + y,
        b'-': lambda x, y: x - y,
        b"*": lambda x, y: y * x,
        b"/": lambda x, y: x / y if y !=0 else 0,
        # Handles division by zero
    }

    # checks if the operation is registered. If operation is pre-registered attempts to
    # Perform the operation
    if operation in operations:
        return operations[operation](operand1, operand2)
    else:
        raise ValueError("This operaton is not accounted for: " % operation)
    
def manage_client(conn, addr):
    # Print the address of the connected client
    print(f"Connection from {addr}")

    # I wanted something that would stop the function if the server did not recieve a
    # simple 2 operand 1 operator problem. A two signed 32-bit big-endian operands 
    # requires 4 bytes. and an operation requires 1

    # This stops cases where the client provides an incomplete equation such as
    # 1 +


    # Recieves data from the client
    # Change: If i had more time i wanted to change functions to take longer equations
    # for example a use case where 3 + 4 - 1 + 4. It would subtract 9 from the length
    # and if len(data) > 9 then 
    # if (len(data) - 9 ) % 5 = 0
    # then it would pass.

    data = conn.recv(1024)
    if len(data) < 9: # checks for sufficient data
        print("Incomplete data recieved")
        conn.close()
        return 
    
    # shutdown 
    # Change: implement signal handling
    if operation == b'shutdown':
        print("Shutting down the server...")
        conn.sendall(struct.pack('>ff', 1, 0.0))
        conn.close()
        return
    
    
    # Extract the operation and operands from the received data
    operation = data[0:1] # First byte for operation
    operand1 = struct.unpack('>f', data[1:5])[0] #Next 4 bytes for first operand
    operand2 = struct.unpack('>f', data[5:9])[0] #Next 4 bytes for Second operand

    try: 
        #attempts to perform the operation using extracted operand
        result = perform_operation(operation,operand1, operand2)
        # Pack the result into a binary format for sending back to the client
        if isinstance(result, int):
            result_data = struct.pack('>fi', 0, result) # For integer result
        
        else:
            result_data = struct.pack('>ff', 1, result) # For float result

        # Send the result back to the client
        conn.sendall(result_data)
    except Exception as e:
        ## Handle any errors during operation
        print(f"Error performing operation: {e}")
        conn.sendall(struct.pack('>ff', 1, 0.0))
        # Send error result

    conn.close()
    
    # change: Use asynchronous I/O with asyncio for better scalability
def main():
    # Set up the server parameters
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port)) # Bind to the specified host and port

    server_socket.listen(5) # Listen for incoming connections
    print(f"Server listening on {host}:{port}")

    # Change: Use a thread pool to manage client connections instead of creating 
    # a new thread for each connection
    while True:
        # Accept a new connection from a client
        conn, addr = server_socket.accept()
        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=manage_client, args=(conn, addr))
        # Start the thread
        client_thread.start()

if __name__ == "__main__":
    main()