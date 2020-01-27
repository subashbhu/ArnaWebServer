import os
import sys
import mimetypes

def serve(request, directory, header,):
    
    method = header[0].split(" ")[0]

    if(method == "GET"):
        file = open(directory, "rb");
        content = file.read()
        file.close()

        file_extension = directory.split(".")[-1];
        
        try:
        	mime = mimetypes.mimes[file_extension];
        except:
        	mime = "text/plain";
        
        response_header = '''HTTP/1.1 200 OK\nContent-Type: '''+mime+'''\n\n'''
        request.sendall(response_header.encode('utf-8') + content)

