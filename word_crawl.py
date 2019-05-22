import docx
import os
import re


docx_file = docx.Document(r'test_files\word_crawl test.docx')
begin = '摘要'
end = '关键词'

target_list = []
mark = False
for para in docx_file.paragraphs:
    text = para.text
    if text.startswith(begin):
        mark = True
    if text.startswith(end):
        break
    elif mark == True and text != '':
        target_list.append(text)

target_words = '\n'.join(target_list)
print(target_words)

with open('output_file.txt', 'w+', encoding='utf-8') as f:
    f.write(target_words)