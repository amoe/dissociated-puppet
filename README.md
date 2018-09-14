# dissociated-puppet

* Tested on CentOS 7
* Spawns on port 57292
* Version-locked to 4.8.2
* Uses ruby 2.3.3
* Python 3.4+ (available from EPEL as `python34`)
* Basic development tools needed: `gcc`, `openssl-devel`

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

You should get something akin to the following:

    Notice: Compiled catalog for myhost.solasistim.net in environment production in 0.60 seconds
    Notice: /Stage[main]/Main/Node[default]/Package[cowsay]/ensure: created
    Notice: Applied catalog in 1.91 seconds

