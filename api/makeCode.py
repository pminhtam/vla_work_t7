from datetime import datetime
char_dict_ori = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'Q',11:'W',12:'E',13:'R',
           14:'T',15:'Y',16:'U',17:'I',18:'O',19:'P',20:'A',21:'S',22:'D',23:'F',24:'G',
           25:'H',26:'J',27:'K',28:'L',29:'Z',30:'X',31:'C',32:'V',33:'B',34:'N',35:'M'}

key = 10
def makeindexRan():      # thuật toán tạo số ngẫu nhiên
    x = 7
    a = 13
    m = 36
    c = 1
    li = []
    for i in range(m):
        b = a*x+c
        (_ , x) = divmod(b,m)
        # x = b%m
        # print(x)
        li.append(x)
    return li
"""
def change_char_dict(char_dict,key):
    char_dic_new = {}
    for i in char_dict:
        char_dic_new[(i+key)%36] = char_dict[i]
    return char_dic_new
"""
# print(makeindexRan())
def change_char_dict(char_dict_ori):
    index = makeindexRan()
    char_dict = {}
    for i in range(36):
        char_dict[index[i]] = char_dict_ori[i]
    return char_dict
char_dict = change_char_dict(char_dict_ori)
# print(char_dict)
def makeGroup2(num,char_dict):          # 7 số đầu
    num_conv = []
    (a,b) = divmod(num,36)
    num_conv.append(b)
    while a>0:
        (a, b) = divmod(a, 36)
        num_conv.append(b)
    for i in range(6 - len(num_conv)):     # kéo dài cho đủ 7 ký tự
        num_conv.append(0)
    num_conv = num_conv[::-1]
    num_conv = num_conv[-6:]                # lấy 7 số cuối
    result = ''
    for i in num_conv:
        result+=char_dict[i]
    return result


def makeGroup3(num,char_dict):        # 3 số sau
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


def makeChecksum(char,char_dict_ori):
    sum_ascii = 0
    for i in char:
        # print(i)
        # print(ord(i))
        sum_ascii+= ord(i)
    sum_ascii%=36
    result = char_dict_ori[sum_ascii]
    return result
def makeCode(num_list,id_sp,char_dict = char_dict,char_dict_ori = char_dict_ori):
    year = char_dict_ori[int(datetime.now().strftime('%Y')) - 2018]
    group3 = makeGroup3(id_sp,char_dict)
    group2_list = []
    checksum_list = []
    code_list = []
    i = 0
    for num in num_list:
        group2 = makeGroup2(num,char_dict)
        group2_iden = makeGroup3(i,char_dict_ori)
        i+=1
        group2_list.append(group2)
        checksum = makeChecksum(year + group2+group3,char_dict_ori)
        checksum_list.append(checksum)
        # code = year+ group2+group2_iden+group3+checksum
        code = year+ group2+group3+checksum
        code_list.append(code)
    result = {
        'year':year,
        'group2_list':group2_list,
        'group3':group3,
        'checksum_list':checksum_list,
        'code_list':code_list
    }
    return result

# print(makeCode([41722,57],4))


