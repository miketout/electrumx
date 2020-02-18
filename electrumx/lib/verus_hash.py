# Portions Copyright (c) 2016 kste
# Portions Copyright (c) 2018 Michael Toutonghi
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''VerusHash hash function.'''

import itertools
import copy
import verushash as vh

# get padded hex for single byte
def hexbyte(x):
    return hex(x)[2:].zfill(2)

# print list of bytes in hex
def ps(s):
    return "".join([hexbyte(x) for x in s])

# verus_hash
def verus_hash(msg):
    return vh.verushash(msg)

# verus_hash
def verus_hash2(msg):
    return vh.verushash_v2(msg)

# verus_hash 2b
def verus_hash2b(msg):
    return vh.verushash_v2b(msg)

# verus_hash 2b1
def verus_hash2_1(msg):
    return vh.verushash_v2b1(msg)

def main():
    s = "Test1234"
    ary = []
    ary.extend(map(ord, s))

    # print Verus Hash output
    print("= test string = ")
    print(s + "\n")
    print("= verus_hash begins = ")

    op = verus_hash(bytes(ary))
    print("= verus_hash v1 complete - output = ")
    print(ps(op) + "\n")

    op = verus_hash2(bytes(ary))
    print("= verus_hash v2 complete - output = ")
    print(ps(op) + "\n")

    # 29674026732870ff73268723987349028fb9901270ff73268723987349028fb990128fb99012752a9b765628749812
    vh2_testdata = [0x29, 0x67, 0x40, 0x26, 0x73, 0x28, 0x70, 0xff, 0x73, 0x26, 0x87, 0x23, 0x98, 0x73, 0x49, 0x02, 0x8f, 0xb9, 0x90, 0x12, 0x70, 0xff, 0x73, 0x26, 0x87, 0x23, 0x98, 0x73, 0x49, 0x02, 0x8f, 0xb9, 0x90, 0x12, 0x8f, 0xb9, 0x90, 0x12, 0x75, 0x2a, 0x9b, 0x76, 0x56, 0x28, 0x74, 0x98, 0x12]

    op = verus_hash2(bytes(vh2_testdata))
    print("= verus_hash v2 on test data 29674026732870ff73268723987349028fb9901270ff73268723987349028fb990128fb99012752a9b765628749812 - output = ")
    print(ps(op) + "\n")

    op = verus_hash2b(bytes(vh2_testdata))
    print("= verus_hash v2b on test data 29674026732870ff73268723987349028fb9901270ff73268723987349028fb990128fb99012752a9b765628749812 - output = ")
    print(ps(op) + "\n")

    op = verus_hash2_1(bytes(vh2_testdata))
    print("= verus_hash v2.1 on test data 29674026732870ff73268723987349028fb9901270ff73268723987349028fb990128fb99012752a9b765628749812 - output = ")
    print(ps(op) + "\n")


if __name__ == '__main__':
    main()