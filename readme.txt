魔灵召唤自动地城脚本 ---Infinity

工会内使用，请勿外传。
本版本为测试版，功能尚不完善，欢迎反馈各种建议。

使用说明：
1.	初次运行前请调整好模拟器分辨率，长宽比等，这些参数如果以后发生改变将需要重新校准脚本。
2.	运行安卓模拟器，不要移动模拟器窗口位置，运行魔灵召唤。
3.		Summoners War Auto Farming Script by Infinity 
		魔灵召唤自动地城脚本 ---Infinity
		Please choose 1)start 2)set up 3)exit
		请选择 1）开始 2）校准 3）退出
	第一次运行脚本请选择校准，输入“2”并回车。
4.		point 0: start button
		第0点：开始按钮
		Enter 0 to skip or just press Enter to start
		点回车键开始校准，或输入0跳过本点校准
	进入校准点所需要的游戏画面。
	回到脚本窗口，点击回车，此时会弹出一个角标是红色“Tk”字样的小窗口。
	如果TK窗口或脚本窗口挡住了模拟器窗口你可以任意拖动他们。
	确保Tk窗口处于激活状态，如果不是可以点击此窗口空白部分。
	将鼠标放到需要校准的位置，点击空格键。
	*如果仅需要重新校准个别点，则在其他点处可输入0跳过。
5.	重复第4步完成全部校准，会需要重复多次地城才能全部校准完，建议打低一点的楼层比较快。
	如不需要自动买体力可跳过10-13点，如只需英雄地城可跳过4,5,15,16点。
	以下是每个点的具体要求：
		point 0: start button
		第0点：开始按钮
	地城队伍选择界面，开始按钮。
		point 1: victory mana label
		point 2: victory energy label
		point 3: victory crystal label
	以上3个点分别为胜利或失败界面中显示所得的魔力石，能量和水晶符号，确保鼠标指在蓝色，黄色和红色部分。
		point 4: rune Get button text
	获得符文界面，“保留”按钮，与“卖掉”对应的那个。
		point 5: scroll OK button below text
	获得未知卷界面，确定按钮的下半部分，鼠标指在文字“确定”以下。
		point 6: replay button text
	通关后“再来一局”按钮。
		point 7: Revive crystal label
	输掉时复活按钮上的水晶。
		point 8: Revive 10 text
	复活按钮上的数字“10”白色部分
		point 9: Revive NO text
	复活选项的“否”按钮上的文字白色部分

	以下是补充能量时连续的操作：
		point 10: recharge Yes button background
	询问是否补充能量的“是”按钮
		point 11: shop recharge energy
	弹出的商店，购买能量按钮
		point 12: recharge comfirm yes button
	选择买能量后弹出的“确定”按钮
		point 13: purchase successful OK button
	购买成功“确定”按钮
		point 14: shop Close button
	商店“关闭”按钮
		point 15: rune 5th star
	掉落符文页面符文图标的第5颗星中心黄色部分
		point 16: rune sell button
	掉落符文页面“出售”按钮
		point 17: HOH pieces OK button
	英雄地城碎片掉落页面“确定”按钮
6.	全部校准完毕后回到开头选择。将游戏进入地城队伍选择界面，确保没有其他窗口挡住模拟器窗口，在脚本窗口输入“1”回车。
7.		Choose map 1)GB/DB/NB 2)HOH
	选择地图 1）巨人、龙、死亡 2）英雄地城
		set number of runs
	设置局数。输入一个数字。
		set initial wait in minutes
	设置初始等待时间。程序在开始识别胜负前的等待时间，单位是分钟。一般你能2.5-3分钟完成地城的话就设2这样。
	只是为了缩短废提示信息的量，不想管就输入0就行。这步写完就会立刻开始，所以点回车之前把窗口移到一边不要挡着。
8.	你可以休息或者忙别的去啦~
9.	掉落记录在“drop_records”文件夹下，文件名为掉落的时间。
10.	以后再次运行脚本时不必对校准过的点再进行校准，重复校准会覆盖相应点的信息。
