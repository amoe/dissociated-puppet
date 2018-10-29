#! /bin/sh

puppet_root=/opt/dissociated-puppet
confdir="${puppet_root}/etc/puppet"
ruby_path="${puppet_root}/lib/ruby/site_ruby"

"${puppet_root}/bin/ruby" -I"$ruby_path" "${puppet_root}/bin/puppet" config \
  --confdir "$confdir" \
  print
