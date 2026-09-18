import os
from dotenv import load_dotenv
from scapy.all import ARP, Ether, srp

load_dotenv()


def scan(ip_range: str, iface: str = None):
    """
    Sends an ARP request to every IP in ip_range and returns
    a list of devices that responded.

    iface: optional network interface name. Linux usually auto-detects
    correctly; Windows sometimes needs this set explicitly when multiple
    virtual adapters (VPNs, VMware, WSL, etc.) are present.
    """
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered, unanswered = srp(packet, timeout=3, verbose=0, iface=iface)

    devices = []
    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


if __name__ == "__main__":
    network_range = os.getenv("NETWORK_RANGE", "192.168.1.0/24")
    interface = os.getenv("NETWORK_IFACE")  # None on Linux, unless needed

    devices = scan(network_range, iface=interface)
    print(f"Found {len(devices)} device(s):\n")
    for d in devices:
        print(f"{d['ip']:15} {d['mac']}")