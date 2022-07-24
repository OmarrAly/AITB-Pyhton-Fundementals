import os

output_stream = os.popen('echo "Hello World!"')
output_stream.read()