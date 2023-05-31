import Client

# TODO:
#   1. save token after login

sock = Client.Client()

host = input('Введите хост(def: localhost): ')
host = host if host != '' else 'localhost'
port = input('Введите порт(def: 9090): ')
port = int(port) if port != '' else 9090

sock.connect(host, port)
# sock.send_auth_cookie()

while True:
    # data, type = sock.recv(1024)
    #
    # if type == 'info+':
    #     print(data)
    #     continue
    # elif type == 'info':
    #     print(data)
    #     cmd = input('>:')
    # elif type == 'prompt':
    #     cmd = input(data+'>:')
    #     sock.send(cmd)
    #     continue
    # elif type == 'cookie':
    #     sock.save_cookie(data)
    #     continue
    #
    # # cmd = input('>:')
    #
    # if cmd == 'exit':
    #     sock.disConnect()
    #     break
    #
    # sock.send(cmd)

    cmd = input('>:')

    if cmd == 'exit':
        sock.disConnect()
        break

    sock.send(cmd)

    data, type = sock.recv(1024)
    print(data)
