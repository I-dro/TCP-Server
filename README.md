TCP Calculator Server

A simple multi-threaded TCP server that performs basic arithmetic operations (+, -, *, /) on two 32-bit floating-point operands received from clients. The server handles multiple simultaneous clients and returns the results in a structured format.

Features

	•	Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
	•	Handles multiple clients simultaneously using threading.
	•	Gracefully shuts down on keyboard interrupt or specific shutdown command.

Requirements

	•	Python 3.x
	•	Standard Python libraries: socket, struct, threading


Getting Started

Installation

	1.	Clone the repository:
     git clone https://github.com/yourusername/tcp-calculator-server.git
     cd tcp-calculator-server

Running the Server

	1.	Open a terminal and navigate to the project directory.
	2.	Run the server:
       python3 tcp_server.py
The server will start listening on localhost at port 12345.

Running the Client

	1.	Open another terminal window.
	2.	Navigate to the project directory.
	3.	Run the client:
       python3 tcp_client.py

4.	Follow the prompts to enter the operation and operands.

Example Usage

	•	Enter operation: +
	•	Enter first operand: 1
	•	Enter second operand: 2

Expected output: Result of 1.0 + 2.0 is 3.0

Stopping the Server

To gracefully shut down the server, you can:

	•	Press Ctrl+C in the server terminal.
	•	Implement a shutdown command in the client to send a specific shutdown message.

Code Structure

	•	tcp_server.py: The main server implementation handling connections and operations.
	•	tcp_client.py: The client implementation that sends requests to the server and receives results.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.


Acknowledgements

	•	Inspired by network programming and socket communication in Python.
