import socket
import re
from binascii import hexlify


def is_valid_hostname(hostname: str):
    """This is a quick implementation of a host checker"""
    if hostname[-1] == ".":
        # strip exactly one dot from the right, if present
        hostname = hostname[:-1]
    if len(hostname) > 253:
        return False

    labels = hostname.split(".")

    # the TLD must be not all-numeric
    if re.match(r"[0-9]+$", labels[-1]):
        return False

    allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(label) for label in labels)

def get_machine_info() -> None:
    hostname: str = socket.gethostname()
    ip_addr: any = socket.gethostbyname(hostname)
    print(f'hostname: {hostname}, ip address: {ip_addr}')


def get_remote_addr(remote: str) -> None:
    
    if is_valid_hostname(remote):
        print(f'remote {remote} is a valid host name')
        try:
            ip_addr = socket.gethostbyname(remote)
            print(f'Ip Addr of {remote} is {ip_addr}')
            convert_ipv4(ip_addr)
        except socket.error as err:
            print(f'err at get_remote_addr -> {err}')
    else:
        print(f'{remote} is not a valid host')


def convert_ipv4(ip_addr):
    packed_ip = socket.inet_aton(ip_addr)
    unpacked_ip = socket.inet_ntoa(packed_ip)
    print(f'IP Addr: {ip_addr} => packed: {hexlify(packed_ip)}, unpacked: {unpacked_ip}')


def find_services():
    print(socket.getservbyport(80))
    print(socket.getservbyport(53))


if __name__ == '__main__':
    get_machine_info()
    hosts: list[str] = ['www.python.org','www.google.com','www.youtube.com','www.facebook.com','afwafwag.awfwagao']
    for remote in hosts:
        get_remote_addr(remote)
    find_services()