import argparse
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import ast

url = ""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--link", help="input Programmers's Chall Link")
    args = parser.parse_args()
    if args.link:
        url = args.link
        html = urlopen(url)
        source = html.read() # read source from byte code
        html.close()

        soup = BeautifulSoup(source, "html5lib")
        # make [Challenge's title].py file
        title = soup.find('li', class_='algorithm-title').text.strip()
        arg_sec = soup.find('table', class_='table')
        arg_name = [x.text for x in arg_sec.find_all('th')]
        arg_val_tmp = arg_sec.find_all('td')
        arg_val_tmp_q = arg_sec.find_all('q')
        print("[Debug] end find_all('q)")
        for i in arg_val_tmp_q:
            i.string = "'"+i.string+"'"
        arg_val = []
        for i in arg_val_tmp:
            arg_val.append(ast.literal_eval(i.text))

        print("title: {}, arg_nme: {}, arg_val:{}".format(title, arg_name, arg_val))
        # file open & write
        if os.path.isfile("./Programmers/"+title+".py"):
            print("[-] file already exists")
            f = open("./Programmers/"+title+"_복사본.py", 'w')
        else:
            f = open("./Programmers/"+title+".py", 'w')
        # hidden 속성으로 #code에 디폴트 코드가 적혀져 있음.
        func_code = soup.find('textarea', id='code').text
        f.write(func_code)

        arg_dic = OrderedDict.fromkeys(arg_name)
        for i in arg_dic:
            arg_dic[i] = []

        print("num({})".format(len(arg_name)))
        for i, val in enumerate(arg_val):
            print("i({}), name({}), val({})".format(i, arg_name[i%len(arg_name)], val))
            (arg_dic[arg_name[i%len(arg_name)]]).append(val)
            print(arg_dic[arg_name[i%len(arg_name)]])

        f.write("\n\n")
        for i in arg_dic:
            if i == 'return':
                continue
                #f.write('#')
            line_str = "{} = {}\n".format(i, arg_dic[i])
            f.write(line_str)

        f.write("\n")
        for i in range(len(arg_dic['return'])):
            line_str = ""
            for j in arg_dic.keys():
                if j != 'return':
                    line_str = line_str+"{}[{}], ".format(j, i)
            else:
                line_str= line_str[:-2]
            f.write("print(solution({}))\n".format(line_str))

        f.write("\n")
        for num, i in enumerate(arg_dic.get('return')):
            f.write("#case{}: {}\n".format(num, i))
        f.close()

if __name__=="__main__":
    main()