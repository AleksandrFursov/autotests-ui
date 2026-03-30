import pytest
import allure
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGISTRATION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty course list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.courses_list_toolbar_view_component.check_visible()
        courses_list_page.course_list_empty_view.check_visible('There is no results',
                                                               'Results from the load test pipeline will be displayed here')

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
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

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.fill("Playwright", "2 weeks", "Playwright", "100", "10")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(0, "Playwright", "100", "10", "2 weeks")
        courses_list_page.course_view_menu.click_edit(0)

        create_course_page.create_course_form.fill("Playwright 2.0", "3 weeks", "Playwright 2.0", "200", "20")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(0, "Playwright 2.0", "200", "20", "3 weeks")
