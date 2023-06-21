import socket
import subprocess


print("Client is running")

host, port = ('192.168.137.1', 8808)




def get_markers():
    try:
        process = subprocess.Popen(['usr/bin/curl', '-s', 'http://127.0.0.1:5001/get_markers', 'r'], stdout=subprocess.PIPE)
    except FileNotFoundError:
        print("Can't find CURL")
        return "e0000"

    output, error = process.communicate()

    if error is not None:
        print("Can't run CURL to make an API call to esieabot-ai-api")
        return "e0001"

    try:
        result = output.decode('utf-8')
        return result

    except UnicodeDecodeError:
        print("Can't decode CURL output")
        return "e0002"



def server_request(host, port):
    con_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con_socket.connect((host, port))

        #data = get_markers()
        data = "bellabito"
        data = data.encode('utf-8')

        con_socket.sendall(data)



    except ConnectionRefusedError:
        print("Connection to the server failed ")

    finally:
        con_socket.close()


server_request(host, port)
server_request(host, port)


