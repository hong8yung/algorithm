import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

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
        arg_val = []
        for i in arg_val_tmp:
            if i.find('q'):
                arg_val.append(i.text)
            else:
                # True/False나 None, 배열 등일 때 처리 추가로 해야함 ㄷㄷ
                arg_val.append(int(i.text))

        print("title: {}, arg_nme: {}, arg_val:{}".format(title, arg_name, arg_val))
        # file open & write
        f = open("./Programmers/"+title+".py", 'w')
        # hidden 속성으로 #code에 디폴트 코드가 적혀져 있음.
        func_code = soup.find('textarea', id='code').text
        f.write(func_code)

        arg_dic = OrderedDict.fromkeys(arg_name, [])
        print("num({})".format(len(arg_name)))
        for i, val in enumerate(arg_val):
            print("i({}), name({}), val({})".format(i, arg_name[i%len(arg_name)], val))
            (arg_dic[arg_name[i%len(arg_name)]]).append(val)
            print(arg_dic[arg_name[i%len(arg_name)]])

        f.write("\n\n")
        f.write(str(arg_dic))
        f.close()

if __name__=="__main__":
    main()