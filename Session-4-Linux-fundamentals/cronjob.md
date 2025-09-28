# setting up a cron job

```bash
crontab -e
# select option 1
# it will open nano editor
```
- add this line
- * * * * * echo "Hello Cron" >> /home/sonam/cron_test.log
- means the mentioned script runs every minute and create logs to this file.

- to verify check logs
- cat home/sonam/cron_test.log

- again to stop this comment the added line
- to stop cron comment the line of code which is added in crontab -e

## Writing multiple cronjobs

```bash
# Every Minutes

* * * * * echo "Job 1 Running" >> /home/sonam/job1.log

# Every 5 Minutes
*/5 * * * * echo "Job 2 Running" >> /home/sonam/job2.log

# EveryDay at 5 AM

0 5 * * * /home/sonam/backup.sh

# Every Monday at 2 PM

0 14 * * 1 /home/sonam/report.sh

# run on alternative weekdays

0 9 * * 1,3,5 /home/sonam/report.sh

```