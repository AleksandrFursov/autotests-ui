from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)

        self.navbar = NavbarComponent(page)

        self.courses_list_toolbar_view_component = CoursesListToolbarViewComponent(page)

        self.course_view = CourseViewComponent(page)

        self.course_list_empty_view = EmptyViewComponent(page, "courses-list")
