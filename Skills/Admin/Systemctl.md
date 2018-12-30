# Start | stop | enable | disable service
systemctl start sshd.service

# Config
/etc/systemctl/system.conf


# TIMERS
systemctl list-timers
# OnCalendar=DayOfWeek Year-Month-Day Hour:Minute:Second
###run first four days of month at 12:00 PM, BUT only if that day is a Monday or a Tuesday
OnCalendar=Mon,Tue *-*-01..04 12:00:00

# Check for valid OnCalendar format
systemd-analyze calendar "Mon,Tue *-*-01..04 12:00:00"
