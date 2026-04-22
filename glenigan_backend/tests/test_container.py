from app.api.deps import get_project_service
from app.core.container import Container


def test_container_singleton_and_service_resolution():
    Container._instance = None
    first = Container.get_instance()
    second = Container.get_instance()

    assert first is second
    assert first.project_service is not None


def test_get_project_service_returns_container_service():
    Container._instance = None
    container = Container.get_instance()
    resolved = get_project_service()

    assert resolved is container.project_service
