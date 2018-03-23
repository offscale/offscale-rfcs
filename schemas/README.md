## JSON-schema generation
After `pip install genson` run:

```python
from os import listdir
import json
import yaml
import genson

def as_dict(fname):
    with open(fname) as f:
        return fname, yaml.load(f)

def to_schema(fname, *ds):
    s = genson.Schema()
    s.add_schema({"type": "object", "properties": {}})
    for d in ds:
      s.add_object(d)
    with open(fname.replace('.yml', '.schema.json'), 'wt') as f:
          f.write(s.to_json(indent=4))

def yml_out(fname):
    with open(fname) as f0, open(fname.replace('.json', '.yml'), 'wt') as f1:
        yaml.safe_dump(json.load(f0), f1,  default_flow_style=False)

ymls = tuple(as_dict(f) for f in listdir('.') if f.endswith('.yml'))
to_schema('service.schema.json', *(yml[1] for yml in ymls if yml[0] in ('deploy.yml', 'redis-service.yml')))
to_schema(*next((yml[0], yml[1]) for yml in ymls if yml[0] == 'paas-package.yml'))
tuple(yml_out(f) for f in listdir('.') if f.endswith('.json'))
```
