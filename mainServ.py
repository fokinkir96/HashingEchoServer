from Server import Server

s = Server()
while True:
    client = s.wait_client()
    data = False
    while data != 'exit':
        try:
            data, type = client.recv(1024)
        except Exception as e:
            print(e)
        # if data == '':
        #     break
        client.send(data)
    else:
        client.disConnect()
        s.connected.remove(client)
