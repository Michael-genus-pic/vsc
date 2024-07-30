###################################################
## DO NOT EDIT THIS FILE ##########################
## THIS FILE IS TO BE GENERATED BY ################
## utils/generateApiFunction.py ###################
###################################################

import json
import requests


class animal:
    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1:3000/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1:3000/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        response = requests.post(f'http://127.0.0.1:3000/', json=payload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class litter:
    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://127.0.0.1:3001/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://127.0.0.1:3001/sire/{sire}/dam/{dam}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1:3001/litterMates/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddANewLitter ( payload ):
        response = requests.post(f'http://127.0.0.1:3001/', json=payload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://127.0.0.1:3001/litterId/{litterId}/pigletIdent/{pigletIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class notification:
    def Addnewqueue ( payload ):
        response = requests.post(f'http://127.0.0.1:3002/queue', json=payload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class versionv1:
    def Apimessage (  ):
        response = requests.get(f'http://127.0.0.1:3003/v1_0/ep')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class versionv2:
    def Apimessage (  ):
        response = requests.get(f'http://127.0.0.1:3003/v2_0/ep')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

