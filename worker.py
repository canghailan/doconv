#! /opt/libreoffice6.0/program/python

import cgi
import cgitb
import os
import time
import json
import uuid
import urllib.request
import urllib.parse
import subprocess
from pathlib import Path

try:
    ''' inputs '''
    BASE_DIR = '/doconv/'
    SERVER_NAME = os.environ['SERVER_NAME'] if 'SERVER_NAME' in os.environ else '127.0.0.1'
    BASE_URI = os.environ['BASE_URI'] if 'BASE_URI' in os.environ else 'http://{SERVER_NAME}/doconv/'.format(SERVER_NAME=SERVER_NAME)

    req = cgi.FieldStorage()
    req_file = req.getvalue('file')
    req_from = req.getvalue('from')
    req_to = req.getlist('to')
    req_callback = req.getvalue('callback')

    graph = {}
    with open('graph.json') as f:
        graph = json.load(f)

    ''' process inputs '''
    file_name = os.path.basename(req_file)
    base_name, extension_name = os.path.splitext(file_name)
    temp_name = str(uuid.uuid4())

    base_dir = Path(BASE_DIR).joinpath(temp_name)
    base_dir.mkdir(parents=True)

    base_uri = urllib.parse.urljoin(BASE_URI, temp_name + '/')

    if not req_from:
        req_from = extension_name[1:]

    def generate_conversion_plan(source, targets):
        conversion_plan = {source: set()}

        for target in targets:
            source_graph = graph[source]
            if target in source_graph:
                conversion = source_graph[target]

                if 'path' in conversion:
                    path = conversion['path']

                    conversion_plan[source].add(path[0])
                    for i in range(len(path) - 1):
                        step = path[i]
                        step_next = path[i + 1]
                        if step not in conversion_plan:
                            conversion_plan[step] = set()
                        conversion_plan[step].add(step_next)
                else:
                    conversion_plan[source].add(target)

        return conversion_plan

    conversion_plan = generate_conversion_plan(req_from, req_to)

    paramters = {
        'base_uri': base_uri,
        'base_dir': str(base_dir),
        'file_name': file_name,
        'base_name': base_name
    }

    ''' prepare '''
    urllib.request.urlretrieve(req_file, str(base_dir.joinpath(file_name)))

    ''' convert '''
    output = {
        'source': {
            'format': req_from,
            'uri': [urllib.parse.urljoin(base_uri, file_name)]
        },
        'targets': [
        ]
    }

    def convert(source):
        if (source in conversion_plan):
            targets = conversion_plan[source]
            for target in targets:
                program = [e.format_map(paramters)
                           for e in graph[source][target]['program']]

                timpstamp = time.time()
                child = subprocess.Popen(program, stdout=subprocess.PIPE)
                child_return = child.communicate()
                conversion_time = time.time() - timpstamp

                output['targets'].append({
                    'format': target,
                    'uri': [urllib.parse.urljoin(base_uri, f) for f in os.listdir(str(base_dir)) if f.endswith('.' + target)],
                    'time': str(conversion_time) + 's'
                })
                convert(target)

    convert(req_from)

    ''' output '''

    print('Content-Type: application/json;charset=utf-8')
    print('')
    print(json.dumps(output))
except BaseException as e:
    print('Content-Type: application/json;charset=utf-8')
    print('')
    print(json.dumps({'error': str(e)}))
