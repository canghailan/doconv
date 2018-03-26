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

workspace = '/workspace/'

request = cgi.FieldStorage()
request_file = request.getvalue('file')
request_from = request.getvalue('from')
request_to = request.getlist('to')

temp = Path(workspace).joinpath(str(uuid.uuid4()))
temp.mkdir(parents=True)

name = os.path.basename(request_file)
base_name, extension_name = os.path.splitext(name)

paramters = {
    'temp': str(temp),
    'name': name,
    'base_name': base_name
}

urllib.request.urlretrieve(request_file, str(temp.joinpath(name)))

cmd_pdf = [
    "unoconv",
    "-f",
    "pdf",
    "-o",
    "{temp}/{base_name}.pdf",
    "{temp}/{name}"
]
cmd_pdf = [e.format_map(paramters) for e in cmd_pdf]

child = subprocess.Popen(cmd_pdf, stdout=subprocess.PIPE)
child_return = child.communicate()

cmd_jpg = [
    "convert",
    "-density",
    "200",
    "-quality",
    "100",
    "-sharpen",
    "0x1.0",
    "{temp}/{base_name}.pdf",
    "{temp}/{base_name}.jpg"
]
cmd_jpg = [e.format_map(paramters) for e in cmd_jpg]

child = subprocess.Popen(cmd_jpg, stdout=subprocess.PIPE)
child_return = child.communicate()

print('Content-Type: application/json;charset=utf-8')
print('')
print(json.dumps({'file':request_file, 'from': request_from, 'to': request_to, 'cmd_pdf': ' '.join(cmd_pdf), 'cmd_jpg': ' '.join(cmd_jpg), 'temp': str(temp), 'base_name': base_name, 'extension_name': extension_name}))