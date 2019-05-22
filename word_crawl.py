import docx
import os
import re
import tkinter
import glob

# 界面初始化
window = tkinter.Tk()
window.geometry('300x200')
window.title('word_crawl')

l1 = tkinter.Label(window, text='文件输入路径', font=('微软雅黑', 10))
input_path_entry = tkinter.Entry(window)
input_path_entry.insert('end', 'test_files')
l2 = tkinter.Label(window, text='开始关键词', font=('微软雅黑', 10))
begin_word_entry = tkinter.Entry(window)
begin_word_entry.insert('end', '摘要')
l3 = tkinter.Label(window, text='结尾关键词（不包含）', font=('微软雅黑', 10))
end_word_entry = tkinter.Entry(window)
end_word_entry.insert('end', '关键词')
l4 = tkinter.Label(window, text='文件输出路径', font=('微软雅黑', 10))
output_path_entry = tkinter.Entry(window)
output_path_entry.insert('end', 'output')

def hit_me():
    files_dir = input_path_entry.get()
    begin_word = begin_word_entry.get()
    end_word = end_word_entry.get()
    output_dir = output_path_entry.get()
    main(files_dir, output_dir, begin_word, end_word)
b1 = tkinter.Button(window, text='开始', command=hit_me)

l1.pack()
input_path_entry.pack()
l2.pack()
begin_word_entry.pack()
l3.pack()
end_word_entry.pack()
l4.pack()
output_path_entry.pack()
b1.pack()

# 当前工作路径
root = os.getcwd()

def work(files_dir, begin_word, end_word):
    if '\\' not in files_dir:
        # 不包含'\'，是相对路径
        work_path = os.path.join(root, files_dir)
    else:
        work_path = files_dir
    # 切换工作路径为指定文件夹
    os.chdir(work_path)
    # 读取指定文件夹中所有docx文件
    all_docx_file = glob.glob('*.docx')

    target_dict = {}
    for f in all_docx_file:
        docx_file = docx.Document(f)    
        file_name = re.findall('(.*)\.docx$', f)[0]

        result_list = []

        # 读取docx文件，找到指定内容保存到列表result_list
        mark = False
        for para in docx_file.paragraphs:
            text = para.text
            if text.startswith(begin_word):
                mark = True
            if text.startswith(end_word):
                break
            elif mark == True and text != '':
                result_list.append(text)

        # result_list中的内容转换为字符串形式
        target_words = '\n'.join(result_list)
        target_dict[file_name] = target_words
    
    for i in target_dict:
        print(i)
    os.chdir(root)
    return target_dict


def save_to_txt(target_dict, output_path):
    with open(output_path+'.txt', 'a+', encoding='utf-8') as f:
        for key, value in target_dict.items():
            f.write('file_name:'+key)
            f.write('\n')
            f.write(value)
            f.write('\n\n')

def main(files_dir, output_name, begin_word='摘要', end_word='关键词'):
    res = work(files_dir, begin_word, end_word)
    save_to_txt(res, output_name)

if __name__ == '__main__':   
    window.mainloop()