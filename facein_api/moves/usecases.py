from rest_framework.generics import get_object_or_404

from common.usecases import UseCase
from moves.models import Camera
from moves.models import MoveLog
from photos.models import Photo
from photos.models import User


class FindUser(UseCase):
    """
    Find Room in which user was last time.
    """

    def __init__(self, username):
        self.username = username

    def execute(self):
        user = get_object_or_404(User, username=self.username)
        last_moved_camera = MoveLog.objects.filter(user__username=user.username,
                                                   user__company_id=user.company_id).latest('date')
        if last_moved_camera:
            return last_moved_camera.camera.to_room
        raise MoveLog.DoesNotExist


class FindCompanyUsers(UseCase):
    def __init__(self, company_id):
        self.company_id = company_id

    def execute(self):
        last_moves = MoveLog.objects.filter(user__company_id=self.company_id)\
            .select_related('user').order_by('user_id', '-date').distinct('user_id') \
            .values_list('user__username', 'camera__to_room')
        rooms_users = {}
        for user, room in last_moves:
            rooms_users[room] = rooms_users.get(room, []) + [user]
        return rooms_users


class GetCompanyCameras(UseCase):
    def __init__(self, company_id):
        self.company_id = company_id

    def execute(self):
        return Camera.objects.filter(to_room__company_id=self.company_id).values_list('id',
                                                                                      flat=True)


class MakePhotoObjectFromPhoto(UseCase):
    def __init__(self, photo, company_id=None):
        self.photo = photo
        self.company_id = company_id

    def execute(self):
        name = self.photo.name
        user = User.objects.filter(username__contains='_'.join(name.split('_')[:2]))
        if self.company_id:
            user = user.filter(company_id=self.company_id)
        if user.exists():
            photo = Photo.objects.create(image=self.photo, user=user.first())
        else:
            photo = Photo.objects.create(image=self.photo)
        return photo
