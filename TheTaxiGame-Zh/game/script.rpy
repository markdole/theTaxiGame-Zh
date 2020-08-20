# 您可以在此编写游戏的脚本。

# 下方的image命令可用于定义一个图像。
# 例：image eileen happy = "eileen_happy.png"

# 下方的define命令可定义游戏中出现的角色名称与对应文本颜色。
# 译注：define还可以定义很多功能，具体请参阅官方文档。
define m = Character('Mike', color="#c8ffc8")
define j = Character('Jane', color='#c8aac8')

# The game starts here.
label start:
    show  theroad at truecenter
# NOTE: 第一个场景
    scene inthecar
    'dudu'
    j " 但愿不要像上次一样把油耗干,这种情况好像已经发生了好多次了..."
    m "可是总觉得和你在一起的时候，一切都具有历险的美丽"
    j "我可不觉得，每次和你在黄郊野外断油的时候，永远都是我的历险，只是我一个人的历险"
    m "天气怎么样了 "
    j "看上去是要下雨了啊"
    m "好象是的，希望能在天气黑下来之前赶到城里"
    jump in_the_car

label in_the_car:
# NOTE: show inthecar
    scene inthecar
    "快走吧，天快黑了"

# 引用游戏OP视频，在进入程序主菜单显示前自动播放。
# 此处也可以使用图片代替。
# label splashscreen:
    # $ renpy.movie_cutscene('data/op.avi')
    # return
# 游戏从这里开始。

# 下面的参数用于设定是否允许用户通过点击或快进功能跳过转场特效。
# $ _skipping = True
# 是否允许用户通过点击或快进跳过暂停时间。
# 暂停时间是通过pause命令实现的，具体请参阅官方文档。
# $ _dismiss_pause = True
# 译注：以上两个命令都是出现后生效，并且有跨label继承性，
# 通常我们设置为True以保证用户能够使用快进，
# 但如果您在特殊情况下设置为False后，应在合适的地方重新
# 调整为True，以便用户能够正常进行游戏。
# 此功能包含在最新的每夜版SDK中，当您发现正式版SDK不兼容此命令时，
# 请将SDK的更新通道设置为每夜版，并进行更新。
    return
