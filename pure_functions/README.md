# Pure Functions

### report_the_grand_goat_race

Welcome to the Grand Goat Race! Every year, goats duke it out to see who is the fastest in our race.

As a special job, we've designed a Grand Goat Race Report, for those who are unable to witness the event in person. We take the data (a list) with the goats data inside (as dictionaries) and we present two awards: `longest_name` and `quickest_time`. In the report, we also want a list of dictionaries of _all_ of the participants.

So if the data looks like this:
```
[{'name': 'harley', 'time_in_seconds': 9}, {'name': 'hobarthobart', 'time_in_seconds': 11}, {'name': 'flamingo', 'time_in_seconds': 15}]
```

Then the report should look like this: 

```
{'longest_name': 'hobarthobart', 'fastest_goat': 'harley', 'participants': [{'name': 'harley'}, {'name': 'hobarthobart'}, {'name': 'flamingo'}]}
```


#### Tasks

`report.py` is a function that collates the return values from three other functions to create the report. It is currenty failing its tests! 

You will have to look through the utility functions in the `utils` folder in order to find out what has gone wrong.

**Hint: you should really check out their test suites ... what seems to be missing?**