from pathlib import Path
import subprocess

list_fp = "./module_list.txt"

with open(list_fp, "rt") as f:
    modules_str = f.read()

modules = modules_str.split("\n")
modules = [x.strip() for x in modules if x]

module_dir = Path("../modules")

module_dir.mkdir(exist_ok=True)

git_base_cmd = "git clone git@github.com:tryton"

for module in modules:

    if not (module_dir / module).exists():

        cmd_str = f"{git_base_cmd}/{module}.git"
        subprocess.run(cmd_str, shell=True, cwd=module_dir)

module_dirs = list(module_dir.glob("*"))

for module_dir in module_dirs:

    ln_dir = Path("trytond/modules") / module_dir.name
    target = Path("../..") / module_dir

    if not ln_dir.exists():

        ln_dir.symlink_to(Path("../..") / module_dir, target_is_directory=True)

sao_path = Path("../sao")

if not sao_path.exists():

    cmd_str = f"{git_base_cmd}/sao.git"
    subprocess.run(cmd_str, shell=True, cwd="..")
