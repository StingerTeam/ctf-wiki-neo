# SSTI（Server-Side Template Injection，服务器端模板注入）

<https://blog.csdn.net/solitudi/article/details/107752717>

## 判断模板类型

- `${7*7}`
  - 执行
    - `a{*comment*}b`
      - 执行
        - Smarty
      - 不执行
        - `${"z".join("ab")}`
          - 执行
            - Mako
          - 不执行
            - Unknown
  - 不执行
    - `{{7*7}}`
      - 执行
        - `{{7*'7}'}`
          - 执行
            - Jinja2
            - Twig
          - 不执行
            - Unkown
      - 不执行
        - Not Vulnerable

## Flask

Flask 模板注入漏洞是一种安全漏洞，它涉及到使用 Flask 框架的 Web 应用程序中的模板引擎，通常是 Jinja2。这种漏洞允许攻击者通过精心构造的输入来注入恶意模板代码，从而可能导致潜在的安全问题，例如数据泄露、远程代码执行等。这是一种典型的服务器端模板注入（Server-Side Template Injection，SSTI）漏洞。

Flask 模板注入漏洞通常发生在以下情况下：

1. 用户输入不经过充分验证或过滤，被动态插入到模板中。这可以发生在应用程序中，例如在用户提交的表单数据中，应用程序将用户输入作为变量插入到模板中，而没有适当的过滤和转义。

2. 攻击者能够控制输入并在其中插入模板标记。这可以发生在应用程序的 URL 参数、Cookie 或其他请求参数中，如果这些输入没有得到正确的验证和处理。

3. 不安全的模板渲染设置。应用程序配置或使用不安全的模板渲染设置，使得攻击者可以注入自己的模板代码。

以下是一个简单的示例，说明 Flask 模板注入漏洞的工作原理：

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()

```

在上述示例中，name 参数的值被插入到 hello.html 模板中，但如果没有进行适当的输入验证和过滤，攻击者可以构造恶意输入，例如`?name={{7*7}}`，这将导致模板注入漏洞，执行`7*7`并显示结果`49`。

## PHP-Twig

<https://xz.aliyun.com/t/10056>
