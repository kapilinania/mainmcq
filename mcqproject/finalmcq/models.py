from django.db import models


class network(models.Model):
    user_ip = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_count = models.CharField(max_length=50)
    total_memory = models.BigIntegerField(default=10019)
    available_memory = models.BigIntegerField(default=10012)
    used_memory = models.BigIntegerField(default=10018)
    free_memory = models.BigIntegerField(default=10015)
    bytes_sent = models.BigIntegerField(default=10014)
    bytes_received = models.BigIntegerField(default=10013)
    packets_sent = models.BigIntegerField(default=100017)
    packets_received = models.BigIntegerField(default=10016)

# ------question insert ------

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
