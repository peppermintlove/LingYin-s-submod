#话接上回DDTID~
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_modding",
            unlocked=True,
            prompt="我要去写Mod了.",
            pool=True
        ),
        code="BYE"
    )
    
label bye_prompt_modding:
    m 3sub"哦要去写Mod了吗？"
    m 3hub"预祝一切顺利~"
    m 3rksdla"不要出现 unexpection 就好..."#ly：习以为常了jpg
    extend 4rksdlb"哈哈."
    m 1eub"那么，[player]，再会！"
    
    return"quit"
