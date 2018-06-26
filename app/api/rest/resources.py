"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Api
from flask.json import jsonify
import logging
import re

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest
from app.api.am_machine import Bossy


@api_rest.route('/connect/<string:resource_id>')
class OpenOPCTunnel(BaseResource):
    def get(self, resource_id):
        Bossy.connect()
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp, 'resourceid': resource_id}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/temperature/<string:resource_id>')
class ResourceTemperature(BaseResource):

    def get(self, resource_id):
        try:
            if not Bossy.connected:
                Bossy.connect()
            if 'Extruder' in resource_id:
                extruder_num = int(re.findall(r'Extruder(\d+)', resource_id)[0])
                if extruder_num == 0:
                    return 'Invalid Extruder Number Element', 404
                target = Bossy.get_tar_temp('Extruder', extruder=extruder_num)
                actual = Bossy.get_act_temp('Extruder', extruder=extruder_num, sensor=1)
            else:
                target = Bossy.get_tar_temp(resource_id)
                actual = Bossy.get_act_temp(resource_id, sensor=1)

            timestamp = datetime.utcnow().isoformat()
            return jsonify({'timestamp': timestamp, 'target_temp': target, 'actual_temp': actual, 'heating_element': resource_id})
        except:
            return 'Invalid Temperature Element', 404

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201
