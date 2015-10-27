from mylib import Logger

mylog = Logger('logfile.txt', priority='CRITICAL',
               datetime=False, scriptname=False)

mylog.debug('will log if priority is DEBUG only')
mylog.info('will log if priority is INFO or DEBUG')
mylog.warning('will log if priority is INFO,DEBUG,WARNING')
mylog.error('will log if priority is INFO,DEBUG,WARNING,ERROR')
mylog.critical('will log in any case')