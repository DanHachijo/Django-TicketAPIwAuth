from django.core.management import call_command

def backup_scheduled_job():
    try:
        call_command('dbbackup')
    except:
        pass

def restore_scheduled_job():
    try:
        call_command('dbrestore', '--noinput')
        
    except:
        pass