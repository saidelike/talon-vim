find / -name "Foo.txt" 2>/dev/null
find / -iname "*foo*txt" 2>/dev/null
find ~/Documents -ls
find ~/Documents/ -name "_txt" -exec grep -Hi penguin {} \;
find ~ -type f
find ~ -type f,l -name "notebook_"
find ~/Public -type d
find ~/Public -type d
find /var/log -iname "*~" -o -iname "*log*" -mtime +30
find /var/log -iname "*~" -o -iname "_log_" -mtime -7
find /var/log -iname "*~" -o -iname "*log*" -mtime -7
find / -type d -name 'img' -ipath "*public_html/example.com\*" 2>/dev/null
