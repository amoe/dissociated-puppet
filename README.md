# dissociated-puppet

* Tested on CentOS 7
* Spawns on port 57292
* Version-locked to 4.8.2
* Uses ruby 2.3.3
* Python 3.5+ (available from IUS as `python35`)
* You need to configure the python3 link
* Basic development tools needed: `gcc`, `openssl-devel` (`libssl1.0-dev` on Debian)

## Configure python3 link

alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 50
alternatives --config python3


## Masterless usage with an existing Puppet repository

    sudo /opt/dissociated-puppet/bin/puppet module install --target-dir=modules puppetlabs-apache

From inside your puppet manifests directory, you can do the following:

    sudo /opt/dissociated-puppet/bin/puppet apply --verbose --no-splay --modulepath ./modules masterless/my-host.pp

The default node will have its manifest applied.  You can specify it as such.

## Smoke test for masterless

    node default {
        package { 'cowsay': status => installed }
    }

Then you can just run:

    sudo /opt/dissociated-puppet/bin/puppet  apply test.pp


You can run the `print_config.sh` script to print the config.

Or run `apply.sh` to apply a manifest.

You should get something akin to the following:

    -bash-4.2$ sudo sh apply.sh test-centos.pp 
    Notice: Compiled catalog for myhost.solasistim.net in environment production in 0.46 seconds
    Notice: /Stage[main]/Main/Node[default]/Package[fortune-mod]/ensure: created
    Notice: Applied catalog in 3.71 seconds

# Install

# Contended resources

Multiple puppets on a system will be able to store their own cronjobs.  That is,
a dissociated-puppet can create cronjobs that will remain untouched by the system
puppet.
