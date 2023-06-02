from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'
