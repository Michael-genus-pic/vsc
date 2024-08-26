
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from utils.config import config

apis = config['apis']

upstream = ""

fileContent = "server {\n\
    listen       80;\n\
    location / {\n\
        proxy_pass http://html;\n\
    }\n"

for api, apiDetail in apis.items():
    print (f" Adding forwarding for {api} at {apiDetail['port']}")
    upstream += f"\
upstream group_{api}{{\n\
    server {api}1:{apiDetail['port']};\n\
    server {api}2:{apiDetail['port']};\n\
}}\n\
    "
    fileContent += f"    location /{api} {{ \n\
        proxy_pass http://group_{api};\n\
    }}\n"

fileContent += "}"
file = open(f"conf.d/default.conf", "w")
file.write(f"{upstream}\n{fileContent}")
file.close()