from conf.read_ini import conf

read_ini=conf()
a=read_ini.read_conf("web","pwd")
#a=read_conf("web","pwd")
print(a)