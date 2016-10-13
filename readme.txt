魔灵召唤自动地城脚本V0.2 ---Infinity

工会内使用，请勿外传。
本版本为测试版，功能尚不完善，欢迎反馈各种建议。

版本更新v0.1		7/18/2016
1.	新增模式选择（Choose mode)。
分为设置刷图次数（set number of runs）与设置购买能量次数（set number of refills)。
后者将在购买能量指定次数后刷到能量不足时停止。选择模式后请按提示输入一个整数。
2.	在地图选择（Choose map）界面新增选项：自动刷剧情地图（senario）。
双倍刷经验用的，自动卖所有符文。没有满级检测，请自行参考魔灵升级经验图表和所在地图的每局经验计算所需设置的局数。
例如：双倍火山一带三，1星怪4次，2星怪10次。
3.	修改：地城中将自动卖掉4星符文且不做记录
4.	修改：地城掉落的符文和非符文将分开记录在rune_drop_records文件夹和other_drop_records文件夹以方便处理
5.	新增：开始检测游戏后如果超过10分钟未结束将会超时退出

版本更新v0.2   10/12/2016
1.	新增：模糊识别
在一定程度上容忍压缩过的低分辨率图像，在使用低于原始画质的屏幕投影软件时也可以使用本脚本了。
2. 	新增：超时补救
识别错误导致卡在某些掉落画面时有概率能够补救。
3.	延长了购买能量时的点击延时2s->5s，减少卡住的几率。



使用说明：
1.	初次运行前请调整好模拟器分辨率，长宽比，窗口位置等，所有这些参数如果以后发生改变将需要重新运行“校准”功能。
2.	运行脚本SWAFS.exe，以下是脚本提示内容。
3.		Summoners War Auto Farming Script by Infinity
		魔灵召唤自动地城脚本 ---Infinity
		Please choose 1)start 2)set up 3)exit
		请选择 1）开始 2）校准 3）退出
	第一次运行脚本必须选择校准，输入“2”并回车。
4.		point 0: start button
		第0点：开始按钮
		Enter 0 to skip or just press Enter to start
		点回车键开始校准，或输入0跳过本点校准
	进入校准点所需要的游戏画面。
	回到脚本窗口，点击回车，此时会弹出一个角标是红色“Tk”字样的小窗口。
	如果TK窗口或脚本窗口挡住了模拟器窗口你可以任意拖动他们。
	确保Tk窗口处于激活状态，如果不是可以点击此窗口空白部分。
	将鼠标放到需要校准的位置，点击空格键。
	*如果仅需要重新校准个别点，则在其他点处可输入0跳过，跳过已校准的点不会对该点做出任何改动。
5.	重复第4步完成全部校准，会需要重复多次地城才能全部校准完，建议打低一点的楼层比较快。
	如不需要自动买体力可跳过13-17点。如只需英雄地城可跳过4-7点。
	以后需要校准这些暂时跳过的点时可以跳过别的已经校准过的点。
	校准必须全部过一遍才会保存更改，中途强制退出会放弃所有本次改动。

	以下是每个点的具体要求：
		point 0: start button
		第0点：开始按钮
	地城队伍选择界面，开始按钮。
		point 1: victory mana label
		point 2: victory energy label
		point 3: victory crystal label
	以上3个点分别为胜利或失败界面中显示所得的魔力石，能量和水晶符号，确保鼠标指在蓝色，黄色和红色部分。

	后面的4-8是各种不同的掉落画面上的点。
		point 4: rune 5th star
	符文掉落界面，5-6星符文的第5颗星正中，用于判定是否是5星以上符文。
		point 5: rune Get button text
	获得符文界面，“保留”按钮，与“卖掉”对应的那个。
		point 6: rune sell button
	符文掉落界面，“出售”按钮。
		point 7: scroll OK button below text
	获得未知卷界面，确定按钮的下半部分，鼠标指在文字“确定”以下。
		point 8: HOH pieces OK button
	英雄地城碎片掉落界面，“确定”按钮。

		point 9: replay button text
	通关后“再来一局”按钮。
		point 10: Revive crystal label
	输掉时复活按钮上的水晶。
		point 11: Revive "10" text
	复活按钮上的数字“10”白色部分
		point 12: Revive NO text
	复活选项的“否”按钮上的文字白色部分

	以下是补充能量时连续的操作：
		point 13: recharge Yes button background
	询问是否补充能量的“是”按钮
		point 14: shop recharge energy
	弹出的商店，购买能量按钮
		point 15: recharge comfirm yes button
	选择买能量后弹出的“确定”按钮
		point 16: purchase successful OK button
	购买成功“确定”按钮
		point 17: shop Close button
	商店“关闭”按钮
		
6.	全部校准完毕后回到开头选择。将游戏进入地城队伍选择界面，确保没有其他窗口挡住模拟器窗口，在脚本窗口输入“1”回车。
7.		Choose map 1)GB/DB/NB 2)HOH 3)senario
	选择地图 1）巨人、龙、死亡 2）英雄地城 3）剧情地图
			Choose mode 1)set number of runs 2)set number of refills
	选择模式 1）设置局数 2）设置购买能量次数
					如果选 1）设置局数
						set number of runs
					设置局数。输入一个数字。
					如果选 2）设置购买能量次数
						set number of refills
					设置购买能量次数。输入一个数字。
			set initial wait in minutes
	设置初始等待时间。程序在开始识别胜负前的等待时间，单位是分钟。一般你能2.5-3分钟完成地城的话就设2这样。
	只是为了缩短废提示信息的量，不想管就输入0就行。这步写完就会立刻开始，所以点回车之前把窗口移到一边不要挡着。
	开始识别结果时每5秒脚本会显示提示 “checking game”，这是正常的。以及其他一些提示，看不懂就别管它们。
8.	你可以休息或者忙别的去啦~
9.	地城掉落的符文和非符文将分开记录在rune_drop_records文件夹和other_drop_records文件夹以方便处理，文件名为掉落的时间。
	英雄地城和剧情地图模式不记录掉落。
10.	以后再次运行脚本时不必对校准过的点再进行校准，重复校准会覆盖相应点的信息。
