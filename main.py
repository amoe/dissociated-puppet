import urllib.request
import logging
from logging import debug
import subprocess
import util
import tarfile
import pathlib
import tempfile

PREFIX = '/opt/dissociated-puppet'
TMP_PREFIX = 'dissociated-puppet-'

ruby_url = "https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.3.tar.gz"
facter_url = "https://downloads.puppetlabs.com/facter/facter-2.4.6.tar.gz"
hiera_url = "https://downloads.puppetlabs.com/hiera/hiera-3.2.0.tar.gz"
puppet_url = "https://downloads.puppetlabs.com/puppet/puppet-4.8.2.tar.gz"



# SIZE:   17813577 bytes
# SHA1:   1014ee699071aa2ddd501907d18cbe15399c997d
# SHA256: 241408c8c555b258846368830a06146e4849a1d58dcaf6b14a3b6a73058115b7
# SHA512: 80d9f3aaf1d60b9b2f4a6fb8866713ce1e201a3778ef9e16f1bedb7ccda35aefdd7babffbed1560263bd95ddcfe948f0c9967b5077a89db8b2e18cacc7323975

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)8s - %(name)s - %(message)s"
)


facter_configuration = {
    'sitelibdir': '/opt/dissociated-puppet/lib/ruby/site_ruby',
    'bindir': '/opt/dissociated-puppet/bin',
    'mandir': '/opt/dissociated-puppet/man'
}

hiera_configuration = {
    'sitelibdir': '/opt/dissociated-puppet/lib/ruby/site_ruby',
    'bindir': '/opt/dissociated-puppet/bin',
    'mandir': '/opt/dissociated-puppet/man',
    'configdir': '/opt/dissociated-puppet/etc'
}

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

def get_install_args(configuration):
    args = []
    for k, v in configuration.items():
        args.append("--%s=%s" % (k, v))
    return args


def do(log_message, local_filename, ruby_url, expected_unpack_dir, commands):
    debug(log_message)
    urllib.request.urlretrieve(ruby_url, local_filename)
    util.extract_tar(local_filename)

    with util.cd(expected_unpack_dir):
        for command in commands:
            subprocess.check_call(command)

with tempfile.TemporaryDirectory(prefix=TMP_PREFIX) as workspace:
    debug("working in temporary directory %s", workspace)
    with util.cd(workspace):
        do("downloading ruby", 'ruby.tar.gz', ruby_url, "ruby-2.3.3", [
            ['./configure', '--prefix', PREFIX],
            ['make'],
            ['sudo', 'make', 'install']
        ])

        do("downloading facter", 'facter.tar.gz', facter_url, "facter-2.4.6", [
            ['sudo', RUBY_PATH, 'install.rb'] + get_install_args(facter_configuration)
        ])

        do("downloading hiera", 'hiera.tar.gz', hiera_url, "hiera-3.2.0", [
            ['sudo', RUBY_PATH, 'install.rb'] + get_install_args(hiera_configuration)
        ])

        do("downloading puppet", 'puppet.tar.gz', hiera_url, "puppet-4.8.2", [
            ['sudo', RUBY_PATH, 'install.rb'] + get_install_args(puppet_configuration)
        ])
