#!/usr/bin/python

import os, sys
import md5, multiprocessing as mp

with open(sys.argv[1]) as f:
        door_id = f.readline().strip()

base_md5 = md5.new(door_id)

password = dict()
index = 0

while len(password) < 8:
        if (index % 1600000) == 0:
                print str(index)

        md5_list = [ base_md5.copy() for i in range(mp.cpu_count()) ]

        for i in range(len(md5_list)):
                md5_list[i].update(str(index + i))

        md5_digests = map(lambda x:x.hexdigest(), md5_list)

        for digest in md5_digests:
                if digest.startswith("00000"):
                        password_index = digest[5]
                        if password_index in ["0", "1", "2", "3", "4", "5", "6", "7"] \
                        and (int(password_index) not in password):
                                password[int(password_index)] = digest[6]
                                print "".join(password.values())

        index += mp.cpu_count()

