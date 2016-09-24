# flexfile-py
flexible file for edit big file (implement by python,later by C )


## 说明

提供一个读写的文件，主要用于大文件的编辑

`flexfile`除了python builtin的`file`有的那些东西之外，

提供`insert(string)`,`delete(n)`,`replace(string)`函数:

1. `insert(string)` 在文件描述符当前指针位置插入一个字符串`string`

2. `delete(n)` 在文件描述符当前指针位置向后删除`n`个字符

3. `replace(string)` 在文件描述符当前位置向后覆盖写入`string`字符串

以后考虑添加`lastline`,`nextline`,`left`,`right`等操作，

just like vim

还有 `dumps`,`merge`等吧

## demo

一段demo的代码

```bash
pip install flexfile
```

```python
from flexfile import open

flexfile = open(path,mode)
output = flexfile.read()
flexfile.write('123456')

flexfile.seek(3)
flexfile.replace('0000')
flexfile.delete(2)
flexfile.insert('www')

flexfile.flush()
flexfile.close()

```

这样就可以编辑大文件了

`seek & replace & delete & insert`

## 规划实现
 
 考虑使用文件块的模式，块大小4k起步，如果超过就翻番，

4k -> 128k -> 256k -> 1M -> 4M -> 16M -> 32M -> 等等
 
 或许要使用mmap 的模式，或者其他的，再说，先做一个出来。
 

文件头，文件头需要精心设计，大概占据多少多少的长度，每个字段的含义，还有做一些校验。

|--size--|-- 等等

block 的链接顺序，

merge 的时候合并小block，调整顺序等操作。


## TODO

1. 文件头设计，flexfile class的设计
2. 针对固定大小的块文件的，insert/delete/replace api
3. 活动大小块，考虑大文件，考虑扩展
4. 主要api的优化，其他api的补全
5. 