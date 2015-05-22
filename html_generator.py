# -*- coding: utf8 -*-
# This little program has a the goal ot taking some concepts from a list and generates the following HTML.

# The function start_lesson_html takes an argument lesson that is the title of the lesson to start generating
#our html.
def start_lesson_html(lesson_title):
	
	html1 = """
	<div class="lesson">
		<div class="title">
			<h2>""" + lesson_title

	html2 ="""</h2>
		</div>"""

	html = html1 + html2
	return html

# The function end_lesson_htm takes no argument and closes the lesson html
def end_lesson_html():

	html = """
	</div>"""
	return html

# The function subsection_html takes 2 arguments subsection_title and subsection_description to generate the html of the subsection
def subsection_html(subsection_title, subsection_description):

	html1 = """
		<div class="subsection">
			<h3>""" + subsection_title

	html2 = """</h3>
			<p>""" + subsection_description

	html3 = """</p>
		</div>"""

	html = html1 + html2 + html3
	return html


lesson = [
["lesson 6", [["For Loops", "This is a for loop"], ["lists", "This is a list"]]],
["lesson 7", [["How to solve problems", "This is how to solve a problem"]]]
]

# The function make_lesson_html is the engine to create an html lesson
def make_lesson_html(lesson):
	
	full_html = ""
	lesson_title = lesson[0]
	full_html += start_lesson_html(lesson_title)

	for e in lesson[1]:
		subsection_title = e[0]
	 	subsection_description = e[1]
	 	full_html += subsection_html(subsection_title, subsection_description)
	 
	full_html += end_lesson_html()
	return full_html

#The function many_lesson_html is the engine to create many html lessons in a row
def many_lesson_html(lesson):

	full_html = ""
	for e in lesson:
		full_html += make_lesson_html(e)
	return full_html

print many_lesson_html(lesson)






	