from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from companies.models import Room
from profiles.models import User


class Camera(models.Model):
    """
    Camera. Tracks people moving through a doorway.

    from_room (Room): Room from which the doorway leads..
    to_room (Room): Room to which the doorway leads.

    """

    from_room = models.ForeignKey(Room,
                                  on_delete=models.PROTECT,
                                  verbose_name=_('Exit Room Camera'),
                                  related_name='from_cameras',
                                  related_query_name='from_camera',
                                  null=True)

    to_room = models.ForeignKey(Room,
                                on_delete=models.PROTECT,
                                verbose_name=_('Enter Room Camera'),
                                related_name='to_cameras',
                                related_query_name='to_camera',
                                null=True)

    class Meta:
        verbose_name = _('Camera')
        verbose_name_plural = _('Cameras')

    def clean(self):
        if self.from_room and self.to_room:
            if self.from_room.company != self.to_room.company:
                raise ValidationError(_("Companies of rooms are different."))

    def __str__(self):
        return f'{self.from_room}->{self.to_room}'


class MoveLog(models.Model):
    """
    Model to log all the moving of Users. If the user passes the doorway the log is created.

    Attributes:
        camera (Camera): Camera through which user passed.
        user (User): User who passed a doorway.
        date (datetime): Date and time of the event.

    """

    camera = models.ForeignKey(Camera,
                               on_delete=models.DO_NOTHING,
                               related_name='logs',
                               related_query_name='log',
                               verbose_name='Запись о том, что человек прошел через камеру')
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             related_name='logs',
                             related_query_name='log',
                             verbose_name='Пользователь')
    date = models.DateTimeField('date joined', auto_now_add=True)
