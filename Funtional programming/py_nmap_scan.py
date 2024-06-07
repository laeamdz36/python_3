"""Modulo para encontrar IP addres con mac address"""

import nmap


def main():
    print('Enter the MAC Address of the device you are looking for Example: "00:00:00:00:00:00"')
    print('Enter the IP address range in this format Example "192.168.10.0/24"')
    print('"Target Found" will be printed under the devices and MAC address if found')

    target_mac = input('Enter MAC Address: ')
    ip_range = input('IP Address Range:  ')

    nm = nmap.PortScanner()

    nm.scan(hosts=ip_range, arguments='-sP')

    host_list = nm.all_hosts()
    for host in host_list:
        if 'mac' in nm[host]['addresses']:
            print(host + ' : ' + nm[host]['addresses']['mac'])
            if target_mac == nm[host]['addresses']['mac']:
                print('Target Found')
    next1 = input('repeat?y,n: ')
    if next1 == 'y':
        main()
    elif next1 == 'n':
        exit()


if __name__ == '__main__':
    main()
