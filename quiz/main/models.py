from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    firstName = models.CharField(max_length=50, blank=True, null=True)
    middleName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    passwordHash = models.CharField(max_length=32)
    host = models.BooleanField(default=False)
    registeredAt = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Quiz(models.Model):
    hostId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    metaTitle = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    type = models.SmallIntegerField(default=0)
    score = models.SmallIntegerField(default=0)
    published = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    startsAt = models.DateTimeField(blank=True, null=True)
    endsAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class QuizAnswer(models.Model):
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionId = models.ForeignKey('QuizQuestion', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer {self.id} for Quiz {self.quizId}"

class QuizMeta(models.Model):
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Meta {self.key} for Quiz {self.quizId}"

class QuizQuestion(models.Model):
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    level = models.SmallIntegerField(default=0)
    score = models.SmallIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Question {self.id} for Quiz {self.quizId}"

class Take(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quizId = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0)
    score = models.SmallIntegerField(default=0)
    published = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    startedAt = models.DateTimeField(blank=True, null=True)
    finishedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Take {self.id} by User {self.userId} for Quiz {self.quizId}"

class TakeAnswer(models.Model):
    takeId = models.ForeignKey(Take, on_delete=models.CASCADE)
    questionId = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answerId = models.ForeignKey(QuizAnswer, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer {self.id} for Take {self.takeId} and Question {self.questionId}"
