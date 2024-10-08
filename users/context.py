from users.models import Consultancy


def consultancy(request):
    if request.user.is_authenticated:
        consultancy = Consultancy.objects.filter(user=request.user).first()
        return {"consultancy": consultancy}
    return {}
