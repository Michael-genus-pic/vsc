
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
import json


from utils.config import config

urls = config['api_urls']



fileContent = "\
###################################################\n\
## DO NOT EDIT THIS FILE ##########################\n\
## THIS FILE IS TO BE GENERATED BY ################\n\
## utils/generateApiFunction.py ###################\n\
###################################################\n\n"


endOfFunction = "\
        if response.status_code  != 200:\n\
            message = (json.loads(response._content.decode('utf-8')))\n\
            raise Exception( f'{response.status_code}: {message}')\n\
        else:\n\
            return json.loads(response._content.decode('utf-8'))\n\n\
"


fileContent += "import json\nimport requests\n\n"
for api, url in urls.items():
    fileContent += f"\nclass {api}:\n"
    response = requests.get(f"{url}/openapi.json")
    specPaths = json.loads(response._content.decode('utf-8'))['paths']
    for path, pathDetail in specPaths.items():
        for method, actionDetail in pathDetail.items():
            functionName = actionDetail['summary'].replace(" ", '')
            params = []
            payload = False
            if 'parameters' in actionDetail:
                for thisParam in actionDetail['parameters']:
                    params.append(thisParam['name'])
            if 'requestBody' in actionDetail:
                payload = True
            functionParamList = list(params)
            if payload: functionParamList.append('payload')
            functionParam = ", ".join(list(functionParamList))
            fileContent += f"    def {functionName} ( {functionParam} ):\n"
            fullPath = f"{url}{path}"
            fileContent += f"        response = requests.{method}(f'{fullPath}'{', json=payload' if payload else ''})\n"
            fileContent += endOfFunction

file = open("utils/apiFunctions.py", "w")
file.write(fileContent)
file.close()

    

