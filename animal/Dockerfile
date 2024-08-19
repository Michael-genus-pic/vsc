# 
FROM python:3.9-slim

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
COPY ./utils /code/utils
COPY ./utils/apiFunctions_docker.py /code/utils/apiFunctions.py
COPY ./utils/addresses_docker.py /code/utils/addresses.py

# 
CMD ["fastapi", "run", "app/server.py", "--port", "3000"]