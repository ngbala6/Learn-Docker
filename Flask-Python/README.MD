# Connect the Python flask application with Gunicorn WSGI

-------------------------------------------------------

# Build the Image
1. Simply execute the command from the folder "docker build . -t flask-python". This command executes the "Dockerfile" that defined as instruction that we said.

# Run the Image to container
2. After building the images, then run the command "docker run -p 9000:5000 flask-python". The gunicorn-docker is the tag name, you can also set your own name while you building your image. The -p hostport:dockerport. 9000 is the external port and the 5000 is your docker port that said in code.

# See the Output in your Browser
3. Go to your browser and type "http://localhost:9000". Now you will the output in browser as well as in Postman tool.



If driver error occured, try to restart the docker and run the image

If you do not use -p hostport:dockerport, the docker port doesn't expose from the container environment

@author

Bala Murugan N G
