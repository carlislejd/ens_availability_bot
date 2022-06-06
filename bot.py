import json
import requests

from os import getenv
from dotenv import load_dotenv

load_dotenv()


api = getenv('THEGRAPH')

registered = []
avaliable = []

with open('name_list.txt', 'r') as name_list:
    for name in name_list:
        name = name.replace('\n', '')
        name = name.lower()
        if len(name) >= 3:
            print(name)
            
            query = """{
                domains(where: {labelName: "foobar"}) {
                    id
                    name
                    labelName
                    createdAt
                }
                }
            """

            query = query.replace('foobar', str(name))
            r = requests.post(f'https://gateway.thegraph.com/api/{api}/subgraphs/id/EjtE3sBkYYAwr45BASiFp8cSZEvd1VHTzzYFvJwQUuJx', json={'query': query})
            json_data = json.loads(r.text)
            print(json_data)

            if json_data['data']['domains']:
                registered.append(name)
            else:
                avaliable.append(name)

with open('avaliable.txt', 'a') as f:
    for item in avaliable:
        f.write("%s\n" % item)