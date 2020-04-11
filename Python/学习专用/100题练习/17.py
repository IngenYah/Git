#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
xs = input('请输入：')
alpha = []
space = []
digit = []
other = []
for x in xs:
    if x.isalpha():
        alpha.append(x)
    elif x.isspace():
        space.append(x)
    elif x.isdigit():
        digit.append(x)
    else:
        other.append(x)
print('字母有{}个，分别是{};空格有{}个;数字有{}个，分别是{}；剩下{}个，分别是{};'.format(len(alpha),alpha,len(space),len(digit),digit,len(other),other))