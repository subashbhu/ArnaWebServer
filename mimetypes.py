#This is used just to store the mime types just like a folder in the form of python directory

mimes  = {
          
          #For Text Based Files
	      
	      "html" : "text/html",
	      "css" : "text/css",
	      "js" : "text/javascript",
	      "arna" : "text/html",
	      "xhtml" : "text/html",
	      "txt" : "text/plain",

	      #For Video Files

	      "mp4" : "content/octet-stream",
	      "3gp" : "content/octet-stream",
	      "mov" : "content/octet-stream",
	      "wmv" : "content/octet-stream",
	      "avi" : "content/octet-stream",
	      "mkv" : "content/octet-stream",
	      #Browser play of the media files, source being located in the server is depreciated due to server being too weak to handle multiple requests

	      #For Pictures 
	      "jpeg" : "image/jpeg",
          "jpg" : "image/jpeg",
          "png" : "image/png",
          "ico" : "image/x-icon",
          "svg" : "image/svg+xml",

          #For Audio Files 
          "mp3" : "audio/mpeg",
          "wav" : "audio/x-wav",

          #For Document Files
          "doc" : "application/msword",


}