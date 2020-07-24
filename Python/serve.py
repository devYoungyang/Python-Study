'''
@Author: Yang
@Date: 2019-10-25 16:46:55
@LastEditors: Yang
@LastEditTime: 2019-10-28 14:53:49
@FilePath: /Python/serve.py
@Description:
'''
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from flask import Flask
import os
app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=1.0, user-scalable=no"/>
<title>测试</title>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
<div style="text-align:center;">
<button type="button" class="call-py" style="font-size:24px;">点击打开计算器</button>
</div>
<script type="text/javascript">
$(function(){
$(".call-py").click(function(){
    $.get("/call_shell",function(result){
        alert("调用成功！")
    })
})
})
</script>
</body>
</html>
"""


@app.route("/")
def main():
    return html


@app.route("/call_shell")
def call():
    # print("调用计算器")
    os.system('./shell.sh')
    return "成功"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5081)
