FROM python:3.9

# Preparations
RUN groupadd -r relay && useradd --no-log-init -r -g relay relay
WORKDIR /code

# Add code
ADD relay.py requirements.txt /code/
RUN chown -R relay:relay /code

# Dependencies
RUN pip install -r requirements.txt

# Start
USER relay
CMD ["/usr/bin/env", "python3", "-u", "relay.py"]
