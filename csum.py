import hashlib

def getmd5(string, isfile=False):
    """ Computes the md5 hash of the string.
        If the isfile flag is true, treats string as filepath to a binary file
        and computes the md5 hash of the file.
    """

    m = hashlib.md5()
    if isfile:
        with open(string, 'rb') as f:
            while True:
                chunk = f.read(1024*1024) #read in chunks of 1MB
                if not chunk:
                    break
                m.update(chunk)
    else:
        m.update(string)

    return str(m.hexdigest())

def verify(string, checksum, algorithm='md5', isfile=False):
    """ Given a string or a filepath and it's expected checksum, verifies if it
        is correct.
        The isfile flag determines whether the string is treated as a filepath.
        Choice of algorithms available: md5, sha512
    """

    if algorithm == 'md5':
        csum = getmd5(string, isfile=isfile)
        return True if csum == checksum else False

    elif algorithm == 'sha512':
        # Not implemented yet
        return False