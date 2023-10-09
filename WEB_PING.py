import subprocess
import os
import time
from colorama import Fore,Back


os.system('figlet WEB PING | lolcat')
print('\n\n')

ping=input(Fore.GREEN+'Enter ip or web link>>>   '+Fore.RED)
print('\n\n')
subprocess.call(f'ping {ping}',shell=True)
