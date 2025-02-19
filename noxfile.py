from pathlib import Path

import nox

""" run code quality report and generate badges

Run each code quality tool in separate session
- this ensures all run regardless of errors
- this provides a summary of success and failures at the end
"""


@nox.session
def create_dirs(session):
    """Create qa directories if not there already."""
    session.run("rm", "-fr", "./docs/qa/")
    session.run("mkdir", "-p", "./docs/qa/tests/")
    session.run("mkdir", "-p", "./docs/qa/coverage/")
    session.run("mkdir", "-p", "./docs/qa/flake8/")
    session.run("mkdir", "-p", "./docs/qa/mypy/")

@nox.session
def coverage_tests(session):
    """Run tests through coverage so it also gets the coverage data."""
    with Path.open("./docs/qa/ran_coverage.txt", "w") as out:
        session.run("coverage", "run", "-m", "pytest", "tests",
            "--junitxml=./docs/qa/tests/junit.xml",
            "--html=./docs/qa/tests/index.html",
            stdout=out,
        ) # run tests with coverage

@nox.session
def tests_badge(session):
    """Generate the tests badge."""
    with Path.open("./docs/qa/ran_coverage.txt", "a") as out:
        session.run("genbadge", "tests",
            "--input-file", "./docs/qa/tests/junit.xml",
            "--output-file", "./docs/qa/tests/tests_badge.svg",
            stdout=out,
        ) # create tests badge

@nox.session
def coverage_badge_xml(session):
    """Generate the xml file needed for the coverage badge."""
    with Path.open("./docs/qa/ran_coverage.txt", "a") as out:
        session.run("coverage", "xml", stdout=out) # create coverage.xml file

@nox.session
def coverage_badge_html(session):
    """Generate the html files."""
    with Path.open("./docs/qa/ran_coverage.txt", "a") as out:
        session.run("coverage", "html", stdout=out) # create coverage HTML files

@nox.session
def coverage_badge(session):
    """Generate the coverage badge."""
    with Path.open("./docs/qa/ran_coverage.txt", "a") as out:
        session.run("genbadge", "coverage",
            "--input-file", "./docs/qa/coverage/coverage.xml",
            "--output-file", "./docs/qa/coverage/coverage_badge.svg",
            stdout=out,
        ) # create coverage badge

@nox.session
def ruff(session):
    """ run the ruff code standards tool """
    with Path.open("./docs/qa/ran_ruff.txt", "w") as out:
        session.run("ruff", "check", stdout=out) # optional parameter: "--fix")

@nox.session
def mypy(session):
    """ run the mypy type checker """
    with Path.open("./docs/qa/ran_mypy.txt", "w") as out:
        session.run("mypy",
            "./healthymeals",
            "--xslt-html-report",
            "./docs/qa/mypy/",
            stdout=out,
        )

@nox.session
def flake8(session):
    """ run the flake8 code standards tool """
    with Path.open("./docs/qa/ran_flake8.txt", "w") as out:
        session.run(
            "flake8",
            "./healthymeals",
            "--exit-zero",
            "--format=html",
            "--htmldir=./docs/qa/flake8/html",
            "--statistics",
            "--tee",
            "--output-file",
            "./docs/qa/flake8/flake8stats.txt",
            "--config=setup.cfg",
            "--select=E251",
            stdout=out,
        )

@nox.session
def flake8_badge(session):
    """Generate the flake8 badge."""
    with Path.open("./docs/qa/ran_flake8.txt", "a") as out:
        session.run("genbadge", "flake8",
            "--input-file", "./docs/qa/flake8/flake8stats.txt",
            "--output-file", "./docs/qa/flake8/flake8_badge.svg",
            stdout=out,
        ) # create coverage badge

# @nox.session  # noqa: ERA001
# def djlint(session):  # noqa: ERA001
#     """ run the djlint code standards tool """  # noqa: ERA001
#     session.run("djlint", "./healthymeals")  # noqa: ERA001

# @nox.session  # noqa: ERA001
# def pylint(session):  # noqa: ERA001
#     """ run the pylint code standards tool """  # noqa: ERA001
#     session.run("pylint", "./healthymeals")  # noqa: ERA001
