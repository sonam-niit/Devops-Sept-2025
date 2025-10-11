# Let's understand how git works

1. create folder named sample-git
2. open that folder inside gitBash
3. make this folder as repo run command: git init

![Git init](images/image1.png)

4. By default When you intialize git it provided default branch as master branch.
5. Whatever you do its indicated that, work done from master branch.
6. Let's understand tracking

![Git Status](images/image2.png)

7. add in staging area and check status

![Git Add](images/image3.png)

8. Let's Modify and understand the changes using tracker

![Git Diff](images/image4.png)

9. This changes you don't want then use restore
   - it Removes the changes from working directory and get the data back
   - from staging area

![Git Restore](images/image5.png)

10. Stage and Unstage files

![Git Unstage](images/image6.png)

- unstage will just remove the file from staging area not from working directory

11. For commit first of all follow the config command if its not created
   - check ![Configuration File](git-config.md)

12. Let's do the first Commit

![Git Commit](images/git-commit.png)

13. You can make some changes to new file and stage it and commit it again.

   - now when you do git logs 2 can see 2 logs

![another commit](images/commit2.png)