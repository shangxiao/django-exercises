Retrieve the First/Last of a Group
==================================

Goal: Obtain the either the first or last row of all groups using a single query

Hint: This is a PostreSQL specific feature


Given the following dataset:

|-------|---------------|-----------|
| Name  | Activity      | Time |
|-------|---------------|-----------|
| Bob   | Comes to work | 9:00 am   |
| Alice | Comes to work | 9:30 am   |
| Bob   | Eats lunch    | 12:00 pm  |
| Alice | Eats lunch    | 1:00 pm   |
| Bob   | Goes home     | 5:00 pm   |
| Alice | Goes home     | 5:30 pm   |
|-------|---------------|-----------|


How do we define a query to retrieve a result set that gets the final activity per person, per day?

|-------|----------------|---------|
| Name  | Final Activity | Time    |
|-------|----------------|---------|
| Bob   | Goes home      | 5:00 pm |
| Alice | Goes home      | 5:30 pm |
|-------|----------------|---------|
