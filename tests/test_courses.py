import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.courses_list_toolbar_view_component.check_visible()
    courses_list_page.course_list_empty_view.check_visible('There is no results',
                                                           'Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.create_course_form.check_visible("", "", "", "0", "0")
    create_course_page.create_course_exercises_toolbar_view.check_visible()
    create_course_page.exercises_empty_view.check_visible('There is no exercises',
                                                          'Click on "Create exercise" button to create new exercise')
    create_course_page.image_upload_widget.check_visible()
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(True)
    create_course_page.create_course_form.fill("Playwright", "2 weeks", "Playwright", "100", "10")
    create_course_page.create_course_toolbar_view.click_create_course_button()
    courses_list_page.course_view.check_visible(0, "Playwright", "100", "10", "2 weeks")
