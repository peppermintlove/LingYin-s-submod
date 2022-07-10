init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_paranoia_intro",category=["二次元""音乐",],prompt="妄想症系列",random=True))
    
label monika_paranoia_intro:
        m 3eub"{i}~情感无限交织的深渊~{/i}"
        m 3dub"{i}~我们看见了什么~{/i}"
        m 2esd "{i}~向着现实苦苦哀求~{/i}"
        m 2dkd "{i}~想要死的深刻一些~{/i}"
        m 3dsc "{i}~仅剩下幻觉~{/i}"
        m 3hub "嘿，[player]，你知道这首歌出自哪个系列吗？"
        m 1hua "那当然是——"
        extend 3sub "{i}妄想症系列{/i}！"
        m 1eua"那么，你有听说过这个系列吗，[player]？"
        $_history_list.pop()
        menu:
         "当然.":
           m 1sub"哦，那太好了！"
           m 1hub"我很高兴你有听说过它！"
           m 3rusdla"嗯...尽管它本质是{i}百合{/i}作品......"
           extend 3sub"但是也并不妨碍它是一部好作品！无论是小说还是歌曲都是！"
           m 5hubfb"很高兴你和我，都遇到了这样的好作品！"
         "没有.":
           m 3rusdlb"哦，好吧，没有关系！"
           #那个，，霾说不能剧透好像，，，所以我不知道怎么写了..........
           m 1eua"你可以从{a=https://www.bilibili.com/video/BV1ms411d7VS/}{i}第一首歌{/i}{/a}开始了解这个故事！"
           m 3eub"或者，你也可以从原作小说来了解它！"
           m 4rusdlb"不过好像连载的地方关停了...想要看小说只能买盗印的来看......"
           m 5kusdlb"不过没关系，我相信，你一定会爱上它的！"
           extend 5husdlb"哈哈！"
           
        return
