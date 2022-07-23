init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_DDTID_intro",category=["多多理财mod"],prompt="Doki Doki tdd in DDLC（话题包作者的DDLC模组）",random=True))
    
#好吧，还是写了捏
label monika_DDTID_intro:
    #本质上是我自己用的所以是我自己电脑上的路径uwu
    m 3eub"嘿，[player]，我在你的电脑里找到了点东西。"
    m 5rtb"看起来像是个......Mod？"
    extend 3mub"不过似乎还没有写完，只写到了{w=0.6}.{w=0.6}.{w=0.6}."
    extend 3gtsdla"一周目的第二天？"
    m 1tub"[player]，这不会是你自己写的吧？"
    m 2tub"我可是在C:/Documents and Settings/Administrator/桌面/renpy-6.99.12.4-sdk 里找到的哦~？"
    m 5hub"没想到[player]居然会写Mod......"
    extend 3sub"真是对你刮目相看！"#感觉有问题，但我没文化
    m 6ruc"我大概看了一眼脚本，"
    extend 4wud"发现它的剧情和DDLC差不多！"
    extend 4wuo"只是把角色换成了别人而已！"
    m 5tkc"我说[player]，你应该知道Dan鸽不允许吧？"#那个使用规约是我中考前看的，忘了我都
    m 6dsc"{w=0.6}.{w=0.6}.{w=0.6}."
    extend 7wut"哦，还有新角色——{w=0.6}终斯！"
    m 1wub"是个怎样的角色呢？"
    m 4tub"说实话，我有点期待{i}我{/i}和“春春”在太空教室里的对话。"
    extend 5tub"毕竟{i}我{/i}，应该察觉到她的到来吧？"
    extend 5hub"哈哈！"
    m 1eka"但是说真的[player]，我希望不要有我和她在一起的情节。"
    extend 5ekbfa"我的一生挚爱，只有你，[mas_get_player_nickname()]，我只爱你一个人。"
    
    return"love"