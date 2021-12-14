# Architecture

## Structure

The code is structured in the following layers. The locations where each type of classes are stored (currently) is shown on the right. A more detailed view of the classes relationships is shown under *Classes* below.

|Layer|Location|
|---|---|
|Main app|`src/ui`|
|Views|`src/ui`|
|View components|`src/ui`|
|Service and configuration classes|`src`|
|Data handling classes|`src`|
|Data source connectors|`src/connectors`|


## Classes

The following diagram shows classes and their relationships.

![Class diagram](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/class_diagram.png "Class diagram")


## Dashboard load sequence

The following diagram shows the logic behind loading a dashboard. Configuration views are omitted from the diagram.

![Sequence diagram](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/sequence.png "Sequence diagram")
