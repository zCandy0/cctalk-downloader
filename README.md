如题，功能就是下载CCtalk的视频课程。

**注意，只有自己已经购买的课，或者是免费的课程才可以下载。**
**此外，根据测试，有用户表示无法下载有版权保护的视频**

## 使用教程
1.购买报名课程

2.确定要下载的课程

来到 `https://www.cctalk.com/account-center` ，点击`课程`，选择想要下载的课点开

3.确定seriesId

打开`开发者工具`，或者是`F12`，`Fn+F12`快捷键打开，换到`网络`选项卡，`Ctrl+R`刷新，左上角过滤填`all_lesson_list`，选单击过滤出来的内容，即可得到`seriesId`
![image](https://github.com/user-attachments/assets/73c87b9b-5439-4119-b829-c3721d7eaa4a)


4.获取cookie

切换到`控制台`选项卡，输入`alert(document.cookie)`即可弹出cookie
![image](https://github.com/user-attachments/assets/03076c4f-11f2-4de5-8575-8f927313dfa1)



5.下载release / 下载源码，并且安装python

*如果是windows X64，可以下载release中的文件，免去源码安装依赖

源码所需依赖：requests，tqdm

`pip install requests,tqdm`即可

## 下载说明
1.默认保存路径为D盘，请确保有足够空间

2.采用单线程，没有使用aria2，防止触发网站防御

## 关于版权保护的问题
我询问过周边的人，但是都没有购买过这样的课程，所以无法处理，暂时搁置
