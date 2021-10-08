import os
from docx import Document

# https://zhuanlan.zhihu.com/p/90855359
# 替换文档指定内容方法


def replace(file_path, old_param, new_param):
    """
     遍历word中所有的 paragraphs,在每段中发现符合的内容
     直接替换对应内容
    """
    # 创建文档对象,获得word文档
    document = Document(file_path)

    for para in document.paragraphs:
        for i in range(len(para.runs)):
            if old_param in para.runs[i].text:
                para.runs[i].text = para.runs[i].text.replace(
                    old_param, new_param)
    document.save("new.docx")


def main():
    replace("demo.docx", "{name}", "黄伟成")


if __name__ == "__main__":
    main()
