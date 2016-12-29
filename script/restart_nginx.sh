#!/bin/shell
nginx -t &&
nginx -s reload &&
service nginx reload &&
echo 'print restart ok!'
sh /sh/reset_www.sh
exit 0