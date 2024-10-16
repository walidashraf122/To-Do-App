{
    'name':'App One',
    'author':'Walid Ashraf',
    'category':'',
    'version':'17.0.0.1.0',
    'depends':['base','sale','account','mail'],
    'data':[
        'views/base_menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
            ],
    'assets': {
        'web.assets_backend': ['app_one\static\src\css\property.css']
    },
    'application': True
}