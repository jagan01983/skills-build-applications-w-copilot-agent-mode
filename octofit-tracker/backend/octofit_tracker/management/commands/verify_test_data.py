from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Verify test data in the database'

    def handle(self, *args, **kwargs):
        # Verify Users
        users = User.objects.all()
        self.stdout.write(f"Users: {users.count()}")
        for user in users:
            self.stdout.write(f"- {user.username}")

        # Verify Teams
        teams = Team.objects.all()
        self.stdout.write(f"Teams: {teams.count()}")
        for team in teams:
            self.stdout.write(f"- {team.name}")

        # Verify Activities
        activities = Activity.objects.all()
        self.stdout.write(f"Activities: {activities.count()}")
        for activity in activities:
            self.stdout.write(f"- {activity.activity_type} by {activity.user.username}")

        # Verify Leaderboard
        leaderboard = Leaderboard.objects.all()
        self.stdout.write(f"Leaderboard Entries: {leaderboard.count()}")
        for entry in leaderboard:
            self.stdout.write(f"- {entry.user.username}: {entry.score}")

        # Verify Workouts
        workouts = Workout.objects.all()
        self.stdout.write(f"Workouts: {workouts.count()}")
        for workout in workouts:
            self.stdout.write(f"- {workout.name}: {workout.description}")