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
    
    
    其中，relatedLink中存放的也是词条对应的number而不是整个url
    
    
2. suggest.用于推荐，当前推荐算法极度简陋，只是比较tags还有relatedlink中相同个数。

   个人想法是到后面用分词找出一些高频词作为属性，然后每个词条有一个对应向量表示，然后对于每个用户，也有一个结构相同的向量对用户的使用习惯进行记录，最后匹配最相近的词条做推荐。
   
   为什么暂时不用Naive-Bayes呢，因为我们现在要把食物分类还不知道怎么分，而且数据量不多，才一万条，直接拿来做训练集。所以先做完上面那一步，有时间再修改，添加NB算法做分类

3. priorityQueue. 顾名思义，做推荐是使用的优先队列类定义

4. main.py. tornado框架实现的服务器，逻辑较为简单 ：
    
    --> 主页面，选择食品

    --> 食品存在跳到展示页面，不存在则提供tips
    
    --> 展示页面
