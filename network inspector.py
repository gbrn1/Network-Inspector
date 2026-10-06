import socket
import os
import struct
import sys
import time

def checksum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xFFFF)
    s += s >> 16
    return (~s) & 0xFFFF

def ping(ip, timeout=1.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(timeout)
    except PermissionError:
        raise PermissionError("Para usar ICMP em Python, o programa precisa ser executado como administrador/root.")
    except OSError as e:
        raise OSError(f"Não foi possível criar o socket ICMP: {e}")

    pid = os.getpid() & 0xFFFF
    packet_id = pid
    packet_type = 8  # ICMP Echo Request
    packet_code = 0
    packet_seq = 1
    

    # ICMP Echo Request: type=8, code=0
    header = struct.pack("!BBHHH", packet_type, packet_code, 0, packet_id, packet_seq)
    payload = b"0123456789abcdef" * 4
    packet = header + payload

    csum = checksum(packet)
    packet = struct.pack("!BBHHH", packet_type, packet_code, csum, packet_id, packet_seq) + payload

    start =time.perf_counter()

    try:
        sock.sendto(packet, (ip, 0))
        reply = sock.recvfrom(1024)
        
        
        reply = (struct.unpack("!BBHHH", reply[0][20:28]))
        reply_id = reply[3]
        reply_seq = reply[4]
        reply_type = reply[0]
        reply_code = reply[1]

        packetchk = (packet_code, packet_id, packet_seq)

        reply_chk = (reply_code, reply_id, reply_seq)

        if packetchk == reply_chk and reply_type == 0:
            print(f"Enviei: {ip}: type={packet_type}, code={packet_code}, id={packet_id}, seq={packet_seq}")
            print(f"Recebi:  {ip}: type={reply_type}, code={reply_code}, id={reply_id}, seq={reply_seq}")
        else:
            print(f"Enviei: {ip}: type={packet_type}, code={packet_code}, id={packet_id}, seq={packet_seq}")
            print(f"Recebi: {ip}: type={reply_type}, code={reply_code}, id={reply_id}, seq={reply_seq}")
            print("O pacote recebido não corresponde ao pacote enviado.")
            return False

        latency_ms = (time.perf_counter() - start) * 1000
        return round(latency_ms, 2)
    except PermissionError:
        raise PermissionError("Para usar ICMP em Python, o programa precisa ser executado como administrador/root.")
    except socket.timeout:
            return False
    except OSError as e:
        print(f"Erro ao enviar/receber pacote ICMP: {e}")
        return False
    finally:
        sock.close()

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((ip, port))
        return "OPEN"
    except socket.timeout:
        return "TIME OUT"
    except ConnectionRefusedError:
        return "CLOSED"
    finally:
        sock.close()


def grab_banner(ip, port, timeout=1.5, max_bytes=1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    chunks = []

    try:
        sock.connect((ip, port))
        time.sleep(0.2)  # alguns serviços enviam o banner logo após a conexão

        while True:
            try:
                data = sock.recv(max_bytes)
                if not data:
                    break
                chunks.append(data)
                if len(b"".join(chunks)) >= max_bytes:
                    break
                time.sleep(0.1)
            except socket.timeout:
                break

        if not chunks:
            return "No banner (no data)"

        banner = b"".join(chunks).decode("utf-8", errors="replace").strip()
        return banner if banner else "No banner (empty reply)"

    except socket.timeout:
        return "No banner (timeout)"
    except ConnectionRefusedError:
        return "No banner (connection refused)"
    except OSError as e:
        return f"Error: {e}"
    finally:
        sock.close()

def identify_service(port, banner):
    service_map = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NetBIOS",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt"
    }

    banner_lower = banner.lower()

    if "ssh" in banner_lower:
        return "SSH"
    elif "ftp" in banner_lower:
        return "FTP"
    elif "telnet" in banner_lower:
        return "Telnet"
    elif "smtp" in banner_lower:
        return "SMTP"
    elif "mysql" in banner_lower:
        return "MySQL"
    elif "rdp" in banner_lower:
        return "RDP"
    elif "smb" in banner_lower:
        return "SMB"
    elif "netbios" in banner_lower:
        return "NetBIOS"
    elif "pop3" in banner_lower:
        return "POP3"
    elif "dns" in banner_lower:
        return "DNS"
    elif "https" in banner_lower:
        return "HTTPS"
    elif "http" in banner_lower:
        return "HTTP"

    if port in service_map:
        return service_map[port]

    return "Unknown service"


def main():
    if not sys.argv[1:]:
        print('Usage: py "network inspector.py" <target>')
        sys.exit(1)

    target = sys.argv[1]

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Unable to resolve hostname")
        sys.exit(1)

    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8000, 8080]

    print("Target:", target)
    print("IP:", ip)

    latency = ping(ip)
    if latency is not False:
        print("Echo Reply válido")
        print(f"Latency: {latency:.2f} ms")
    else:
        print("ICMP Sem Resposta")

    print()
    print("Scanning ports...")

    for port in ports:
        status = check_port(ip, port)
        if status == "OPEN":
            banner = grab_banner(ip, port)
            service = identify_service(port, banner)
            print(f"Port {port} -> {status}\nService-> {service}\nBanner-> {banner}")
        else:
            print(f"Port {port} -> {status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
