#!/usr/bin/env python3
import subprocess
import re
import os
import sys

# Some devices contain both iOS and watchOS for some reason + ignoring SE simulators
bashCommand = "xcrun xctrace list devices 2>&1 >/dev/null | grep iPhone | grep -v Watch | grep -v 'iPhone SE'"
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True, env=os.environ.copy())
output, error = process.communicate()

lines = [line for line in output.decode("utf-8").split("\n") if line]

if not lines or error:
  sys.exit(1)

r = re.compile("\(\d{1,2}\.\d{1,2}(\.\d{1,2})?\)")
device = sorted(lines, key=lambda x: re.search(r, x).group(), reverse=True)[1]
ios_version = re.search(r, device).group()[1:-1]
simulator_id = device.split()[-1][1:-1]
print(f"{ios_version} {simulator_id}")
