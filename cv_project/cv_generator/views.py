from django.shortcuts import render

def cv_view(request):
    context = {
        'personal_info': {
            'name': 'Alex Smith',
            'email': 'alex@dev.com',
            'phone': '+1 555 123 4567',
            'linkedin': 'linkedin.com/in/alex-smith'
        },
        'experience': [
            {
                'title': 'Full Stack Developer',
                'company': 'Tech Innovators',
                'dates': '2021-Present',
                'achievements': [
                    'Developed 15+ production applications',
                    'Implemented CI/CD pipelines'
                ]
            }
        ],
        'education': [
            {
                'degree': 'B.Sc Computer Science',
                'institution': 'State Tech University',
                'dates': '2017-2021'
            }
        ],
        'skills': ['Python', 'Django', 'JavaScript', 'AWS']
    }
    return render(request, 'cv_generator/cv_template.html', context)
