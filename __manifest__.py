### Custom Hotel Management Module

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'sequence': -100,
    'category': 'Medicine',
    'author': 'Jeff Nyak',
    'summary': 'Hospital Management System for Clinics and Pharmacies',
    'description': """Odoo Module for Doctors,Clinicians, Nurses etc""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},

}