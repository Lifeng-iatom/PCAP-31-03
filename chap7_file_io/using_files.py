#!/usr/bin/env python3.11
my_file = open("xmen.txt",'w+')
my_file.write('beast\n')
my_file.write('phoenix\n')
my_file.writelines([
      'cyclops\n',
      'Bishop\n',
      'Night Crawler\n'
])
my_file.seek(0)
print(my_file.read())
my_file.close()