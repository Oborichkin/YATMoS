import git
import pytest
import platform


@pytest.fixture(scope="session", autouse=True)
def record_info_about_test_session(record_testsuite_property):
    repo = git.Repo(search_parent_directories=True)
    record_testsuite_property("EXECUTOR", "pytest")
    record_testsuite_property("PLATFORM", platform.platform())
    record_testsuite_property("COMMIT_HASH", repo.head.commit.hexsha)
    # TODO record commit hash
    yield


@pytest.fixture(scope="function", autouse=True)
def record_info_about_test_case(request: pytest.FixtureRequest, record_property):
    # Через request можем вытаскивать всю инфу о тесте:
    #   - имя файла
    #   - имя функции
    #   - строчка
    # эту инфу можно сохранять например в junit и пушить при экспорте
    # а на фронте генерировать ссылку на гит (на текущий коммит конечно же)
    path, lineno, domain_info = request.node.location
    record_property("path", path)
    record_property("lineno", int(lineno))
    # также можем доставать все маркеры и брать оттуда описание, имена и
    # придумать прочие биндинги
    # TODO extract allure descriptions
    request.node.get_closest_marker("biba")
    # также стоит получше изучить API pytest и его зависимость pluggy
    yield

# xunit