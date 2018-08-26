# v2ex_block

### 用途
这是一个专用v2ex的block项目
block名单用的ini文件格式(比较好读)

### 用法
自带一个自动屏蔽的脚本，需要传进cookie，就不加登录了

```
python v2ex_block.py -c "cookie" -f "ini_filename" -l "block level" -[bu]
        [options]
        -h, --help        Get option help
        -c, --cookie      Add cookie str or saved cookie file name (No more than 10 characters.)
        -f, --file        Add block list file name 
        -l, --level       Block list level ,defult 1
        -b, --block       Defult block
        -u, --unblock
```
欢迎引用和提交
