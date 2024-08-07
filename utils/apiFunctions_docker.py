###################################################
## DO NOT EDIT THIS FILE ##########################
## THIS FILE IS TO BE GENERATED BY ################
## utils/generateApiFunction.py ###################
###################################################

import json
import requests


class animal_v1_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/v1_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class animal_v2_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/v2_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://127.0.0.1/animal/v2_0/addEvent/{ident}', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class animal_latest:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/latest/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/latest/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/latest/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/latest/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://127.0.0.1/animal/latest/addEvent/{ident}', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class litter_v1_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/litter/v1_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/sire/{sire}/dam/{dam}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/litterMates/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://127.0.0.1/litter/v1_0/litterId/{litterId}/pigletIdent/{pigletIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class litter_latest:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/litter/latest/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/litter/latest/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/latest/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://127.0.0.1/litter/latest/sire/{sire}/dam/{dam}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/latest/litterMates/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://127.0.0.1/litter/latest/litterId/{litterId}/pigletIdent/{pigletIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class notification_v1_0:
    def Addnewqueue ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/v1_0/queue', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class notification_latest:
    def Addnewqueue ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/latest/queue', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class event_v1_0:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/event/v1_0/onTest', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Geteventsbyident ( ident ):
        response = requests.post(f'http://127.0.0.1/event/v1_0/ident/{ident}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class event_latest:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/event/latest/onTest', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Geteventsbyident ( ident ):
        response = requests.post(f'http://127.0.0.1/event/latest/ident/{ident}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

import json
import requests


class animal_v1_0:
    def Getall (  ):
        response = requests.get(f'http://animal:3000/animal/v1_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://animal:3000/animal/v1_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://animal:3000/animal/v1_0/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://animal:3000/animal/v1_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class animal_v2_0:
    def Getall (  ):
        response = requests.get(f'http://animal:3000/animal/v2_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://animal:3000/animal/v2_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://animal:3000/animal/v2_0/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://animal:3000/animal/v2_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://animal:3000/animal/v2_0/addEvent/{ident}', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class animal_latest:
    def Getall (  ):
        response = requests.get(f'http://animal:3000/animal/latest/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://animal:3000/animal/latest/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://animal:3000/animal/latest/ident/{animalIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://animal:3000/animal/latest/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://animal:3000/animal/latest/addEvent/{ident}', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class litter_v1_0:
    def Getall (  ):
        response = requests.get(f'http://litter:3001/litter/v1_0/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://litter:3001/litter/v1_0/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://litter:3001/litter/v1_0/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://litter:3001/litter/v1_0/sire/{sire}/dam/{dam}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://litter:3001/litter/v1_0/litterMates/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://litter:3001/litter/v1_0/litterId/{litterId}/pigletIdent/{pigletIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class litter_latest:
    def Getall (  ):
        response = requests.get(f'http://litter:3001/litter/latest/')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://litter:3001/litter/latest/', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://litter:3001/litter/latest/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://litter:3001/litter/latest/sire/{sire}/dam/{dam}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://litter:3001/litter/latest/litterMates/litterId/{litterId}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://litter:3001/litter/latest/litterId/{litterId}/pigletIdent/{pigletIdent}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class notification_v1_0:
    def Addnewqueue ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://notification:3002/notification/v1_0/queue', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class notification_latest:
    def Addnewqueue ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://notification:3002/notification/latest/queue', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class event_v1_0:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://event:3003/event/v1_0/onTest', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Geteventsbyident ( ident ):
        response = requests.post(f'http://event:3003/event/v1_0/ident/{ident}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))


class event_latest:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://event:3003/event/latest/onTest', json=realPayload)
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

    def Geteventsbyident ( ident ):
        response = requests.post(f'http://event:3003/event/latest/ident/{ident}')
        if response.status_code  != 200:
            message = (json.loads(response._content.decode('utf-8')))
            raise Exception( f'{response.status_code}: {message}')
        else:
            return json.loads(response._content.decode('utf-8'))

