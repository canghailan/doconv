#! /opt/libreoffice6.0/program/python

import cgi
import cgitb
import os
import sys
import json
import uuid
import urllib.request
import subprocess
from pathlib import Path

graph = {}
with open('graph.json') as f:
    graph = json.load(f)


def get_conversion_plan(source, targets):
    conversion_plan = {source: set()}

    for target in targets:
        conversion = graph[source][target]
        if 'path' in conversion:
            path = conversion['path']
            conversion_plan[source].add(path[0])

            for i in range(len(path) - 1):
                step = path[i]
                step_next = path[i + 1]
                if step not in conversion_plan:
                    conversion_plan[step] = set()
                conversion_plan[step].add(step_next)

    return conversion_plan


workspace = '/workspace/'

request = cgi.FieldStorage()
request_file = request.getvalue('file')
request_from = request.getvalue('from')
request_to = request.getlist('to')

name = os.path.basename(request_file)
base_name, extension_name = os.path.splitext(name)

temp = Path(workspace).joinpath(str(uuid.uuid4()))
temp.mkdir(parents=True)

paramters = {
    'temp': str(temp),
    'name': name,
    'base_name': base_name
}

conversion_plan = get_conversion_plan(request_from, request_to)

''' prepare source '''
urllib.request.urlretrieve(request_file, str(temp.joinpath(name)))


def convert(source):
    targets = conversion_plan[source]
    for target in targets:
        cmd = [e.format_map(paramters) for e in graph[source][target]['exec']]
        child = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        child_return = child.communicate()
        convert(target)


convert(request_from)

print('Content-Type: application/json;charset=utf-8')
print('')
print(json.dumps({'file': request_file, 'from': request_from, 'to': request_to, 'cmd_pdf': ' '.join(
    cmd_pdf), 'cmd_jpg': ' '.join(cmd_jpg), 'temp': str(temp), 'base_name': base_name, 'extension_name': extension_name}))
