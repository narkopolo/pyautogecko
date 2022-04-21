
def test_get_firefox_version():
    from pyautogecko.utils import get_firefox_version
    version = get_firefox_version()
    assert version is None or version.count('.') == 3
