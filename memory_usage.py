import resource

rsrc = resource.RLIMIT_DATA
soft, hard = resource.getrlimit(rsrc)
print ('Soft limit starts as  :', soft)

# resource.setrlimit(rsrc, (1024, hard)) #limit to one kilobyte

soft, hard = resource.getrlimit(rsrc)
print ('Soft limit changed to :', soft)