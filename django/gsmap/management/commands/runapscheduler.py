# runapscheduler.py
import logging

from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from gsmap.models import Snapshot

logger = logging.getLogger(__name__)


def create_screenshots():
    no_screenshots_snapshots = Snapshot.objects.filter(screenshot_generated='')
    created_screenshots = []
    for snapshot in no_screenshots_snapshots:
        snapshot.create_screenshot()
        created_screenshots.append({
            'snapshot_id': snapshot.id,
            'screenshot': snapshot.screenshot,
        })
    if not no_screenshots_snapshots:
        return None

def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        
        scheduler.add_job(
            create_screenshots,
            trigger=CronTrigger(minute=settings.SCREENSHOT_SCHEDULER_CRON_MINUTES),  # Every 10 minutes
            id="create_screenshots",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'create_screenshots'.")

        # scheduler.add_job(
        #     delete_old_job_executions,
        #     trigger=CronTrigger(
        #         day_of_week="mon", hour="00", minute="00"
        #     ),  # Midnight on Monday, before start of the next work week.
        #     id="delete_old_job_executions",
        #     max_instances=1,
        #     replace_existing=True,
        # )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
