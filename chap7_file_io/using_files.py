#!/usr/bin/env python3.11
with open("xmen.txt",'w+') as my_file:
      my_file.write('beast\n')
      my_file.write('phoenix\n')
      my_file.writelines([
            'cyclops\n',
            'Bishop\n',
            'Night Crawler\n'
      ])
      my_file.seek(0)
      my_file.write('Morph\n')
      my_file.write('Morph1')
      my_file.seek(0)
      for line in my_file.readlines():
            print(line)