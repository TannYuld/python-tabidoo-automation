import subprocess, pkg_resources

dependencies = {'platform', 'psutil', 'request', 'keyboard', 'colorama', 'pyinstaller'}

def is_module_installed(module):
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    return module.lower() in installed_packages

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def check_and_install_module(module):
    if not is_module_installed(module):
        run_command("pip install " + module)

for dependency in dependencies:
    check_and_install_module(dependency)

# run_command('pip install platform')
# run_command('pip install psutil')
# run_command('pip install requests')
# run_command('pip install keyboard')
# run_command('pip install colorama')
# run_command('pip install pyinstaller')

run_command('pyinstaller -F main.py')

print('Compile process completed...')