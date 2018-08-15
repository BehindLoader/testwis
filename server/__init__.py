from flask import Flask
from os import path

server = Flask(__name__)
server.template_folder = path.abspath('template/')