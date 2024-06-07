from email.message import EmailMessage
from tinydb import TinyDB, Query
import datetime as dt
import ssl
import smtplib
import cv2
import nmap

# 1. Scan network for requiered mac address and return the ruquested IP
# Get and storage current ip address for required mac address
# Execute routine to get image from required ip address
# Storage images with timestamps named format and also name insert into tiny DB
# build email object with attachment, content sent the local hour format
# Send email to reciver


def build_time_stamp(camera_name: str) -> str:
    """Construccion de string de tiempo para incrustacion en nombre de arhivo
        para alacenar la fotografica capturada
    """
    # * Formato de stampa CameraName_YYYYMMDD_HHMMSS

    date = dt.datetime.today()
    date_str = dt.datetime.strftime
    return None


def build_url(camera, ip):
    """Construction of url to get pircture from camera
        url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
        url_480p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
    """
    PORT = 554
    cams = {
        "calle": {"user": "callemdz", "psw": "luismdz36"},
        "pasillo": {"user": "luismdz36", "psw": "Luismdz36"},
        "sala": {"user": "luismdz36", "psw": "Luismdz36"}
    }
    # * url_1080p
    result_url = f"rtsp://{cams[camera]['user']}:{cams[camera]['psw']}@{ip}:{PORT}/stream1"
    return result_url


def get_picture(cams_list: dict):
    """utilizacion de modulo open cv ara obtene rimagenes de camaras IP"""

    # * Definition of parameters

    url = build_url()

    print(cams_list)
    return


def get_ip_by_mac(camera: dict) -> str:
    """Get ip addres by requested mac address"""
    # * Inicia la definicion de parametros para la obtencion de las ip's
    host_ip_range = "192.168.0.1/24"
    nm = nmap.PortScanner()
    nm.scan(hosts=host_ip_range, arguments='-sP')
    host_list = nm.all_hosts()

    for host in host_list:
        # print(host)
        if "mac" in nm[host]["addresses"]:
            # print(nm[host]["addresses"])
            for cam, pars in camera.items():
                # print(f"{cam - {pars}}")
                if nm[host]['addresses']['mac'] == pars["mac"]:
                    camera[cam]["ip"] = host
    print(camera)
    return camera


def get_host_list():
    """Escaneo mediante nmap"""

    ip_range = "192.168.0.1/24"
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sP')

    return nm


def target_cams() -> dict:
    """Dicionario de parametros de camaras"""

    macs_dict = {
        "calle": {"ip": "", "mac": "84:D8:1B:F5:5A:9F"},
        "pasillo": {"ip": "", "mac": "C0:C9:E3:46:7C:92"},
        "sala": {"ip": "", "mac": "E4:C3:2A:03:8B:98"},
    }
    return macs_dict


def email_config():
    """Asignacion de parametros a variables globales"""

    pws = "polqnpilozmwnrcw"  # password
    sender = "luis3mendez6@gmail.com"
    reciver = "luis3mendez6@gmail.com"
    content = """Hola Mundo Mundial"""

    mail_dict = {"ps": pws, "snr": sender, "rcr": reciver, "cnt": content}

    return mail_dict


def config() -> dict:
    """Definicion de variables globales y configuraciones iniciales"""

    global calle
    global pasillo
    global sala

    construc_list = [
        # definition of cameras list, name, ip, mac, user, pass
        ["calle", "", "84:D8:1B:F5:5A:9F", "callemdz", "luismdz36"],
        ["pasillo", "", "C0:C9:E3:46:7C:92",]
    ]

    return None


def run_program():
    """Execution of main program"""

    cams_list = config()

    # obtner lista de mac targets
    macs = target_cams()  # dictionary
    cams_list = get_ip_by_mac(macs)
    print(cams_list)
    get_picture(cams_list)


if __name__ == "__main__":
    run_program()
