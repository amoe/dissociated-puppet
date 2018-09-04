import urllib.request
import logging
from logging import debug
import subprocess
import util
import tarfile
import pathlib

PREFIX = '/opt/dissociated-puppet'

ruby_url = "https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.3.tar.gz"
puppet_url = "https://downloads.puppetlabs.com/puppet/puppet-4.8.2.tar.gz"

# SIZE:   17813577 bytes
# SHA1:   1014ee699071aa2ddd501907d18cbe15399c997d
# SHA256: 241408c8c555b258846368830a06146e4849a1d58dcaf6b14a3b6a73058115b7
# SHA512: 80d9f3aaf1d60b9b2f4a6fb8866713ce1e201a3778ef9e16f1bedb7ccda35aefdd7babffbed1560263bd95ddcfe948f0c9967b5077a89db8b2e18cacc7323975

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)8s - %(name)s - %(message)s"
)

workspace = "/home/amoe/workspace"
util.mkdir_uncaring(workspace)

puppet_configuration = {
    'configdir': '/opt/dissociated-puppet/etc/puppet',
    'codedir': '/opt/dissociated-puppet/etc/puppet/code',
    'sitelibdir': '/opt/dissociated-puppet/lib/ruby/site_ruby',
    'vardir': '/opt/dissociated-puppet/lib/ruby/site_ruby',
    'rundir': '/opt/dissociated-puppet/var/run', 
    'logdir': '/opt/dissociated-puppet/var/log',
    'bindir': '/opt/dissociated-puppet/bin',
    'mandir': '/opt/dissociated-puppet/man'
}

RUBY_PATH = "/opt/dissociated-puppet/bin/ruby"

def get_install_args():
    args = []
    for k, v in puppet_configuration.items():
        args.append("--%s=%s" % (k, v))
    return args

with util.cd(workspace):
    debug("downloading ruby")
    local_filename = 'ruby.tar.gz'
    urllib.request.urlretrieve(ruby_url, local_filename)
    util.extract_tar(local_filename)

    with util.cd("ruby-2.3.3"):
        subprocess.check_call(['./configure', '--prefix', PREFIX])
        subprocess.check_call(['make'])
        subprocess.check_call(['sudo', 'make', 'install'])

    debug("downloading puppet")
    local_filename = 'puppet.tar.gz'
    urllib.request.urlretrieve(puppet_url, local_filename)
    util.extract_tar(local_filename)

    with util.cd("puppet-4.8.2"):
        subprocess.check_call(['sudo', RUBY_PATH, 'install.rb'] + get_install_args())
