# port_scanner_project

import socket
import sys
# 1. get user input
target = input("Enter target IP/Domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\n[+] Starting scan on host: {target}")
print(f"[+] Scanning range: {start_port} to {end_port}\n")
try:
    # 2. open scan_results.txt to save the result
    with open("scan_results.txt", "w") as result_file:
        result_file.write(f"--- Scan Results for {target} ---\n")

    # 3. loop over every port in the range
        for port in range(start_port, end_port + 1):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # AF_INET: we use IPv4 addresses
            # SOCK_STREAM: we use TCP protocol

            s.settimeout(1.0)
            # we set a timeout (one second) for each connection attempt

            response = s.connect_ex((target, port))
            # Attempts to establish a full TCP connection to the target and port
            # Returns 0 if the connection succeeds (the port is open)
            # and returns an error code (such as ECONNREFUSED) if the port is closed

            if response == 0:
                output_msg = f"[+] Port {port}: OPEN"
                print(output_msg)
                result_file.write(output_msg + "\n")

            s.close()

    print("\n[+] Scan finished! Results saved to scan_results.txt")
except socket.gaierror:
    print("\n[-] Error: Hostname could not be resolved. Check the target and try again.")
    sys.exit()

except KeyboardInterrupt:
    print("\n[-] Scan stopped by user.")
    sys.exit()

except socket.error:
    print("\n[-] Could not connect to the target.")
    sys.exit()
