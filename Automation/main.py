from tests.test_login import test_login_valid, test_login_invalid
from tests.test_dashboard import test_navbar_visible_after_login
from tests.test_booking import test_booking_page_load, test_book_now_button_visible
from tests.test_ui import test_ui_zoom, test_responsive_navbar


def run_test(test_func, name):
    try:
        print(f"\n🚀 Running {name}...")
        test_func()
    except Exception as e:
        print(f"❌ {name} ERROR:", e)


run_test(test_login_valid, "TC-LOG-001")
run_test(test_login_invalid, "TC-LOG-002")
run_test(test_navbar_visible_after_login, "TC-DASH-001")
run_test(test_booking_page_load, "TC-BK-001")
run_test(test_book_now_button_visible, "TC-BK-002")
run_test(test_ui_zoom, "TC-UI-001")
run_test(test_responsive_navbar, "TC-UI-002")