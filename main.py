import struct
import os


class BinaryReader:
    """
    x 	pad byte 	        no value
    c 	char 	            bytes of length 1
    b 	signed char 	    integer 	    1
    B 	unsigned char 	    integer 	    1
    ? 	_Bool 	            bool 	        1
    h 	short 	            integer 	    2
    H 	unsigned short 	    integer 	    2
    i 	int 	            integer 	    4
    I 	unsigned int 	    integer 	    4
    l 	long 	            integer 	    4
    L 	unsigned long 	    integer 	    4
    q 	long long 	        integer 	    8
    Q 	unsigned long long 	integer 	    8
    n 	ssize_t 	        integer
    N 	size_t 	            integer
    f 	float 	            float 	        4
    d 	double 	            float 	        8
    s 	char[] 	            bytes
    p 	char[] 	            bytes
    P 	void * 	            integer
    """

    def __init__(self, file_name):
        self.file = open(file_name, 'rb')

    def read(self, fmt, length=1):
        fmt *= length
        type_size = struct.calcsize(fmt)
        value = self.file.read(type_size)
        if type_size != len(value):
            raise EOFError
        return struct.unpack(fmt, value)


def main():
    file = 'data.win'
    output_dir = os.getcwd()
    full_size = os.path.getsize(file)
    f = BinaryReader(file)
    try:
        os.mkdir(os.path.join(output_dir, 'CHUNK'))
    except OSError:
        pass

    chunk_offset = 0
    while chunk_offset < full_size:
        chunk_name = f.read('c', 4)
        print(chunk_name)
        chunk_size = f.read('I')
        print(chunk_size)

if __name__ == '__main__':
    main()