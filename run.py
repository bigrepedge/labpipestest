
import logging
import os

logging.basicConfig(level=logging.INFO)

from app import app, opc_ua_machine

try:
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        opc_ua_machine.start(virtual=True)
    app.run(host='localhost', port=5000, debug=True, ssl_context = ('cert.pem', 'privkey.pem')) #added self signed certificate and private key alongwith https
finally:
    opc_ua_machine.stop()
