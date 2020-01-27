import os
import sys
import config

dir_listing = config.dir_listing;

def showError(request, number):
    print("\t\t\tError "+str(number))

    if(number == 404):
        response_header = '''HTTP/1.1 400 Not Found\nContent-Type: text/html\n\n'''

        if(os.path.exists("./ErrPages/404.html")):
       
            error_page = open("./ErrorPages/404.html","rb");
            data = error_page.read()
            error_page.close()

            response = response_header.encode("utf-8") + data;
        
            request.sendall(response);
        
        else:
        	request.sendall(response_header.encode('utf-8') + "No Such File Found".encode('utf-8'))
   

def indexNotFound(request, directory):
    if (dir_listing == True):
    	response_header = '''HTTP/1.1 200 OK\nContent-Type: text/html\n\n'''
        

