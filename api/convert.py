a = 4000222555
char_dict= {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'Q',11:'W',12:'E',13:'R',
           14:'T',15:'Y',16:'U',17:'I',18:'O',19:'P',20:'A',21:'S',22:'D',23:'F',24:'G',
           25:'H',26:'J',27:'K',28:'L',29:'Z',30:'X',31:'C',32:'V',33:'B',34:'N',35:'M'}

key = 10
def change_char_dict(char_dict,key):
    char_dic_new = {}
    for i in char_dict:
        char_dic_new[(i+key)%36] = char_dict[i]
    return char_dic_new

def makeGroup12(num,char_dict):          # 7 số đầu
    # char_dict = change_char_dict(char_dict, key)
    num_conv = []
    (a,b) = divmod(num,36)
    num_conv.append(b)
    while a>0:
        (a, b) = divmod(a, 36)
        num_conv.append(b)
        # print(a,b)
    for i in range(6 - len(num_conv)):     # kéo dài cho đủ 7 ký tự
        num_conv.append(0)
    num_conv = num_conv[::-1]
    num_conv = num_conv[-6:]                # lấy 7 số cuối
    result = ''
    for i in num_conv:
        result+=char_dict[i]
    return result

# print(makeGroup12(a,char_dict,key))
# print(list(char_dict.keys())[list(char_dict.values()).index('q')])      # tìm key theo value

def makeGroup3(num,char_dict):        # 3 số sau
    # char_dict = change_char_dict(char_dict, key)
    num_conv = []
    (a,b) = divmod(num,36)
    num_conv.append(b)
    while a>0:
        (a, b) = divmod(a, 36)
        num_conv.append(b)
        # print(a,b)
    for i in range(3 - len(num_conv)):     # kéo dài tối thiểu 3 ký tự
        num_conv.append(0)
    num_conv = num_conv[::-1]
    num_conv = num_conv[-3:]                # lấy 3 số cuối
    result = ''
    for i in num_conv:
        result+=char_dict[i]
    return result
# print(makeGroup3(a,char_dict,11))

def deconvertGroup12(char,char_dict):
    result = 0
    char = char[::-1]
    bias = 0
    for i in char:
        result+= list(char_dict.keys())[list(char_dict.values()).index(i)]*36**bias
        bias+=1
    return result
# b = deconvertGroup12('2A6LE7',char_dic)
# print(type(b))
# print(b)
def makeChecksum(char,char_dict):
    sum_ascii = 0
    for i in char:
        # print(i)
        # print(ord(i))
        sum_ascii+= ord(i)
    sum_ascii%=36
    result = char_dict[sum_ascii]
    return result
print(makeChecksum('fewgwg',char_dict))

