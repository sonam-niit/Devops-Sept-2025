# background and foreground process

- Foreground: A process which takes control of your terminal
- Background: A process that runs without blocking your terminal

- let's say one of my code needs delay for 60 seconds so i dont want to wait
- then I can put that task to execute in background

```bash
sleep 60 & # & is used to run task in background
# when this command execute you can see the process ID
# to see the junning background processes
jobs #check the job number (assume its 1 here)
# if that job you want to get back in forground then
fg %1
# now wait running in foreground again to send back use ctrl+z
jobs # you can see the job is stopped
bg # this will resume your stopped job
jobs # you can see its running
# if its comepleted you can see done
# after Done it will removed from the list of jobs
```