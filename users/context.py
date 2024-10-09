from users.models import Consultancy


def consultancy(request):
    if request.user.is_authenticated and request.user.role == "consultancy":
        consultancy = request.user.role == "consultancy"
        is_profile_complete = Consultancy.objects.filter(user=request.user).exists()
        return {"consultancy": consultancy, "is_profile_complete": is_profile_complete}
    return {"consultancy": None, "is_profile_complete": False}
