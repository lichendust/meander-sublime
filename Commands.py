import os
import sublime
import sublime_plugin

class meander_remove_scene_number(sublime_plugin.TextCommand):
	def run(self, edit):
		# get all scene headings
		region_list = self.view.find_by_selector('entity.name.section')

		# going bottom to top means all region indexes are
		# preserved despite the rolling changes across the
		# entire buffer
		region_list.reverse()

		# expand to the entire line, replacing it with just the matched heading
		for region in region_list:
			self.view.replace(edit, self.view.line(region), self.view.substr(region))

class meander_add_scene_number(sublime_plugin.TextCommand):
	def run(self, edit):
		# get all scene headings
		region_list = self.view.find_by_selector('entity.name.section')

		# going bottom to top means all region indexes are
		# preserved despite the rolling changes across the
		# entire buffer
		region_list.reverse()
		count = len(region_list)

		# replace the entire line with a newly formatted scene heading
		for region in region_list:
			new_string = "{} #{}#".format(self.view.substr(region).rstrip(), str(count))
			self.view.replace(edit, self.view.line(region), new_string)
			count -= 1

class meander_toggle_boneyard(sublime_plugin.TextCommand):
	def run(self, edit):
		all_blocks = self.view.find_by_selector('comment.block')
		if self.view.fold(all_blocks):
			self.view.fold(all_blocks)
		else:
			self.view.unfold(all_blocks)

class meander_open_include(sublime_plugin.TextCommand):
	def run(self, edit):
		# gets list of caret positions
		selections = self.view.sel()
		cursor_pos = selections[0] # first one

		# checks if the cursor is currently located inside a test_scope
		if self.view.scope_name(cursor_pos.begin()) == "text.fountain include ":
			# create a valid path and open it!
			region = self.view.extract_scope(cursor_pos.begin())
			target_file = os.path.join(os.path.dirname(self.view.file_name()), self.view.substr(region))
			sublime.active_window().open_file(target_file)

def move_to_region(view, scope, forward=True):
	# gets list of caret positions
	selections = view.sel()
	cursor_pos = selections[0] # first one

	# get all matching scope regions
	section_list = view.find_by_selector(scope)

	# new target position
	the_point = 0

	for i, region in enumerate(section_list):
		# if we're in a section presently, adjust accordingly
		if region.contains(cursor_pos) or region.end() == cursor_pos.end():
			if forward and len(section_list) - 1 > i:
				the_point = section_list[i + 1].end()
				break

			if not forward and i > 0:
				the_point = section_list[i - 1].end()
				break

		# if we're between sections, adjust accordingly
		if region.begin() > cursor_pos.begin() and region.end() > cursor_pos.end():
			if not forward and i > 0:
				the_point = section_list[i - 1].end()
				break

			the_point = region.end()
			break
	# end loop

	# if we didn't find anything, we need to do nothing at
	# the top of the file and go to the last entry if we're
	# at the bottom
	if the_point == 0:
		if forward:
			return
		else:
			the_point = section_list[len(section_list) - 1].end()

	# moves caret position and viewport
	selections.clear()
	selections.add(the_point)
	view.show_at_center(the_point) # animate is on

class meander_move_to_section(sublime_plugin.TextCommand):
	def run(self, edit, forward=True, include_scenes=False):
		section_scope = 'punctuation.definition.heading'
		all_scope     = 'punctuation.definition.heading, entity.name.section'

		move_to_region(self.view, all_scope if include_scenes else section_scope, forward)

class meander_move_to_tag(sublime_plugin.TextCommand):
	def run(self, edit, forward=True):
		move_to_region(self.view, 'variable.annotation', forward)
