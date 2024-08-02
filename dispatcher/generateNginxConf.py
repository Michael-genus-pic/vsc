
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from utils.config import config

apis = config['apis']

fileContent = "server {\n\
    listen       80;\n\
    location / {\n\
        index index.html;\n\
    }\n"

for api, apiDetail in apis.items():
    print (f" Adding forwarding for {api} at {apiDetail['port']}")
    fileContent += f"location /{api} {{ \n\
        proxy_pass http://{api}:{apiDetail['port']}/{api};\n\
    }}\n"

fileContent += "}"
file = open(f"conf.d/default.conf", "w")
file.write(fileContent)
file.close()