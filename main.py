import os
import sys
import socket
import helper
import channel
import config

# Server configurations are changed from ./config.py

os.chdir(os.getcwd() + "/" + config.default_directory)
print(os.getcwd())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);

# socket option (SO_REUSEADDR) has to be set on to prevent crashes due to port unavailability

HOST = config.host
PORT = config.port

DefaultPages = config.default_pages
MaxConn = config.maximum_concurrent_connections

server.bind((HOST, PORT))
server.listen(MaxConn)

print("Address\t\t\tRequested Directory");

while True:
    request, address = server.accept();
    
    header = request.recv(1024).decode("utf-8").split("\n")

    method = header[0].split(" ")[0];
    directory = os.getcwd() + "/" + header[0].split(" ")[1][1:];

    print(address[0] + "\t\t" + directory)

    if("." in directory):

        if(os.path.exists(directory)):
            channel.serve(request, directory, header)
        else:
            helper.showError(request, 404)

    else:
        if( os.path.exists(directory)):
            found = False
            for default_page in DefaultPages:
                if(os.path.exists(directory + "/" + default_page)):
                    channel.serve(request, directory + "/" + default_page, header)
                    found = True;
                    break

            if(found == False):
                helper.indexNotFound(request, directory)

        else:
            helper.showError(request, 404)


    request.close()

