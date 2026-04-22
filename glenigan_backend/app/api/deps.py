from app.core.container import Container
from app.interfaces.service import IProjectService

def get_project_service() -> IProjectService:
    return Container.get_instance().project_service
