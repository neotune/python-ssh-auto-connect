# python-ssh-auto-connect

-----

## info

* 주기적으로 서버 접속해야 하는 곳에 사용
* 접속 후 날리는 명령어는 'whoami'

## install

```sh
pip install -r requirements.txt
```

## how to use

* **server_info.json** 열어 user_name, password, server_list 항목 수정
* 아래의 명령어를 통해 실행

```
python ssh_auto_connect.py 
```

* 실행 후 아래의 파일이 py 파일과 같은 경로에 생성
  * log_YYYYMMDD.log : 실행 로그
  * error_server_list.txt : server_info.json 의 server_list 항목 중 실패한 서버 리스트

