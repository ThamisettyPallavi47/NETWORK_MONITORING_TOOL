# # # # import socket
# # # # import time


# # # # def check_port(ip_address, port):
# # # #     try:
# # # #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # #         sock.settimeout(1)

# # # #         result = sock.connect_ex((ip_address, port))

# # # #         sock.close()

# # # #         if result == 0:
# # # #             return "OPEN"
# # # #         else:
# # # #             return "CLOSED"

# # # #     except OSError:
# # # #         return "ERROR"


    
# # # # hostname=input("Enter Hostname: ")
# # # # try:
# # # #     ip_address=socket.gethostbyname(hostname)
# # # #     print("Hostname: ",hostname)
# # # #     print("IP Address: ",ip_address)
# # # #     start_time = time.time()

# # # #     socket.create_connection((ip_address, 443), timeout=3)

# # # #     end_time = time.time()

# # # #     response_time = (end_time - start_time) * 1000

# # # #     # print("Status: Reachable")
# # # #     # print("Response Time:", round(response_time, 2), "ms")
# # # #     print("\n========================================")
# # # #     print("       NETWORK MONITORING REPORT")
# # # #     print("========================================")

# # # #     print("Hostname       :", hostname)
# # # #     print("IP Address     :", ip_address)
# # # #     print("Host Status    : Reachable")
# # # #     print("Response Time  :", round(response_time, 2), "ms")

# # # #     print("\nTCP PORT STATUS")
# # # #     print("----------------------------------------")

# # # #     ports = [21, 22, 80, 443]

# # # #     print("\nPort Status:")

# # # #     for port in ports:
# # # #         status = check_port(ip_address, port)
# # # #         print(f"Port {port}: {status}")

# # # #     print("----------------------------------------")
# # # #     print("Overall Status : ONLINE")
# # # #     print("========================================")

# # # # except socket.gaierror:
# # # #     print("Unable to resolve hostname.")
    
# # # # except socket.timeout:
# # # #     print("Connection timed out.")

# # # # except OSError:
# # # #     print("Unable to connect to host.")


# # # import socket
# # # import time


# # # def check_port(ip_address, port):
# # #     try:
# # #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #         sock.settimeout(1)

# # #         result = sock.connect_ex((ip_address, port))

# # #         sock.close()

# # #         if result == 0:
# # #             return "OPEN"
# # #         else:
# # #             return "CLOSED"

# # #     except OSError:
# # #         return "ERROR"


# # # hostnames = input("Enter Hostnames separated by comma: ").split(",")

# # # hostnames = [hostname.strip() for hostname in hostnames]


# # # for hostname in hostnames:

# # #     try:
# # #         ip_address = socket.gethostbyname(hostname)

# # #         start_time = time.time()

# # #         socket.create_connection((ip_address, 443), timeout=3)

# # #         end_time = time.time()

# # #         response_time = (end_time - start_time) * 1000

# # #         print("\n========================================")
# # #         print("       NETWORK MONITORING REPORT")
# # #         print("========================================")

# # #         print("Hostname       :", hostname)
# # #         print("IP Address     :", ip_address)
# # #         print("Host Status    : Reachable")
# # #         print("Response Time  :", round(response_time, 2), "ms")

# # #         print("\nTCP PORT STATUS")
# # #         print("----------------------------------------")

# # #         ports = [21, 22, 80, 443]

# # #         for port in ports:
# # #             status = check_port(ip_address, port)
# # #             print(f"Port {port:<10}: {status}")

# # #         print("----------------------------------------")
# # #         print("Overall Status : ONLINE")
# # #         print("========================================")

# # #     except socket.gaierror:
# # #         print(f"\n{hostname}: Unable to resolve hostname.")

# # #     except socket.timeout:
# # #         print(f"\n{hostname}: Connection timed out.")

# # #     except OSError:
# # #         print(f"\n{hostname}: Unable to connect to host.")





# # import socket
# # import time


# # # Check whether a TCP port is open or closed
# # def check_port(ip_address, port):
# #     try:
# #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #         sock.settimeout(1)

# #         result = sock.connect_ex((ip_address, port))

# #         sock.close()

# #         if result == 0:
# #             return "OPEN"
# #         else:
# #             return "CLOSED"

# #     except OSError:
# #         return "ERROR"


# # # Resolve hostname to IP address
# # def resolve_hostname(hostname):
# #     try:
# #         return socket.gethostbyname(hostname)

# #     except socket.gaierror:
# #         return None


# # # Check whether the host is reachable and calculate response time
# # def check_connectivity(ip_address):
# #     try:
# #         start_time = time.time()

# #         socket.create_connection((ip_address, 443), timeout=3)

# #         end_time = time.time()

# #         response_time = (end_time - start_time) * 1000

# #         return True, response_time

# #     except socket.timeout:
# #         return False, None

# #     except OSError:
# #         return False, None


# # # Monitor a single host
# # def monitor_host(hostname):

# #     ip_address = resolve_hostname(hostname)

# #     if ip_address is None:
# #         print(f"\n{hostname}: Unable to resolve hostname.")
# #         return

# #     reachable, response_time = check_connectivity(ip_address)

# #     if not reachable:
# #         print(f"\n{hostname}: Unable to connect to host.")
# #         return

# #     print("\n========================================")
# #     print("       NETWORK MONITORING REPORT")
# #     print("========================================")

# #     print("Hostname       :", hostname)
# #     print("IP Address     :", ip_address)
# #     print("Host Status    : Reachable")
# #     print("Response Time  :", round(response_time, 2), "ms")

# #     print("\nTCP PORT STATUS")
# #     print("----------------------------------------")

# #     ports = [21, 22, 80, 443]

# #     for port in ports:
# #         status = check_port(ip_address, port)
# #         print(f"Port {port:<10}: {status}")

# #     print("----------------------------------------")
# #     print("Overall Status : ONLINE")
# #     print("========================================")


# # # Main program
# # def main():

# #     hostnames = input(
# #         "Enter Hostnames separated by comma: "
# #     ).split(",")

# #     hostnames = [hostname.strip() for hostname in hostnames]

# #     for hostname in hostnames:
# #         monitor_host(hostname)


# # # Start the program
# # if __name__ == "__main__":
# #     main()


# import socket
# import time
# from datetime import datetime


# # Check whether a TCP port is open or closed
# def check_port(ip_address, port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)

#         result = sock.connect_ex((ip_address, port))

#         sock.close()

#         if result == 0:
#             return "OPEN"
#         else:
#             return "CLOSED"

#     except OSError:
#         return "ERROR"


# # Resolve hostname to IP address
# def resolve_hostname(hostname):
#     try:
#         return socket.gethostbyname(hostname)

#     except socket.gaierror:
#         return None


# # Check host connectivity and response time
# def check_connectivity(ip_address):
#     try:
#         start_time = time.time()

#         socket.create_connection((ip_address, 443), timeout=3)

#         end_time = time.time()

#         response_time = (end_time - start_time) * 1000

#         return True, response_time

#     except socket.timeout:
#         return False, None

#     except OSError:
#         return False, None


# # Monitor a single host
# def monitor_host(hostname):

#     ip_address = resolve_hostname(hostname)

#     if ip_address is None:
#         print(f"\n{hostname}: Unable to resolve hostname.")

#         save_report(
#             f"{hostname}: Unable to resolve hostname.\n"
#         )

#         return

#     reachable, response_time = check_connectivity(ip_address)

#     if not reachable:
#         print(f"\n{hostname}: Unable to connect to host.")

#         save_report(
#             f"{hostname}: Unable to connect to host.\n"
#         )

#         return

#     ports = [21, 22, 80, 443]

#     report = "\n"
#     report += "========================================\n"
#     report += "       NETWORK MONITORING REPORT\n"
#     report += "========================================\n"

#     report += f"Hostname       : {hostname}\n"
#     report += f"IP Address     : {ip_address}\n"
#     report += "Host Status    : Reachable\n"
#     report += f"Response Time  : {round(response_time, 2)} ms\n"

#     report += "\nTCP PORT STATUS\n"
#     report += "----------------------------------------\n"

#     for port in ports:
#         status = check_port(ip_address, port)
#         report += f"Port {port:<10}: {status}\n"

#     report += "----------------------------------------\n"
#     report += "Overall Status : ONLINE\n"
#     report += "========================================\n"

#     print(report)

#     save_report(report)


# # Save report to file
# def save_report(report):

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open("network_report.txt", "a") as file:
#         file.write(f"\nReport Time: {timestamp}\n")
#         file.write(report)


# # Main program
# def main():

#     hostnames = input(
#         "Enter Hostnames separated by comma: "
#     ).split(",")

#     hostnames = [hostname.strip() for hostname in hostnames]

#     for hostname in hostnames:
#         monitor_host(hostname)


# # Start the program
# if __name__ == "__main__":
#     main()


import socket
import time
from datetime import datetime


# Check whether a TCP port is open or closed
def check_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip_address, port))

        sock.close()

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"

    except OSError:
        return "ERROR"


# Resolve hostname to IP address
def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)

    except socket.gaierror:
        return None


# Check host connectivity and response time
def check_connectivity(ip_address):
    try:
        start_time = time.time()

        socket.create_connection((ip_address, 443), timeout=3)

        end_time = time.time()

        response_time = (end_time - start_time) * 1000

        return True, response_time

    except socket.timeout:
        return False, None

    except OSError:
        return False, None


# Monitor a single host
def monitor_host(hostname):

    ip_address = resolve_hostname(hostname)

    if ip_address is None:
        print(f"\n{hostname}: Unable to resolve hostname.")

        save_report(
            f"{hostname}: Unable to resolve hostname.\n"
        )

        return False

    reachable, response_time = check_connectivity(ip_address)

    if not reachable:
        print(f"\n{hostname}: Unable to connect to host.")

        save_report(
            f"{hostname}: Unable to connect to host.\n"
        )

        return False

    ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"}

    report = "\n"
    report += "========================================\n"
    report += "       NETWORK MONITORING REPORT\n"
    report += "========================================\n"

    report += f"Hostname       : {hostname}\n"
    report += f"IP Address     : {ip_address}\n"
    report += "Host Status    : Reachable\n"
    report += f"Response Time  : {round(response_time, 2)} ms\n"

    report += "\nTCP PORT STATUS\n"
    report += "----------------------------------------\n"

    for port, service in ports.items():
        status = check_port(ip_address, port)
        report += f"Port {port:<4} ({service:<5}): {status}\n"

    report += "----------------------------------------\n"
    report += "Overall Status : ONLINE\n"
    report += "========================================\n"

    print(report)

    save_report(report)

    return True


# Save report to file
def save_report(report):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("network_report.txt", "a") as file:
        file.write(f"\nReport Time: {timestamp}\n")
        file.write(report)


# Main program
# def main():

#     hostnames = input(
#         "Enter Hostnames separated by comma: "
#     ).split(",")

#     hostnames = [hostname.strip() for hostname in hostnames]

#     total_hosts = len(hostnames)
#     online_hosts = 0
#     offline_hosts = 0

#     for hostname in hostnames:

#         status = monitor_host(hostname)

#         if status:
#             online_hosts += 1
#         else:
#             offline_hosts += 1

#     # Monitoring summary
#     summary = "\n"
#     summary += "========================================\n"
#     summary += "          MONITORING SUMMARY\n"
#     summary += "========================================\n"
#     summary += f"Total Hosts   : {total_hosts}\n"
#     summary += f"Online Hosts  : {online_hosts}\n"
#     summary += f"Offline Hosts : {offline_hosts}\n"
#     summary += "========================================\n"

#     print(summary)

#     save_report(summary)


# # Start the program
# if __name__ == "__main__":
#     main()


def main():

    hostnames = input(
        "Enter Hostnames separated by comma: "
    ).split(",")

    hostnames = [hostname.strip() for hostname in hostnames]

    interval = int(input("Enter monitoring interval in seconds: "))

    print("\nMonitoring started...")
    print("Press Ctrl+C to stop monitoring.")

    try:

        while True:

            total_hosts = len(hostnames)
            online_hosts = 0
            offline_hosts = 0

            for hostname in hostnames:

                status = monitor_host(hostname)

                if status:
                    online_hosts += 1
                else:
                    offline_hosts += 1

            # Monitoring summary
            summary = "\n"
            summary += "========================================\n"
            summary += "          MONITORING SUMMARY\n"
            summary += "========================================\n"
            summary += f"Total Hosts   : {total_hosts}\n"
            summary += f"Online Hosts  : {online_hosts}\n"
            summary += f"Offline Hosts : {offline_hosts}\n"
            summary += "========================================\n"

            print(summary)

            save_report(summary)

            print(f"Next check in {interval} seconds...")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


# Start the program
if __name__ == "__main__":
    main()