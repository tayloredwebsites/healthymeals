
import nox


''' run code quality report and generate badges

Run each code quality tool in separate session
- this ensures all run regardless of errors
- this provides a summary of success and failures at the end
'''

@nox.session
def coverage_tests(session):
    ''' run tests through coverage so it also gets the coverage data '''
    session.run("coverage", "run", "-m", "pytest", "tests") # run tests with coverage

@nox.session
def coverage_report(session):
    ''' generate the coverage html pages '''
    session.run("coverage", "report", "-m") # generates coverate summary report in console

@nox.session
def tests_badge_files(session):
    ''' run pytest to generate the information needed for the tests badge and summary report '''
    session.run("pytest",
        "--junitxml=./reports/junit/junit.xml",
        "--html=./reports/junit/index.html",
    )

@nox.session
def coverage_badge_xml(session):
    ''' generate the xml file needed for the coverage badge '''
    session.run("coverage", "xml") # create coverage.xml file

@nox.session
def coverage_badge(session):
    ''' generate the coverage badge '''
    session.run("genbadge", "coverage") # create coverage badge

@nox.session
def tests_badge(session):
    ''' generate the tests badge '''
    session.run("genbadge", "tests") # create tests badge

@nox.session
def ruff(session):
    ''' run the ruff code standards tool '''
    session.run("ruff", "check") # optional parameter: "--fix")

@nox.session
def djlint(session):
    ''' run the djlint code standards tool '''
    session.run("djlint", "./healthymeals")

@nox.session
def pylint(session):
    ''' run the pylint code standards tool '''
    session.run("pylint", "./healthymeals")

@nox.session
def flake8(session):
    ''' run the flake8 code standards tool '''
    session.run(
        "flake8",
        "./healthymeals",
        "--exit-zero",
        "--format=html",
        "--htmldir",
        "./reports/flake8",
        "--statistics",
        "--tee",
        "--output-file",
        "./reports/flake8stats.txt",
    )

@nox.session
def mpyp(session):
    ''' run the mypy type checker '''
    session.run("mypy", "./healthymeals")
