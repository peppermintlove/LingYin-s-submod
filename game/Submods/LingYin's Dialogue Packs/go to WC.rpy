init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gotoWC",
            category=['马上回来'],
            prompt="我要去方便一下",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )
    
label gotoWC:
    m 3rusdlb "啊哈哈，我知道的，“人有三急”..."
    m 1eua"快去吧，等你回来哦！"
$ mas_idle_mailbox.send_idle_cb("gotoWC_callback")
return"idle"
    
#谁曾想到我居然因为这个要自己写这个话题，泪
label gotoWC_callback:
   
    m 1hub"哦，欢迎回来！"
    m 5eub"接下来我们要做什么呢？"
return

#之后可能会加点击这个话题次数>3次的时候的对话，，，大概吧，，，，，，，