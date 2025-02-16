
import nox


@nox.session
def tests(session):
    """ Run the test suite, including test reports generation and coverage reports. """
    session.run("coverage", "run", "-m", "pytest", "tests") # run tests with coverage
    session.run("coverage", "report", "-m") # generates reports/coverage_html/index.html
    session.run("ruff", "check") # optional parameter: "--fix")
    session.run("mypy", ".")
    # run the following to generate and upload custom badges (problems with travis and circle ci)
    session.run("pytest",
        "--junitxml=reports/junit/junit.xml",
        "--html=reports/junit/index.html",
    )
    session.run('coverage', 'xml') # create coverage.xml file
    session.run('genbadge', 'coverage') # create coverage badge
    session.run('genbadge', 'tests') # create tests badge
