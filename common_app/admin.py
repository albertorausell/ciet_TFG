from django.contrib import admin
from common_app.models import exercise, organization, capability, objective, dimension, phase, activity, content, training_technique, evaluation, question, answer, capability_objective, capability_learner
# Register your models here.

admin.site.register(organization)
admin.site.register(capability)
admin.site.register(objective)
admin.site.register(dimension)
admin.site.register(phase)
admin.site.register(activity)
admin.site.register(content)
admin.site.register(training_technique)
admin.site.register(evaluation)
admin.site.register(exercise)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(capability_objective)
admin.site.register(capability_learner)
