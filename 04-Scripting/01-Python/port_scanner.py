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

