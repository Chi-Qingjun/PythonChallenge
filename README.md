# PythonChallenge
The Python Challenge(http://www.pythonchallenge.com/)

## Challenge 0
计算2的38次方就能得到新的url。
下一关地址：`http://www.pythonchallenge.com/pc/def/274877906944.html`

## Challenge 1
使用凯撒密码（替换式密码）进行了加密，解密偏移量为2。
下一关地址：`http://www.pythonchallenge.com/pc/def/ocr.html`

## Challenge 2
根据提示查看网页源代码，在注释中找到一长串文本，在其中找到出现次数最少的字母。
下一关地址：`http://www.pythonchallenge.com/pc/def/equality.html`

## Challenge 3
在网页源代码字符串中用正则表达式匹配满足“左右两侧各有三个大写字母的小写字母”条件的字符。
下一关地址：`http://www.pythonchallenge.com/pc/def/linkedlist.php`

## Challenge 4
迭代获得的nothing值进行网络请求。
下一关地址：`http://www.pythonchallenge.com/pc/def/peak.html`

## Challenge 5
根据提示pronounce it，读网页标题peak hell，谐音为pickle，被操作的文本在网页源代码中指向的banner.p。反序列化后的文本是一个二维list，
最小元素由一个字符和一个数字组成。在终端中能够打印出channel。
下一关地址：`http://www.pythonchallenge.com/pc/def/channel.html`

## Challenge 6
根据画面主体拉链的英文zip修改url为`http://www.pythonchallenge.com/pc/def/channel.zip`，下载文件后先读readme.txt，与Challenge 4类似。最后通过zipfile模块读取压缩包中文件的注释，并打印得到结果。
下一关地址：`http://www.pythonchallenge.com/pc/def/oxygen.html`

## Challenge 7
页面上只有一幅图，其他什么提示也没有。彩图中有一条灰度矩形色块，考虑色块的灰度值代表了ascii码数值，使用Pillow模块处理。
下一关地址：`http://www.pythonchallenge.com/pc/def/integrity.html`

## Challenge 8
网页上图中的昆虫可以点击，需要输入用户名密码才行。查看网页源代码发现两行名为un和pw的注释，即username和password。网上搜了一下说是bz2的压缩格式，需要用bz2模块解压缩。将解压后的用户名和密码输入提示框就可以进入下一关。
通关用户名：`huge`，密码：`file`。

## Challenge 9
网页标题`connect the dots`应该是要我们在图片中画一个多边形出来，查看网页源码中给出了两组坐标，使用Pillow模块绘制图案，最后是一头牛。下一关即是bull。
下一关地址：`http://www.pythonchallenge.com/pc/return/bull.html`

## Challenge 10
点击图片中的牛出现list a的前几个元素，要找到规律求出a[30]的长度。规律就是——1个1，写作11；2个1，写作21；1个2，1个1，写作1211...
下一关地址：`http://www.pythonchallenge.com/pc/return/5808.html`

## Challenge 11
根据图像水平坐标x和垂直坐标y的奇偶性, 把原图的像素分成四个部分, 每个部分形成一张小图，答案在图中。
下一关地址：`http://www.pythonchallenge.com/pc/return/evil.html`

## Challenge 12
实在不会做，看答案了：
> The image shows a deck of cards being dealt into 5 piles. The cards even have the number '5' on theirs backs. The image itself is named 'evil1.jpg', a deviation from previous levels. So we increment the number, and there is indeed an evil2.jpg. This image tells you to look for a .gfx file; you'll find a evil2.gfx file.

>Before we dissect that file, look further and find evil3.jpg, which claims there are 'no more evils...'. Will you believe the claim? You shouldn't, because evil4.jpg does exist, altough it is not a JPEG image at all. It is in fact a text file telling you that "Bert is evil!" and to go back.

>So we go back to our evil2.gfx file, which appears to be binary soup. But remember the hints. All you have to do is deal the data into 5 equal piles and save those piles to disc. It turns out there are 5 images in there. Image one contains the letters 'dis', the next contains 'pro', the 3rd 'port', the 4th 'ional' and the 5th 'ity', but has those letters scored out. Indeed, the next level is at 'disproportional'.

>The fourth image may not load in all PNG viewers, because it has been truncated to fit in the pile of images; Firefox is tolerant enough to show what it can; you can also try and pad the data with zeros until it can be loaded (use PIL to automate this). As is, PIL can create an Image from the fourth piece, but cannot save it (im.save() and im.show() fail).

下一关地址是`http://www.pythonchallenge.com/pc/return/disproportional.html`。
