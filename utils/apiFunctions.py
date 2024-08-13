###################################################
## DO NOT EDIT THIS FILE ##########################
## THIS FILE IS TO BE GENERATED BY ################
## utils/generateApiFunction.py ###################
###################################################

import json
import requests

def httpToJson(response):
    if response.status_code  != 200:
        message = (json.loads(response._content.decode('utf-8')))
        raise Exception( f'{response.status_code}: {message}')
    else:
        return json.loads(response._content.decode('utf-8'))


class animal_v1_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/')
        return httpToJson(response)

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/v1_0/', json=realPayload)
        return httpToJson(response)

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/ident/{animalIdent}')
        return httpToJson(response)

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/v1_0/litterId/{litterId}')
        return httpToJson(response)


class animal_v2_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/')
        return httpToJson(response)

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/v2_0/', json=realPayload)
        return httpToJson(response)

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/ident/{animalIdent}')
        return httpToJson(response)

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/v2_0/litterId/{litterId}')
        return httpToJson(response)

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://127.0.0.1/animal/v2_0/addEvent/{ident}', json=realPayload)
        return httpToJson(response)


class animal_latest:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/animal/latest/')
        return httpToJson(response)

    def Addanimal ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/animal/latest/', json=realPayload)
        return httpToJson(response)

    def Getanimalbyid ( animalIdent ):
        response = requests.get(f'http://127.0.0.1/animal/latest/ident/{animalIdent}')
        return httpToJson(response)

    def Getanimalbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/animal/latest/litterId/{litterId}')
        return httpToJson(response)

    def Addevent ( ident, payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.put(f'http://127.0.0.1/animal/latest/addEvent/{ident}', json=realPayload)
        return httpToJson(response)


class litter_v1_0:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/')
        return httpToJson(response)

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/litter/v1_0/', json=realPayload)
        return httpToJson(response)

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/litterId/{litterId}')
        return httpToJson(response)

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/sire/{sire}/dam/{dam}')
        return httpToJson(response)

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/v1_0/litterMates/litterId/{litterId}')
        return httpToJson(response)

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://127.0.0.1/litter/v1_0/litterId/{litterId}/pigletIdent/{pigletIdent}')
        return httpToJson(response)


class litter_latest:
    def Getall (  ):
        response = requests.get(f'http://127.0.0.1/litter/latest/')
        return httpToJson(response)

    def AddANewLitter ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/litter/latest/', json=realPayload)
        return httpToJson(response)

    def Getlitterbyid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/latest/litterId/{litterId}')
        return httpToJson(response)

    def Getlitterbysiredam ( sire, dam ):
        response = requests.get(f'http://127.0.0.1/litter/latest/sire/{sire}/dam/{dam}')
        return httpToJson(response)

    def Getlittermatesbylitterid ( litterId ):
        response = requests.get(f'http://127.0.0.1/litter/latest/litterMates/litterId/{litterId}')
        return httpToJson(response)

    def AddPigletToLitter ( litterId, pigletIdent ):
        response = requests.put(f'http://127.0.0.1/litter/latest/litterId/{litterId}/pigletIdent/{pigletIdent}')
        return httpToJson(response)


class notification_v1_0:
    def Queueapifunction ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/v1_0/apiFunction', json=realPayload)
        return httpToJson(response)

    def Queuescheduled ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/v1_0/scheduled', json=realPayload)
        return httpToJson(response)


class notification_latest:
    def Queueapifunction ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/latest/apiFunction', json=realPayload)
        return httpToJson(response)

    def Queuescheduled ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/notification/latest/scheduled', json=realPayload)
        return httpToJson(response)


class event_v1_0:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/event/v1_0/onTest', json=realPayload)
        return httpToJson(response)

    def Geteventsbyident ( ident ):
        response = requests.get(f'http://127.0.0.1/event/v1_0/ident/{ident}')
        return httpToJson(response)


class event_latest:
    def Addontestevent ( payload ):
        realPayload = json.loads(json.dumps(payload, indent=4, sort_keys=True, default=str))
        response = requests.post(f'http://127.0.0.1/event/latest/onTest', json=realPayload)
        return httpToJson(response)

    def Geteventsbyident ( ident ):
        response = requests.get(f'http://127.0.0.1/event/latest/ident/{ident}')
        return httpToJson(response)

