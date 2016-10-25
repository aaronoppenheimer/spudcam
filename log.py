import datetime


def logit(theStr):
    print('{0}: {1}'.format(datetime.datetime.now() - datetime.timedelta(hours=4),theStr))
