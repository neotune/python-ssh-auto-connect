import paramiko
import logging
import datetime
import json
import os


def json_file_load():
    with open(os.path.join(file_path, 'server_info.json')) as json_file:
        server_info = json.load(json_file)
        log.info('user id : %s', server_info["user_name"])
        log.info('server list count : %s', len(server_info["server_list"]))
    return server_info


def login(host_name, user_name, password):
    try:
        log.info('connect to : %s', host_name)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host_name, port=22, username=user_name, password=password)

        stdin, stdout, stderr = client.exec_command("whoami")
        log.info('command success : %s', stdout.read())

        client.close()

        return "success"
    except Exception as e:
        client.close()
        log.error("connection error : %s", host_name)
        return "fail"


def write_txt_file(error_server_ip_list):
    with open(os.path.join(file_path, 'error_server_list.txt'), 'w') as f:
        for item in error_server_ip_list:
            f.write("%s\n" % item)


def main():
    server_info = json_file_load()
    error_server_ip_list = []
    for host_name in server_info["server_list"]:
        status = login(host_name, server_info["user_name"], server_info["password"])
        if status == 'fail':
            error_server_ip_list.append(host_name)

    if len(error_server_ip_list) > 0:
        log.info('connect error server list count : %s', len(error_server_ip_list))
        write_txt_file(error_server_ip_list)


if __name__ == "__main__":
    # file path
    file_path = os.getcwd()

    # logging formatter
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')

    # log file setting
    file_handler = logging.FileHandler(os.path.join(file_path, 'log_{:%Y%m%d}.log').format(datetime.datetime.now()), encoding='utf-8')
    file_handler.setFormatter(formatter)

    # console log setting
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # logging 전역 설정
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.addHandler(file_handler)
    log.addHandler(console_handler)

    # start
    main()

