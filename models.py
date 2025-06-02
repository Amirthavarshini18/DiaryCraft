# # from django.db import models
# # from django.contrib.auth.models import User

# # class DiaryEntry(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     date = models.DateField(auto_now_add=True)
# #     hints = models.TextField()
# #     formatted_entry = models.TextField()

# #     def __str__(self):
# #         return f"{self.user.username} - {self.date}"


# from django.db import models
# from django.contrib.auth.models import User

# class DiaryEntry(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title or f"Entry {self.pk} - {self.created_at.strftime('%Y-%m-%d')}"

from django.db import models

class DiaryEntry(models.Model):
    date_created = models.DateField(auto_now_add=True)
    hints = models.TextField()
    entry = models.TextField()                        # AI-formatted diary entry

    def __str__(self):
        return f"Entry on {self.date_created}"
