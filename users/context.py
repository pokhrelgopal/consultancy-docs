from users.models import Consultancy


def consultancy(request):
    is_profile_complete = False
    if request.user.is_authenticated:
        if request.user.role == "consultancy":
            consultancy = request.user.role == "consultancy"
            is_profile_complete = Consultancy.objects.filter(user=request.user).exists()
            return {
                "consultancy": consultancy,
                "is_profile_complete": is_profile_complete,
            }
        elif request.user.role == "student":
            consultancy = request.user.associated_with
            return {
                "student_consultancy": consultancy,
            }
    return {
        "consultancy": None,
        "is_profile_complete": False,
        "student_consultancy": None,
    }
