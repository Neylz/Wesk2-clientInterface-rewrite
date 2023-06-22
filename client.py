import json
import socket
import requests
import platform


print("Client is running")

host, port = ('192.168.137.1', 8808)





def get_markers():
    try:
        response = requests.get('http://127.0.0.1:5001/get_markers')

        if response.status_code != 200:
            print("Can't get markers from esieabot-ai-api, status code: {}".format(response.status_code))
            return "e0003_{}".format(response.status_code)

        req = response.json()

        req["sender"] = str(platform.node())

        return json.dumps(req)



    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return "e0000"



def server_request(host, port, data=None):
    con_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con_socket.connect((host, port))

        if data is None:
            data = get_markers()

        data = data.encode('utf-8')

        con_socket.sendall(data)

        apply_instructions(con_socket.recv(1024).decode('utf-8'))





    except ConnectionRefusedError:
        print("Connection to the server failed ")

    finally:
        con_socket.close()



def apply_instructions(data):
    print(data)




server_request(host, port)


