import socket 
import argparse
import sys
from colorama import Fore, Style, init

init()

def scan_port(ip, port):

    try:
        socket.create_connection((ip, port), timeout = 1)  # Don't wait longer than a second, doesnt need settimeout(1)
        return "OPEN"

    except ConnectionRefusedError:
        return "CLOSED"

    except TimeoutError:
        return "TIMEOUT"

    except OSError:
        return "ERROR"

    # finally:
    #     socket.close()




def main():

    parser = argparse.ArgumentParser()  # How able to understand what user types in 
    parser.add_argument("target")  # What the user puts after python3 main.py ______ is now target 
    parser.add_argument("--start-port", default = 20, type = int)  # These to make it so the user can chose the port range 
    parser.add_argument("--end-port", default = 30, type = int)    # But it is defaulted to 20-30 if they dont add it specifically 
    parser.add_argument("--ports") # optional ports argument to specify without searching for everything in between
    parser.add_argument("--verbose", action="store_true") # Detailed ouput 


    args = parser.parse_args()
    # print(args.ports)  # Testing purposes only 

# --ports
# Handles port input both optional specific and default range
    if args.ports: # if user does use --ports

        try:
            ports = [int(port) for port in args.ports.split(",")] # Seperates optional ports based on commas and converts to int from str
        except ValueError: 
            print("Error: Invalid port")
            sys.exit(1)

        if any(port < 1 or port > 65535 for port in ports): # Makes sure specific input port is still in range same as we did for the input range start and stop 
            print("Error: Invalid port range")
            sys.exit(1)

        ports = list(dict.fromkeys(ports))  # Just handles duplicates incase user inputs identical ports 

    else: 
        ports = range(start, end + 1)
    # print(ports) # Testing puposes only


# --start-port and --end-port
    # Makes sure user input is within the valid range 1 - 65535 for ports and logically correct 
    if (args.start_port < 1   
        or args.start_port > 65535 
        or args.end_port < args.start_port 
        or args.end_port < 1 
        or args.end_port > 65535):

        print("Error: Invalid Port Range")  
        sys.exit(1)  # Stops the prog after the invalid port range (System exit)

    target = args.target
    start = args.start_port
    end = args.end_port

    # If they use an invalid target quit and produce error message 
    try:    
        ip = socket.gethostbyname(target)
        print(ip)
    except socket.gaierror:
        print("Error: Could not resolve target")
        sys.exit(1)




    results = []   # Empty list so result.append adds a tuple (port, result) to the list as it tests the connections, essentially storing them 

    print("Scanning...")

    for port in ports:  # Checks every port from the range the user picks or defualt range
        result = scan_port(ip, port)   # Calls the scan_port function above for each number between 20-30 and ouputs each return as printed result
        # print(port, result)     # Figure out how to store the result???
        results.append((port, result))  # tuple
        if args.verbose:        # Only print the detailed scan if --verbose
            print(f"Port {port}: {result}")  

    
    # Store so i can properly format for the actual CLI    
    open_ports = []
    closed_ports = []
    timeout_ports = []
    error_ports = []

    for port, result in results:

        if result == "OPEN":
            open_ports.append((port))       # For these put the port in a empty listed based on its status (sort them)
        elif result == "CLOSED":
            closed_ports.append((port))     # Take port and add it to the end of the existing closed_ports list if result is closed
        elif result == "TIMEOUT":
            timeout_ports.append((port))
        elif result == "ERROR": 
            error_ports.append((port))



    # ACTUAL SCANNER OUTPUT

    print("=" * 40)
    print("SYSRECON".center(40))
    print("TCP PORT SCANNER".center(40))
    print("=" * 40)
    print()

    print(f"Target: {target}")
    print(f"IP: {ip}")
    print(f"Ports: {len(results)}")
    print()


    # Sorts into open, closed, and timeout. Also if it has a length of zero say non found. 
    print(Fore.GREEN + "OPEN PORTS" + Style.RESET_ALL)  # Green color added
    if len(open_ports) == 0:  #If none
        print("None")
    else:
        for port in open_ports:  # Print out the ports that were OPEN because the for loop above sorted them into open_ports, etc, etc
            print(port)

    print()

    print(Fore.RED + "CLOSED PORTS" + Style.RESET_ALL)
    if len(closed_ports) == 0:
        print("None")
    else:
        for port in closed_ports:
            print(port)

    print()

    print(Fore.YELLOW + "TIMEOUTS" + Style.RESET_ALL)
    if len(timeout_ports) == 0:
        print("None")
    else:
        for port in timeout_ports:
            print(port)

    print()

    print(Fore.RED + Style.BRIGHT +"ERRORS" + Style.RESET_ALL)    # Bold 
    if len(error_ports) == 0:
        print("None")
    else:
        for port in error_ports:
            print(port)

    print("-" * 40)
    print("SCAN SUMMARY".center(40))
    print("-" * 40)
    print(f"Scanned: {len(results)}")
    print(f"Open: {len(open_ports)}")
    print(f"Closed: {len(closed_ports)}")
    print(f"Timeout: {len(timeout_ports)}")
    print(f"Errors: {len(error_ports)}")
    print("-------------------------------------")



if __name__ == "__main__":
    main()