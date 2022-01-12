to excute the job seeker app with external sources

First, build and execute the application:

$ docker build . -t avatureexternaljobs
$ docker run -p 8081:8080 avatureexternaljobs

Alternatively, you can run npm install and node app.js instead of using docker.

Now, you can access http://localhost:8081/jobs, which can receive the following params to filter the jobs:

    name
    salary_min
    salary_max
    country

Example: http://localhost:8081/jobs?name=Java

The API response is JSON-formatted and contains a list of jobs, where each job is represented by an array of four positions (name, salary, country, skills).

Example:

[
    ["Developer", 30000, "Argentina", ["OOP", "PHP", "MySQL"]],
    ["DBA", 35000, "Spain", ["MySQL", "Percona", "Bash"]]
]


to excute the email alert is neede an valid Host with Email and PASSWORD 
this data should be as enviroment variables
