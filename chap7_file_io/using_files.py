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

with open('xmen.txt','rb') as f:
      print(f.read())

with open('xmen.txt','rb') as f:
      b_array = bytearray(10)
      f.readinto(b_array)
      print(b_array)
      new_b_array = bytearray(f.read(5))
      print(new_b_array)
