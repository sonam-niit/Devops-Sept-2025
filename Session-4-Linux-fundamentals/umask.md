# Umask
- defines what permission should NOT be set when a new file or directory created
- masked out permissions
- by default 
    - files: 666 (read/write for user/group/others)
    - directory: 777 (read/write/execute for all)

- check the current umask value
```bash
umask # output will be like 0022
```
- default file permission 
- 666 - 022 = 644 (rw_r__r__)
- default deirectory permission 
- 777 - 022 = 755 (rwxr_xr_x)

- update umask value
```bash
umask 007
```
- default file permission 
- 666 - 007 = 660 (rw_rw_r__)
- default deirectory permission 
- 777 - 007 = 770 (rwxrwx---)

## Practice Task

- calculate File Permission and Dir Permission

- usmask (000)
- umask (077)
- umask  (002)