import requests
import platform
import socket
import psutil


def send_to_tg_bot(message):
    bot_token = ""  # Ganti dengan token bot Telegram Anda
    chat_id = ""  # Ganti dengan ID chat yang sesuai
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Successfully sent to TG bot :)")
        else:
            print(f"Failed to send. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


def get_system_info():
    info = []

    # Hostname & OS info
    info.append(f"Host Name: {socket.gethostname()}")
    info.append(f"OS: {platform.system()} {platform.release()} (Version: {platform.version()})")
    info.append(f"Architecture: {platform.architecture()[0]}")

    # CPU info
    info.append(f"Processor: {platform.processor()}")
    info.append(f"Cores: {psutil.cpu_count(logical=False)} | Threads: {psutil.cpu_count(logical=True)}")

    # Memory info
    mem = psutil.virtual_memory()
    info.append(f"Total RAM: {mem.total // (1024 ** 3)} GB")

    # Disk info
    disk_info = [f"{part.device} ({part.fstype})" for part in psutil.disk_partitions()]
    info.append(f"Disk Partitions: {', '.join(disk_info)}")

    # Network info
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                info.append(f"Interface: {interface}, IP: {addr.address}, Mask: {addr.netmask}")
            elif addr.family == psutil.AF_LINK:
                # Perbaikan: langsung ambil alamat MAC tanpa UUID
                info.append(f"MAC Address ({interface}): {addr.address}")

    return '\n'.join(info)


if __name__ == "__main__":
    test_message = "wkwkwk"
    send_to_tg_bot(test_message)

    system_info = get_system_info()
    send_to_tg_bot(system_info)
