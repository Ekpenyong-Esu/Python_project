import nox
import subprocess

@nox.session(python="3.12")
def tests(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "requirements-test.txt")
    session.run("pytest", "test.py")

@nox.session(python="3.12")
def coverage(session):
    session.install("-r", "requirements.txt")
    session.install("-r", "requirements-test.txt")
    session.install("coverage")
    session.run("coverage", "run", "-m", "pytest", "test.py")
    session.run("coverage", "report")

@nox.session(python="3.12")
def docs(session):
    session.install("sphinx")
    session.run("sphinx-build", "docs", "docs/_build", "--color")

@nox.session(python="3.12")
def docs_pdf(session):
    session.install("sphinx", "sphinxcontrib-napoleon") 
    session.run("sphinx-build", "-b", "latex", "docs", "docs/_build/latex", external=True)
    session.cd("docs/_build/latex")
    latexmk_command = ["latexmk", "-silent", "all-pdf"]
    subprocess.run(latexmk_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@nox.session(python="3.12")
def format(session):
    session.install("black")
    session.run("black", "simple_factory.py")

@nox.session(python="3.12")
def flake8(session):
    session.install("flake8")
    session.run("flake8", "simple_factory.py")


