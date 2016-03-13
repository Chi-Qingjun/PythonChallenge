# PythonChallenge
The Python Challenge(http://www.pythonchallenge.com/)

## Challenge 0
计算2的38次方就能得到新的url。

## Challenge 1
使用凯撒密码（替换式密码）进行了加密，解密偏移量为2。

## Challenge 2
根据提示查看网页源代码，在注释中找到一长串文本，在其中找到出现次数最少的字母。

## Challenge 3
在网页源代码字符串中用正则表达式匹配满足“左右两侧各有三个大写字母的小写字母”条件的字符。

## Challenge 4
迭代获得的nothing值进行网络请求。

## Challenge 5
根据提示pronounce it，读网页标题peak hell，谐音为pickle，被操作的文本在网页源代码中指向的banner.p。反序列化后的文本是一个二维list，
最小元素由一个字符和一个数字组成。在终端中能够打印出channel。

## Challenge 6
根据画面主体拉链的英文zip修改url为`http://www.pythonchallenge.com/pc/def/channel.zip`，下载文件后先读readme.txt，与Challenge 4类似。最后通过zipfile模块读取压缩包中文件的注释，并打印得到结果。

## Challenge 7
页面上只有一幅图，其他什么提示也没有。彩图中有一条灰度矩形色块，考虑色块的灰度值代表了ascii码数值，使用Pillow模块处理。

## Challenge 8
网页上图中的昆虫可以点击，需要输入用户名密码才行。查看网页源代码发现两行名为un和pw的注释，即username和password。网上搜了一下说是bz2的压缩格式，需要用bz2模块解压缩。将解压后的用户名和密码输入提示框就可以进入下一关。

## Challenge 9
网页标题`connect the dots`应该是要我们在图片中画一个多边形出来，查看网页源码中给出了两组坐标，使用Pillow模块绘制图案，最后是一头牛。下一关即是bull。

## Challenge 10
点击图片中的牛出现list a的前几个元素，要找到规律求出a[30]的长度。规律就是——1个1，写作11；2个1，写作21；1个2，1个1，写作1211...
