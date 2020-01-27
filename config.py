host = "127.0.0.1";
port = 8080;                    

#Note :Use of port 80 may require super user or equivalent previlages
#depending upon your system configuration. 

default_pages = ["index.html","index.htm","default.html"];

#The default pages should be set in priority order. If two or more pages are available 
#in the serving directory, the pages will be served based on the order of the default_pages

maximum_concurrent_connections = 100;


#The default server directory must always reside under the dirctory of the server itself.
#Trying to change to a different directory outside will break things and no-such except-
#-ions handlers has been set till now.

#Although, it is further processed, omission of '/' or '\' or './' symbol is highly encouraged.

default_directory = "htdocs";
dir_listing = True;                

