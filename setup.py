import os
import subprocess
import zipfile

target_dir = os.path.expanduser("~/.local/bin")
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for zip_file in ['pew.zip', 'websrv.zip']:
    if os.path.isfile(zip_file):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(target_dir)

subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "-y", "mono-complete"])

shell = os.environ.get("SHELL", "")
bash_rc = os.path.expanduser("~/.bashrc")
zsh_rc = os.path.expanduser("~/.zshrc")
alias_command = "alias pew='python3 ~/.local/bin/pew/pew.py'\n"

if "bash" in shell and os.path.isfile(bash_rc):
    with open(bash_rc, "a") as f:
        f.write(alias_command)
    shell_rc = bash_rc
elif "zsh" in shell and os.path.isfile(zsh_rc):
    with open(zsh_rc, "a") as f:
        f.write(alias_command)
    shell_rc = zsh_rc
else:
    shell_rc = None

if shell_rc:
    print("\033[37mDon't forget to source your shell\033[0m")
    print(f"  \033[32msource {shell_rc}\033[0m")
