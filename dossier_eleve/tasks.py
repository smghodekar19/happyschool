# This file is part of HappySchool.
#
# HappySchool is the legal property of its developers, whose names
# can be found in the AUTHORS file distributed with this source
# distribution.
#
# HappySchool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HappySchool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with HappySchool.  If not, see <http://www.gnu.org/licenses/>.

from celery import shared_task

from django.conf import settings

from core.email import send_email
from core.models import ResponsibleModel, EmailModel

from .models import CasEleve, DossierEleveSettingsModel


@shared_task(bind=True)
def send_sanction_to_student_resp(self, instance_id):
    instance = CasEleve.objects.get(id=instance_id)
    student = instance.matricule
    context = {'student': student, 'sanction': instance}
    recipient = student.additionalstudentinfo.resp_email
    send_email(
        to=[recipient],
        subject="Sanction concernant %s" % student.fullname,
        email_template="dossier_eleve/email_sanction.html",
        context=context
    )


@shared_task(bind=True)
def task_send_info_email(self, instance_id):
    instance = CasEleve.objects.get(id=instance_id)
    student = instance.matricule
    teachers_obj = ResponsibleModel.objects.filter(classe=student.classe)
    dossier_eleve_settings = DossierEleveSettingsModel.objects.first()

    teachers = []
    context = {'student': student, 'info': instance, 'info_type': instance.info.info}
    for t in teachers_obj:
        if not t.email_school:
            send_email(to=[settings.EMAIL_ADMIN],
                       subject='ISLN : À propos de ' + student.fullname + " non envoyé à %s" % t.fullname,
                       email_template="dossier_eleve/email_info.html",
                       context=context,
                       attachments=instance.attachments.all(),
                       )
        else:
            if dossier_eleve_settings.use_school_email:
                teachers.append(t.email_school)
            else:
                teachers.append(t.email)

    # Add coord and educs to email list
    teachers += map(lambda e: e.email, EmailModel.objects.filter(teaching=student.teaching,
                                                                 years=student.classe.year))
    teachers += list(map(lambda e: e.email, EmailModel.objects.filter(is_pms=True)))

    if not settings.DEBUG:
        try:
            send_email(to=teachers,
                       subject='ISLN : À propos de ' + student.fullname,
                       email_template="dossier_eleve/email_info.html",
                       context=context,
                       attachments=instance.attachments.all(),
                       use_bcc=True,
                       )
        except Exception as err:
            send_email(to=teachers,
                       subject='ISLN : À propos de ' + student.fullname,
                       email_template="dossier_eleve/email_info.html",
                       context=context,
                       attachments=instance.attachments.all(),
                       use_bcc=True,
                       )
    else:
        print(teachers)
        send_email(to=[settings.EMAIL_ADMIN],
                   subject='ISLN : À propos de ' + student.fullname,
                   email_template="dossier_eleve/email_info.html",
                   context=context,
                   attachments=instance.attachments.all(),
                   )
        for t in teachers:
            print("Sending email to : " + t)