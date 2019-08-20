import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        func_code = soup.find('textarea', id='code').text
        f.write(func_code)
        f.close()

if __name__=="__main__":
    main()