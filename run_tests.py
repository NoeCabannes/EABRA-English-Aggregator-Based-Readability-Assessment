import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERR:", result.stderr)
    return result.returncode

run(f"{sys.executable} -m pip install pydantic==1.10.15 spacy==3.7.2")
run(f"{sys.executable} -m spacy download en_core_web_sm")
run(f"{sys.executable} test_eabra.py")
