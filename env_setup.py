from pathlib import Path
import subprocess

list_fp = "./module_list.txt"
release_branch = "6.2"

with open(list_fp, "rt") as f:
    modules_str = f.read()

modules = modules_str.split("\n")
modules = [x.strip() for x in modules if x and not x.startswith("#")]

module_dir = Path("../modules")

module_dir.mkdir(exist_ok=True)

git_base_cmd = "git clone git@github.com:tryton"

for module in modules:

    if not (module_dir / module).exists():

        cmd_str = f"{git_base_cmd}/{module}.git --branch {release_branch}"
        subprocess.run(cmd_str, shell=True, cwd=module_dir)

    ln_dir = Path("trytond/modules") / module

    if not ln_dir.exists():

        target = Path("../..") / module_dir / module
        ln_dir.symlink_to(target, target_is_directory=True)

sao_path = Path("../sao")

if not sao_path.exists():

    cmd_str = f"{git_base_cmd}/sao.git --branch {release_branch}"
    subprocess.run(cmd_str, shell=True, cwd="..")

sao_ln = Path("./sao")

if not sao_ln.is_symlink():

    sao_ln.symlink_to(sao_path, target_is_directory=True)
