FROM python:3.6

# This seems like "cd /app". If the folder doesn't exists, it creates automatically 
WORKDIR /app

# This adds all the files in the local folder into image
ADD . /app

# This command installs the supported packages to execute the program
RUN pip install -r requirements.txt

# Finally this Command runs in docker container
CMD ["gunicorn","-b","0.0.0.0:5000","app:app"]


# This command runs without using Gunicorn
# CMD ["python","app.py"]


# @author

# Bala Murugan N G




