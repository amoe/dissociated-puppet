target_path = /usr/local/bin/dissociated-puppet-apply

install:
	cp dissociated_puppet_apply.py $(target_path)
	chmod 0755 $(target_path)
