# #!/usr/bin/python3
# 1 Byte = 8 Bits
# 1 KB = 1024 Bytes
# 1 MB = 1024 * 1024 Bytes
# 1 GB = 1024 * 1024 * 1024 Bytes
# 1 TB = 1024 * 1024 * 1024 * 1024 Bytes

def btm(bytes):
    mb = 1024**2
    result = bytes / mb
    return result
#    print('%.2f' %  (result))

def btg(bytes):
    gb = 1024**3
    result = bytes / gb
    return result
 #   print('%.2f' % (result))
