# rpa_project

For starting the project:

1. Download the repo to your local machine.
2. Install Docker, if you don't have one.
3. Open your terminal and go into the same directory, where you did download the repo.
4. Run following command: "docker compose up".
5. Run following command: "docker compose run -it -e START="-start={START}" -e END="-end={END}" -e SUPERVISOR="-s={SUPERVISOR}" rpa_app",
  where {START} is the beginning of search date; {END} is the last search date; and {SUPERVISOR} is the supervisor name, whos project you are interested
  to get. Important: separate the first and last name of a supervisor by a slash symbol "/", e.g. "Joku/Jokunen".
6. Last command will create the reports-folder in the directory, where you will find a timesheet.xlsl -file.
