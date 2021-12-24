# Testing

The app was tested with automated unit tests as well as manually testing the UI and configuration.

## Unit testing

Except for the UI, most classes have unit tests written for them. The test class names are identical to the class names they test except for the `_test` suffix added to the names. The tests use a variety of ways to test data sources, including mock clients for MongoDb, test configurations, and so forth.

## Test coverage

Test coverage is somewhere above 70%.

![Test coverage](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/coverage.png "Test coverage")

The REST API connector doesn't have unit tests, and some other classes have methods that are not tested.

## System testing

Lots of manual testing has gone into the development of the app, and many bugs have been squashed, and many errors that may come up with bad configuration have been identified and error messages are generated for these errors.

## Installation and configuration

The app was developed on a Windows 11 machine and additionally tested on the university's Cubbli remote desktop.

## Features testing

Features mentioned in the user guide have been manually tested. Several test dashboards were created to test different combinations.

## Quality issues

The app has multiple connectors and it's possible to misconfigure the dashboard in myriad ways. Some of the most obvious errors get specific error messages in the UI, but there are certainly many that do not.
