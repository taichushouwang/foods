foods
=====

食品推荐

demo作品

文件主要分为：

1.readContent。用于读取数据，由于数据量比较大，就不放上来。
  每个词条对应一个文件夹，文件夹命名方式为数字，该数字是从该词条在百度百科上的url中的数字标号决定。如 :
  
    http://baike.baidu.com/view/59062.htm ---- 白切鸡
  
  则有白切鸡的文件夹编号为59062.
  
  此外，每个文件夹有可能下面几个文件：
    --> pic.jpg 该词条的照片(不一定有)
    --> tags.txt 该词条在百度百科上的标签(词条对应网页的最下方)
    --> introduction.txt 该词条在页面右上方的小方框内的简要介绍(不一定有)
    --> link.txt 该词条的url,注意还有该食品名字
    --> view.txt & albums.txt & picview.txt 词条页面正文中的链接，view、albums、picview 分别代表指向 其他词条、相册 和 图片的链接 (文件一定有，单文件内部可能为空),demo 版本中只读view.txt,储存为relatedLink
    
  读取完后，会在内存中形成一个字典对象foods，其构造如下 ： 
    foods = {
              "食品名字" ： {
                  "tags" : ["tag1", "tag2", ...],
                  "intros" : "introString", 
                  "relatedLink" : ["link1", "link2", ...],
                  "link" : "urlForTheTopic", 
                  "number" : numberForTheTopic
              }
    }    
