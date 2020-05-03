#!/bin/env python3

import json
import os
from pathlib import Path
from shutil import copyfile


manifest_chrome = json.load(open('manifest-chromium.json'))
manifest_firefox = json.load(open('manifest-firefox.json'))

home_dir = str(Path.home())
lib_dir = os.path.join(home_dir, '.local', 'lib', 'ee.sumzary.yt2p')

manifest_chrome['path'] = manifest_firefox['path'] = os.path.join(lib_dir, 'host.py')

os.makedirs(os.path.join(lib_dir), exist_ok=True)
copyfile('host.py', os.path.join(lib_dir, 'host.py'))
os.chmod(os.path.join(lib_dir, 'host.py'), 0o0764)

os.makedirs(os.path.join(home_dir, '.config', 'chromium', 'NativeMessagingHosts'), exist_ok=True)
json.dump(manifest_chrome, open(os.path.join(home_dir, '.config', 'chromium', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'), 'w'))

os.makedirs(os.path.join(home_dir, '.config', 'vivaldi', 'NativeMessagingHosts'), exist_ok=True)
json.dump(manifest_chrome, open(os.path.join(home_dir, '.config', 'vivaldi', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'), 'w'))

os.makedirs(os.path.join(home_dir, '.config', 'google-chrome', 'NativeMessagingHosts'), exist_ok=True)
json.dump(manifest_chrome, open(os.path.join(home_dir, '.config', 'google-chrome', 'NativeMessagingHosts', 'ee.sumzary.yt2p.json'), 'w'))

os.makedirs(os.path.join(home_dir, '.mozilla', 'native-messaging-hosts'), exist_ok=True)
json.dump(manifest_firefox, open(os.path.join(home_dir, '.mozilla', 'native-messaging-hosts', 'ee.sumzary.yt2p.json'), 'w'))
