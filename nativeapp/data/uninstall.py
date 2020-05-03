#!/bin/env python3

import os
from pathlib import Path


home_dir = str(Path.home())
lib_dir = os.path.join(home_dir, '.local', 'lib', 'ee.sumzary.yt2p')

os.remove(os.path.join(lib_dir, 'host.py'))

os.remove(os.path.join(home_dir, '.config', 'chromium', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'))

os.remove(os.path.join(home_dir, '.config', 'vivaldi', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'))

os.remove(os.path.join(home_dir, '.config', 'google-chrome', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'))

os.remove(os.path.join(home_dir, '.mozilla', 'native-messaging-hosts', 'ee.sumzary.yt2p.json'))
