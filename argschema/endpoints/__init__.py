import json

import requests

from .endpoint import Endpoint
from .addable_arg import AddableArg
from .endpoint_spec import EndpointSpec


def write_to_json(data, output_json):
    if output_json is not None:
        with open(output_json, 'w') as jf:
            json.dump(data, jf)
    else:
        print(data)


builtin_sources = EndpointSpec(**{
    'json': Endpoint(
        lambda **k: json.load(open(k['input_json'], 'r')) if k['input_json'] is not None else {},
        AddableArg('--input_json', type=str, help='filesystem path to json containing argument values')
    ),
    'http': Endpoint(
        lambda **k: requests.get(k['uri']).json() if k['uri'] is not None else {},
        AddableArg('--uri', type=str, help='URI of gettable json-formatted argument values')
    )
})


builtin_sinks = EndpointSpec(**{
    'json': Endpoint(
        write_to_json,
        AddableArg('--output_json', type=str, help='write outputs here')
    )
})
