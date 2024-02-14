from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class Course:
    def __init__(self, course_id, course_name, convenor, number_of_students):
        self.course_id = course_id
        self.course_name = course_name
        self.convenor = convenor
        self.number_of_students = number_of_students


course_list = [Course(0, "Biology", "Jim Smith", 5),
               Course(1, "Maths", "Jack Jones", 8)]


@app.get("/")
async def home():
    return "Hello World"


@app.get("/courses", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="ViewCourses.html",
                                      context={"course_list": course_list})

@app.get("/courses/sign-up", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="CourseSignUp.html",
                                      context={"course_list": course_list})

@app.post("/courses/sign-up", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="CourseSignUpSuccess.html")
