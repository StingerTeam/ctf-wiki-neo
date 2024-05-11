文件上传漏洞是指用户上传了一个可执行脚本文件，并通过此文件获得了执行服器端命令的能力。在大多数情况下，文件上传漏洞一般是指上传 WEB 脚本能够被服务器解析的问题，也就是所谓的 webshell 问题。完成这一攻击需要这样几个条件，一是上传的文件能够被 WEB 容器执行，其次用户能从 WEB 上访问这个文件，最后，如果上传的文件被安全检查、格式化、图片压缩等功能改变了内容，则可能导致攻击失败。

# 黑名单绕过

- 前端检查

  - 控制台重构检查函数

  - 抓包

- 改为`php5,php4,php3,php2,phtml,pht`

- 大小写绕过

- 加空格

- 加点

- 加：:$DATA

- 加点+空格+点+空格（`deldot()`删除末尾空格、`trim()`首尾去空）

- 双写

# 上传路径可控

- 上传路径+文件名拼接时，上传路径后输入保存文件名并使用 00 截断，GET：%00 截断，POST：00 截断（需要`php`版本小于 5.3.4，`php.ini`的`magic_quotes_gpc`为`OFF`状态）

# 文件内容检测绕过

- 文件头绕过（添加 GIF89a 等）

# 二次渲染

- 测试图片的渲染后没有修改的位置，将一句话木马添加进去，这样就可以利用文件包含去执行 php 一句话木马了

- 对于 GIF=的上传，只需要判断没有修改的位置，然后将 php 一句话木马添加即可

- 对于 PNG 的上传，需要修改 PLTE 数据块或者修改 IDAT 数据块，

- 详见 [制作绕过二次渲染的图片马](https://blog.csdn.net/weixin_45519736/article/details/105775721)

# 条件竞争

针对上传后删除的情况

# 解析漏洞

- Apache 解析

  - Apache 对后缀解析是从右向左的

    - `phpshell.php.rar.rar.rar.rar` 因为 Apache 不认识 `.rar` 这个文件类型，所以会一直遍历后缀到 `.php`，然后认为这是一个 PHP 文件。

- IIS 解析

  - IIS 6 下当文件名为 `abc.asp;xx.jpg` 时，会将其解析为 `abc.asp`。

- PHP CGI 路径解析

  - 当访问 `http://www.a.com/path/test.jpg/notexist.php` 时，会将 `test.jpg` 当做 PHP 解析， `notexist.php` 是不存在的文件。此时 Nginx 的配置如下

  ```nginx

  location ~ \.php$ {

    root html;

    fastcgi_pass 127.0.0.1:9000;

    fastcgi_index index.php;

    fastcgi_param SCRIPT_FILENAME /scripts$fastcgi_script_name;

    include fastcgi_param;

  }

  ```
