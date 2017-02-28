# -*- coding:utf-8 -*-
__date__ = '2017/2/28 18:44'

"""
选择所有需要merge的节点，然后执行该工具即可将所有需要的merge的节点merge在一起。
建议设置一个快捷键。
"""

import hou

sel_node = hou.selectedNodes()

try:
	panel = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
	pos = panel.selectPosition()

	merge_node = sel_node[0].parent().createNode("merge")
	merge_node.setPosition(pos)
	merge_node.setRenderFlag(1)
	merge_node.setDisplayFlag(1)

	for index, item in enumerate(sel_node):
		item.setSelected(0)
		merge_node.setInput(index, item)

except:
	hou.ui.displayMessage(u"请选择需要 merge 的节点", buttons=("Ok",))
