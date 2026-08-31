## LESSON 1 VARIABLES 

# target_IP = "10.10.10.20"
# port = 631
# timeout = 1
# service = "CUPS"
# is_open = True

# print(f"Target: {target_IP}",
#       f"Port: {port}",
#       f"Timeout: {timeout}",
#       f"Service: {service}",
#       f"Open: {is_open}"
#       )


## LESSON 2 CONDITIONALS

# port = 443 
# status = "Closed"


# if status == "Open": 
#     print(f"Port {port} is open")

# elif status == "Closed":
#     print(f"Port {port} is closed")

# elif status == "Timeout": 
#     print(f"Port {port} timed out")

# else:
#     print("Error")


## LESSON 3 LOOPS

# target = "10.10.10.20"

# for port in range(20, 31):
    # print(f"Scanning {target}:{port}")


## LESSON 4 FUNCTIONS

# ports = [22, 53, 80, 443, 631]
# target = "10.10.10.20"

# def scan_port(target, port):        #Handles the one port 
#     print(f"Scanning {target}:{port}")

# for port in ports:                  #Handles the repitition of the one port 
#     scan_port(target, port)



## LESSON 5 RETURN

# def check_port(port):

#     if port == 631:
#         return "OPEN"
#     else:
#         return "CLOSED"     # Gives something back to rest of program 

# result = check_port(631)
# print(result)               #displays something 


## LESSON 6 TRY/EXCEPT

# def test_number(value):   #This function checks if it is a int

#     try: 
#         value = int(value)   
#         return "VALID"
#     except ValueError:
#         return "INVALID"

# print(test_number("123"))
# print(test_number("hello"))
