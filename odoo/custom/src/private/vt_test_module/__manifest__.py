{
    'name': 'Visiotech Test Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Módulo de prueba simple para Doodba/Odoo.',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/test_model_views.xml',
    ],
}
