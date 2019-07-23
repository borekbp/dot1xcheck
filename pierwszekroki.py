
f1 = open('TWR-SWT-P2_filter.txt', 'r')
f2 = open('TWR-SWT-P2_liniowo.txt', 'w')
for line in f1:
    f2.write(line.replace("mode_trunk", "trunk"))
f1.close()
f2.close()