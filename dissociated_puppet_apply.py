#! /usr/bin/python3

import subprocess
import os
import sys

puppet_root = "/opt/dissociated-puppet"
confdir = os.path.join(puppet_root, "etc/puppet")
ruby_lib_path = os.path.join(puppet_root, "lib/ruby/site_ruby")
ruby_bin_path = os.path.join(puppet_root, "bin/ruby")
puppet_bin_path = os.path.join(puppet_root, "bin/puppet")

manifest = sys.argv[1]

subprocess.check_call([
    ruby_bin_path,
    "-I", ruby_lib_path,
    puppet_bin_path,
    "apply",
    "--confdir", confdir,
    "--modulepath", './modules',
    "--verbose", "--debug",
    manifest
])
