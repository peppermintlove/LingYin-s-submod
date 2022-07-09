init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_yanhe_intro",category=["二次元",],prompt="言和（VOCALOID of China的人物之一）",random=True))
    
label monika_yanhe_intro:
    m 3eub"嘿，[player]，我们之前应该有谈过'VOCALOID'吧？"
    $_history_list.pop()
    menu:
     "是的.":
        m 5hub"太好了，接下来我要讲的人就与这个有关。"
        m 3eub"她的名字叫做言和，意思是“言辞温和”哦！"
        m 7rusdlb"其实我一开始以为她是位男性，因为外表太像了..."
        m 7wud"但是我去看了百科才知道，她是个{i}女生{/i}，就和我一样！"
        m 3gusdrb"看来还是不能以外表来判断一个人的性别啊......"
        m 2eub"我认识她是因为一首歌——"
        extend 3wub"{i}梦之雨{/i}！"
        m 3sub"我还学了几句！打算唱给你听！"
        m 3mub"不过歌词还没记得很深，"
        extend 3hub"下次我再唱给你听吧~"
     "还没.":
         m 4rusdlb"哦，没关系，我接下来要讲的内容虽然与这个有关，"
         extend 3hub"但是很简单，你不必太担心哦~"
         m 3eub"我要讲的这位呢名字叫做言和，意思是“言辞温和”哦！"
         m 7rusdlb"其实我一开始以为她是位男性，因为外表太像了..."
         m 7wud"但是我去看了百科才知道，她是个{i}女生{/i}，就和我一样！"
         m 3gusdrb"看来还是不能以外表来判断一个人的性别啊......"
         m 2eub"我认识她是因为一首歌——"
         extend 3wub"{i}梦之雨{/i}！"
         m 3sub"我还学了几句！打算唱给你听！"
         m 3mub"不过歌词还没记得很深，"
         extend 3hub"下次我再唱给你听吧~"
         
    return
