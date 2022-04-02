def formCube(_sorted = False, _scramble = "scramble.bin"):
    f = open(_scramble, "rb")
    cube = {}
    byte = f.read(1)
    for i in range(26):
        #print(str(i) + " " + str(byte))
        if   i == 0 or i == 2  or i == 6  or i == 8  or i == 17 or i == 19 or i == 23 or i == 25:
            #print("corner")
            if   byte == b'\x00': cube['a'] = [1, i + 1]
            elif byte == b'\x10': cube['a'] = [2, i + 1]
            elif byte == b'\x20': cube['a'] = [3, i + 1]
            elif byte == b'\x02': cube['c'] = [1, i + 1]
            elif byte == b'\x12': cube['c'] = [2, i + 1]
            elif byte == b'\x22': cube['c'] = [3, i + 1]
            elif byte == b'\x06': cube['g'] = [1, i + 1]
            elif byte == b'\x16': cube['g'] = [2, i + 1]
            elif byte == b'\x26': cube['g'] = [3, i + 1]
            elif byte == b'\x08': cube['i'] = [1, i + 1]
            elif byte == b'\x18': cube['i'] = [2, i + 1]
            elif byte == b'\x28': cube['i'] = [3, i + 1]
            elif byte == b'\x31': cube['r'] = [1, i + 1]
            elif byte == b'\x41': cube['r'] = [2, i + 1]
            elif byte == b'\x51': cube['r'] = [3, i + 1]
            elif byte == b'\x33': cube['t'] = [1, i + 1]
            elif byte == b'\x43': cube['t'] = [2, i + 1]
            elif byte == b'\x53': cube['t'] = [3, i + 1]
            elif byte == b'\x37': cube['x'] = [1, i + 1]
            elif byte == b'\x47': cube['x'] = [2, i + 1]
            elif byte == b'\x57': cube['x'] = [3, i + 1]
            elif byte == b'\x39': cube['z'] = [1, i + 1]
            elif byte == b'\x49': cube['z'] = [2, i + 1]
            elif byte == b'\x59': cube['z'] = [3, i + 1]
            else:
                print("fucked up on corner" + " " + str(i) + " " + str(byte))
        elif i == 4 or i == 10 or i == 12 or i == 13 or i == 15 or i == 21:
            #print("center")
            if   byte == b'\x04': cube['e'] = [1,5]
            elif byte == b'\x0a': cube['k'] = [1,11]
            elif byte == b'\x0c': cube['m'] = [1,13]
            elif byte == b'\x0d': cube['n'] = [1,14]
            elif byte == b'\x0f': cube['p'] = [1,16]
            elif byte == b'\x35': cube["v"] = [1,22]
            else:
                print("fucked up on center" + " " + str(i) + " " + str(byte))
        else:
            #print("edge")
            if   byte == b'\x01': cube['b'] = [1, i + 1]
            elif byte == b'\x11': cube['b'] = [2, i + 1]
            elif byte == b'\x03': cube['d'] = [1, i + 1]
            elif byte == b'\x13': cube['d'] = [2, i + 1]
            elif byte == b'\x05': cube['f'] = [1, i + 1]
            elif byte == b'\x15': cube['f'] = [2, i + 1]
            elif byte == b'\x07': cube['h'] = [1, i + 1]
            elif byte == b'\x17': cube['h'] = [2, i + 1]
            elif byte == b'\x09': cube['j'] = [1, i + 1]
            elif byte == b'\x19': cube['j'] = [2, i + 1]
            elif byte == b'\x0b': cube['l'] = [1, i + 1]
            elif byte == b'\x1b': cube['l'] = [2, i + 1]
            elif byte == b'\x0e': cube['o'] = [1, i + 1]
            elif byte == b'\x1e': cube['o'] = [2, i + 1]
            elif byte == b'\x30': cube['q'] = [1, i + 1]
            elif byte == b'\x40': cube['q'] = [2, i + 1]
            elif byte == b'\x32': cube['s'] = [1, i + 1]
            elif byte == b'\x42': cube['s'] = [2, i + 1]
            elif byte == b'\x34': cube['u'] = [1, i + 1]
            elif byte == b'\x44': cube['u'] = [2, i + 1]
            elif byte == b'\x36': cube['w'] = [1, i + 1]
            elif byte == b'\x46': cube['w'] = [2, i + 1]
            elif byte == b'\x38': cube['y'] = [1, i + 1]
            elif byte == b'\x48': cube['y'] = [2, i + 1]
            else:
                print("fucked up on edge" + " " + str(i) + " " + str(byte))
        byte = f.read(1)
    if _sorted == True:
        return dict(sorted(cube.items(), key= lambda x: x))
    return cube

def formBin(name, cube):
    f = open(name, "wb")
    for i in cube:
        f.write(bin(cube[i]))

def bin(cubeForm):
    if   cubeForm == [1, 1]:  hexForm = b'\x00'
    elif cubeForm == [2, 1]:  hexForm = b'\x10'
    elif cubeForm == [3, 1]:  hexForm = b'\x20'
    elif cubeForm == [1, 3]:  hexForm = b'\x02'
    elif cubeForm == [2, 3]:  hexForm = b'\x12'
    elif cubeForm == [3, 3]:  hexForm = b'\x22'
    elif cubeForm == [1, 7]:  hexForm = b'\x06'
    elif cubeForm == [2, 7]:  hexForm = b'\x16'
    elif cubeForm == [3, 7]:  hexForm = b'\x26'
    elif cubeForm == [1, 9]:  hexForm = b'\x08'
    elif cubeForm == [2, 9]:  hexForm = b'\x18'
    elif cubeForm == [3, 9]:  hexForm = b'\x28'
    elif cubeForm == [1, 18]: hexForm = b'\x31'
    elif cubeForm == [2, 18]: hexForm = b'\x41'
    elif cubeForm == [3, 18]: hexForm = b'\x51'
    elif cubeForm == [1, 20]: hexForm = b'\x33'
    elif cubeForm == [2, 20]: hexForm = b'\x43'
    elif cubeForm == [3, 20]: hexForm = b'\x53'
    elif cubeForm == [1, 24]: hexForm = b'\x37'
    elif cubeForm == [2, 24]: hexForm = b'\x47'
    elif cubeForm == [3, 24]: hexForm = b'\x57'
    elif cubeForm == [1, 26]: hexForm = b'\x39'
    elif cubeForm == [2, 26]: hexForm = b'\x49'
    elif cubeForm == [3, 26]: hexForm = b'\x59'
    elif cubeForm == [1, 5]:  hexForm = b'\x04'
    elif cubeForm == [1, 11]: hexForm = b'\x0a'
    elif cubeForm == [1, 13]: hexForm = b'\x0c'
    elif cubeForm == [1, 14]: hexForm = b'\x0d'
    elif cubeForm == [1, 16]: hexForm = b'\x0f'
    elif cubeForm == [1, 22]: hexForm = b'\x35'
    elif cubeForm == [2, 2]:  hexForm = b'\x11'
    elif cubeForm == [1, 2]:  hexForm = b'\x01'
    elif cubeForm == [1, 4]:  hexForm = b'\x03'
    elif cubeForm == [2, 4]:  hexForm = b'\x13'
    elif cubeForm == [1, 6]:  hexForm = b'\x05'
    elif cubeForm == [2, 6]:  hexForm = b'\x15'
    elif cubeForm == [1, 8]:  hexForm = b'\x07'
    elif cubeForm == [2, 8]:  hexForm = b'\x17'
    elif cubeForm == [1, 10]: hexForm = b'\x09'
    elif cubeForm == [2, 10]: hexForm = b'\x19'
    elif cubeForm == [1, 12]: hexForm = b'\x0b'
    elif cubeForm == [2, 12]: hexForm = b'\x1b'
    elif cubeForm == [1, 15]: hexForm = b'\x0e'
    elif cubeForm == [2, 15]: hexForm = b'\x1e'
    elif cubeForm == [1, 17]: hexForm = b'\x30'
    elif cubeForm == [2, 17]: hexForm = b'\x40'
    elif cubeForm == [1, 19]: hexForm = b'\x32'
    elif cubeForm == [2, 19]: hexForm = b'\x42'
    elif cubeForm == [1, 21]: hexForm = b'\x34'
    elif cubeForm == [2, 21]: hexForm = b'\x44'
    elif cubeForm == [1, 23]: hexForm = b'\x36'
    elif cubeForm == [2, 23]: hexForm = b'\x46'
    elif cubeForm == [1, 25]: hexForm = b'\x38'
    elif cubeForm == [2, 25]: hexForm = b'\x48'
    return hexForm

def bing(cubeForm):
    if   cubeForm == [1, 1]:  hexForm = "00"
    elif cubeForm == [2, 1]:  hexForm = "10"
    elif cubeForm == [3, 1]:  hexForm = "20"
    elif cubeForm == [1, 3]:  hexForm = "02"
    elif cubeForm == [2, 3]:  hexForm = "12"
    elif cubeForm == [3, 3]:  hexForm = "22"
    elif cubeForm == [1, 7]:  hexForm = "06"
    elif cubeForm == [2, 7]:  hexForm = "16"
    elif cubeForm == [3, 7]:  hexForm = "26"
    elif cubeForm == [1, 9]:  hexForm = "08"
    elif cubeForm == [2, 9]:  hexForm = "18"
    elif cubeForm == [3, 9]:  hexForm = "28"
    elif cubeForm == [1, 18]: hexForm = "31"
    elif cubeForm == [2, 18]: hexForm = "41"
    elif cubeForm == [3, 18]: hexForm = "51"
    elif cubeForm == [1, 20]: hexForm = "33"
    elif cubeForm == [2, 20]: hexForm = "43"
    elif cubeForm == [3, 20]: hexForm = "53"
    elif cubeForm == [1, 24]: hexForm = "37"
    elif cubeForm == [2, 24]: hexForm = "47"
    elif cubeForm == [3, 24]: hexForm = "57"
    elif cubeForm == [1, 26]: hexForm = "39"
    elif cubeForm == [2, 26]: hexForm = "49"
    elif cubeForm == [3, 26]: hexForm = "59"
    elif cubeForm == [1, 5]:  hexForm = "04"
    elif cubeForm == [1, 11]: hexForm = "0a"
    elif cubeForm == [1, 13]: hexForm = "0c"
    elif cubeForm == [1, 14]: hexForm = "0d"
    elif cubeForm == [1, 16]: hexForm = "0f"
    elif cubeForm == [1, 22]: hexForm = "35"
    elif cubeForm == [2, 2]:  hexForm = "11"
    elif cubeForm == [1, 2]:  hexForm = "01"
    elif cubeForm == [1, 4]:  hexForm = "03"
    elif cubeForm == [2, 4]:  hexForm = "13"
    elif cubeForm == [1, 6]:  hexForm = "05"
    elif cubeForm == [2, 6]:  hexForm = "15"
    elif cubeForm == [1, 8]:  hexForm = "07"
    elif cubeForm == [2, 8]:  hexForm = "17"
    elif cubeForm == [1, 10]: hexForm = "09"
    elif cubeForm == [2, 10]: hexForm = "19"
    elif cubeForm == [1, 12]: hexForm = "0b"
    elif cubeForm == [2, 12]: hexForm = "1b"
    elif cubeForm == [1, 15]: hexForm = "0e"
    elif cubeForm == [2, 15]: hexForm = "1e"
    elif cubeForm == [1, 17]: hexForm = "30"
    elif cubeForm == [2, 17]: hexForm = "40"
    elif cubeForm == [1, 19]: hexForm = "32"
    elif cubeForm == [2, 19]: hexForm = "42"
    elif cubeForm == [1, 21]: hexForm = "34"
    elif cubeForm == [2, 21]: hexForm = "44"
    elif cubeForm == [1, 23]: hexForm = "36"
    elif cubeForm == [2, 23]: hexForm = "46"
    elif cubeForm == [1, 25]: hexForm = "38"
    elif cubeForm == [2, 25]: hexForm = "48"
    return hexForm