# Scheduled Workflow

- you can run pipeline automatically as cron job
- run jobs automatically at specific time like
- nightly builds, daily reports, clean up tasksm backups

```yml
on:
    schedule:
        - cron: "CRON_EXPRESSION" 
```

- CRON FORMAT -> * * * * * 
- minute hour day-of-month month day-of-week

- 0 0 * * * # every day at midnight
- */15 * * * * # every 15 minutes

- Run Every monday at 7 AM -->  0 7 * * 1
