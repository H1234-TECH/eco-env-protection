from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # 这里可以添加代码处理联系表单，例如保存到数据库、发送邮件等
    print(f'Name: {name}, Email: {email}, Message: {message}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



import os

print("当前工作目录:", os.getcwd())
print("模板文件夹中的文件:", os.listdir(os.path.join(os.getcwd(), 'templates')))

import os
print("当前工作目录:", os.getcwd())