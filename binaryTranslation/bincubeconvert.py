# This is entirely for converting the virtual 
# representation of the cube from one form to 
# another. It can create a cube from a binary 
# file, convert from cube form to bin form,
# convert from bin form to cube form, and
# convert from cube form to string form.

def form_cube(_sorted=False, _scramble="scrambles/solved.cube"):
    f = open(_scramble, "rb")
    cube = {}
    byte = f.read(1)
    for i in range(26):
        if i == 0 or i == 2 or i == 6 or i == 8 or i == 17 or i == 19 or i == 23 or i == 25:
            if byte == b'\x00':
                cube['a'] = [1, i + 1]
            elif byte == b'\x10':
                cube['a'] = [2, i + 1]
            elif byte == b'\x20':
                cube['a'] = [3, i + 1]
            elif byte == b'\x02':
                cube['c'] = [1, i + 1]
            elif byte == b'\x12':
                cube['c'] = [2, i + 1]
            elif byte == b'\x22':
                cube['c'] = [3, i + 1]
            elif byte == b'\x06':
                cube['g'] = [1, i + 1]
            elif byte == b'\x16':
                cube['g'] = [2, i + 1]
            elif byte == b'\x26':
                cube['g'] = [3, i + 1]
            elif byte == b'\x08':
                cube['i'] = [1, i + 1]
            elif byte == b'\x18':
                cube['i'] = [2, i + 1]
            elif byte == b'\x28':
                cube['i'] = [3, i + 1]
            elif byte == b'\x31':
                cube['r'] = [1, i + 1]
            elif byte == b'\x41':
                cube['r'] = [2, i + 1]
            elif byte == b'\x51':
                cube['r'] = [3, i + 1]
            elif byte == b'\x33':
                cube['t'] = [1, i + 1]
            elif byte == b'\x43':
                cube['t'] = [2, i + 1]
            elif byte == b'\x53':
                cube['t'] = [3, i + 1]
            elif byte == b'\x37':
                cube['x'] = [1, i + 1]
            elif byte == b'\x47':
                cube['x'] = [2, i + 1]
            elif byte == b'\x57':
                cube['x'] = [3, i + 1]
            elif byte == b'\x39':
                cube['z'] = [1, i + 1]
            elif byte == b'\x49':
                cube['z'] = [2, i + 1]
            elif byte == b'\x59':
                cube['z'] = [3, i + 1]
            else:
                print("fucked up on corner" + " " + str(i) + " " + str(byte))
        elif i == 4 or i == 10 or i == 12 or i == 13 or i == 15 or i == 21:
            if byte == b'\x04':
                cube['e'] = [1, 5]
            elif byte == b'\x0a':
                cube['k'] = [1, 11]
            elif byte == b'\x0c':
                cube['m'] = [1, 13]
            elif byte == b'\x0d':
                cube['n'] = [1, 14]
            elif byte == b'\x0f':
                cube['p'] = [1, 16]
            elif byte == b'\x35':
                cube["v"] = [1, 22]
            else:
                print("fucked up on center" + " " + str(i) + " " + str(byte))
        else:
            if byte == b'\x01':
                cube['b'] = [1, i + 1]
            elif byte == b'\x11':
                cube['b'] = [2, i + 1]
            elif byte == b'\x03':
                cube['d'] = [1, i + 1]
            elif byte == b'\x13':
                cube['d'] = [2, i + 1]
            elif byte == b'\x05':
                cube['f'] = [1, i + 1]
            elif byte == b'\x15':
                cube['f'] = [2, i + 1]
            elif byte == b'\x07':
                cube['h'] = [1, i + 1]
            elif byte == b'\x17':
                cube['h'] = [2, i + 1]
            elif byte == b'\x09':
                cube['j'] = [1, i + 1]
            elif byte == b'\x19':
                cube['j'] = [2, i + 1]
            elif byte == b'\x0b':
                cube['l'] = [1, i + 1]
            elif byte == b'\x1b':
                cube['l'] = [2, i + 1]
            elif byte == b'\x0e':
                cube['o'] = [1, i + 1]
            elif byte == b'\x1e':
                cube['o'] = [2, i + 1]
            elif byte == b'\x30':
                cube['q'] = [1, i + 1]
            elif byte == b'\x40':
                cube['q'] = [2, i + 1]
            elif byte == b'\x32':
                cube['s'] = [1, i + 1]
            elif byte == b'\x42':
                cube['s'] = [2, i + 1]
            elif byte == b'\x34':
                cube['u'] = [1, i + 1]
            elif byte == b'\x44':
                cube['u'] = [2, i + 1]
            elif byte == b'\x36':
                cube['w'] = [1, i + 1]
            elif byte == b'\x46':
                cube['w'] = [2, i + 1]
            elif byte == b'\x38':
                cube['y'] = [1, i + 1]
            elif byte == b'\x48':
                cube['y'] = [2, i + 1]
            else:
                print("fucked up on edge" + " " + str(i) + " " + str(byte))
        byte = f.read(1)
    if _sorted:
        return dict(sorted(cube.items(), key=lambda x: x))
    return cube


def form_bin(name, cube):
    f = open(name, "wb")
    for i in cube:
        f.write(convert_cube(cube[i]))


def convert_cube(cube_form):
    if cube_form == [1, 1]:
        hex_form = b'\x00'
    elif cube_form == [2, 1]:
        hex_form = b'\x10'
    elif cube_form == [3, 1]:
        hex_form = b'\x20'
    elif cube_form == [1, 3]:
        hex_form = b'\x02'
    elif cube_form == [2, 3]:
        hex_form = b'\x12'
    elif cube_form == [3, 3]:
        hex_form = b'\x22'
    elif cube_form == [1, 7]:
        hex_form = b'\x06'
    elif cube_form == [2, 7]:
        hex_form = b'\x16'
    elif cube_form == [3, 7]:
        hex_form = b'\x26'
    elif cube_form == [1, 9]:
        hex_form = b'\x08'
    elif cube_form == [2, 9]:
        hex_form = b'\x18'
    elif cube_form == [3, 9]:
        hex_form = b'\x28'
    elif cube_form == [1, 18]:
        hex_form = b'\x31'
    elif cube_form == [2, 18]:
        hex_form = b'\x41'
    elif cube_form == [3, 18]:
        hex_form = b'\x51'
    elif cube_form == [1, 20]:
        hex_form = b'\x33'
    elif cube_form == [2, 20]:
        hex_form = b'\x43'
    elif cube_form == [3, 20]:
        hex_form = b'\x53'
    elif cube_form == [1, 24]:
        hex_form = b'\x37'
    elif cube_form == [2, 24]:
        hex_form = b'\x47'
    elif cube_form == [3, 24]:
        hex_form = b'\x57'
    elif cube_form == [1, 26]:
        hex_form = b'\x39'
    elif cube_form == [2, 26]:
        hex_form = b'\x49'
    elif cube_form == [3, 26]:
        hex_form = b'\x59'
    elif cube_form == [1, 5]:
        hex_form = b'\x04'
    elif cube_form == [1, 11]:
        hex_form = b'\x0a'
    elif cube_form == [1, 13]:
        hex_form = b'\x0c'
    elif cube_form == [1, 14]:
        hex_form = b'\x0d'
    elif cube_form == [1, 16]:
        hex_form = b'\x0f'
    elif cube_form == [1, 22]:
        hex_form = b'\x35'
    elif cube_form == [2, 2]:
        hex_form = b'\x11'
    elif cube_form == [1, 2]:
        hex_form = b'\x01'
    elif cube_form == [1, 4]:
        hex_form = b'\x03'
    elif cube_form == [2, 4]:
        hex_form = b'\x13'
    elif cube_form == [1, 6]:
        hex_form = b'\x05'
    elif cube_form == [2, 6]:
        hex_form = b'\x15'
    elif cube_form == [1, 8]:
        hex_form = b'\x07'
    elif cube_form == [2, 8]:
        hex_form = b'\x17'
    elif cube_form == [1, 10]:
        hex_form = b'\x09'
    elif cube_form == [2, 10]:
        hex_form = b'\x19'
    elif cube_form == [1, 12]:
        hex_form = b'\x0b'
    elif cube_form == [2, 12]:
        hex_form = b'\x1b'
    elif cube_form == [1, 15]:
        hex_form = b'\x0e'
    elif cube_form == [2, 15]:
        hex_form = b'\x1e'
    elif cube_form == [1, 17]:
        hex_form = b'\x30'
    elif cube_form == [2, 17]:
        hex_form = b'\x40'
    elif cube_form == [1, 19]:
        hex_form = b'\x32'
    elif cube_form == [2, 19]:
        hex_form = b'\x42'
    elif cube_form == [1, 21]:
        hex_form = b'\x34'
    elif cube_form == [2, 21]:
        hex_form = b'\x44'
    elif cube_form == [1, 23]:
        hex_form = b'\x36'
    elif cube_form == [2, 23]:
        hex_form = b'\x46'
    elif cube_form == [1, 25]:
        hex_form = b'\x38'
    elif cube_form == [2, 25]:
        hex_form = b'\x48'
    else:
        raise "Cube piece doesn't exist"
    return hex_form


def bing(cube_form):
    if cube_form == [1, 1]:
        hex_form = "00"
    elif cube_form == [2, 1]:
        hex_form = "10"
    elif cube_form == [3, 1]:
        hex_form = "20"
    elif cube_form == [1, 3]:
        hex_form = "02"
    elif cube_form == [2, 3]:
        hex_form = "12"
    elif cube_form == [3, 3]:
        hex_form = "22"
    elif cube_form == [1, 7]:
        hex_form = "06"
    elif cube_form == [2, 7]:
        hex_form = "16"
    elif cube_form == [3, 7]:
        hex_form = "26"
    elif cube_form == [1, 9]:
        hex_form = "08"
    elif cube_form == [2, 9]:
        hex_form = "18"
    elif cube_form == [3, 9]:
        hex_form = "28"
    elif cube_form == [1, 18]:
        hex_form = "31"
    elif cube_form == [2, 18]:
        hex_form = "41"
    elif cube_form == [3, 18]:
        hex_form = "51"
    elif cube_form == [1, 20]:
        hex_form = "33"
    elif cube_form == [2, 20]:
        hex_form = "43"
    elif cube_form == [3, 20]:
        hex_form = "53"
    elif cube_form == [1, 24]:
        hex_form = "37"
    elif cube_form == [2, 24]:
        hex_form = "47"
    elif cube_form == [3, 24]:
        hex_form = "57"
    elif cube_form == [1, 26]:
        hex_form = "39"
    elif cube_form == [2, 26]:
        hex_form = "49"
    elif cube_form == [3, 26]:
        hex_form = "59"
    elif cube_form == [1, 5]:
        hex_form = "04"
    elif cube_form == [1, 11]:
        hex_form = "0a"
    elif cube_form == [1, 13]:
        hex_form = "0c"
    elif cube_form == [1, 14]:
        hex_form = "0d"
    elif cube_form == [1, 16]:
        hex_form = "0f"
    elif cube_form == [1, 22]:
        hex_form = "35"
    elif cube_form == [2, 2]:
        hex_form = "11"
    elif cube_form == [1, 2]:
        hex_form = "01"
    elif cube_form == [1, 4]:
        hex_form = "03"
    elif cube_form == [2, 4]:
        hex_form = "13"
    elif cube_form == [1, 6]:
        hex_form = "05"
    elif cube_form == [2, 6]:
        hex_form = "15"
    elif cube_form == [1, 8]:
        hex_form = "07"
    elif cube_form == [2, 8]:
        hex_form = "17"
    elif cube_form == [1, 10]:
        hex_form = "09"
    elif cube_form == [2, 10]:
        hex_form = "19"
    elif cube_form == [1, 12]:
        hex_form = "0b"
    elif cube_form == [2, 12]:
        hex_form = "1b"
    elif cube_form == [1, 15]:
        hex_form = "0e"
    elif cube_form == [2, 15]:
        hex_form = "1e"
    elif cube_form == [1, 17]:
        hex_form = "30"
    elif cube_form == [2, 17]:
        hex_form = "40"
    elif cube_form == [1, 19]:
        hex_form = "32"
    elif cube_form == [2, 19]:
        hex_form = "42"
    elif cube_form == [1, 21]:
        hex_form = "34"
    elif cube_form == [2, 21]:
        hex_form = "44"
    elif cube_form == [1, 23]:
        hex_form = "36"
    elif cube_form == [2, 23]:
        hex_form = "46"
    elif cube_form == [1, 25]:
        hex_form = "38"
    elif cube_form == [2, 25]:
        hex_form = "48"
    else:
        raise "Cube piece doesn't exist"
    return hex_form
