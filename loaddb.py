import json
from catalog.models import Mineral

def load_json():
    print('Start loading Minerals')
    with open('minerals.json', 'r') as f:
        data = json.load(f)
        for mineral in data:
            name = mineral['name']
            caption = mineral['image caption']
            img = mineral['image filename']
            fields = mineral
            del fields['name']
            del fields['image caption']
            del fields['image filename']
            mineral = Mineral(
                name=name,
                caption=caption,
                img=img,
                fields=json.dumps(fields)
            )
            mineral.save()