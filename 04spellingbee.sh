#softlink
ln -s ../MCB185/data/dictionary.gz ./dictionary.gz

#original command
gunzip -c dictionary.gz | grep -E "r" | grep -E "[acinozr].{2}+[acinozr]" | grep -v "[bdefghjklmpqstuvwxy]"

#modified command
gunzip -c dictionary.gz | grep -E "r" | grep -Ev "[^acinozr]" | grep ....