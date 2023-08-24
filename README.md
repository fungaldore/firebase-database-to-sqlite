## Intro

A simple script to convert the Firebase Realtime Database to a sqlite database that can be queried and analyzed outside the app.

## Usage

-   First download the Realtime Database JSON export from the Firebase console.
-   Edit the script so filename variables match yours.
-   Run the python script.

I named my json export file `database-export-20230823.json` and my sqlite database file `db_20230823.db`.

## Also

If you're new to sqlite like I am, I added these lines to my `~/.sqliterc` file so it would look more like mysql output.

```
.mode columns
.headers on
```

And use sqlite commands `.tables` and `.schema <tablename>` to make sure things converted properly.
