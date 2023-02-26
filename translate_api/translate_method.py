def get_translate(information):
    import requests
    import json
    apiKey = '953FNW0-7SH4AYS-M8K5M1P-PCCEVET'

    headers = {
        'X-API-Key': apiKey,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    data = {"texts": [information["text"]], "to": [information["to_lang"], ], "from": information["from_lang"]}

    response = requests.post('https://api.lecto.ai/v1/translate/text', headers=headers, data=json.dumps(data))

    return response