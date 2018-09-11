import sys,codecs,re,io,os

#采用循环计数统计行数
def CmdLine(filename):
    try:
        file = codecs.open(filename,'rb')
    except:
        print("文件打开失败，请确认输入是否正确")
        sys.exit(1)
    count = -1
    for count,line in enumerate(file):
        pass
    count +=1
    return dict({'文件':filename,'行数':count})
#统计字符数
def CmdChar(filename):
    try:
        file = codecs.open(filename,'rb')
    except:
        print("文件打开失败，请确认输入是否正确")
        sys.exit(1)
    return dict({'文件':filename,'字符数':len(file.read().strip())})

#统计单词数
def CmdWord(filename):
    wordcount = dict()
    try:
        with io.open(filename, encoding="utf-8") as f:
            words = [s.lower() for s in re.findall("\w+", f.read())]
            for word in words :
                wordcount[word] = wordcount.get(word,0) +1
        return dict({'文件':filename,'单词数':wordcount})
    except:
        print("文件打开失败，请确认输入是否正确")
        sys.exit(1)

def CmdSpecialLine(filename):
    try:
        file = codecs.open(filename,'rb')
    except:
        print("文件打开失败，请确认输入是否正确")
        sys.exit(1)
    specialline = dict({
        'line_value':0,
        'line_none':0,
        'line_comment':0
    })
    for line in file.readlines():
        if not line.split():
            specialline['line_none'] +=1
        elif '#' in str(line):
            specialline['line_comment'] +=1
        else:
            specialline['line_value'] +=1
    return dict({'文件':filename,'特殊行':specialline})

def CmdDirPath(command,filename,result):
    command_detail = command.replace('-s','')
    files = os.listdir(filename)
    for fi in files:
        fi_d = os.path.join(filename, fi)
        if os.path.isdir(fi_d):
            CmdDirPath(command,fi_d,result)
        else:
            result_one=CommandList(command=command_detail,filename=str(os.path.join(fi_d))),
            result.append(result_one)
    return result
def CommandList(command,filename):
    if command == '-l':
        result = CmdLine(filename)
    elif command == '-c':
        result = CmdChar(filename)
    elif command == '-w':
        result = CmdWord(filename)
    elif command == '-a':
        result = CmdSpecialLine(filename)
    elif '-s' in command:
        result=[]
        result = CmdDirPath(command,filename,result)
    else :
        print("请输入 -w -l -c -a -s命令")
        sys.exit(1)
    return result

def main():
    if len(sys.argv) != 3:
        print("请输入格式为 python wc.py -l file.c 的命令")
        sys.exit(1)
    command = sys.argv[1]
    filename = sys.argv[2]
    result = CommandList(command,filename)
    print(result)
    sys.exit(1)
if __name__=="__main__":
    main()