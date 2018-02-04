#!/bin/bash -x
cd "$(dirname "$0")"
TMP=$(mktemp -d)
out=$TMP/smtp2disk-config-$(grep '^ *Version:' smtp2disk-config.spec  | sed 's/^ *//; s/Version://; s/^ *//; s/ *$//').tar.gz
git archive -v -o $out HEAD
SRCRPM=$(rpmbuild -ts $out | grep ^Wrote | grep src.rpm$ | sed 's/^Wrote: //')
mock $SRCRPM


