import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest

def pytest_addoption(parser: Parser) -> None:
    """Register --n command prompt argument for pytest."""
    parser.addoption(
        "--n",
        action="store",
        default=5,
        type=int,
        help="The size of the side of the grid for testing (initially: 5)"
    )

@pytest.fixture
def grid_size(request: SubRequest) -> int:
    """Fixture, which gives back the given n value."""
    return int(request.config.getoption("--n"))
