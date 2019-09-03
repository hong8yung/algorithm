import argparse
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import ast

url = ""
ret_string = ""

# read source from url as byte code
def read_source(url):
        html = urlopen(url)
        source = html.read() # read source from byte code
        html.close()

        return source
    
# parse Challenge's info
def parse_chal(soup):
    global ret_string
    title = soup.find('li', class_='algorithm-title').text.strip()
    arg_sec = soup.find('table', class_='table')
    arg_name = [x.text for x in arg_sec.find_all('th')]
    if 'return' in arg_name:
        ret_string = "return"
    elif 'result' in arg_name:
        ret_string = "result"


    arg_val_tmp = arg_sec.find_all('td')
    arg_val_tmp_q = arg_sec.find_all('q')

    # hidden 속성으로 #code에 디폴트 코드가 적혀져 있음.
    func_code = soup.find('textarea', id='code').text

    # modify <q>::before STRING </q>::after
    # to     'STRING'
    for i in arg_val_tmp_q:
        i.string = "'"+i.string+"'"

    # set value from string expression 
    # ex) "['text', 'tmp']" -> ['text', 'tmp']
    arg_val = []
    for i in arg_val_tmp:
        arg_val.append(ast.literal_eval(i.text))

    # set {arg_name: arg_value, ...}
    arg_dic = OrderedDict.fromkeys(arg_name)
    for i in arg_dic:
        arg_dic[i] = []
    for i, val in enumerate(arg_val):
        (arg_dic[arg_name[i%len(arg_name)]]).append(val)

    return (title, func_code, arg_dic)

# make [Challenge's title].py file
def create_file(title, func_code, arg_dic):
    # file open & write
    # check already exists file
    if os.path.isfile("./Programmers/"+title+".py"):
        print("[-] file already exists")
        f = open("./Programmers/"+title+"_복사본.py", 'w')
    else:
        f = open("./Programmers/"+title+".py", 'w')

    f.write(func_code)
    f.write("\n\n")
    for i in arg_dic:
        if i == ret_string:
            continue
            #f.write('#')
        line_str = "{} = {}\n".format(i, arg_dic[i])
        f.write(line_str)

    f.write("\n")
    for i in range(len(arg_dic[ret_string])):
        line_str = ""
        for j in arg_dic.keys():
            if j != ret_string:
                line_str = line_str+"{}[{}], ".format(j, i)
        else:
            line_str= line_str[:-2]
        f.write("print(solution({}))\n".format(line_str))

    f.write("\n")
    for num, i in enumerate(arg_dic.get(ret_string)):
        f.write("#case{}: {}\n".format(num, i))

    f.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--link", help="input Programmers's Chall Link")
    args = parser.parse_args()
    if args.link:
        url = args.link
        
        soup = BeautifulSoup(read_source(url), "html5lib")

        title, func_code, arg_dic = parse_chal(soup)
        create_file(title, func_code, arg_dic)

if __name__=="__main__":
    main()