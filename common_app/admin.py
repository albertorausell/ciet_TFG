from django.contrib import admin

from common_app.models import trainer_profile, learner_profile, stakeholders, exercise, organization, capability, objective, dimension, phase, activity, content, training_technique, evaluation, question, answer, capability_objective, capability_learner

# Register your models here.
admin.site.site_header = "CiET Admin"
admin.site.site_title = "CiET Admin Portal"
admin.site.index_title = "Welcome to CiET admin Portal"

admin.site.register(trainer_profile)
admin.site.register(learner_profile)
admin.site.register(stakeholders)
admin.site.register(organization)
# admin.site.register(capability)
# admin.site.register(objective)
admin.site.register(dimension)
admin.site.register(phase)
admin.site.register(activity)
# admin.site.register(content)
# admin.site.register(training_technique)
# admin.site.register(evaluation)
# admin.site.register(exercise)
# admin.site.register(question)
# admin.site.register(answer)
# admin.site.register(capability_objective)
# admin.site.register(capability_learner)
