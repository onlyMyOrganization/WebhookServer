import subprocess
from config import DEPLOY_SCRIPT

def run():

    subprocess.Popen(
        [
            "powershell.exe",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            DEPLOY_SCRIPT
        ]
    )
