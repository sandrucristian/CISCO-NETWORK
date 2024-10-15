## Python : Create a port scanner

- Type of Challenge: `Verify Coding Knowledge` 
- Duration: `2 days`
- Challenge Type : `Team`

### Prerequisites

1. Identify libraries required.
2. Learn about ARP (Address Resolution Protocol) and ICMP (Internet Control Message Protocol) protocols used for scanning. 
3. Learn about TCP SYN scan for identifying open ports.
4. Creating a range of IP addresses within your local network subnet.
5. Understand ethical considerations and limited testing.
6. Understanding how you can detect port scanning.
7. Understanding how software design reports are written.


### To Do

1. Write the code to create a port scanner in Python.
2. Implement error handling and input validation to ensure the program handles unexpected scenarios gracefully.
2. Test the port scanner on localhost and a remote host to verify its functionality.(Note: Remote host must be within a subnet created with VMs)
3. Write a detailed software designing report.
4. Write a testing report.
5. Write a report on ethical considerations and whether you have complied to the condideration.
6. Write a report on how detection of port scanning can be achieved.

### Bonus

7. Enhance the port scanner with basic security measures, such as rate limiting to prevent excessive scanning.
8. Implement logging functionality to record scan results and any errors encountered.
9. Review the code for potential security vulnerabilities and apply best practices for secure coding.
10. Include the enhancements in the report.

### To Document

11. Planing.
12. Issues/Constraints.
13. Coding Considerations.
14. Properly Documented Code.

## CODE

```python3
import socket
from concurrent.futures import ThreadPoolExecutor
def scan_port(host, port):
    """
    Scans a single port on the specified host.
    Args:
        host (str): The hostname or IP address of the target.
        port (int): The port number to scan.
    Returns:
        str: A message indicating whether the port is open or closed.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set a timeout for the connection attempt
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                return f"Port {port} is open"
            else:
                return f"Port {port} is closed"
        except socket.error:
            return f"Could not connect to server {host}"
def scan_ports(host, ports):
    """
    Scans a range of ports on the specified host.
    Args:
        host (str): The hostname or IP address of the target.
        ports (list): A list of port numbers to scan.
    Returns:
        None: Prints the result of each port scan.
    """
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(host, port), ports)
    for result in results:
        print(result)
def main():
        """

        Main function to execute the port scanner.
        Prompts the user for a target host and port range to scan.
        """
        host = input("Enter the host to scan (IP or domain): ")
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
        # Create a list of ports to scan
        ports = range(start_port, end_port + 1)
        print(f"Scanning {host} from port {start_port} to {end_port}...")
        scan_ports(host, ports)

if __name__ == "__main__":
    main()
```

## Documentation

**Overview**

This script is a simple `port scanner` that checks which ports are `open` on a specified host. It can scan a range of ports concurrently to speed up the process.

**Requirements**

-	Python 3.x
-	Basic knowledge of command-line interfaces.

**Functions**

-	scan_port(host, port): Scans a single port on the specified host.
-	Parameters:
-	host (str): The hostname or IP address of the target.
-	port (int): The port number to scan.
-	Returns: A message indicating whether the port is open or closed.
-	scan_ports(host, ports): Scans a list of ports on the specified host.
-	Parameters:
-	host (str): The hostname or IP address of the target.
-	ports (list): A list of port numbers to scan.
-	Returns: None (prints results to the console).
-	main(): The entry point of the script. It prompts the user for input and initiates the port scan.

**Usage**

- Save the code to a file named port_scanner.py.
- Run the script from the command line:
 
```bash
python3 port_scanner.py
```

- Follow the prompts to enter the target host and port range.

**Notes**

-	This scanner uses a thread pool to scan multiple ports simultaneously, which significantly speeds up the scanning process.
-	Ensure you have permission to scan the target host to avoid legal issues.

Teamwork: @sandrucristian , @Motoko Kiza
