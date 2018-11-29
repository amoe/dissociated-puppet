#! /bin/sh

puppet_root=/opt/dissociated-puppet
confdir="${puppet_root}/etc/puppet"
ruby_path="${puppet_root}/lib/ruby/site_ruby"

if [ "$#" -eq 0 ]; then
    echo "Need a manifest to apply." >&2
    exit 1
fi

"${puppet_root}/bin/ruby" -I"$ruby_path" "${puppet_root}/bin/puppet" apply \
  --confdir "$confdir" --verbose --debug \
  "$@"
