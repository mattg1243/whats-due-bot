from canvasapi import Canvas
from datetime import date, time, datetime, timedelta

API_URL = "https://4cd.instructure.com/"

canvas = Canvas(API_URL, "7774~4yWk23pgg4ndgqsMd1a6Xzo6ZMrsYFyP5YeFcvHY3VAe1179boM6jCyH4AUJ39tx")
# get the whole calculus class object
course = canvas.get_course(75853)
print(course.name)
# create the empty response arrary of empy tuples
assignments_response = []
# assemble a list of all assignments
assignments = course.get_assignments()
for a in assignments:
    assignments_response.append((a.name, a.due_at))
# date logic
today = date.today()
nextWeek = today + timedelta(days=7)
print("Today: ", today)
print("Next Week: ", nextWeek)
print(assignments_response)
