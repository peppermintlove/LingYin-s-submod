init -990 python:
    store.mas_submod_utils.Submod(
    author="LingYin",
    name="泠茵的话题包",
    description="大都是一些个人喜好内容.",
    version="0.1.1"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
            store.sup_utils.SubmodUpdater(
            submod="泠茵的话题包",
            user_name="peppermintlove",
            repository_name="LingYin-s-Dialogue-Packs",
            update_dir="",
            attachment_id=None
            )