#!/bin/bash
i=0
for D in `find ../../ -name build -prune -o -path */ckanext-*/ckanext/*i18n/sk/LC_MESSAGES/*.po -print`
do
field[$i]=$D
((i++))
done
echo Num items: ${#field[@]}
echo Data: ${field[@]}

msgcat --use-first ${field[@]} \
    "../../ckan/ckan/i18n/sk/LC_MESSAGES/ckan.po" \
    | msgfmt - -o "../../ckan/ckan/i18n/sk/LC_MESSAGES/ckan.mo"
