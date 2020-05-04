#!/usr/bin/env python3
# Moddified version of https://github.com/mdn/webextensions-examples/blob/master/native-messaging/app/ping_pong.py

import os
import sys
import time
import json
import struct
import select


def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)


def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}


def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()


start_time = time.time()
while True:
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        receivedMessage = getMessage()
        if receivedMessage == "ping":
            sendMessage(encodeMessage("pong3"))
        if 'command' in receivedMessage.keys():
            sendMessage(encodeMessage(True))
            os.system(receivedMessage['command'] + ' &')
            break

    if time.time() - start_time > 1:
        break

    time.sleep(0.01)
