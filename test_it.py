import pytest
from crawler import Crawler


def test_create_crawler():
    crawler = Crawler("https://www.seznam.cz")
    assert crawler is not None
    crawler.close()


def test_gathering_urls():
    crawler = Crawler("https://www.seznam.cz")
    crawler.get_urls()
    assert len(crawler.urls) > 0
    crawler.close()


def test_gathering_emails():
    crawler = Crawler("https://www.korycany.cz")
    crawler.get_emails()
    assert len(crawler.emails) > 0
    crawler.close()


def test_gathering_phones():
    crawler = Crawler("https://www.korycany.cz")
    crawler.get_phones()
    assert len(crawler.phones) > 0
    crawler.close()


def test_which_always_fails():
    assert False
