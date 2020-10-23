FROM nvcr.io/nvidia/pytorch:20.03-py3

# Set the working directory.
WORKDIR /usr/src/app

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y apt-utils
RUN DEBIAN_FRONTEND=noninteractive apt install -y pciutils

# Copy the file from your host to your current location.
COPY requirements.txt .

# Run the command inside your image filesystem.
RUN pip install -r requirements.txt


# Add metadata to the image to describe which port the container is listening on at runtime.
# EXPOSE 8080

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Run the specified command within the container.
CMD [ "python", "app.py" ]

