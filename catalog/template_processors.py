
def groups(request):
    tags = ['Silicates',
            'Oxides',
            'Sulfates',
            'Sulfides',
            'Carbonates',
            'Halides',
            'Sulfosalts',
            'Phosphates',
            'Borates',
            'Organic Minerals',
            'Arsenates',
            'Native Elements',
            'Other'
            ]
    return {'groups': tags}