import shutil
import os
import subprocess

def set_up_vardir():
    subprocess.check_call(['sudo', 'mkdir', '/opt/dissociated-puppet/var/cache'])

def copy_configuration():
    subprocess.check_call(['sudo', 'cp', 'puppet.conf', '/opt/dissociated-puppet/etc/puppet/puppet.conf'])
