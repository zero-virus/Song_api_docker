# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /song_api_docker

# Set the working directory to /music_service
WORKDIR /song_api_docker

# Copy the current directory contents into the container at /music_service
ADD . /song_api_docker/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

CMD bash -c "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:$PORT"