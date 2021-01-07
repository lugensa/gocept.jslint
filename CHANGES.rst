CHANGES
=======

2.1 (2021-01-07)
----------------

- Add support for Python 3.8.

- Migrate to GitHub and GitHub Actions.


2.0 (2019-02-25)
----------------

- Add support for Python 3.6 and 3.7.

- Stop testing with Python 2.6.

- Run the tests against currently most recent versions of the dependencies.

- Change testrunner to py.test.


1.1.1 (2014-10-22)
------------------

- Get jshint command from environment (#13073).


1.1 (2012-05-21)
----------------

- Use jshint instead of jslint.


1.0.1 (2012-04-18)
------------------

- Uniquify duplicate file names in a prettier way: increment a counter, don't
  just blindly append '_1' (#9454).


1.0 (2011-08-25)
----------------

- Add support for linting JS files contained in zipped eggs (#9453).
- Add an entry point for running jslint from the command line (#9449).
- Skip tests if node.js is not available. Skipping tests only works properly in
  Python >= 2.7, though. (#9458)


0.2 (2011-08-24)
----------------

- Implement custom error ignores (#9456).


0.1 (2011-08-10)
----------------

- first release.
