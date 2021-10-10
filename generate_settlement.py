import os
import requests
from docx import Document

# 常量参数
login_url = 'https://login.hand-china.com/sso/login'
query_url = "http://app.hand-china.com/hrms/autocrud/hr.lbr.LBR150.get_timeSheet_records/query"

# 替换文档指定内容方法 https://zhuanlan.zhihu.com/p/90855359


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

# 模拟oa系统登录请求


def login(url, user_name, password):
    r1 = requests.get(url=login_url, params={
                      'username': user_name, 'password': password})
    print(tuple(r1.cookies))


def test():
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Cookies': 'ISTIMEOUT=false; TARGETURL=%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20modules/hr/lbr/LBR150/hr_lbr_employee_view.screen%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20; FUNCTION_CODE=LBR150; SERVICE_URL=modules/hr/wfl/WFL502/WorkflowInstanceList.screen; SERVICE_PARA=; JSESSIONID=90C8EF3A453B95B707C8253515A78999; JSID=70EFCE768464298D; IS_NTLM=N; vh=616; tj95eceba51d1749cd98415c14e7456b=1; vw=880; Hm_lvt_afc5bec53effc77c4ec7e2a702b8f1f4=1619232548; GUEST_LANGUAGE_ID=en_US'
               }

    rep = requests.get(url=query_url, params={
        'employee_id': 900023853, 'pagesize': 100, 'pagenum': 1})
    print(rep.text)


def main():
    test()


if __name__ == "__main__":
    main()
